.. _tag_Gripperconnect_sensor:

传感器连接
=========================

本文介绍如何在 Gripper 相关设备开发中快速连接传感器。

1. 扫描传感器列表
---------------------
导入模块并扫描可用传感器，需替换实际主控服务标识：

.. container:: step-block

  .. code-block:: python

    import sys
    from xensesdk import ExampleView, Sensor, call_service

    MASTER_SERVICE = "master_d672f584b17a"
    ret = call_service(MASTER_SERVICE, "scan_sensor_sn")
    if ret is None:
        print("扫描失败，检查主控服务")
        sys.exit(1)
    serial_number = list(ret.keys())[0]

2. 创建传感器实例
-----------------
用序列号和提取的 MAC 地址创建传感器对象：

.. container:: step-block

  .. code-block:: python

    mac_address = MASTER_SERVICE.split("_")[-1]
    sensor = Sensor.create(serial_number, mac_addr=mac_address)

3. 配置数据处理（可选）
-----------------------
如需可视化，创建视图并定义数据回调：

.. container:: step-block

  .. code-block:: python

    view = ExampleView(sensor)
    view_2d = view.create2d(Sensor.OutputType.Difference, Sensor.OutputType.Depth)

    def data_callback():
        diff_data, depth_data = sensor.selectSensorInfo(
            Sensor.OutputType.Difference, Sensor.OutputType.Depth
        )
        view_2d.setData(Sensor.OutputType.Difference, diff_data)
        view_2d.setData(Sensor.OutputType.Depth, depth_data)
    view.setCallback(data_callback)
    view.show()

4. 启动与释放资源
-----------------
启动显示并在结束时释放资源：

.. container:: step-block

  .. code-block:: python

    sensor.release()
    sys.exit()

注意事项
--------
- 确保主控服务标识正确，传感器通电且在同一网络
- 多传感器可循环遍历 `ret` 中所有序列号
- 需调用 `release()` 避免设备占用冲突
