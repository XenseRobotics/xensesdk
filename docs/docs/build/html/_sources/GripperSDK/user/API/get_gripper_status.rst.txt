.. _tag_Gripper_get_gripper_status_:

get_gripper_status Method
===================================

.. container:: step-block

    .. py:method:: XenseGripper.get_gripper_status(self)
        :module: xensegripper

        Retrieves the current status information of the gripper (including operating parameters and device status). It is used to read real-time working data of the gripper and returns a dictionary containing key operating parameters, which can be used to monitor the current state of the gripper.

        :return: A dictionary of the gripper's current status, containing the following key-value pairs:

                 - ``position``: Current position (unit: mm)
                 - ``velocity``: Current velocity (unit: mm/s)
                 - ``force``: Current output force (unit: N)
                 - ``temperature``: Motor temperature (unit: ℃)
        :rtype: dict