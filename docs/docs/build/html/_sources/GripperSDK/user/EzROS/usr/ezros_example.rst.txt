.. _tag_ezros_example:

如何使用EzROS命令行工具?
========================

.. container:: step-block

    1、初次使用可以通过以下命令来快速了解 ezros 的功能。

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

.. container:: step-block

    2、当要对特定 Topic 查询时，可以使用如下命令，以监听 Gripper 为例：

    .. code-block:: bash

        ezros topic -e gripper_d672f584b17a  -t 30

    终端输出示例：

    .. code-block:: text

        监听话题: gripper_d672f584b17a
        持续时间: 30 秒
        按 Ctrl+C 停止
        ============================================================
        成功订阅话题 gripper_d672f584b17a (类型: BytesMessage)
        开始监听话题 gripper_d672f584b17a...

        [15:36:20] [gripper_d672f584b17a]: {'position': 59.0, 'velocity': 0.0, 'force': -2.99, 'temperature': 42}
        [15:36:20] [gripper_d672f584b17a]: {'position': 59.0, 'velocity': 0.0, 'force': -2.99, 'temperature': 42}
        [15:36:20] [gripper_d672f584b17a]: {'position': 59.0, 'velocity': 0.0, 'force': -2.94, 'temperature': 42}
        [15:36:20] [gripper_d672f584b17a]: {'position': 59.0, 'velocity': 0.0, 'force': -2.94, 'temperature': 42}
        [15:36:20] [gripper_d672f584b17a]: {'position': 59.0, 'velocity': 0.0, 'force': -2.94, 'temperature': 42}
        [15:36:20] [gripper_d672f584b17a]: {'position': 59.0, 'velocity': 0.0, 'force': -2.94, 'temperature': 42}
        [15:36:20] [gripper_d672f584b17a]: {'position': 59.0, 'velocity': 0.0, 'force': -2.94, 'temperature': 42}
        [15:36:20] [gripper_d672f584b17a]: {'position': 59.0, 'velocity': 0.0, 'force': -2.94, 'temperature': 42}
        [15:36:20] [gripper_d672f584b17a]: {'position': 59.0, 'velocity': 0.0, 'force': -2.94, 'temperature': 42}
        [15:36:20] [gripper_d672f584b17a]: {'position': 59.0, 'velocity': 0.0, 'force': -2.94, 'temperature': 42}
        [15:36:20] [gripper_d672f584b17a]: {'position': 59.0, 'velocity': 0.0, 'force': -2.94, 'temperature': 42}
        [15:36:20] [gripper_d672f584b17a]: {'position': 59.01, 'velocity': 0.0, 'force': -2.94, 'temperature': 42}
        [15:36:20] [gripper_d672f584b17a]: {'position': 59.0, 'velocity': 0.0, 'force': -2.94, 'temperature': 42}

.. container:: step-block

    3、当要对特定 Service 服务调用时，可使用如下命令，以调用 Gripper 服务为例：

    .. code-block:: bash

        ezros service -n gripper_d672f584b17a -c set_led_color:=red

    终端输出示例：

    .. code-block:: text

        调用服务: gripper_d672f584b17a
        动作: set_led_color
        参数: ['red']
        ----------------------------------------
        调用失败: 无响应

.. container:: step-block

    4、`-a` 参数，显示所有节点信息，终端打印如下：

    .. code-block:: bash

        ezros -a

    终端输出示例：

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

.. container:: step-block

    5、`-f` 参数，过滤包含指定字符串的节点名，以匹配 master 节点为例：

    .. code-block:: bash

        ezros -a -f "master"

    终端输出示例：

    .. code-block:: text

        扫描网络中... (预计 2 秒)
        [███████████████████████████░░░] 90%
        ================================================================================
        EzROS 网络节点信息
        ================================================================================
        1. Node: master_d672f584b17a (udp/192.168.1.127:59477)
          Services:
            - master_d672f584b17a: [kill_sensor, list_camera, launch_sensor, launch_gripper, kill_camera, scan_sensor_sn, reboot, launch_camera, kill_gripper]