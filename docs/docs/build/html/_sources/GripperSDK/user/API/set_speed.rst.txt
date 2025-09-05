.. _tag_set_speed_:

set_speed方法
=====================

.. container:: step-block

   .. py:method:: XenseGripper.set_speed(self, speed)
       :module: xensegripper

       设置夹爪的运动速度。

       :param speed: 夹爪的目标速度，单位为毫米 / 秒 (mm/s)。
                        正值表示闭合方向运动,负值表示打开方向运动,0 表示停止。
                        速度绝对值必须在 (0,350) 范围内。
       :type speed: float

示例代码
--------
.. container:: step-block

    .. code-block:: python

        from xensesdk import XenseGripper

        # 创建夹爪实例
        gripper = XenseGripper.create("9a14e81bb832")

        gripper.set_speed(50)   # 设置速度 50 mm/s
        time.sleep(2)
        gripper.set_speed(0)    # 停止

        # 手动模式切换
        gripper.enable_mode(XenseGripper.ControlMode.SPEED)
        gripper.set_speed(30)
        gripper.disable_mode()  # 自动停止并恢复原模式





