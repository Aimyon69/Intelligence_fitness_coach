# 🏋️‍♂️ AI 智能健身教练 - 实战开发路线图 (Project Roadmap)

**项目目标**：构建一个基于 Web 的 AI 应用，用户打开摄像头做深蹲，系统实时绘制骨骼、计数，并语音/文字提示动作是否标准。
**核心技术**：YOLOv8-Pose, OpenCV, geometric-algebra, FastAPI, WebSocket, Streamlit, Docker, ONNX.

---

## 📅 第一周：核心视觉层 —— “看清动作”
**目标**：掌握 YOLOv8-Pose，实现从视频中提取人体 17 个关键点坐标。

- **Day 1: 环境搭建与 YOLO 初体验**
    - [ ] 创建虚拟环境：`conda create -n fitness_ai python=3.9`
    - [ ] 安装核心库：`pip install ultralytics opencv-python numpy`
    - [ ] **里程碑**：运行官方 Demo，输入一张只有人的图片，输出画了骨骼线的图片。

- **Day 2: 深入 YOLOv8 输入输出**
    - [ ] 编写脚本：读取单张图片，不画图，而是打印出关键点坐标 `(x, y, conf)`。
    - [ ] 理解数据结构：查阅 COCO 17点定义，搞清哪个点是膝盖，哪个是脚踝。
    - [ ] **知识迁移**：对比 MTCNN 的 5 点输出与 YOLO 的 17 点输出。

- **Day 3: 视频流处理 Pipeline**
    - [ ] 复习 OpenCV 的 `VideoCapture` 和 `VideoWriter`。
    - [ ] **里程碑**：编写 `process_video.py`，输入 `squat.mp4`，输出每一帧都画了骨骼的 `output.mp4`。
    - [ ] 性能初探：计算 FPS (每秒处理帧数)。

- **Day 4-7: 几何数学基础与测试**
    - [ ] 编写工具函数 `calculate_angle(a, b, c)` (输入三个坐标，输出角度)。
    - [ ] 测试：找几张不同深蹲幅度的图，验证角度计算是否准确 (如深蹲到底 < 90度)。

---

## 🧠 第二周：业务逻辑层 —— “看懂动作”
**目标**：利用几何数学和状态机，把坐标变成“计数”和“纠错”。

- **Day 8-10: 状态机设计 (计数器核心)**
    - [ ] 理解状态机概念 (State Machine)。
    - [ ] 定义状态常量：`STANDING` (角度 > 160), `SQUATTING` (角度 < 90)。
    - [ ] **里程碑**：实现完整的深蹲计数逻辑，在视频左上角实时显示 "Count: 5"。

- **Day 11-12: 动作纠错算法**
    - [ ] 逻辑实现：**膝盖内扣检测** (比较膝盖与脚踝的 X 坐标相对位置)。
    - [ ] 逻辑实现：**下蹲深度不足** (判断角度最低点是否小于 100度)。
    - [ ] 可视化：动作错误时，骨骼线变红并在屏幕提示 "Knees Out!"。

- **Day 13-14: 代码重构 (OOP)**
    - [ ] 告别脚本式编程，封装类。
    - [ ] 创建 `PoseDetector` (负责识别)。
    - [ ] 创建 `SquatCounter` (负责计数与状态)。
    - [ ] 创建 `Visualizer` (负责画图)。

---

## 🚀 第三周：后端服务化 —— “脱离本机”
**目标**：学习 FastAPI，将算法封装为 API 接口，模拟真实的互联网服务架构。

- **Day 15-17: FastAPI 快速入门**
    - [ ] 安装 `fastapi`, `uvicorn`。
    - [ ] 编写 Hello World 接口，浏览器访问成功。

- **Day 18-19: 接口设计与测试**
    - [ ] 设计 POST 接口：接收图片文件 -> 返回 JSON (包含计数、状态、关键点)。
    - [ ] 使用 Postman 进行接口测试。

- **Day 20-21: WebSocket 实时流 (难点)**
    - [ ] 学习 HTTP vs WebSocket 的区别。
    - [ ] **里程碑**：搭建 WebSocket 服务端，实现客户端发图片流，服务端实时处理并回传结果。

---

## 🌐 第四周：前端与部署 —— “产品落地”
**目标**：制作可视化网页，并进行模型加速和容器化部署。

- **Day 22-24: Streamlit 极速开发前端**
    - [ ] 安装 `streamlit`。
    - [ ] 使用 `st.camera_input` 调用网页摄像头。
    - [ ] 前后端联调：前端发送数据给后端，实时渲染返回的画面。

- **Day 25-28: 模型量化加速 (简历加分项)**
    - [ ] 导出 YOLO 模型为 **ONNX** 格式。
    - [ ] 使用 `onnxruntime` 进行推理。
    - [ ] **数据对比**：记录并对比 PyTorch 原版和 ONNX 版的 FPS 差异。

- **Day 29-30: 整理与发布**
    - [ ] 编写 `Dockerfile` 实现容器化。
    - [ ] 录制 Demo 演示视频。
    - [ ] 编写最终的 README 文档，上传 GitHub。

---

## 📂 最终项目结构预览

```text
AI_Fitness_Coach/
├── app/
│   ├── main.py            # FastAPI 后端入口
│   ├── core/
│   │   ├── pose.py        # YOLO 模型封装
│   │   ├── counter.py     # 计数逻辑与状态机
│   │   └── utils.py       # 角度计算等数学工具
│   └── routers/           # API 路由
├── web/
│   └── streamlit_app.py   # 前端界面
├── models/
│   ├── yolov8n-pose.pt    # 原版权重
│   └── yolov8n-pose.onnx  # 加速版权重
├── docker/
│   └── Dockerfile         # 部署文件
├── requirements.txt
└── README.md
```