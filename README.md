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

## 示例程序

### 示例源代码

可以在以下目录中查找示例源代码：

```
site-packages/xensesdk/examples/*
```

一个简单的例程如下:

```python
from xensesdk.xenseInterface.XenseSensor import Sensor
from time import sleep

def main():
    # 1. 创建传感器
    #    Sensor.create("serial_number", config_path="path_to_config_file")
    sensor = Sensor.create('OP000064', config_path = "/config")
    # 注意OP000064 是传感器的序列号，config_path 是配置文件的路径，config_path下需要有名为OP000064的配置文件

    # 2. 读取传感器数据
    #   sensor.selectSensorInfo 可以通过传入 `Sensor.OutputType` 枚举量获取相应的传感器数据, 且的顺序或者数量无限制
    #   可选的输出类型有:
    #       * Difference : 差分图像
    #       * Depth : 深度图
    #       * Marker2D : Marker点的二维像素坐标
    #       * Marker2DInit : Marker点的初始二维坐标
    #       * Marker3D : Marker点的三维坐标
    #       * Marker3DInit : Marker点的初始三维坐标
    #       * Marker3DFlow : Marker3D - Marker3DInit
    #       * Force : 三维分布力
    #       * ForceNorm : 法向分布力
    while True:
        diff_img, depth= sensor.selectSensorInfo(Sensor.OutputType.Difference, Sensor.OutputType.Depth)

        # 数据处理
        # ...
        sleep(0.02)

if __name__ == '__main__':
    main()
```

---

# API 文档

本文件提供了用于处理传感器图像的各类方法，包含深度图生成、差异图计算、标记检测以及传感器数据的综合聚合。

---

## 1. `create` 方法

### 描述

创建一个传感器

### 输入参数

- cam_id: 传感器id或者序列号, 默认为 0。如果是传感器id，则输入的数据类型是整形。如果是序列号，则输入的数据类型是字符串。
- config_path: 配置文件所在文件夹，或者配置文件的路径。如果是配置文件所在文件夹的话，该文件夹内需要包含名为传感器序列号的配置文件。比如，该传感器的配置文件名为OP000064，config_path是 `/home/linux/xensesdk/xensesdk/`，则在/home/linux/xensesdk/xensesdk/ 下需要包含名为OP000064的标定文件。

### 返回

- 一个 `Sensor` 对象

### 示例

```python
from xensesdk.xenseInterface.XenseSensor import Sensor
sensor = Sensor.create('OP000064', config_path = 'config/') # config_path 是配置文件的路径，config_path下需要有名为OP000064的配置文件
```

## 2. `selectSensorInfo` 方法

### 描述

获取传感器信息

### 输入参数

args: 需要获取的传感器数据种类, `Sensor.OutputType` 类型的枚举量, 可选如下:

* Difference : 差分图像
* Depth : 深度图
* Marker2D : Marker点的二维像素坐标
* Marker2DInit : Marker点的初始二维坐标
* Marker3D : Marker点的三维坐标
* Marker3DInit : Marker点的初始三维坐标
* Marker3DFlow : Marker3D - Marker3DInit
* Force : 三维分布力
* ForceNorm : 法向分布力

### 返回

- 计算得到的传感器信息

### 示例

```python
from xensesdk.xenseInterface.XenseSensor import Sensor

sensor = Sensor.create(camera_id,config_path = configPath)
difference, marker3d, marker3dInit, marker3dFlow, depth= sensor.selectSensorInfo(
    Sensor.OutputType.Difference, 
    Sensor.OutputType.Marker3D, 
    Sensor.OutputType.Marker3DInit,
    Sensor.OutputType.Marker3DFlow,
    Sensor.OutputType.Depth
)
```

## 3. `startSaveSensorInfo` 方法

### 描述

开始录像

### 输入参数

- data_to_save: list，用于选择要记录的数据类型：

  - Sensor.OutputType.Difference
  - Sensor.OutputType.Depth
  - Sensor.OutputType.Marker2D
- path: 数据流保存路径

### 返回

- None

### 示例

```python
from xensesdk.xenseInterface.XenseSensor import Sensor

sensor = Sensor.create(camera_id,config_path = configPath)
data_to_save = [
    Sensor.OutputType.Difference,
    Sensor.OutputType.Depth,
    Sensor.OutputType.Marker2D
]
sensor.startSaveSensorInfo(path, data_to_save)
```

## 4. `stopSaveSensorInfo` 方法

### 描述

停止录像

### 输入参数

- None

### 返回

- None

### 示例

```python
from xensesdk.xenseInterface.XenseSensor import Sensor

sensor = Sensor.create(camera_id, config_path = configPath)
data_to_save = [
    Sensor.OutputType.Difference,
    Sensor.OutputType.Depth,
    Sensor.OutputType.Marker2D
]
sensor.startSaveSensorInfo(path, data_to_save)
# ...

sensor.stopSaveSensorInfo()
```

## 常见问题解答 (FAQ)

**问：** 无法加载 Qt 平台插件 "xcb" 虽然它已被找到，错误信息为 "..."
**答：**

```shell
sudo apt install libxcb-cursor0 
```

**问：** 无法加载 Qt 平台插件 "xcb" 虽然它已被找到，错误信息为 "..."
**答：** 进入 `.../site-packages/.../Qt/plugins/platform` 目录并删除 `libqxcb.so` 文件。

**问：** from 6.5.0, xcb-cursor0 or libxcb-cursor0 is needed to load the Qt xcb platform plugin.
Could not load the Qt platform plugin "xcb" in "" even though it was found. This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.
**答：** 终端内执行：

```shelll
sudo apt-get update
sudo apt-get install libxcb-cursor0
```
