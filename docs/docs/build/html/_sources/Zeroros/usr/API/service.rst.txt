.. _tag_service:

测试Service
==============

.. container:: step-block

    当要对特定Service服务查询时,可使用如下命令: 

    .. tabs::

        .. tab:: Sensor对应服务

            .. code-block:: python

                zeroros_cli -azeroros_cli service --name OG000266 --cmd get_img
                
                #zeroros_cli service --name {service_name} --cmd {action_name}


        .. tab:: Gripper对应服务

            .. code-block:: python

                zeroros_cli service --name gripper_9a14e81bb832 --cmd control_gripper_pos:=10,80,27
                
                #zeroros_cli service --name {service_name} --cmd {action_name}:={args}

    .. tabs::

        .. tab:: get_img服务 成功

            .. code-block:: python
            
                Calling service 'OG000266' with command 'get_img' and arguments []
                {'success': True, 'ret': array([[[229, 135, 100],
                        [232, 136, 101],
                        [232, 137, 100],
                        ...,
                        [221, 145,  89],
                        [222, 144, 106],
                        [213, 128,  94]],

                    [[225, 134,  98],
                        [228, 137, 101],
                        [232, 137, 100],
                        ...,
                        [220, 144,  92],
                        [217, 139, 104],
                        [219, 136, 107]],

                    ...,

                    [[194, 119,  66],
                        [195, 116,  69],
                        [200, 119,  73],
                        ...,
                        [197, 139,  45],
                        [197, 137,  54],
                        [196, 134,  63]]], dtype=uint8)}

        .. tab:: get_img服务 失败

            .. code-block:: python
                
                ValueError: Service OG000266 not found.

        .. tab:: control_gripper_pos服务 成功

            .. code-block:: python

                Calling service 'gripper_9a14e81bb832' with command 'control_gripper_pos' and arguments [10, 80, 27]
                {'success': True, 'ret': {'success': True}}

        .. tab:: control_gripper_pos服务 失败

            .. code-block:: python

                ValueError: Service gripper_9a14e81bb832 not found.

.. admonition:: tips
    :class: tip

    ``--name/-n`` 指定服务器名称, ``--cmd/-c`` 指定aciton名称,如果anciton包含参数,使用 ``:=`` 连接参数,多个参数使用 ``,`` 分隔。

    上述指令的参数参考
    `zeroros_cli -a <./all_info.html>`_ 的打印信息。