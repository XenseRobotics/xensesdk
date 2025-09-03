.. _tag_scanSerialNumber:

scanSerialNumber 方法
============================

.. container:: step-block

    .. py:method:: Sensor.scanSerialNumber() -> dict
        :module: xensesdk
        :noindex:

        扫描并返回当前设备上所有已连接的传感器信息。

        该方法会检测系统中已连接的传感器设备，返回其序列号与对应的相机 ID 映射关系，方便后续通过序列号创建传感器实例。

        :return: 包含所有已连接传感器的字典，键为传感器序列号( ``serial_number`` )，值为对应的相机 ID( ``camera_id`` )
        :rtype: dict
        