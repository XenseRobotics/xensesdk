.. _tag_Gripper_get_gripper_status_:

get_gripper_status 方法
=========================

.. container:: step-block

    .. py:method:: XenseGripper.get_gripper_status(self)
        :module: xensegripper

        获取夹爪当前的状态信息（包括运行参数和设备状态）。

        该方法用于读取夹爪的实时工作数据，返回包含关键运行参数的字典，可用于监控夹爪的当前状态。

        :return: 夹爪当前状态的字典，包含以下键值：
                 - position: 当前位置 (单位: mm)
                 - velocity: 当前速度 (单位: mm/s)
                 - force: 当前输出力 (单位: N)
                 - temperature: 电机温度（单位：℃）
        :rtype: dict
