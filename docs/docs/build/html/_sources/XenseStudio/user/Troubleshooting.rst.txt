.. _tag_troubleshooting:

V. Troubleshooting
======================


1. Printing During Initialization
-------------------------------------

    Problem Description:

        The first launch and loading after installation may be relatively slow.

    Solution:

        During initialization, all components need to be loaded and cached for the first time. Normal usage will be restored in subsequent launches.

2. Graphics Card Driver
---------------------------

    Problem Description:

        The software can start without a sensor connected, but fails to start when a sensor is connected. The command line may show similar errors or outputs as follows:

    .. code-block:: bash
        :caption: Command Line Output
        :linenos:

        Segmentation fault (core dumped)
        Segmentation Fault
        Init infer engine   
        infer session using CPU(GPU) 
           

    Solution:

        This issue is most likely caused by a graphics card driver problem.
        First, install a compatible graphics card driver.
        (If the graphics card is an NVIDIA card) Check if the following command outputs normally. If not, install a compatible graphics card driver first.

    .. code-block:: bash
        :caption: Command Line Input

        nvidia-smi
        
3. Error Handling
---------------------

    Problem Description:

    .. code-block:: bash
        :caption: Command Line Output
        :linenos:

        From version 6.5.0, xcb-cursor0 or libxcb-cursor0 is needed to load the Qt xcb platform plugin.
        Could not load the Qt platform plugin "xcb" in "" even though it was found. This
        application failed to start because no Qt platform plugin could be initialized.
        Reinstalling the application may fix this problem.
        
        
    Solution:

    .. code-block:: bash
        :caption: Command Line Input
        :linenos:

        sudo apt-get update
        sudo apt-get install libxcb-cursor0