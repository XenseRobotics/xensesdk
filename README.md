# Xense SDK 文档

**如有使用问题，请添加微信 qjrobot9966 来交流**

SDK开发文档和软件操作手册更新至： https://xensedoc.readthedocs.io/en/latest/

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

SDK 需要 **onnxruntime_gpu**，以及配套的**cudnn、 cudatoolkit**。根据您的环境，选择以下安装方式：

#### 选项 1: onnxruntime_gpu>1.18.0

1. 安装所需版本：
   ```bash
   # 这个例子使用cuda12.9
   conda install nvidia/label/cuda-12.9.0::cuda-toolkit nvidia::cudnn
   ```
2. 将cuda的路径加入环境变量 ‘LD_LIBRARY_PATH‘：
   ```bash
   # linux里可以运行如下命令
   export LD_LIBRARY_PATH=$CONDA_PREFIX/lib:$CONDA_PREFIX/lib64 #（临时）
   mkdir -p $CONDA_PREFIX/etc/conda/activate.d && echo 'export LD_LIBRARY_PATH=$CONDA_PREFIX/lib:$CONDA_PREFIX/lib64:$LD_LIBRARY_PATH' > $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh #（永久）
   ```

#### 选项 2: onnxruntime_gpu==1.18.0 (50系列显卡不可用)

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
pip install xensesdk -i https://repo.huaweicloud.com/repository/pypi/simple/
```
或:
```bash
pip install xensesdk-0.1.0-cp39-cp39-win_amd64.whl # (对于定制软件包)
```

---

### 步骤 4: ubuntu环境注意事项

在ubuntu环境下初次安装 `>=1.6.7` 的xensesdk时，先执行下方脚本才能正常使用。
```
#!/bin/bash

# 1) 创建组（若已存在不会报错）
sudo groupadd -f xense

# 如果规则文件已存在，先删除（可选）
if [ -f '/etc/udev/rules.d/99-xense.rules' ]; then
    echo "Udev rule already exists, removing old one..."
    sudo rm /etc/udev/rules.d/99-xense.rules
fi

# 2) 写 udev 规则（匹配 vendor id 3938，适用于所有当前和将来 Xense 设备）
sudo tee /etc/udev/rules.d/99-xense.rules > /dev/null <<EOF
# 99-xense.rules - allow users in 'xense' group to access Xense Robotics USB devices
SUBSYSTEM=="usb", ENV{DEVTYPE}=="usb_device", ATTR{idVendor}=="3938", MODE="0660", GROUP="${USER}"
EOF

# 3) 重新加载 udev 规则并触发（使规则生效）
sudo udevadm control --reload-rules
sudo udevadm trigger


echo "Xense udev rule installed. Please reboot"
```
执行完上述操作后重启电脑

## 示例程序

### 示例源代码

可以在以下目录中查找示例源代码：

```
site-packages/xensesdk/examples/*
```

一个简单的例程如下:

```python
from xensesdk import Sensor
from time import sleep

def main():
    # 1. 创建传感器

    sensor = Sensor.create('OP000064')

    # 2. 读取传感器数据
    #   sensor.selectSensorInfo 可以通过传入 `Sensor.OutputType` 枚举量获取相应的传感器数据, 顺序或者数量无限制
    #   可选的输出类型参考API说明
    while True:
        rectify_img, depth= sensor.selectSensorInfo(Sensor.OutputType.Rectify, Sensor.OutputType.Depth)

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

创建一个传感器实例，在结束时请调用`release`。

### 输入参数

* **cam\_id** (`int | str`, 可选): 传感器 ID、序列号或视频路径。默认为 0。
* **use\_gpu** (`bool`, 可选): 是否使用 GPU 推理，默认为 True。
* **config\_path** (`str | Path`, 可选): 配置文件路径或目录。如果是目录，需包含与传感器序列号同名的标定文件。
* **api** (`Enum`, 可选): 相机 API 类型（如 OpenCV 后端），用于指定相机访问方式。
* **check\_serial** (`bool`, 可选): 是否检查传感器序列号，默认 True。
* **rectify\_size** (`tuple[int, int]`, 可选): 校正图像尺寸。
* **ip\_address** (`str`, 可选): 远程连接使用的相机 IP。
* **video\_path** (`str`, 可选): 离线模拟的视频路径。

### 返回

* `Sensor` 对象

### 示例

```python

# Example 1：  用SN码开启
from xensesdk import Sensor
sensor = Sensor.create('OP000064') 

# Example 2：  用相机编号开启
sensor = Sensor.create(0) 

# Example 3： 打开储存的数据
sensor = Sensor.create(None, video_path=r"data.h5")

# Example 4： 打开算力板上的传感器
sensor =  Sensor.create('OP000064', ip_address="192.168.66.66")
```

---

## 2. `selectSensorInfo` 方法

### 描述

获取指定类型的传感器数据。

### 输入参数

* **args**: 任意数量的 `Sensor.OutputType` 枚举，用于指定需要获取的数据类型：

    * Rectify: Optional[np.ndarray]          # 校正图像, shape=(700, 400, 3), RGB
    * Difference: Optional[np.ndarray]       # 差分图像, shape=(700, 400, 3), RGB
    * Depth: Optional[np.ndarray]            # 深度图像, shape=(700, 400), 单位mm

    * Marker2D: Optional[np.ndarray]         # 切向位移, shape=(26, 14, 2)
    * Force: Optional[np.ndarray]            # 三维力分布, shape=(35, 20, 3)
    * ForceNorm: Optional[np.ndarray]        # 法向力分量, shape=(35, 20, 3)
    * ForceResultant: Optional[np.ndarray]   # 六维合力, shape=(6,)

    * Mesh3D: Optional[np.ndarray]           # 当前帧3D网格, shape=(35, 20, 3)
    * Mesh3DInit: Optional[np.ndarray]       # 初始3D网格, shape=(35, 20, 3)
    * Mesh3DFlow: Optional[np.ndarray]       # 网格形变向量, shape=(35, 20, 3)

    * TimeStamp: Optional[np.ndarray]        # 传感器时间戳，shape=(26,14,2)

### 返回

* 所请求的传感器数据（返回数量和顺序与参数一致）

### 示例

```python
from xensesdk import Sensor
sensor = Sensor.create('OP000064') 
rectify, marker3d, marker3dInit, marker3dFlow, depth = sensor.selectSensorInfo(
    Sensor.OutputType.Rectify, 
    Sensor.OutputType.Marker3D, 
    Sensor.OutputType.Marker3DInit,
    Sensor.OutputType.Marker3DFlow,
    Sensor.OutputType.Depth
)
...
sensor.release()
```

---

## 3. `calibrateSensor` 方法

### 描述

重新校准传感器，(需在无物理接触时调用)。

---

## 4. `scanSerialNumber` 方法

### 描述

扫描并返回当前设备上所有已连接的传感器信息。

该方法会检测系统中已连接的传感器设备，返回其序列号与对应的相机 ID 映射关系，方便后续通过序列号创建传感器实例。

### 返回

* 包含所有已连接传感器的字典，键为传感器序列号( serial_number )，值为对应的相机 ID( camera_id )

---


## 5. `getCameraID` 方法

### 描述

获取当前传感器的相机编号。

---

## 6. `createSolver` 方法

### 描述

工厂方法（类方法），用于从给定的 runtime 配置路径创建一个 SensorSolver 实例。

### 输入参数

* **runtime\_path** (`Union[str, Path]`): 指向 runtime 配置文件的路径。


### 返回

* 成功时返回 SensorSolver 实例，失败时返回 False。

### 示例

```python
from pathlib import Path
SCRIPT_DIR = Path(__file__).resolve().parent
SAVE_DIR = Path(SCRIPT_DIR / "test_dir")  # 存放目录
SAVE_DIR.mkdir(parents=True, exist_ok=True)
import cv2
import time
import numpy as np

from xensesdk import Sensor

sensor_id = 'OG000232'

def save_data():
    fps = 30
    duration = 3   # 秒
    frame_interval = 1.0 / fps
    total_frames = fps * duration

    sensor_0 = Sensor.create(sensor_id)
    for i in range(total_frames):
        start_time = time.time()

        # 采集一帧
        rec = sensor_0.selectSensorInfo(Sensor.OutputType.Rectify)

        # 生成文件名
        filename = SAVE_DIR / f"{sensor_id}_{i:03d}.png"

        # 保存图片
        cv2.imwrite(str(filename), rec)
        print(f"Saved {filename}")

        # 控制帧率（30Hz）
        elapsed = time.time() - start_time
        sleep_time = frame_interval - elapsed
        if sleep_time > 0:
            time.sleep(sleep_time)

    # 导出配置
    sensor_0.exportRuntimeConfig(SAVE_DIR)

    sensor_0.release()

def replay_data():
    sensor_solver = Sensor.createSolver(SAVE_DIR / f"runtime_{sensor_id}")
    for png_file in sorted(SAVE_DIR.glob("*.png")):
        if not png_file.name.endswith("_depth.png"):
            img = cv2.imread(str(png_file), cv2.IMREAD_UNCHANGED)
            depth, force, diff = sensor_solver.selectSensorInfo(
                Sensor.OutputType.Depth,
                Sensor.OutputType.Force,
                Sensor.OutputType.Difference,
                rectify_image=img
            )
            depth_vis = np.clip(depth*200, 0, 255)
            cv2.imwrite(SAVE_DIR / f"{png_file.stem}_depth.png", depth_vis)

    sensor_solver.release()

if __name__ == '__main__':
    save_data()
    replay_data()
    print("Data saved and replayed successfully.")
```

---

## 7. `exportRuntimeConfig` 方法

### 描述

将当前传感器的运行时配置导出到指定目录。

### 输入参数

* **save\_dir** (`Union[str, Path]`，可选): 配置文件保存目录，默认为当前目录。
* **binary** (`bool`，可选): 是否返回二进制加密数据而非保存到文件，默认为 False。


### 返回

* 无

### 示例

```python
from pathlib import Path
SCRIPT_DIR = Path(__file__).resolve().parent
SAVE_DIR = Path(SCRIPT_DIR / "test_dir")  # 存放目录
SAVE_DIR.mkdir(parents=True, exist_ok=True)
import cv2
import time
import numpy as np

from xensesdk import Sensor

sensor_id = 'OG000232'

def save_data():
    fps = 30
    duration = 3   # 秒
    frame_interval = 1.0 / fps
    total_frames = fps * duration

    sensor_0 = Sensor.create(sensor_id)
    for i in range(total_frames):
        start_time = time.time()

        # 采集一帧
        rec = sensor_0.selectSensorInfo(Sensor.OutputType.Rectify)

        # 生成文件名
        filename = SAVE_DIR / f"{sensor_id}_{i:03d}.png"

        # 保存图片
        cv2.imwrite(str(filename), rec)
        print(f"Saved {filename}")

        # 控制帧率（30Hz）
        elapsed = time.time() - start_time
        sleep_time = frame_interval - elapsed
        if sleep_time > 0:
            time.sleep(sleep_time)

    # 导出配置
    sensor_0.exportRuntimeConfig(SAVE_DIR)

    sensor_0.release()

def replay_data():
    sensor_solver = Sensor.createSolver(SAVE_DIR / f"runtime_{sensor_id}")
    for png_file in sorted(SAVE_DIR.glob("*.png")):
        img = cv2.imread(str(png_file), cv2.IMREAD_UNCHANGED)
        depth, force, diff = sensor_solver.selectSensorInfo(
            Sensor.OutputType.Depth,
            Sensor.OutputType.Force,
            Sensor.OutputType.Difference,
            rectify_image=img
        )
        depth_norm = cv2.normalize(depth, None, 0, 255, cv2.NORM_MINMAX)
        depth_vis = np.uint8(depth_norm)
        cv2.imwrite(SAVE_DIR / f"{png_file.stem}_depth.png", depth_vis)

    sensor_solver.release()

if __name__ == '__main__':
    save_data()
    replay_data()
    print("Data saved and replayed successfully.")
```

---

## 8. `call_service` 方法

### 描述

调用算力板上的服务。

### 输入参数

* **master\_ip** (`str`): 算力板 IP 地址，例如: 192.168.99.2。
* **service\_name** (`str`): 服务名称。
* **action\_name** (`str`): 服务支持的 action 名称。
* **args** : 传递给服务的可变参数。
* **kwargs** : 传递给服务的关键字参数。


### 返回

* 字典，结构为: {"success": True, "ret": ret}，其中： success: 布尔值，表示调用是否成功 ret: 服务返回的具体结果数据

---

## 9. `release` 方法

### 描述

释放资源，关闭传感器。

---

## 常见问题解答 (FAQ)

**问：** 无法加载 Qt 平台插件 "xcb" 虽然它已被找到，错误信息为 "..."

**答：** 进入 `.../site-packages/.../Qt/plugins/platform` 目录并删除 `libqxcb.so` 文件。

**问：** from 6.5.0, xcb-cursor0 or libxcb-cursor0 is needed to load the Qt xcb platform plugin.
Could not load the Qt platform plugin "xcb" in "" even though it was found. This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

**答：** 终端内执行：

```shelll
sudo apt-get update
sudo apt-get install libxcb-cursor0
```

