.. _tag_all_info:

Viewing EzROS Service Information
======================================

.. container:: step-block

    EzROS supports combining global parameters to realize "full information display" or "target node filtering display". The specific usage for different scenarios is explained below:

    **Scenario 1: View All Nodes, Topics, and Services (Full Information)**  
    Trigger a full scan using the ``-a/--all`` parameter to display complete information of all nodes in the network:

    .. code-block:: bash

        ezros -a
        # or ezros --all

    The terminal will print the following information:

    .. code-block:: text

        Scanning the network... (estimated 2 seconds)
        [███████████████████████████░░░] 90%
        ================================================================================
        EzROS Network Node Information
        ================================================================================
        1. Node: gripper_d672f584b17a (udp/192.168.1.127:46067)
          Topics:
            - gripper_d672f584b17a
          Services:
            - gripper_d672f584b17a: [set_led_color, restart_control_subscriber]

        2. Node: master_d672f584b17a (udp/192.168.1.127:59477)
          Services:
            - master_d672f584b17a: [scan_sensor_sn, kill_sensor, launch_camera, launch_gripper, list_camera, reboot, kill_camera, launch_sensor, kill_gripper]


    **Scenario 2: Filter and View Target Nodes (Only Display Nodes Containing the Target String)**  
    Combine the ``-a/--all`` and ``-f/--filter`` parameters to display only information of nodes whose names contain the specified string (e.g., only view "gripper"-related nodes):

    .. code-block:: bash

        ezros -a -f gripper  # Filter to show nodes with "gripper" in their names

    The terminal will print the following information (only nodes containing "gripper" are retained):

    .. code-block:: text

        Scanning the network... (estimated 2 seconds)
        [███████████████████████████░░░] 90%
        ================================================================================
        EzROS Network Node Information
        ================================================================================
        1. Node: gripper_d672f584b17a (udp/192.168.1.127:58614)
          Topics:
            - gripper_d672f584b17a
          Services:
            - gripper_d672f584b17a: [restart_control_subscriber, set_led_color]


    In both scenarios, the string "d672f584b17a" after the node name represents the device's MAC address, which can be used to create a gripper instance:

    .. code-block:: python

        from xensegripper import XenseGripper

        gripper = XenseGripper.create("d672f584b17a")


.. admonition:: tips
    :class: tip 

    - ``-a/--all``: A global parameter used to trigger the "full information display" function, which scans and shows information of all nodes.
    - ``-f/--filter``: A global parameter that must be used with ``-a``. It filters node names containing the specified string (matches all nodes by default). For example, ``ezros -a -f master`` can display only nodes with "master" in their names.