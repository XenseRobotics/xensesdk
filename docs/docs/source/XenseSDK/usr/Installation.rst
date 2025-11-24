.. _tag_xensesdkinstallation:

***************
安装XenseSDK
***************

安装指南
-------------
.. container:: step-block

    **步骤 1:** 准备 Python 开发环境

    .. code-block:: bash

        # 进入 Xense SDK 目录
        cd xensesdk

        # 创建并激活虚拟环境
        conda create -n xenseenv python=3.9
        # or conda create -n xenseenv python=3.10
        conda activate xenseenv

.. note:: 

    推荐使用 Anaconda,并使用 Python 版本 3.9或者3.10。

.. container:: step-block

    **步骤 2:** 安装 CUDA 工具包和 cuDNN

    SDK 需要 onnxruntime_gpu，以及配套的 cudnn、cudatoolkit。根据您的环境，选择以下安装方式：

    .. tab-set::

        .. tab-item:: 选项 1：onnxruntime_gpu>1.18.0  

            1. 安装所需版本：

            .. code-block:: bash

                # 这个例子使用 cuda12.9
                conda install nvidia/label/cuda-12.9.0::cuda-toolkit nvidia::cudnn

            2. 将 cuda 的路径加入环境变量 ‘LD_LIBRARY_PATH‘：

            .. code-block:: bash

                # linux 里可以运行如下命令
                export LD_LIBRARY_PATH=$CONDA_PREFIX/lib:$CONDA_PREFIX/lib64 #（临时）
                mkdir -p $CONDA_PREFIX/etc/conda/activate.d && echo 'export LD_LIBRARY_PATH=$CONDA_PREFIX/lib:$CONDA_PREFIX/lib64:$LD_LIBRARY_PATH' > $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh #（永久）

        .. tab-item:: 选项 2: onnxruntime_gpu==1.18.0 (50 系列显卡不可用)  

            1. 搜索所需版本：

            .. code-block:: bash

                conda search cudnn
                conda search cudatoolkit

            2. 安装所需版本：

            .. code-block:: bash

                conda install cudnn==8.9.2.26 cudatoolkit==11.8.0

.. container:: step-block

    **步骤 3:** 安装 Xense SDK 包
    将 SDK 包安装到您的环境中:

    .. code-block:: bash

        # 如果是从本地目录安装
        pip install xensesdk-0.1.0-cp39-cp39-win_amd64.whl # (对于定制软件包)
        # 或者从 PyPI 安装
        pip install xensesdk -i https://repo.huaweicloud.com/repository/pypi/simple/ 

.. container:: step-block

    **步骤 4:** ubuntu环境注意事项
    
    在ubuntu环境下初次安装 ``>=1.6.7`` 的xensesdk时，先执行下方脚本才能正常使用。

    .. code-block:: bash

        #!/bin/bash

        # 1) 创建组（若已存在不会报错）
        sudo groupadd -f xense

        # 如果规则文件已存在，先删除（可选）
        if [ -f '/etc/udev/rules.d/99-xense.rules' ]; then
            echo "Udev rule already exists, removing old one..."
            sudo rm /etc/udev/rules.d/99-xense.rules
        fi

        # 2) 写 udev 规则（匹配 vendor id 3938，适用于所有当前和将来 Xense 设备）
        sudo tee /etc/udev/rules.d/99-xense.rules > /dev/null <<'EOF'
        # 99-xense.rules - allow users in 'xense' group to access Xense Robotics USB devices
        SUBSYSTEM=="usb", ENV{DEVTYPE}=="usb_device", ATTR{idVendor}=="3938", MODE="0660", GROUP="xense"
        EOF

        # 3) 重新加载 udev 规则并触发（使规则生效）
        sudo udevadm control --reload-rules
        sudo udevadm trigger

        # 4) 把你（或其它用户）加入 xense 组（替换为具体用户名或多次运行）
        sudo usermod -aG xense $USER

        echo "Xense udev rule installed. Please reboot"
