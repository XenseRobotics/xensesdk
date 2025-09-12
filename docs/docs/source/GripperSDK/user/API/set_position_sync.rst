.. _tag_set_position_sync_:

set_position_sync方法
=====================

.. container:: step-block

    .. py:method:: XenseGripper.set_position_sync(self, position, vmax=80.0, fmax=27.0, tolerance=0.01, timeout=5.0, poll_interval=0.05)
        :module: xensegripper

        同步位置控制 (将夹爪移动到目标位置，并阻塞直到到达目标位置或超时)

        :param position: 夹爪的目标位置，单位为毫米(mm)。
                            必须在 (0, 85) 范围内。
                            0 mm 表示完全打开, 85 mm 表示完全闭合。
        :type position: float
        
        :param vmax: 最大运动速度，单位为毫米/秒(mm/s)。
                        必须在 (0, 350) 范围内。
                        默认值为 80 mm/s。
        :type vmax: float
        
        :param fmax: 最大输出力，单位为牛顿(N)。
                        必须在 (0, 60) 范围内。
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

        :return: 若夹爪在超时时间内到达目标位置（在允许的误差范围内），则返回 True, 否则返回 False。
        :rtype: bool



示例代码
--------
.. container:: step-block

    .. code-block:: python

        from xensegripper import XenseGripper

        # 创建夹爪实例
        gripper = XenseGripper.create("9a14e81bb832")

        # 同步设置夹爪位置为 30mm，使用默认参数
        success = gripper.set_position_sync(30)

        # 同步设置夹爪位置为 70mm，指定参数（符合最新范围）
        success = gripper.set_position_sync(
            position=70,          # 在 (0, 85) 范围内
            vmax=250,             # 在 (0, 350) 范围内（高于原示例，体现新上限）
            fmax=50,              # 在 (0, 60) 范围内（高于原示例，体现新上限）
            tolerance=0.02,
            timeout=8.0,
            poll_interval=0.04
        )
        # 错误示例：力参数超出范围（体现最新上限60N）
        try:
            gripper.set_position_sync(40, fmax=70)  # 70N 超过最大 60N 限制
        except ValueError as e:
            print(e)
