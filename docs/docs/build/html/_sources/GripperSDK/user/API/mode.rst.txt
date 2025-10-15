.. _tag_mode_:

mode Method
=====================

XenseGripper supports three control modes, which can be switched via the ``mode`` method (context manager) or the ``enable_mode``/``disable_mode`` methods:

- **POSITION**: Position control mode (default), precisely controls the gripper to reach a specified position.
- **SPEED**: Speed control mode, drives the gripper to move at the set speed.
- **SAFE**: Safe control mode (sensor required), enables safe operation with force feedback.


.. container:: step-block

    .. py:method:: XenseGripper.mode(self, control_mode, serial_number=None)
        :module: xensegripper

        A context manager for temporarily switching the gripper's control mode. The original mode is automatically restored when exiting the context (recommended for use).
        Use this method with a ``with`` statement to ensure the mode is automatically reset after the code block is executed, preventing abnormalities caused by residual modes.

        :param control_mode: Enumerated value of the control mode.
                              ``XenseGripper.ControlMode.POSITION``: Position control mode.
                              ``XenseGripper.ControlMode.SPEED``: Speed control mode.
                              ``XenseGripper.ControlMode.SAFE``: Safe control mode.
        :type control_mode: XenseGripper.ControlMode
        :param serial_number: Sensor serial number (required only for SAFE mode; defaults to the first detected sensor).
        :type serial_number: str, optional
        
        :return: Context manager object, used to temporarily switch modes in a ``with`` statement block.
        :rtype: context manager


    .. py:method:: XenseGripper.enable_mode(self, control_mode, serial_number=None)
        :module: xensegripper

        Manually enables the specified control mode.

        :param control_mode: Enumerated value of the control mode (same as the ``mode`` method).
        :type control_mode: XenseGripper.ControlMode
        :param serial_number: Sensor serial number (required only for SAFE mode).
        :type serial_number: str, optional
        :return: Whether the operation is successful.
        :rtype: bool


    .. py:method:: XenseGripper.disable_mode(self)
        :module: xensegripper

        Manually disables the current control mode, automatically restores to the default mode, and stops the action.

        :return: Whether the operation is successful.
        :rtype: bool


Example Code
--------------------

.. container:: step-block

    1. Position Control Mode (default mode, no manual switching required)

    .. code-block:: python

        from xensegripper import XenseGripper

        gripper = XenseGripper.create(mac_addr="9a14e81bb832")
        gripper.set_position(30)  # Directly set position (defaults to POSITION mode)


    2. Speed Control Mode

    .. code-block:: python

        # Use context manager (recommended)
        with gripper.mode(XenseGripper.ControlMode.SPEED):
            gripper.set_speed(50)   # Set speed to 50 mm/s
            time.sleep(2)
            gripper.set_speed(0)    # Stop

        # Manual mode switching
        gripper.enable_mode(XenseGripper.ControlMode.SPEED)
        gripper.set_speed(30)
        gripper.disable_mode()  # Automatically stop and restore original mode


    3. Safe Control Mode (sensor required)

    .. code-block:: python

        # Use context manager (recommended)
        # Sensor serial number can be specified; defaults to the first detected sensor
        with gripper.mode(XenseGripper.ControlMode.SAFE, serial_number=None):
            # Set control parameters (optional; stiffness range: 0.1~0.6)
            gripper.set_control_param(stiffness=0.35)
            
            # Position control (with force feedback protection)
            gripper.set_position(20)

        # Manual mode switching
        gripper.enable_mode(XenseGripper.ControlMode.SAFE, serial_number="OG000285")
        gripper.set_control_param(stiffness=0.4)
        gripper.set_position(15)
        gripper.disable_mode()  # Automatically stop and restore original mode