.. _tag_Gripperpre_configuration:

Hardware Connection & Network Configuration
=================================================

Connect the server side and the host computer to the same local area network (LAN) to enable communication between them.

.. raw:: html

    <style>
    /* 步骤标题样式（外显，无边框） */
    .step-title {
        font-size: 1.3em !important;
        font-weight: 700 !important;
        color: #2c3e50 !important;
        margin-top: 1.8em !important;
        margin-bottom: 0.5em !important;
        font-family: "Microsoft YaHei", sans-serif !important;
    }
    
    /* 步骤内容容器（带边框） */
    .step-content {
        border: 1px solid #ddd !important;
        border-radius: 6px !important;
        padding: 15px 20px !important;
        background-color: #f9f9f9 !important;
        margin-bottom: 1em !important;
    }
    
    /* 方法标题样式 */
    .method-title {
        font-size: 1.1em !important;
        font-weight: 600 !important;
        color: #34495e !important;
        margin-top: 1.2em !important;
        margin-bottom: 0.6em !important;
        padding-left: 5px !important;
        border-left: 3px solid #3498db !important; /* 左侧装饰线 */
    }
    </style>



.. rubric:: Step 1: Connect the Gripper Device to Power
   :class: step-title  

.. container:: step-content

    1. Plug the power adapter of the gripper device into a mains socket.
    2. Wait for the gripper to complete initialization, and observe that the status light first flashes and then stays on.


.. rubric:: Step 2: Connect to the Network
   :class: step-title

.. container:: step-content

    .. rubric:: Method 1: Using a Switch
       :class: method-title  

    Connect the gripper and the computer to different network ports of the switch respectively, and ensure the network is connected. At this time, the gripper's IP address is automatically obtained using ``dhcp``, and subsequent scanning needs to be performed using `ezros <./EzROS/usr/ezros_example.html>`_.


    .. rubric:: Method 2: Direct Connection to Computer's Network Port
       :class: method-title

    In this case, the gripper uses a static IP ``192.168.99.2``, and the computer needs to set its own IP within the same network segment as the gripper (open Network Settings -> Wired Settings -> IPv4).
    Reference settings are as follows:

    .. list-table::
        :widths: 15 20 35
        :header-rows: 1  

        * - Parameter Item  
          - Example/Fixed Value 
          - Configuration Description  
            
        * - IP Address  
          - ``192.168.99.10`` 
          - Format: ``192.168.99.X``, (X ranges from 1 to 254, avoiding the gripper's IP)
        * - Subnet Mask  
          - ``255.255.255.0`` 
          - Fixed configuration, no modification required  

    Use an Ethernet cable to directly connect the PC's Ethernet port to the gripper device's network port, and ensure the Ethernet cable is firmly plugged into the PC's port.

    .. admonition:: tips
        :class: tip

        When using the SDK, if the host computer is connected to both the gripper via a wired connection and WiFi, configure multi-network card discovery at the beginning of the program:

        .. code-block:: python

            from xensesdk import setup_multi_net_interface

            setup_multi_net_interface()


.. rubric:: Step 3: Test Network Connectivity
   :class: step-title

.. container:: step-content

    1. Open the PC's command prompt (Windows: Press ``Win+R``, enter ``cmd`` and press Enter; Linux: Open the terminal).
    2. Enter the following command in the command line and press Enter:

        .. code-block:: bash

            ping 192.168.99.2

    3. Result Judgment:
   
        .. tab-set::

            .. tab-item:: Successful Network Connection
                
                If messages like **"Reply from 192.168.99.2"** are displayed, you can directly proceed with subsequent operations.

            .. tab-item:: Connection Timeout

                If **"Request timed out"** is displayed, please check the following items in sequence:

                - Whether the Ethernet IP configuration is correct (recheck Step 2)
                - Whether the Ethernet cable is loose or damaged
                - Whether the gripper device has completed initialization (whether the status light stays on)