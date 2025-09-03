.. _tagstart_save_sensor_info_method:

startSaveSensorInfo 方法
==========================

.. container:: step-block
        
    .. py:method:: Sensor.startSaveSensorInfo(path, data_to_save=None)
        :module: xensesdk
        
        开始保存指定类型的传感器数据。
        
        :param path: 数据保存的文件夹路径。
        :type path: str
        
        :param data_to_save: 需要保存的数据类型列表。为 None 则保存所有类型。
        :type data_to_save: List[Sensor.OutputType], 可选
        
        :return: None

.. note::
    在结束时务必调用 :meth:`~Sensor.stopSaveSensorInfo` 来停止保存数据。


示例代码
---------
.. container:: step-block

    .. code-block:: python

        from xensesdk import Sensor
        import time

        # 创建传感器实例
        sensor = Sensor.create('OP000064')

        # 开始保存指定类型的数据
        sensor.startSaveSensorInfo('/path/to/save', [
            Sensor.OutputType.Rectify,
            Sensor.OutputType.Difference,
            Sensor.OutputType.Depth,
            Sensor.OutputType.Marker2D
        ])

        # 进行数据采集...
        time.sleep(5)

        # 停止保存数据
        sensor.stopSaveSensorInfo()

        # 释放资源
        sensor.release()
