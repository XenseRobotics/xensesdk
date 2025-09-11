
.. _tag_set_control_param_:

set_control_param方法
=====================

.. container:: step-block

   .. py:method:: XenseGripper.set_control_param(self, stiffness=0.35)
       :module: xensegripper

       设置夹爪的控制参数（如刚度）。

       :param stiffness: 夹爪的刚度参数，用于调整夹爪运动的响应特性。
                           必须在 (0.1, 0.6) 范围内。
                           默认值为 0.35。
       :type stiffness: float, 可选
       
       :raises ValueError: 当刚度值超出允许范围时触发。

示例代码
--------
.. container:: step-block

    .. code-block:: python

        from xensegripper import XenseGripper

        # 创建夹爪实例
        gripper = XenseGripper.create("9a14e81bb832")

        # 设置控制参数 (可选)
        gripper.set_control_param(stiffness=0.35)  # 使用默认值

        # 设置自定义刚度值
        gripper.set_control_param(stiffness=0.5)   # 设置刚度为0.5

        # 错误示例：刚度超出范围
        try:
            gripper.set_control_param(stiffness=0.7)  # 0.7超过最大0.6限制
        except ValueError as e:
            print(e)

        try:
            gripper.set_control_param(stiffness=0.05)  # 0.05低于最小0.1限制
        except ValueError as e:
            print(e)