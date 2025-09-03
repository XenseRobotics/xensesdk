.. _tagselect_sensor_info_method:

selectSensorInfo 方法
=======================

.. container:: step-block

  .. py:method:: Sensor.selectSensorInfo(*args)
    :module: xensesdk

    获取指定类型的传感器数据，返回数量和顺序与输入参数一致。

    :param args: 任意数量的 ``Sensor.OutputType`` 枚举，用于指定需要获取的数据类型。支持的枚举值及对应数据如下：
    :type args: Sensor.OutputType

    .. list-table:: 支持的数据类型及说明
        :widths: 20 30 50
        :header-rows: 1

        * - 枚举值
          - 数据类型
          - 说明
        * - ``Sensor.OutputType.Rectify``
          - Optional[np.ndarray]
          - 校正图像,shape=(700, 400, 3),BGR 格式
        * - ``Sensor.OutputType.Difference``
          - Optional[np.ndarray]
          - 差分图像,shape=(700, 400, 3),BGR 格式
        * - ``Sensor.OutputType.Depth``
          - Optional[np.ndarray]
          - 深度图像,shape=(700, 400)，单位为毫米(mm)
        * - ``Sensor.OutputType.Force``
          - Optional[np.ndarray]
          - 三维力分布,shape=(35, 20, 3)
        * - ``Sensor.OutputType.ForceNorm``
          - Optional[np.ndarray]
          - 法向力分量,shape=(35, 20, 3)
        * - ``Sensor.OutputType.ForceResultant``
          - Optional[np.ndarray]
          - 六维合力,shape=(6,)
        * - ``Sensor.OutputType.Marker2D``
          - Optional[np.ndarray]
          - 切向位移,shape=(35,20,2)   
        * - ``Sensor.OutputType.Mesh3D``
          - Optional[np.ndarray]
          - 当前帧 3D 网格,shape=(35, 20, 3)
        * - ``Sensor.OutputType.Mesh3DInit``
          - Optional[np.ndarray]
          - 初始 3D 网格,shape=(35, 20, 3)
        * - ``Sensor.OutputType.Mesh3DFlow``
          - Optional[np.ndarray]
          - 网格形变向量，shape=(35, 20, 3)

    :return: 所请求的传感器数据，返回数量和顺序与输入参数一致。
    :rtype: 与输入参数对应的 ``np.ndarray`` 或 ``None`` (数据未获取到时)

.. note::
  
    如果需要同时获取多种类型的数据，请按照例程中的形式用同一次函数调用获取，这样可以保证所有数据来自于同一帧，并且计算速度是最优化的
    

示例代码
--------
.. container:: step-block

  .. code-block:: python

    from xensesdk import Sensor

    # 创建传感器实例
    sensor = Sensor.create('OP000064')

    # 获取指定类型的传感器数据
    rectify, depth, force = sensor.selectSensorInfo(
        Sensor.OutputType.Rectify,
        Sensor.OutputType.Depth,
        Sensor.OutputType.Force
    )

    # 输出数据形状（示例）
    print("校正图像形状:", rectify.shape)       # (700, 400, 3)
    print("深度图像形状:", depth.shape)         # (700, 400)
    print("三维力分布形状:", force.shape)       # (35, 20, 3)

    # 释放资源
    sensor.release()