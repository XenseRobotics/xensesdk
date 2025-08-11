.. _tag_set_position_:

set_position方法
=====================

.. container:: step-block

    .. py:method:: XenseGripper.set_position(self, position, vmax=80.0, fmax=27.0)
        :module: xensegripper

        设置夹爪的目标位置。

        :param position: 夹爪的目标位置,单位为毫米(mm)。
                            必须在 (0, 85) 范围内。
                            0 mm 表示完全打开,85 mm 表示完全闭合。
        :type position: float
        
        :param vmax: 最大运动速度，单位为毫米/秒(mm/s)。
                        必须在 (0, 200) 范围内。
                        默认值为 80 mm/s。
        :type vmax: float, 可选
        
        :param fmax: 最大输出力,单位为牛顿(N)。
                        必须在 (0, 40) 范围内。
                        默认值为 27 N。
        :type fmax: float, 可选
        
        :raises ValueError: 当任何输入参数超出其允许的物理限制范围时触发。

示例代码
--------

.. container:: step-block

    .. code-block:: python

        from xensesdk import XenseGripper

        # 创建夹爪实例
        gripper = XenseGripper.create("9a14e81bb832")

        # 设置夹爪位置为 40mm，使用默认速度和力
        gripper.set_position(40)

        # 设置夹爪位置为 60mm，指定速度 100mm/s 和力 30N
        gripper.set_position(60, vmax=100, fmax=30)

        # 错误示例：位置超出范围（会触发 ValueError）
        try:
            gripper.set_position(90)  # 90mm 超过最大 85mm 限制
        except ValueError as e:
            print(e)