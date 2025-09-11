.. _tag_Grippercreate_:

create 方法
=============

.. container:: step-block

    .. py:method:: XenseGripper.create(mac_addr=None)
        :module: xensegripper

        创建一个 XenseGripper 实例

        :param mac_addr: 提供正确的 mac 通信地址。
        :type mac_addr: str, 可选
        
        :return: 实现 `Gripper` 接口的夹爪实例。
        :rtype: :class:`XenseTCPGripper`

示例代码
--------

.. container:: step-block

    通过 MAC 地址连接夹爪

    .. code-block:: python

        from xensegripper import XenseGripper

        # 使用 MAC 地址创建连接的夹爪实例
        gripper = XenseGripper.create(mac_addr="9a14e81bb832")

.. admonition:: tips
   :class: tip

   如果不清楚夹爪的MAC地址,可以使用 ``ezros`` 工具进行查询,具体请参考 `EzROS命令行工具 <../../GripperSDK/usr/EzROS/usr/ezros_example.html>`。
   
   
.. admonition:: tips
   :class: tip

   如果不清楚夹爪的MAC地址,可以使用 ``ezros`` 工具进行查询,具体请参考 :doc:`../EzROS/usr/ezros_example`。

.. note::
    
    长时间不连接传感器(10mins),传感器会进入休眠模式,下一次启动会需要更长的时间。
            