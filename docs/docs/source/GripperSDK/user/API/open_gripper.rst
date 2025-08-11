.. _tag_Gripper_open_gripper_:

open_gripper 方法
==================

.. container:: step-block

    .. py:method:: XenseGripper.open_gripper(self)
        :module: xensegripper

        打开夹爪（将夹爪位置设置为完全打开状态）。

        该方法通过调用 :meth:`~XenseGripper.set_gripper_position` 实现，
        固定将位置设为 0 mm(完全打开),速度为 40 mm/s,力为 27 N。

示例代码
--------

.. container:: step-block

    .. code-block:: python

        from xensesdk import XenseGripper

        # 创建夹爪实例
        gripper = XenseGripper.create("9a14e81bb832")  

        # 打开夹爪
        gripper.open_gripper()