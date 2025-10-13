.. _tag_ezros_example:

使用EzROS命令行工具
========================

.. container:: ezros-tool-guide

    初次使用可以通过以下命令来快速了解 ezros 的功能。

    .. code-block:: bash

        ezros -h
        # 或者 ezros --help

    终端打印如下信息：

    .. code-block:: text

        usage: ezros [-h] [-d DOMAIN_ID] [-q] [-a] [-t TIMEOUT] [-f FILTER] {service,topic} ...

        EzROS CLI - 简单的网络工具

        positional arguments:
          {service,topic}       命令
            service             调用服务
            topic               监听话题

        optional arguments:
          -h, --help            show this help message and exit
          -d DOMAIN_ID, --domain-id DOMAIN_ID
                                DDS域ID
          -q, --quiet           静默模式
          -a, --all             显示所有节点信息
          -t TIMEOUT, --timeout TIMEOUT
                                扫描超时时间(秒),默认2秒
          -f FILTER, --filter FILTER
                                过滤包含指定字符串的节点名，默认匹配所有节点

    .. container:: ezros-cmd-catalog-section

        更多详细用法请见目录 EzROS 中的调试命令:

        .. container:: command-catalog

            - :ref:`查看EzROS服务信息 <tag_all_info>`
            - :ref:`监控话题 <tag_echo>`
            - :ref:`调用服务 <tag_service>`

.. toctree::
   :maxdepth: 2
   :caption: 目录
   :hidden:

   API/all_info
   API/echo
   API/service