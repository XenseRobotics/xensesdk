.. _tag_mode_:

mode 方法
=====================

XenseGripper 支持三种控制模式，可通过 ``mode`` 方法（上下文管理器）或 ``enable_mode``/``disable_mode`` 方法切换：

- **POSITION**: 位置控制模式 (默认)，精确控制夹爪到达指定位置
- **SPEED**: 速度控制模式，按设定速度驱动夹爪运动
- **SAFE**: 安全控制模式 (需要传感器)，结合力反馈实现安全操作


.. container:: step-block

    .. py:method:: XenseGripper.mode(self, control_mode, serial_number=None)
        :module: xensegripper

        上下文管理器，用于临时切换夹爪控制模式，退出上下文时自动恢复原模式（推荐使用）。
        通过 with 语句使用该方法，可确保模式在代码块执行完毕后自动重置，避免模式残留导致的异常。

        :param control_mode: 控制模式枚举值
                              ``XenseGripper.ControlMode.POSITION``: 位置控制模式
                              ``XenseGripper.ControlMode.SPEED``: 速度控制模式
                              ``XenseGripper.ControlMode.SAFE``: 安全控制模式
        :type control_mode: XenseGripper.ControlMode
        :param serial_number: 传感器序列号（仅安全模式需要，默认使用第一个扫描到的传感器）
        :type serial_number: str, 可选
        
        :return: 上下文管理器对象，用于 with 语句块中临时切换模式
        :rtype: context manager


    .. py:method:: XenseGripper.enable_mode(self, control_mode, serial_number=None)
        :module: xensegripper

        手动启用指定的控制模式

        :param control_mode: 控制模式枚举值（同 mode 方法）
        :type control_mode: XenseGripper.ControlMode
        :param serial_number: 传感器序列号（仅安全模式需要）
        :type serial_number: str, 可选
        :return: 操作是否成功
        :rtype: bool


    .. py:method:: XenseGripper.disable_mode(self)
        :module: xensegripper

        手动禁用当前控制模式，自动恢复到默认模式并停止动作

        :return: 操作是否成功
        :rtype: bool


示例代码
--------

.. container:: step-block

    1. 位置控制模式（默认模式，无需手动切换）

    .. code-block:: python

        from xensegripper import XenseGripper

        gripper = XenseGripper.create(mac_addr="9a14e81bb832")
        gripper.set_position(30)  # 直接设置位置（默认在 POSITION 模式）


    2. 速度控制模式

    .. code-block:: python

        # 使用上下文管理器 (推荐)
        with gripper.mode(XenseGripper.ControlMode.SPEED):
            gripper.set_speed(50)   # 设置速度 50 mm/s
            time.sleep(2)
            gripper.set_speed(0)    # 停止

        # 手动模式切换
        gripper.enable_mode(XenseGripper.ControlMode.SPEED)
        gripper.set_speed(30)
        gripper.disable_mode()  # 自动停止并恢复原模式


    3. 安全控制模式 (需要传感器)

    .. code-block:: python

        # 使用上下文管理器 (推荐)
        # 可指定传感器序列号，默认使用扫描到的第一个传感器
        with gripper.mode(XenseGripper.ControlMode.SAFE, serial_number=None):
            # 设置控制参数 (可选，刚度范围 0.1~0.6)
            gripper.set_control_param(stiffness=0.35)
            
            # 位置控制 (带力反馈保护)
            gripper.set_position(20)

        # 手动模式切换
        gripper.enable_mode(XenseGripper.ControlMode.SAFE, serial_number="OG000285")
        gripper.set_control_param(stiffness=0.4)
        gripper.set_position(15)
        gripper.disable_mode()  # 自动停止并恢复原模式
