.. _tag_all_info:

查看ezros服务信息
========================

.. container:: step-block

    EzROS 支持通过全局参数组合，实现“全量信息展示”或“指定节点过滤展示”，以下分场景说明具体用法：

    **场景1: 查看所有节点、话题和服务（全量信息）**  

    通过 ``-a/--all`` 参数触发全量扫描，展示网络中所有节点的完整信息：

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


    **场景2: 过滤查看指定节点（仅展示含目标字符串的节点）**  
    
    结合 ``-a/--all`` 和 ``-f/--filter`` 参数，仅展示节点名包含指定字符串的信息（如仅看“gripper”相关节点）：

    .. code-block:: bash

        ezros -a -f gripper  # 过滤节点名包含"gripper"的信息

    终端打印如下信息(仅保留含“gripper”的节点):

    .. code-block:: text

        扫描网络中... (预计 2 秒)
        [███████████████████████████░░░] 90%
        ================================================================================
        EzROS 网络节点信息
        ================================================================================
        1. Node: gripper_d672f584b17a (udp/192.168.1.127:58614)
          Topics:
            - gripper_d672f584b17a
          Services:
            - gripper_d672f584b17a: [restart_control_subscriber, set_led_color]


    两种场景中，节点名后的 “d672f584b17a” 字符串均代表设备 MAC 地址，可用于创建 gripper 夹爪实例：

    .. code-block:: python

        from xensegripper import XenseGripper

        gripper = XenseGripper.create("d672f584b17a")


.. admonition:: tips
    :class: tip 

    - ``-a/--all``: 全局参数，用于触发“全量信息展示”功能，扫描并显示所有节点信息。
    - ``-f/--filter``: 全局参数，需与 ``-a`` 搭配使用，用于过滤包含指定字符串的节点名（默认匹配所有节点），例如 ``ezros -a -f master`` 可仅显示名称包含“master”的节点信息。