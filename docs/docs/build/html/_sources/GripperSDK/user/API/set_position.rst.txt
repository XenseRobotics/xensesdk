.. _tag_set_position_:

set_position方法
=====================

.. container:: step-block

    .. py:method:: XenseGripper.set_position(self, position, vmax=80.0, fmax=27.0)
        :module: xensegripper

        设置夹爪的目标位置。

        :param position: 夹爪的目标位置，单位为毫米(mm)。
                            必须在 (0, 85) 范围内。
                            85 mm 表示完全打开, 0 mm 表示完全闭合。
        :type position: float
        
        :param vmax: 最大运动速度，单位为毫米/秒(mm/s)。
                        必须在 (0, 350) 范围内。
                        默认值为 80 mm/s。
        :type vmax: float
        
        :param fmax: 最大输出力，单位为牛顿(N)。
                        必须在 (0, 60) 范围内。
                        默认值为 27 N。
        :type fmax: float
        
        :raises ValueError: 当任何输入参数超出其允许的物理限制范围时触发。


示例代码
--------

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


