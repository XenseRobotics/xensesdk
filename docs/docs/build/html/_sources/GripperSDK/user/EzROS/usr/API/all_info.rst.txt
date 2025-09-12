.. _tag_all_info:

查看ezros服务信息
========================

.. container:: step-block

    初次使用可以通过以下命令来快速了解 ezros 的功能。

    .. code-block:: bash

        ezros -a
        # 或者 ezros --all

    终端打印如下信息：

    .. code-block:: text

        扫描网络中... (预计 2 秒)
        [███████████████████████████░░░] 90%
        ================================================================================
        EzROS 网络节点信息
        ================================================================================
        1. Node: gripper_d672f584b17a (udp/192.168.1.127:46067)
          Topics:
            - gripper_d672f584b17a
          Services:
            - gripper_d672f584b17a: [set_led_color, restart_control_subscriber]

        2. Node: master_d672f584b17a (udp/192.168.1.127:59477)
          Services:
            - master_d672f584b17a: [scan_sensor_sn, kill_sensor, launch_camera, launch_gripper, list_camera, reboot, kill_camera, launch_sensor, kill_gripper]

    其中 master 节点后的 “d672f584b17a” 字符串代表 MAC 地址，可以根据这个地址来创建 gripper 夹爪实例：

    .. code-block:: python

        from xensegripper import XenseGripper

        gripper = XenseGripper.create("d672f584b17a")


.. admonition:: tips
    :class: tip 

    -all/-a 全局参数，用于触发“全量信息展示”功能