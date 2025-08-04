.. _tag_zeroroslist:

如何使用Zeroros_cli调试工具?
================================

.. container:: step-block

    初次使用可以通过以下命令来快速了解zeroros_cli的功能

    .. code-block:: bash

        zeroros_cli -h 
        
        #或者zeroros_cli --help
    
    终端打印如下信息:

    .. code-block:: bash

        usage: zeroros_cli [-h] [-v] [-i MASTER_IP] [-a] {core,topic,service,node,param} ...

        ZeroROS command line tool

        positional arguments:
        {core,topic,service,node,param}
                                subcommands
            core                launch roscore
            topic               topic commands
            service             service commands
            node                node commands
            param               parameter commands

        optional arguments:
        -h, --help            show this help message and exit
        -v, --vis             list running roscores
        -i MASTER_IP, --master_ip MASTER_IP
                                ROS master address, format: 192.168.99.2
        -a, --all_info        show all information, including topics, services, nodes
    
.. container:: step-block

    更多详细用法请见目录Zeroros中的调试命令

    
    .. list-table::
        :width: 30
        :header-rows: 1

        * - 命令目录
        
        * - :ref:`查看核心服务 <tag_vis>`
        
        * - :ref:`查看Zeroros服务信息 <tag_all_info>`
        
        * - :ref:`测试服务 <tag_service>` 

        * - :ref:`测试话题 <tag_topic>`
    
.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: 目录
    
    
    API/vis

    API/all_info

    API/service

    API/echo

