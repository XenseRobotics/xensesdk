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
        from xensegripper import XenseGripper

        # 创建夹爪实例
        gripper = XenseGripper.create("9a14e81bb832")

        # 设置速度 50mm/s
        gripper.set_speed(50)
        time.sleep(2)
        gripper.set_speed(0)  # 停止

        # 错误示例：速度超出 440mm/s 限制
        try:
            gripper.set_speed(500)  # 500mm/s 超过最大 440mm/s 限制
        except ValueError as e:
            print(e)





