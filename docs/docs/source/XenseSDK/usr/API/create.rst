.. _tagcreate_method:

create方法
=============

.. container:: step-block

    .. py:method:: Sensor.create(cam_id=0, config_path=None, api=None, check_serial=True, rectify_size=None, mac_addr=None)
        :module: xensesdk

        创建一个传感器实例，使用完成后请调用 :meth:`~Sensor.release` 释放资源。

        :param cam_id: 传感器 ID、序列号或视频路径。默认为 0。
        :type cam_id: int | str，可选
        
        :param config_path: 配置文件路径或目录。若为目录，需包含与传感器序列号同名的标定文件。
        :type config_path: str | Path，可选
        
        :param api: 相机 API 类型（如 OpenCV 后端），用于指定相机访问方式。
        :type api: Enum，可选
        
        :param check_serial: 是否检查传感器序列号。
        :type check_serial: bool，可选
        
        :param rectify_size: 校正图像尺寸（宽, 高）。
        :type rectify_size: tuple[int, int]，可选
        
        :param mac_addr: 远程连接使用的相机 MAC 地址。
        :type mac_addr: str，可选
        
        :return: 传感器实例，用于后续数据采集和处理。
        :rtype: :class:`Sensor`

.. note::
    
    使用完毕后务必调用 :meth:`~Sensor.release` 释放系统资源。

示例代码
--------
.. container:: step-block

    .. tab-set::

        .. tab-item:: 示例 1:通过 SN 码开启传感器

            .. code-block:: python

                from xensesdk import Sensor

                # 使用传感器序列号（SN）创建实例
                sensor = Sensor.create('OP000064')

                # 使用完毕后释放资源
                sensor.release()

        .. tab-item:: 示例 2:通过相机编号开启传感器

            .. code-block:: python

                from xensesdk import Sensor

                # 使用相机编号（如 0、1）创建实例
                sensor = Sensor.create(0)

                # 使用完毕后释放资源
                sensor.release()

        .. tab-item:: 示例 3:连接远程算力板上的传感器

            .. code-block:: python

                from xensesdk import Sensor

                # 指定 MAC 地址连接远程传感器
                master_service = "master_000000000000"
                sensor = Sensor.create('OP000064', mac_addr="000000000000")

                # 使用完毕后释放资源
                sensor.release()

.. admonition:: tips
    :class: tip

        如何获取示例 3中master_service 可参考
        `EzROS </home/xense/projects/doc/xensesdk/docs/docs/source//GripperSDK/user/EzROS/ezros_example.html>`_。