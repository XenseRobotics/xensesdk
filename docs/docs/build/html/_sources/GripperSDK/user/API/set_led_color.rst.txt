
.. _tag_set_led_color_:

set_led_color方法
=====================

.. container:: step-block

   .. py:method:: XenseGripper.set_led_color(self, r, g, b)
       :module: xensegripper

       设置夹爪的LED灯颜色,通过RGB三色值控制。

       :param r: 红色通道值,范围为0-255。
       :type r: int
       
       :param g: 绿色通道值,范围为0-255。
       :type g: int
       
       :param b: 蓝色通道值,范围为0-255。
       :type b: int
       
       :raises ValueError: 当任何颜色通道值超出0-255范围时触发。

示例代码
--------
.. container:: step-block

    .. code-block:: python

        from xensesdk import XenseGripper

        # 创建夹爪实例
        gripper = XenseGripper.create("9a14e81bb832")

        # 设置LED颜色 (RGB 0-255)
        gripper.set_led_color(255, 0, 0)    # 红色
        gripper.set_led_color(0, 255, 0)    # 绿色
        gripper.set_led_color(0, 0, 255)    # 蓝色
        

        # 错误示例：颜色值超出范围
        try:
            gripper.set_led_color(300, 0, 0)  # 300超过最大255限制
        except ValueError as e:
            print(e)

        try:
            gripper.set_led_color(-10, 0, 0)  # -10低于最小0限制
        except ValueError as e:
            print(e)