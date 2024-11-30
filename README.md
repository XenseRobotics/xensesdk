# Xense SDK 文档

## 概述

**Xense SDK** 是一款为触觉-视觉传感器和可视化工具设计的开发工具包，旨在帮助高效且无缝地将其集成到应用程序中。

---

## 安装指南

### 步骤 1: 准备 Python 开发环境

推荐使用 **Anaconda**，并使用 Python 版本 **3.9.19**。

```bash
# 进入 Xense SDK 目录
cd xensesdk

# 创建并激活虚拟环境
conda create -n xenseenv python=3.9.19
conda activate xenseenv
```

---

### 步骤 2: 安装 CUDA 工具包和 cuDNN

SDK 支持 **CUDA Toolkit 11.8** 和 **cuDNN 8.9.2.26**。根据您的环境，选择以下安装方式：

#### 选项 1: 从本地 Conda 环境包安装

```bash
conda install --use-local cudatoolkit-11.8.0-hd77b12b_0.conda
conda install --use-local cudnn-8.9.2.26-cuda11_0.conda
```

#### 选项 2: 通过 Conda 直接安装

1. 搜索所需版本：
   ```bash
   conda search cudnn
   conda search cudatoolkit
   ```
2. 安装所需版本：
   ```bash
   conda install cudnn==8.9.2.26 cudatoolkit==11.8.0
   ```

---

### 步骤 3: 安装 Xense SDK 包

将 SDK 包安装到您的环境中：

```bash
pip install xensesdk-0.1.0-cp39-cp39-win_amd64.whl
```

---

## 运行演示

从终端直接运行演示应用程序：

```bash
xense_demo
```

### 示例源代码

可以在以下目录中查找示例源代码：

```
site-packages/xensesdk/examples/*
```


---

# API 文档

本文件提供了用于处理传感器图像的各类方法，包含深度图生成、差异图计算、标记检测以及传感器数据的综合聚合。

---

## 1. `getRectifyImage`

### 描述

从传感器获取一个校正后的图像。

### 返回

- 一个形状为 `[700, 400, 3]`（`h, w, c`）的 `uint8` 数组，表示校正后的图像。

### 示例

```python
from xensesdk.xenseInterface.OmniSensor import Sensor
sensor = Sensor(cam_id="your_cam_id", use_gpu=True, config_path="your_config_path")
rectified_image = sensor.getRectifyImage()
```

---

## 2. `getDepthImage`

### 描述

根据输入的图像生成深度图。

### 参数

- `image`：（可选）一个形状为 `[700, 400, 3]`（`h, w, c`）的 `uint8` 数组。如果未提供图像，则默认为 `getRectifyImage` 的输出。

### 返回

- 一个形状为 `[336, 192]`（`h, w`）的 `float32` 数组，单位为毫米，表示深度图。

### 示例

```python
from xensesdk.xenseInterface.OmniSensor import Sensor
sensor = Sensor(cam_id="your_cam_id", use_gpu=True, config_path="your_config_path")
depth_map = sensor.getDepthImage(image)
```

---

## 3. `getDiffImage`

### 描述

根据输入的图像生成差异图。

### 参数

- `image`：（可选）一个形状为 `[700, 400, 3]`（`h, w, c`）的 `uint8` 数组。如果未提供图像，则默认为 `getRectifyImage` 的输出。

### 返回

- 一个形状为 `[336, 192, 3]`（`h, w, c`）的 `uint8` 数组，表示差异图。

### 示例

```python
from xensesdk.xenseInterface.OmniSensor import Sensor
sensor = Sensor(cam_id="your_cam_id", use_gpu=True, config_path="your_config_path")
diff_img = sensor.getDiffImage(image)
```

---

## 4. `getMarker`

### 描述

检测标记位置，并更新内部的标记追踪器。

### 参数

- `image`：（可选）一个形状为 `[700, 400, 3]`（`h, w, c`）的 `uint8` 数组。如果未提供图像，则默认为 `getRectifyImage` 的输出。

### 返回

- 一个元组 `[current_marker_grid, confidence]`：
  - `current_marker_grid`：形状为 `[18, 9, 2]`（`float32`），表示检测到的标记位置。
  - `confidence`：形状为 `[18, 9]`（`float32`），表示每个标记的检测置信度。

### 示例

```python
from xensesdk.xenseInterface.OmniSensor import Sensor
sensor = Sensor(cam_id="your_cam_id", use_gpu=True, config_path="your_config_path")
current_marker_grid, confidence = sensor.getMarker(image)
```

---

## 5. `getMarkerUnordered`

### 描述

检测无序的标记位置，不更新内部标记追踪器。

### 参数

- `image`：（可选）一个形状为 `[700, 400, 3]`（`h, w, c`）的 `uint8` 数组。如果未提供图像，则默认为 `getRectifyImage` 的输出。

### 返回

- 一个数组，表示检测到的标记。格式取决于检测方法和配置。

### 示例

```python
from xensesdk.xenseInterface.OmniSensor import Sensor
sensor = Sensor(cam_id="your_cam_id", use_gpu=True, config_path="your_config_path")
unordered_markers = sensor.getMarkerUnordered(image)
```

---

## 6. `getAllSensorInfo`

### 描述

聚合并返回所有处理过的传感器数据，包括校正图像、深度图、标记数据和差异图，便于统一访问。

### 参数

- `image`：（可选）一个形状为 `[700, 400, 3]`（`h, w, c`）的 `uint8` 数组。如果未提供图像，则默认为 `getRectifyImage` 的输出。

### 返回

- 一个字典，包含以下键：
  - `"src_img"`：源图像，一个形状为 `[700, 400, 3]`（`h, w, c`）的 `uint8` 数组。
  - `"depth_map"`：深度图，一个形状为 `[336, 192]`（`h, w`）的 `float32` 数组，单位为毫米，表示每个像素的深度。
  - `"marker"`：一个列表，包含：
    - `current_marker_grid`：标记网格，形状为 `[18, 9, 2]`（`float32`），表示标记的位置。
    - `confidence`：置信度图，形状为 `[18, 9]`（`float32`），表示每个标记的检测置信度。
  - `"diff_img"`：差异图，一个形状为 `[336, 192, 3]`（`uint8`）的图像。

### 示例

```python
from xensesdk.xenseInterface.OmniSensor import Sensor
sensor = Sensor(cam_id="your_cam_id", use_gpu=True, config_path="your_config_path")
sensor_info = sensor.getAllSensorInfo(image)
```

---

## 7. `drawMarkerMove`

### 描述

在图像上绘制标记的运动向量。该方法使用标记追踪器可视化标记的运动。

### 参数

- `image`：一个形状为 `[700, 400, 3]`（`h, w, c`）的 `uint8` 数组。

### 返回

- 一个形状为 `[700, 400, 3]`（`h, w, c`）的 `uint8` 数组，表示输入图像并绘制标记的运动向量。

### 示例

```python
from xensesdk.xenseInterface.OmniSensor import Sensor
sensor = Sensor(cam_id="your_cam_id", use_gpu=True, config_path="your_config_path")
img_with_marker_move = sensor.drawMarkerMove(image)
```

---

## 8. `drawMarker`

### 描述

在图像上绘制标记。

### 参数

- `image`：一个形状为 `[700, 400, 3]`（`h, w, c`）的 `uint8` 数组。
- `marker`：一个包含要绘制的标记位置的列表或数组。
- `color`：一个元组 `(r, g, b)`，表示标记的颜色，默认为 `(3, 253, 253)`。
- `radius`：绘制标记的半径，默认为 `2`。
- `thickness`：标记边界的厚度，默认为 `2`。

### 返回

- 一个形状为 `[700, 400, 3]`（`h, w, c`）的 `uint8` 数组，表示输入图像并绘制标记。

### 示例

```python
from xensesdk.xenseInterface.OmniSensor import Sensor
sensor = Sensor(cam_id="your_cam_id", use_gpu=True, config_path="your_config_path")
img_with_markers = sensor.drawMarker(image, markers)
```

---

## 9. `loadConfig`

### 描述

从配置文件加载设置，并更新内部的标记和校正配置。

### 参数

- `file_path`：配置文件的路径。

### 返回

- 无。该方法根据提供的文件修改内部配置。

### 示例

```python
from xensesdk.xenseInterface.OmniSensor import Sensor
sensor = Sensor(cam_id="your_cam_id", use_gpu=True, config_path="your_config_path")
sensor.loadConfig("path_to_config_file")
```

---

### 注意事项：
- 每个接受 `image` 参数的函数，如果未提供图像，将默认使用 `getRectifyImage` 的输出。

---


### 常见问题解答 (FAQ)

**问：** 无法加载 Qt 平台插件 "xcb" 虽然它已被找到，错误信息为 "..."
**答：** 进入 `.../plugins/platform` 目录并删除 `libqxcb.so` 文件。
