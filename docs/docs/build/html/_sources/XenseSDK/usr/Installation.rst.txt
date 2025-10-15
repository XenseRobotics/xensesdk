.. _tag_xensesdkinstallation:

**********************
Installing XenseSDK
**********************

Installation Guide
----------------------
.. container:: step-block

    **Step 1:** Prepare the Python Development Environment



    .. code-block:: bash
        
        # Navigate to the Xense SDK directory
        cd xensesdk

        # Create and activate a virtual environment
        conda create -n xenseenv python=3.9
        # or conda create -n xenseenv python=3.10

        conda activate xenseenv

.. note:: 

    It is recommended to use Anaconda with Python version 3.9 or 3.10.

.. container:: step-block

    **Step 2:** Install CUDA Toolkit and cuDNN

    The SDK requires onnxruntime_gpu, along with the matching cuDNN and cudatoolkit. Select the following installation method based on your environment:

    .. tab-set::

        .. tab-item:: Option 1: onnxruntime_gpu>1.18.0  

            1. Install the required versions:

            .. code-block:: bash

                # This example uses CUDA 12.9
                conda install nvidia/label/cuda-12.9.0::cuda-toolkit nvidia::cudnn

            2. Add the CUDA path to the environment variable 'LD_LIBRARY_PATH':

            .. code-block:: bash

                # Run the following command in Linux
                export LD_LIBRARY_PATH=$CONDA_PREFIX/lib:$CONDA_PREFIX/lib64 # (Temporary)
                mkdir -p $CONDA_PREFIX/etc/conda/activate.d && echo 'export LD_LIBRARY_PATH=$CONDA_PREFIX/lib:$CONDA_PREFIX/lib64:$LD_LIBRARY_PATH' > $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh # (Permanent)

        .. tab-item:: Option 2: onnxruntime_gpu==1.18.0 (Not available for Series 50 GPUs)  

            1. Search for the required versions:

            .. code-block:: bash

                conda search cudnn
                conda search cudatoolkit

            2. Install the required versions:

            .. code-block:: bash

                conda install cudnn==8.9.2.26 cudatoolkit==11.8.0


.. container:: step-block

    **Step 3:** Install the Xense SDK Package
    Install the SDK package into your environment:

    .. code-block:: bash

        # Install from a local directory (for custom packages)
        pip install xensesdk-0.1.0-cp39-cp39-win_amd64.whl 
        # Or install from PyPI
        pip install xensesdk -i https://repo.huaweicloud.com/repository/pypi/simple/