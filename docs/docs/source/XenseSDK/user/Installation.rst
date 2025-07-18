***************
安装XenseSDK
***************

安装指南
-------------

**步骤 1:** 准备 Python 开发环境
    推荐使用 Anaconda，并使用 Python 版本 3.9.19。

.. code-block:: bash
    :caption: 安装命令
    
    # 进入 Xense SDK 目录
    cd xensesdk

    # 创建并激活虚拟环境
    conda create -n xenseenv python=3.9.19
    conda activate xenseenv




**步骤 2:** 安装 CUDA 工具包和 cuDNN
SDK 支持 CUDA Toolkit 11.8 和 cuDNN 8.9.2.26。根据您的环境，选择以下安装方式：

选项 1: 从本地 Conda 环境包安装

.. code-block:: bash
    :caption: 安装命令

    # 安装 CUDA Toolkit 和 cuDNN
    conda install --use-local cudatoolkit-11.8.0-hd77b12b_0.conda
    conda install --use-local cudnn-8.9.2.26-cuda11_0.conda

选项 2: 通过 Conda 直接安装

搜索所需版本：

.. code-block:: bash
    :caption: 命令行输入

    conda search cudnn
    conda search cudatoolkit

安装所需版本：

.. code-block:: bash
    :caption: 命令行输入

    conda install cudnn==8.9.2.26 cudatoolkit==11.8.0






步骤 3: 安装 Xense SDK 包
将 SDK 包安装到您的环境中：

.. code-block:: bash
    :caption: 安装命令

    # 如果是从本地目录安装
    pip install xensesdk-0.1.0-cp39-cp39-win_amd64.whl # (对于定制软件包)
    # 或者从 PyPI 安装
    pip install xensesdk 

示例程序
---------------

示例源代码
可以在以下目录中查找示例源代码：

site-packages/xensesdk/examples/*

一个简单的例程如下:

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