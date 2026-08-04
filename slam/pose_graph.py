"""
TRUSTIA SLAM - Pose Graph Optimization.

Pose graph: Robotun geçmiş pozisyonları (node) ve aralarındaki
göreli ölçümler (edge). Loop closure tespit edilince graf optimize
edilir → drift düzeltilir.

Basitleştirilmiş g2o benzeri least-squares optimization.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

import numpy as np

from slam.types import Pose2D


@dataclass
class PoseNode:
    """Pose graph node - tek robot pozu."""
    node_id: int
    pose: Pose2D
    timestamp_ns: int = 0
    fixed: bool = False  # Optimize edilmesin mi? (örn. başlangıç)

    def to_vector(self) -> np.ndarray:
        """[x, y, θ] optimizasyon vektörü."""
        return self.pose.to_array()

    def from_vector(self, vec: np.ndarray) -> None:
        """Optimizasyon sonucunu uygula."""
        self.pose = Pose2D.from_array(vec)


@dataclass
class PoseEdge:
    """Pose graph edge - iki pose arası göreli ölçüm."""
    from_node: int
    to_node: int
    measurement: Pose2D  # Göreli dönüşüm (from → to)
    information: np.ndarray = field(default_factory=lambda: np.eye(3))  # 3x3
    
    def error(self, nodes: Dict[int, PoseNode]) -> np.ndarray:
        """Hata vektörü: ölçüm vs tahmin farkı.
        
        e = (T_from^-1 * T_to) - measurement
        """
        pose_from = nodes[self.from_node].pose
        pose_to = nodes[self.to_node].pose
        
        # Tahmin edilen göreli pose
        predicted = pose_from.inverse().compose(pose_to)
        
        # Hata (residual)
        dx = predicted.x_m - self.measurement.x_m
        dy = predicted.y_m - self.measurement.y_m
        dtheta = predicted.angle_diff(self.measurement)
        
        return np.array([dx, dy, dtheta])


class PoseGraph:
    """Pose graph SLAM data structure.
    
    Node'lar robot pozisyonları, edge'ler odometry/ICP ölçümleri.
    Loop closure tespit edilince yeni edge eklenir → optimize.
    """

    def __init__(self) -> None:
        self.nodes: Dict[int, PoseNode] = {}
        self.edges: List[PoseEdge] = []
        self._next_node_id = 0

    def add_node(self, pose: Pose2D, timestamp_ns: int = 0, fixed: bool = False) -> int:
        """Yeni node ekle."""
        node_id = self._next_node_id
        self._next_node_id += 1
        
        self.nodes[node_id] = PoseNode(
            node_id=node_id,
            pose=pose,
            timestamp_ns=timestamp_ns,
            fixed=fixed,
        )
        
        return node_id

    def add_edge(
        self,
        from_node: int,
        to_node: int,
        measurement: Pose2D,
        information: Optional[np.ndarray] = None,
    ) -> None:
        """Yeni edge ekle (ölçüm)."""
        if from_node not in self.nodes or to_node not in self.nodes:
            raise ValueError("Node bulunamadı")
        
        if information is None:
            # Varsayılan information matrix (identity)
            information = np.eye(3)
        
        edge = PoseEdge(
            from_node=from_node,
            to_node=to_node,
            measurement=measurement,
            information=information,
        )
        
        self.edges.append(edge)

    def get_pose(self, node_id: int) -> Pose2D:
        """Node pose'unu döndür."""
        return self.nodes[node_id].pose

    def node_count(self) -> int:
        return len(self.nodes)

    def edge_count(self) -> int:
        return len(self.edges)

    def chi_square_error(self) -> float:
        """Toplam kare hata (chi-square)."""
        total_error = 0.0
        
        for edge in self.edges:
            e = edge.error(self.nodes)
            total_error += e.T @ edge.information @ e
        
        return float(total_error)


def optimize_pose_graph(
    graph: PoseGraph,
    max_iterations: int = 20,
    convergence_threshold: float = 1e-4,
) -> Tuple[PoseGraph, bool]:
    """Pose graph optimization - Gauss-Newton.
    
    Least-squares problem:
        min Σ e_i^T Ω_i e_i
    
    Gauss-Newton linearization:
        H Δx = -b
    
    Returns:
        optimized_graph: Optimize edilmiş graf
        converged: Yakınsadı mı
    """
    # Kopyala (orijinali değiştirme)
    optimized = PoseGraph()
    optimized.nodes = {nid: PoseNode(n.node_id, n.pose, n.timestamp_ns, n.fixed)
                       for nid, n in graph.nodes.items()}
    optimized.edges = list(graph.edges)
    optimized._next_node_id = graph._next_node_id
    
    # Optimize edilecek node'ları bul
    free_nodes = [nid for nid, node in optimized.nodes.items() if not node.fixed]
    
    if not free_nodes:
        return optimized, True
    
    # Node ID → state vector indeksi
    node_to_idx = {nid: i for i, nid in enumerate(free_nodes)}
    n_params = len(free_nodes) * 3  # Her pose 3 parametre (x, y, θ)
    
    prev_error = float('inf')
    
    for iteration in range(max_iterations):
        # Hessian ve gradient
        H = np.zeros((n_params, n_params))
        b = np.zeros(n_params)
        
        for edge in optimized.edges:
            # Edge'e dahil node'lar free mi?
            from_free = edge.from_node in node_to_idx
            to_free = edge.to_node in node_to_idx
            
            if not (from_free or to_free):
                continue  # İkisi de fixed
            
            # Hata ve Jacobian
            e = edge.error(optimized.nodes)
            J = _compute_jacobian(edge, optimized.nodes)
            
            # Information matrix
            Omega = edge.information
            
            # From node contribution
            if from_free:
                idx_from = node_to_idx[edge.from_node] * 3
                J_from = J[:, :3]
                
                H[idx_from:idx_from+3, idx_from:idx_from+3] += J_from.T @ Omega @ J_from
                b[idx_from:idx_from+3] += J_from.T @ Omega @ e
                
                # Cross terms
                if to_free:
                    idx_to = node_to_idx[edge.to_node] * 3
                    J_to = J[:, 3:]
                    
                    H[idx_from:idx_from+3, idx_to:idx_to+3] += J_from.T @ Omega @ J_to
                    H[idx_to:idx_to+3, idx_from:idx_from+3] += J_to.T @ Omega @ J_from
            
            # To node contribution
            if to_free:
                idx_to = node_to_idx[edge.to_node] * 3
                J_to = J[:, 3:] if from_free else J
                
                H[idx_to:idx_to+3, idx_to:idx_to+3] += J_to.T @ Omega @ J_to
                b[idx_to:idx_to+3] += J_to.T @ Omega @ e
        
        # Solve H Δx = -b
        try:
            delta_x = np.linalg.solve(H, -b)
        except np.linalg.LinAlgError:
            # Singular matrix - regularize
            H += np.eye(n_params) * 1e-6
            delta_x = np.linalg.solve(H, -b)
        
        # Update poses
        for nid in free_nodes:
            idx = node_to_idx[nid] * 3
            node = optimized.nodes[nid]
            
            current = node.to_vector()
            updated = current + delta_x[idx:idx+3]
            node.from_vector(updated)
        
        # Check convergence
        current_error = optimized.chi_square_error()
        error_change = abs(prev_error - current_error)
        
        if error_change < convergence_threshold:
            return optimized, True
        
        prev_error = current_error
    
    return optimized, False


def _compute_jacobian(edge: PoseEdge, nodes: Dict[int, PoseNode]) -> np.ndarray:
    """Edge hata fonksiyonunun Jacobian'ı.
    
    Numerical differentiation (finite differences) - basitleştirilmiş.
    Gerçek implementasyon analytical Jacobian kullanmalı.
    """
    eps = 1e-5
    
    pose_from = nodes[edge.from_node].pose
    pose_to = nodes[edge.to_node].pose
    
    # e_0
    e0 = edge.error(nodes)
    
    # Jacobian (3x6: e=[dx,dy,dθ], params=[x_from, y_from, θ_from, x_to, y_to, θ_to])
    J = np.zeros((3, 6))
    
    # From node perturbations
    for i in range(3):
        perturb = np.zeros(3)
        perturb[i] = eps
        
        nodes[edge.from_node].from_vector(pose_from.to_array() + perturb)
        e_perturbed = edge.error(nodes)
        nodes[edge.from_node].pose = pose_from  # Restore
        
        J[:, i] = (e_perturbed - e0) / eps
    
    # To node perturbations
    for i in range(3):
        perturb = np.zeros(3)
        perturb[i] = eps
        
        nodes[edge.to_node].from_vector(pose_to.to_array() + perturb)
        e_perturbed = edge.error(nodes)
        nodes[edge.to_node].pose = pose_to  # Restore
        
        J[:, 3+i] = (e_perturbed - e0) / eps
    
    return J
