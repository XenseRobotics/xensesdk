.. _tag_Grippermethodlist:

如何使用GripperSDK?
=========================

.. container:: step-block

    在使用GripperSDK之前,请先确保:

    .. note::

        1.请先确保夹爪正确连接PC,如未连接请参考
        `GripperSDK <./pre_configuration.html>`_。

        2.需要开启夹爪的服务,可使用以下命令开启:

        .. code-block:: python

            python /home/Tronlong/xense_workspace/xensegripper/xensegripper/__main__.py -m


.. container:: step-block

    GripperSDK更多使用方法请参考

    .. list-table::
        :widths: 30
        :header-rows: 1

        * - API目录

        * - :ref:`create 方法 <tag_Grippercreate_>`

        * - :ref:`set_position 方法 <tag_set_position_>`

        * - :ref:`open_gripper 方法 <tag_Gripper_open_gripper_>`

        * - :ref:`close_gripper 方法 <tag_Gripper_close_gripper_>`

        * - :ref:`get_gripper_status 方法 <tag_Gripper_get_gripper_status_>`

    .. toctree:: 
        :maxdepth: 1
        :hidden:
        :caption: API目录

        API/create_gripper
        API/set_position
        API/open_gripper
        API/close_gripper
        API/get_gripper_status


