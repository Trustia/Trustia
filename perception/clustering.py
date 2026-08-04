"""
TRUSTIA Algı Sistemi - Nokta bulutu kümeleme.

Engel noktalarını gruplara ayırır. Her küme bir engel adayı.

Algoritmalar:
  * Euclidean Clustering - mesafe bazlı kümeleme (PCL uyumlu)
  * DBSCAN - yoğunluk bazlı, gürültü dayanıklı
  * Region Growing - bölge büyütme, düzgün yüzeyler için
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

import numpy as np

from perception.types import PointCloud, BoundingBox


@dataclass
class Cluster:
    """Nokta kümesi - bir engel adayı."""
    indices: np.ndarray  # Orijinal buluttaki indisler
    points: np.ndarray   # (N, 3) nokta koordinatları
    centroid: np.ndarray # (3,) küme merkezi
    bbox: BoundingBox    # Bounding box

    @property
    def size(self) -> int:
        return len(self.indices)

    @classmethod
    def from_indices(cls, cloud: PointCloud, indices: np.ndarray) -> "Cluster":
        """Bulut ve indislerden küme oluştur."""
        if len(indices) == 0:
            raise ValueError("Boş küme oluşturulamaz")
        
        points = cloud.xyz()[indices]
        centroid = points.mean(axis=0)
        
        # Basit axis-aligned bounding box
        min_pt = points.min(axis=0)
        max_pt = points.max(axis=0)
        size = max_pt - min_pt
        center = (min_pt + max_pt) / 2.0
        
        bbox = BoundingBox(
            center=center,
            size=size,
            heading=0.0,  # Basit: rotasyon yok
        )
        
        return cls(
            indices=indices,
            points=points,
            centroid=centroid,
            bbox=bbox,
        )


class Clusterer:
    """Kümeleme algoritması temel sınıfı ve polar/euclidean kümeleyici."""

    def __init__(
        self,
        tolerance: float = 0.5,
        angular_resolution_rad: float = 0.05,
        gap_scale: float = 1.2,
        min_cluster_points: int = 2,
        min_cluster_size: int = 2,
        max_cluster_size: int = 1000,
    ) -> None:
        self.tolerance = tolerance
        self.angular_resolution_rad = angular_resolution_rad
        self.gap_scale = gap_scale
        self.min_cluster_points = min_cluster_points
        self.min_cluster_size = min_cluster_size
        self.max_cluster_size = max_cluster_size

    def cluster(self, cloud) -> List[Any]:
        if isinstance(cloud, list):
            if not cloud:
                return []
            if hasattr(cloud[0], "range_m") and hasattr(cloud[0], "angle_rad"):
                sorted_pts = sorted(cloud, key=lambda p: p.angle_rad)
                clusters = []
                curr_cluster = [sorted_pts[0]]
                max_gap = self.angular_resolution_rad * self.gap_scale

                for i in range(1, len(sorted_pts)):
                    prev_p = sorted_pts[i - 1]
                    curr_p = sorted_pts[i]
                    angle_diff = abs(curr_p.angle_rad - prev_p.angle_rad)
                    if angle_diff <= max_gap:
                        curr_cluster.append(curr_p)
                    else:
                        if len(curr_cluster) >= self.min_cluster_points:
                            clusters.append(curr_cluster)
                        curr_cluster = [curr_p]

                if len(curr_cluster) >= self.min_cluster_points:
                    clusters.append(curr_cluster)

                return clusters

        if hasattr(cloud, "xyz"):
            pts = cloud.xyz()
            if len(pts) == 0:
                return []
            ec = EuclideanClusterer(
                tolerance=self.tolerance,
                min_cluster_size=self.min_cluster_size,
                max_cluster_size=self.max_cluster_size,
            )
            return ec.cluster(cloud)
        return []


class EuclideanClusterer(Clusterer):
    """Euclidean mesafe bazlı kümeleme.
    
    PCL'deki EuclideanClusterExtraction benzeri. Noktalar arasında
    mesafe threshold'dan küçükse aynı küme.
    
    Algoritma: Flood fill (BFS) - komşuluk grafiği üzerinde
    connected components bulma.
    
    Parametreler:
        tolerance: Maksimum komşu mesafesi (metre)
        min_cluster_size: Minimum nokta sayısı
        max_cluster_size: Maksimum nokta sayısı
    """

    def __init__(
        self,
        tolerance: float = 0.5,
        min_cluster_size: int = 10,
        max_cluster_size: int = 25000,
    ) -> None:
        if tolerance <= 0.0:
            raise ValueError("tolerance pozitif olmalı")
        if min_cluster_size < 1:
            raise ValueError("min_cluster_size >= 1 olmalı")
        if max_cluster_size < min_cluster_size:
            raise ValueError("max_cluster_size >= min_cluster_size olmalı")
        
        self.tolerance = tolerance
        self.min_cluster_size = min_cluster_size
        self.max_cluster_size = max_cluster_size

    def cluster(self, cloud: PointCloud) -> List[Cluster]:
        if cloud.size == 0:
            return []
        
        xyz = cloud.xyz()
        visited = np.zeros(cloud.size, dtype=bool)
        clusters = []
        
        for i in range(cloud.size):
            if visited[i]:
                continue
            
            # BFS ile connected component bul
            queue = [i]
            cluster_indices = []
            visited[i] = True
            
            while queue:
                current = queue.pop(0)
                cluster_indices.append(current)
                
                if len(cluster_indices) > self.max_cluster_size:
                    break
                
                # Komşuları bul (brute force - optimize edilebilir KD-tree ile)
                current_pt = xyz[current]
                distances = np.linalg.norm(xyz - current_pt, axis=1)
                neighbors = np.where(
                    (distances < self.tolerance) & (~visited)
                )[0]
                
                for neighbor in neighbors:
                    visited[neighbor] = True
                    queue.append(neighbor)
            
            # Kümeyi kaydet (boyut kontrolü)
            if self.min_cluster_size <= len(cluster_indices) <= self.max_cluster_size:
                clusters.append(
                    Cluster.from_indices(cloud, np.array(cluster_indices))
                )
        
        return clusters


class DBSCANClusterer(Clusterer):
    """DBSCAN (Density-Based Spatial Clustering).
    
    Yoğunluk bazlı kümeleme - gürültüye dayanıklı, düzensiz
    şekilli kümeler bulabilir. Core/border/noise noktalar.
    
    Parametreler:
        eps: Komşuluk yarıçapı (epsilon)
        min_samples: Core nokta için minimum komşu sayısı
    """

    def __init__(
        self,
        eps: float = 0.5,
        min_samples: int = 5,
    ) -> None:
        if eps <= 0.0:
            raise ValueError("eps pozitif olmalı")
        if min_samples < 1:
            raise ValueError("min_samples >= 1 olmalı")
        
        self.eps = eps
        self.min_samples = min_samples

    def cluster(self, cloud: PointCloud) -> List[Cluster]:
        if cloud.size == 0:
            return []
        
        xyz = cloud.xyz()
        labels = np.full(cloud.size, -1, dtype=int)  # -1 = noise
        cluster_id = 0
        
        for i in range(cloud.size):
            if labels[i] != -1:
                continue  # Zaten işlendi
            
            # Komşuları bul
            distances = np.linalg.norm(xyz - xyz[i], axis=1)
            neighbors = np.where(distances < self.eps)[0]
            
            if len(neighbors) < self.min_samples:
                # Noise point
                continue
            
            # Yeni küme başlat
            labels[i] = cluster_id
            seed_set = list(neighbors)
            
            # Kümeyi genişlet
            j = 0
            while j < len(seed_set):
                q = seed_set[j]
                j += 1
                
                if labels[q] == -1:
                    labels[q] = cluster_id
                elif labels[q] != cluster_id:
                    continue
                
                # q'nun komşularını kontrol et
                q_distances = np.linalg.norm(xyz - xyz[q], axis=1)
                q_neighbors = np.where(q_distances < self.eps)[0]
                
                if len(q_neighbors) >= self.min_samples:
                    # q bir core point, komşularını ekle
                    for neighbor in q_neighbors:
                        if labels[neighbor] == -1:
                            seed_set.append(neighbor)
                            labels[neighbor] = cluster_id
            
            cluster_id += 1
        
        # Kümeleri oluştur (noise hariç)
        clusters = []
        for cid in range(cluster_id):
            indices = np.where(labels == cid)[0]
            if len(indices) >= self.min_samples:
                clusters.append(Cluster.from_indices(cloud, indices))
        
        return clusters


class RegionGrowingClusterer(Clusterer):
    """Region Growing kümeleme.
    
    Seed noktadan başla, benzer komşuları ekle (normal vektör
    benzerliği, eğrilik vs). Düzgün yüzeyler için iyi.
    
    Not: Basitleştirilmiş versiyon - normal vektör hesabı yok,
    sadece mesafe + yoğunluk bazlı.
    
    Parametreler:
        seed_threshold: Seed nokta seçim eşiği (düşük eğrilik)
        neighbor_threshold: Komşu ekleme eşiği
        k_neighbors: Komşu sayısı
    """

    def __init__(
        self,
        seed_threshold: float = 0.1,
        neighbor_threshold: float = 0.05,
        k_neighbors: int = 30,
    ) -> None:
        self.seed_threshold = seed_threshold
        self.neighbor_threshold = neighbor_threshold
        self.k_neighbors = k_neighbors

    def cluster(self, cloud: PointCloud) -> List[Cluster]:
        if cloud.size < self.k_neighbors:
            return []
        
        xyz = cloud.xyz()
        labels = np.full(cloud.size, -1, dtype=int)
        
        # Basitleştirilmiş "eğrilik" - komşu mesafe varyansı
        curvatures = np.zeros(cloud.size)
        for i in range(cloud.size):
            dists = np.linalg.norm(xyz - xyz[i], axis=1)
            nearest_indices = np.argpartition(dists, self.k_neighbors)[:self.k_neighbors]
            nearest_dists = dists[nearest_indices]
            curvatures[i] = nearest_dists.std()
        
        # Seed noktaları: düşük eğrilik
        seed_indices = np.where(curvatures < self.seed_threshold)[0]
        seed_indices = seed_indices[np.argsort(curvatures[seed_indices])]
        
        cluster_id = 0
        
        for seed_idx in seed_indices:
            if labels[seed_idx] != -1:
                continue
            
            # Region growing
            region = [seed_idx]
            labels[seed_idx] = cluster_id
            i = 0
            
            while i < len(region):
                current = region[i]
                i += 1
                
                # Komşuları bul
                dists = np.linalg.norm(xyz - xyz[current], axis=1)
                nearest_indices = np.argpartition(dists, min(self.k_neighbors, cloud.size - 1))[:self.k_neighbors]
                
                for neighbor in nearest_indices:
                    if labels[neighbor] != -1:
                        continue
                    
                    # Komşu ekleme kriteri: düşük eğrilik
                    if curvatures[neighbor] < self.neighbor_threshold:
                        labels[neighbor] = cluster_id
                        region.append(neighbor)
            
            if len(region) >= 10:  # Minimum küme boyutu
                cluster_id += 1
        
        # Kümeleri oluştur
        clusters = []
        for cid in range(cluster_id):
            indices = np.where(labels == cid)[0]
            if len(indices) >= 10:
                clusters.append(Cluster.from_indices(cloud, indices))
        
        return clusters
