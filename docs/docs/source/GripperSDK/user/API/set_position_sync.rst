.. _tag_set_position_sync_:

set_position_sync Method
============================

.. container:: step-block

    .. py:method:: XenseGripper.set_position_sync(self, position, vmax=80.0, fmax=27.0, tolerance=0.01, timeout=5.0, poll_interval=0.05)
        :module: xensegripper

        Synchronous position control (moves the gripper to the target position and blocks until the target position is reached or a timeout occurs).

        :param position: Target position of the gripper in millimeters (mm).
                            Must be within the range (0, 85).
                            0 mm indicates fully open, 85 mm indicates fully closed.
        :type position: float
        
        :param vmax: Maximum movement speed in millimeters per second (mm/s).
                        Must be within the range (0, 350).
                        Default value is 80 mm/s.
        :type vmax: float
        
        :param fmax: Maximum output force in Newtons (N).
                        Must be within the range (0, 60).
                        Default value is 27 N.
        :type fmax: float
        
        :param tolerance: Position error tolerance for determining movement completion, in millimeters (mm).
                            Default value is 0.01 mm.
        :type tolerance: float, optional

        :param timeout: Maximum time to wait for the target position to be reached, in seconds.
                        Default value is 5.0 seconds.
        :type timeout: float, optional

        :param poll_interval: Time interval for position checks, in seconds.
                                Default value is 0.05 seconds.
        :type poll_interval: float, optional
        
        :raises ValueError: Triggered when any input parameter exceeds its allowed physical limit range.

        :return: Returns True if the gripper reaches the target position within the timeout period (within the allowed error range), otherwise returns False.
        :rtype: bool



Example Code
-------------------
.. container:: step-block

    .. code-block:: python

        from xensegripper import XenseGripper

        # Create a gripper instance
        gripper = XenseGripper.create("9a14e81bb832")

        # Synchronously set the gripper position to 30mm using default parameters
        success = gripper.set_position_sync(30)

        # Synchronously set the gripper position to 70mm with specified parameters (complying with the latest ranges)
        success = gripper.set_position_sync(
            position=70,          # Within (0, 85) range
            vmax=250,             # Within (0, 350) range (higher than original example, reflecting new upper limit)
            fmax=50,              # Within (0, 60) range (higher than original example, reflecting new upper limit)
            tolerance=0.02,
            timeout=8.0,
            poll_interval=0.04
        )
        # Error example: Force parameter out of range (reflecting the latest upper limit of 60N)
        try:
            gripper.set_position_sync(40, fmax=70)  # 70N exceeds the maximum limit of 60N
        except ValueError as e:
            print(e)