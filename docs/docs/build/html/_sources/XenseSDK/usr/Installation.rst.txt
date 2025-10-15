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

