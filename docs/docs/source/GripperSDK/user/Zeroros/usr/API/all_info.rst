.. _tag_all_info:

查看ezros服务信息
===================================

.. container:: step-block

    如果我们想要查看ezros所有节点、话题和服务,可通过以下命令来实现:

    .. tabs::

        .. tab:: 查看所有节点信息
            
            .. code-block:: python

                ezros -a

                #或者ezros --all
        
        .. tab:: 过滤节点信息

            .. code-block:: python

                ezros -a -f gripper

                #或者ezros --all --filter gripper
    
    以下为打印信息：

    .. tabs::

        .. tab:: 查看所有节点信息
            
            .. code-block:: python

                ================================================================================
                EzROS 网络节点信息
                ================================================================================
                2. Node: OG000249 (udp/192.168.1.127:55480)
                Topics:
                    - OG000249
                Services:
                    - OG000249: [reset_fetch_types, get_img, check_is_alive, terminate_node, calibrate]

                3. Node: OG000285 (udp/192.168.1.127:50015)
                Topics:
                    - OG000285
                Services:
                    - OG000285: [get_img, reset_fetch_types, check_is_alive, terminate_node, calibrate]

                4. Node: gripper_d672f584b17a (udp/192.168.1.127:46730)
                Topics:
                    - gripper_d672f584b17a
                Services:
                    - gripper_d672f584b17a: [set_led_color, restart_control_subscriber]

                5. Node: gripper_d672f584b17a* (udp/192.168.1.63:55100)
                Topics:
                    - gripper_control_d672f584b17a

                6. Node: master_d672f584b17a (udp/192.168.1.127:42042)
                Services:
                    - master_d672f584b17a: [kill_gripper, launch_sensor, check_sensor_online, reboot, scan_gripper_sn, scan_sensor_sn, kill_sensor, check_gripper_online, launch_gripper]

                7. Node: service_server_example (udp/192.168.1.60:57441)
                Services:
                    - math_service: [stats, multiply, add, block_time]

        .. tab:: 过滤节点信息

            .. code-block:: python
                
                ================================================================================
                EzROS 网络节点信息
                ================================================================================
                1. Node: gripper_d672f584b17a (udp/192.168.1.127:46730)
                Topics:
                    - gripper_d672f584b17a
                Services:
                    - gripper_d672f584b17a: [set_led_color, restart_control_subscriber]

                2. Node: gripper_d672f584b17a* (udp/192.168.1.63:55100)
                Topics:
                    - gripper_control_d672f584b17a



      

.. admonition:: tips
    :class: tip

    --all/-a	全局参数，用于触发 “全量信息展示” 功能
    --filter/-f	全局参数，用于过滤节点名，默认匹配所有节点



        
