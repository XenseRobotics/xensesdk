.. _tag_set_speed_:

set_speed Method
=====================

.. container:: step-block

   .. py:method:: XenseGripper.set_speed(self, velocity, fmax=27)
       :module: xensegripper

       Speed closed-loop control (sets the movement speed of the gripper).

       :param velocity: Target speed of the gripper in millimeters per second (mm/s).
                        A positive value indicates movement in the closing direction, a negative value indicates movement in the opening direction, and 0 indicates stopping.
                        The absolute value of the speed must be within the range (0, 440).
       :type velocity: float
       
       :param fmax: Maximum thrust force in Newtons (N).
                    Must be within the range [0, 60].
                    Default value is 27 N.
       :type fmax: float, optional


Example Code
------------------
.. container:: step-block

    .. code-block:: python

        import time 
        from threading import Thread

        from pynput import keyboard

        from xensegripper import XenseGripper


        CLOSE = False
        BREAK = False

        def on_press(key):
            try:
                global CLOSE
                if key == keyboard.Key.space:
                    if CLOSE:
                        CLOSE = False
                        print("Start opening")
                    else:
                        CLOSE = True
                        print("Start closing")
                if key == keyboard.Key.esc:
                    global BREAK
                    BREAK = True
                    print("Exit program")
                    return False

            except AttributeError:
                pass

        def data_fetch():
            while True:
                status = gripper.get_gripper_status()
                time.sleep(0.05)


        listener = keyboard.Listener(on_press=on_press)
        listener.start()  

        gripper = XenseGripper.create("9a14e81bb832")
        data_fetch_thread = Thread(target=data_fetch, daemon=True)
        data_fetch_thread.start()   

        # Choose one of the following two methods
        # with gripper.mode(XenseGripper.ControlMode.SAFE) as gripper:
        #     while True:
        #         if not CLOSE:  
        #             # print("Opening")
        #             gripper.set_position(80)
        #         else:
        #             # print("Closing")
        #             gripper.set_position(0) 
        #             pass
        #         time.sleep(0.05)       
        with gripper.mode(XenseGripper.ControlMode.SPEED) as gripper:
            while True:
                if not CLOSE:  
                    # print("Opening")
                    gripper.set_speed(40)
                else:
                    # print("Closing")
                    gripper.set_speed(-40) 
                time.sleep(0.05)