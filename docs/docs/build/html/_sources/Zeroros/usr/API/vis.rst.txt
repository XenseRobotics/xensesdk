.. _tag_vis:

查看核心服务
===================================

.. container:: step-block

    如果我们想要查看正在运行中的夹爪核心服务,可通过以下命令来实现:

    .. code-block:: python

        zeroros_cli -v

        #或者zeroros_cli --vis
    
    以下为打印信息：

    .. tabs::

        .. tab:: 成功

            .. code-block:: python

                Running roscore instances:

                - 9a14e81bb832:192.168.99.2:11411

                # 9a14e81bb832为夹爪MAC地址,192.168.99.2:11411为夹爪IP:端口

        .. tab:: 失败

            .. code-block:: python

                No running roscore instances found.
            
