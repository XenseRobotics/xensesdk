.. _tag_set_speed_:

set_speed方法
=====================

.. container:: step-block

   .. py:method:: XenseGripper.set_speed(self, velocity, fmax=27)
       :module: xensegripper

       速度闭环控制（设置夹爪的运动速度）。

       :param velocity: 夹爪的目标速度，单位为毫米/秒 (mm/s)。
                        正值表示闭合方向运动, 负值表示打开方向运动, 0 表示停止。
                        速度绝对值必须在 (0, 440) 范围内。
       :type velocity: float
       
       :param fmax: 最大推力，单位为牛顿 (N)。
                    必须在 [0, 60] 范围内。
                    默认值为 27 N。
       :type fmax: float, 可选


示例代码
--------
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
                        print("开始打开")
                    else:
                        CLOSE = True
                        print("开始关闭")
                if key == keyboard.Key.esc:
                    global BREAK
                    BREAK = True
                    print("退出程序")
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

        # 下列方法二选一
        # with gripper.mode(XenseGripper.ControlMode.SAFE) as gripper:
        #     while True:
        #         if not CLOSE:  
        #             # print("正在打开")
        #             gripper.set_position(80)
        #         else:
        #             # print("正在关闭")
        #             gripper.set_position(0) 
        #             pass
        #         time.sleep(0.05)       
        with gripper.mode(XenseGripper.ControlMode.SPEED) as gripper:
            while True:
                if not CLOSE:  
                    # print("正在打开")
                    gripper.set_speed(40)
                else:
                    # print("正在关闭")
                    gripper.set_speed(-40) 
                time.sleep(0.05)







