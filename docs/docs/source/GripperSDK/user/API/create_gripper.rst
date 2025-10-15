.. _tag_Grippercreate_:

create Method
==================

.. container:: step-block

    .. py:method:: XenseGripper.create(mac_addr=None)
        :module: xensegripper

        Creates an XenseGripper instance.

        :param mac_addr: Provide the correct MAC communication address. For how to query the MAC address, see: `ezros <../EzROS/usr/ezros_example.html>`_.
        :type mac_addr: str, optional
        
        :return: A gripper instance that implements the `Gripper` interface.
        :rtype: :class:`XenseTCPGripper`

Example Code
-----------------

.. container:: step-block

    Connect to the gripper via MAC address

    .. code-block:: python

        from xensegripper import XenseGripper

        # Create a connected gripper instance using the MAC address
        gripper = XenseGripper.create(mac_addr="9a14e81bb832")

   
.. admonition:: tips
   :class: tip

   If you don't know the gripper's MAC address, you can use the ``ezros`` tool to query it. For details, please refer to :doc:`../EzROS/usr/ezros_example`.