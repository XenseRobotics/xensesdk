.. _tag_vis:

跨域通信
===================================

.. container:: step-block

    通过DDS域实现逻辑隔离,不同域之间通信可通过以下命令实现:

    .. tabs::

        .. tab:: 监控域0话题

            .. code-block:: python

                ezros -d 0 topic -e OG000285

        .. tab:: 监控域1话题

            .. code-block:: python

                ezros -d 1 topic -e OG000285

        .. tab:: 查看域0信息

            .. code-block:: python

                ezros -d 0 -a

        .. tab:: 查看域1信息

            .. code-block:: python

                ezros -d 1 -a
    
    以下为打印信息：

    .. tabs::

          .. tab:: 监控域0话题

            .. code-block:: python

                监听话题: OG000285
                持续时间: 30 秒
                按 Ctrl+C 停止
                ============================================================
                成功订阅话题 OG000285 (类型: BytesMessage)
                开始监听话题 OG000285...

                [03:47:15] [OG000285]: {<OutputType.Difference: 2>: array([[[109, 110, 111],
                        [110, 110, 111],
                        [111, 111, 111],
                        ...,
                        [122, 110, 120],
                        [133, 109, 129],
                        [139, 109, 133]],

                    [[108, 110, 109],
                        [109, 110, 110],
                        [110, 111, 110],
                        ...,
                        [122, 111, 122],
                        [134, 110, 131],
                        [141, 110, 136]]

        .. tab:: 监控域1话题

            .. code-block:: python

                监听话题: OG000285
                持续时间: 30 秒
                按 Ctrl+C 停止
                ============================================================
                成功订阅话题 OG000285 (类型: BytesMessage)
                开始监听话题 OG000285...


                监听被用户中断

        .. tab:: 查看域0信息

            .. code-block:: python

                ================================================================================
                EzROS 网络节点信息
                ================================================================================
                1. Node: OG000249 (udp/192.168.1.127:44188)
                Topics:
                    - OG000249
                Services:
                    - OG000249: [get_img, calibrate, terminate_node, reset_fetch_types, check_is_alive]

                2. Node: OG000285 (udp/192.168.1.127:60052)
                Topics:
                    - OG000285
                Services:
                    - OG000285: [get_img, calibrate, terminate_node, reset_fetch_types, check_is_alive]

                3. Node: gripper_d672f584b17a (udp/192.168.1.127:46730)
                Topics:
                    - gripper_d672f584b17a
                Services:
                    - gripper_d672f584b17a: [restart_control_subscriber, set_led_color]

                4. Node: gripper_d672f584b17a* (udp/192.168.1.63:55100)
                Topics:
                    - gripper_control_d672f584b17a

                5. Node: master_d672f584b17a (udp/192.168.1.127:42042)
                Services:
                    - master_d672f584b17a: [kill_sensor, scan_gripper_sn, reboot, launch_gripper, scan_sensor_sn, kill_gripper, check_sensor_online, launch_sensor, check_gripper_online]

                6. Node: service_server_example (udp/192.168.1.60:57441)
                Services:
                    - math_service: [multiply, block_time, add, stats]

        .. tab:: 查看域1信息

            .. code-block:: python

                ================================================================================
                EzROS 网络节点信息
                ================================================================================
                未发现任何节点
            
.. admonition:: tips
    :class: tip

    --domain-id/-d    全局参数,指定DDS域ID;

    由ezros -d 0 和 ezros -d 1 可见,不同域之间的节点、话题和服务是隔离的,需要通过指定域ID来访问对应域内的信息,如需跨域访问,请确保对应域内有网关节点在运行。


