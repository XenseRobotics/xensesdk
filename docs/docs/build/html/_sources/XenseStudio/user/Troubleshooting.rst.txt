.. _tag_troubleshooting:

五、故障排查
================

常见问题及解决方案
----------------------

(1)	初始化时打印

    问题描述：

        安装后的初次启动加载会比较慢

    解决方案：

        初始化时，第一次需要加载所有组件并缓存，后续可正常使用

(2)	显卡驱动

    问题描述：

        如果不插传感器能启动,但插传感器无法启动，且命令行有如下类似报错或输出

    .. code-block:: bash
        :caption: 命令行输出
        :linenos:

        段错误已中止(核心已转储)
        Segmentation Fault
        Init infer engine   
        infer session using CPU(GPU) 
           

    解决方案：

        大概率是显卡驱动问题,
        先安装适配的显卡驱动
        (如果显卡是nvidia显卡的话)检查如下命令是否正常输出,如果不正常的话，先安装适配的显卡驱动。

    .. code-block:: bash
        :caption: 命令行输入

        nvidia-smi
        
(3)	报错：

    问题描述：

    .. code-block:: bash
        :caption: 命令行输出
        :linenos:

        from 6.5.0, xcb-cursor0 or libxcb-cursor0 is needed to lload the Qt xcb platform plugin.
        Could not load the Qt platform plugin "xcb" in "" even tkhough it was found. This
        application failed to start because no Qt platform plugiIn could be initialized.
        Reinstalling the application may fix this problem.
        
        
    解决方案：

    .. code-block:: bash
        :caption: 命令行输入
        :linenos:

        sudo apt-get update
        sudo apt-get install libxcb-cursor0
        
    