"""
TRUSTIA CenterPoint / PointPillars ONNX Model Exporter.
Exports a valid ONNX graph for BEV 3D detection heads (nuScenes 7 classes).
Opset: 17, Input: pseudo_image [1, 64, 128, 128], Outputs: heatmap [1, 7, 128, 128], box_reg [1, 8, 128, 128], velocity [1, 2, 128, 128].
"""

import os
import numpy as np
import onnx
from onnx import helper, TensorProto


def export_centerpoint_onnx(output_path: str) -> str:
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    
    # Deterministic weights
    np.random.seed(42)
    
    # Input tensor definition
    input_pseudo_image = helper.make_tensor_value_info('pseudo_image', TensorProto.FLOAT, [1, 64, 128, 128])
    
    # Output tensor definitions
    output_heatmap = helper.make_tensor_value_info('heatmap', TensorProto.FLOAT, [1, 7, 128, 128])
    output_box_reg = helper.make_tensor_value_info('box_reg', TensorProto.FLOAT, [1, 8, 128, 128])
    output_velocity = helper.make_tensor_value_info('velocity', TensorProto.FLOAT, [1, 2, 128, 128])
    
    # Initializers (Weights & Biases)
    # Layer 1: Conv 64 -> 64 (3x3)
    w_conv1 = np.random.normal(0.0, 0.05, size=(64, 64, 3, 3)).astype(np.float32)
    b_conv1 = np.zeros(64, dtype=np.float32)
    
    # Layer 2: Conv 64 -> 64 (3x3)
    w_conv2 = np.random.normal(0.0, 0.05, size=(64, 64, 3, 3)).astype(np.float32)
    b_conv2 = np.zeros(64, dtype=np.float32)
    
    # Head 1: Heatmap Conv 64 -> 7 (1x1)
    w_head_cls = np.random.normal(0.0, 0.02, size=(7, 64, 1, 1)).astype(np.float32)
    # Bias initialized to -2.19 (sigmoid(-2.19) ~ 0.1) as standard CenterPoint focal loss prior
    b_head_cls = np.full(7, -2.19, dtype=np.float32)
    
    # Head 2: Box Reg Conv 64 -> 8 (1x1)
    w_head_box = np.random.normal(0.0, 0.02, size=(8, 64, 1, 1)).astype(np.float32)
    b_head_box = np.zeros(8, dtype=np.float32)
    
    # Head 3: Velocity Conv 64 -> 2 (1x1)
    w_head_vel = np.random.normal(0.0, 0.02, size=(2, 64, 1, 1)).astype(np.float32)
    b_head_vel = np.zeros(2, dtype=np.float32)
    
    initializers = [
        helper.make_tensor('w_conv1', TensorProto.FLOAT, [64, 64, 3, 3], w_conv1.flatten()),
        helper.make_tensor('b_conv1', TensorProto.FLOAT, [64], b_conv1.flatten()),
        helper.make_tensor('w_conv2', TensorProto.FLOAT, [64, 64, 3, 3], w_conv2.flatten()),
        helper.make_tensor('b_conv2', TensorProto.FLOAT, [64], b_conv2.flatten()),
        helper.make_tensor('w_head_cls', TensorProto.FLOAT, [7, 64, 1, 1], w_head_cls.flatten()),
        helper.make_tensor('b_head_cls', TensorProto.FLOAT, [7], b_head_cls.flatten()),
        helper.make_tensor('w_head_box', TensorProto.FLOAT, [8, 64, 1, 1], w_head_box.flatten()),
        helper.make_tensor('b_head_box', TensorProto.FLOAT, [8], b_head_box.flatten()),
        helper.make_tensor('w_head_vel', TensorProto.FLOAT, [2, 64, 1, 1], w_head_vel.flatten()),
        helper.make_tensor('b_head_vel', TensorProto.FLOAT, [2], b_head_vel.flatten()),
    ]
    
    # Graph Nodes
    # 1. Conv1: pseudo_image -> conv1_out
    node_conv1 = helper.make_node('Conv', ['pseudo_image', 'w_conv1', 'b_conv1'], ['conv1_out'], kernel_shape=[3, 3], pads=[1, 1, 1, 1])
    # 2. Relu1: conv1_out -> relu1_out
    node_relu1 = helper.make_node('Relu', ['conv1_out'], ['relu1_out'])
    
    # 3. Conv2: relu1_out -> conv2_out
    node_conv2 = helper.make_node('Conv', ['relu1_out', 'w_conv2', 'b_conv2'], ['conv2_out'], kernel_shape=[3, 3], pads=[1, 1, 1, 1])
    # 4. Relu2: conv2_out -> feat_bev
    node_relu2 = helper.make_node('Relu', ['conv2_out'], ['feat_bev'])
    
    # 5. Head Cls Conv: feat_bev -> cls_logits
    node_head_cls = helper.make_node('Conv', ['feat_bev', 'w_head_cls', 'b_head_cls'], ['cls_logits'], kernel_shape=[1, 1])
    # 6. Sigmoid: cls_logits -> heatmap
    node_sigmoid = helper.make_node('Sigmoid', ['cls_logits'], ['heatmap'])
    
    # 7. Head Box Conv: feat_bev -> box_reg
    node_head_box = helper.make_node('Conv', ['feat_bev', 'w_head_box', 'b_head_box'], ['box_reg'], kernel_shape=[1, 1])
    
    # 8. Head Velocity Conv: feat_bev -> velocity
    node_head_vel = helper.make_node('Conv', ['feat_bev', 'w_head_vel', 'b_head_vel'], ['velocity'], kernel_shape=[1, 1])
    
    nodes = [
        node_conv1, node_relu1,
        node_conv2, node_relu2,
        node_head_cls, node_sigmoid,
        node_head_box,
        node_head_vel
    ]
    
    graph = helper.make_graph(
        nodes=nodes,
        name='TrustiaCenterPointBEV',
        inputs=[input_pseudo_image],
        outputs=[output_heatmap, output_box_reg, output_velocity],
        initializer=initializers
    )
    
    model = helper.make_model(
        graph,
        producer_name='Trustia-AI',
        opset_imports=[helper.make_opsetid('', 17)],
        ir_version=9
    )
    onnx.checker.check_model(model)
    onnx.save(model, output_path)
    return output_path


if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    target_onnx = os.path.join(script_dir, '..', 'models', 'trustia_centerpoint_backbone.onnx')
    out = export_centerpoint_onnx(target_onnx)
    print(f"Exported ONNX Model to: {out} ({os.path.getsize(out)} bytes)")
