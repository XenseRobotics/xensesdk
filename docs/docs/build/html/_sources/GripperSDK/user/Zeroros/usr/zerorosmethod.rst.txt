.. _tag_zeroroslist:

如何使用EzROS调试工具?
================================

.. container:: step-block

    初次使用可以通过以下命令来快速了解ezros的功能

    .. code-block:: bash

        ezros -h 
        
        #或者ezros --help
        #或者ezros
    
    终端打印如下信息:

    .. code-block:: bash

        usage: ezros [-h] [-d DOMAIN_ID] [-q] [-a] [-t TIMEOUT] {service,topic} ...

        EzROS CLI - 简单的网络工具

        optional arguments:
        -h, --help                  show this help message and exit
        -d DOMAIN_ID, --domain-id   DOMAIN_ID
                                    DDS域ID
        -q, --quiet                 静默模式
        -a, --all                   显示所有节点信息
        -t TIMEOUT, --timeout TIMEOUT
                                    扫描超时时间(秒)，默认2秒
        -f FILTER, --filter FILTER
                                    过滤包含指定字符串的节点名，默认匹配所有节点

        commands:
        {service,topic}             命令
            service                 调用服务
            topic                   监听话题
    
.. container:: step-block

    更多详细用法请见目录EzROS中的调试命令

    
    .. list-table::
        :width: 30
        :header-rows: 1

        * - 命令目录
         
        * - :ref:`查看EzROS服务信息 <tag_all_info>`
        
        * - :ref:`监控话题 <tag_topic>` 
        
        * - :ref:`调用服务 <tag_service>` 

         
.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: 目录
    
    API/all_info

    API/echo

    API/service
    
