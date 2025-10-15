.. _tag_set_position_:

set_position Method
=======================

.. container:: step-block

    .. py:method:: XenseGripper.set_position(self, position, vmax=80.0, fmax=27.0)
        :module: xensegripper

        Sets the target position of the gripper.

        :param position: Target position of the gripper in millimeters (mm).
                            Must be within the range (0, 85).
                            85 mm indicates fully open, 0 mm indicates fully closed.
        :type position: float
        
        :param vmax: Maximum movement speed in millimeters per second (mm/s).
                        Must be within the range (0, 350).
                        Default value is 80 mm/s.
        :type vmax: float, optional
        
        :param fmax: Maximum output force in Newtons (N).
                        Must be within the range (0, 60).
                        Default value is 27 N.
        :type fmax: float, optional
        
        :raises ValueError: Triggered when any input parameter exceeds its allowed physical limit range.


Example Code
----------------

.. container:: step-block

    .. code-block:: python

        import time 
        from threading import Thread

        from xensegripper import XenseGripper


        def data_fetch():
            while True:
                status = gripper.get_gripper_status()
                if isinstance(status, dict):
                    info_str = "\rGripper Status: {"
                    for key, value in status.items():
                        info_str += f"{key}:{value:+8.4f}, "
                    info_str += "}"
                    print(info_str, end="", flush=True)
                time.sleep(0.05)

        if __name__=="__main__":

            gripper = XenseGripper.create("d672f584b17a")
            data_fetch_thread = Thread(target=data_fetch, daemon=True)
            data_fetch_thread.start()

            flag = True
            while True:
                if flag:
                    gripper.set_position(80, 80, 20)
                    flag = not flag
                else:
                    gripper.set_position(10, 80, 20)
                    flag = not flag
                time.sleep(1)