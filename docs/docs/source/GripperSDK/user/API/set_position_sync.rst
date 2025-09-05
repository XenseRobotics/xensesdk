.. _tag_set_position_sync_:

set_position_sync方法
=====================

.. container:: step-block

    .. py:method:: XenseGripper.set_position_sync(self, position, vmax=80.0, fmax=27.0, tolerance=0.01, timeout=5.0, poll_interval=0.05)
        :module: xensegripper

        同步位置控制 (阻塞直到到达目标位置)

        :param position: 夹爪的目标位置，单位为毫米(mm)。
                            必须在 (0, 85) 范围内。
                            0 mm 表示完全打开,85 mm 表示完全闭合。
        :type position: float
        
        :param vmax: 最大运动速度，单位为毫米/秒(mm/s)。
                        必须在 (0, 350) 范围内。
                        默认值为 80 mm/s。
        :type vmax: float
        
        :param fmax: 最大输出力，单位为牛顿(N)。
                        必须在 (0, 40) 范围内。
                        默认值为 27 N。
        :type fmax: float
        
        :param tolerance: 判定运动完成的位置误差容忍度，单位为毫米(mm)。
                            默认值为 0.01 mm。
        :type tolerance: float, 可选

        :param timeout: 等待目标位置到达的最大时间，单位为秒。
                        默认值为 5.0 秒。
        :type timeout: float, 可选

        :param poll_interval: 位置检查的时间间隔，单位为秒。
                                默认值为 0.05 秒。
        :type poll_interval: float, 可选
        
        :raises ValueError: 当任何输入参数超出其允许的物理限制范围时触发。

        :return: 若夹爪在超时时间内到达目标位置（在允许的误差范围内），则返回 True,否则返回 False。
        :rtype: bool


示例代码
--------
.. container:: step-block

    .. code-block:: python

        from xensesdk import XenseGripper

        # 创建夹爪实例
        gripper = XenseGripper.create("9a14e81bb832")

        # 同步设置夹爪位置为 30mm，使用默认参数
        success = gripper.set_position_sync(30)
        print(f"位置设置成功: {success}")

        # 同步设置夹爪位置为 50mm，指定参数
        success = gripper.set_position_sync(
            position=50,
            vmax=120,
            fmax=35,
            tolerance=0.02,
            timeout=10.0,
            poll_interval=0.03
        )
        print(f"位置设置成功: {success}")

        # 错误示例：位置超出范围
        try:
            gripper.set_position_sync(90)  # 90mm 超过最大 85mm 限制
        except ValueError as e:
            print(e)