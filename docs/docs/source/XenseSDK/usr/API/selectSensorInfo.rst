.. _tagselect_sensor_info_method:

selectSensorInfo Method
================================

.. container:: step-block

  .. py:method:: Sensor.selectSensorInfo(*args)
    :module: xensesdk

    Retrieves sensor data of specified types, with the quantity and order matching the input parameters.

    :param args: Any number of ``Sensor.OutputType`` enums specifying the data types to retrieve. Supported enum values and corresponding data are as follows:
    :type args: Sensor.OutputType

    .. list-table:: Supported Data Types and Descriptions
        :widths: 20 30 50
        :header-rows: 1

        * - Enum Value
          - Data Type
          - Description
        * - ``Sensor.OutputType.Rectify``
          - Optional[np.ndarray]
          - Rectified image, shape=(700, 400, 3), BGR format
        * - ``Sensor.OutputType.Difference``
          - Optional[np.ndarray]
          - Difference image, shape=(700, 400, 3), BGR format
        * - ``Sensor.OutputType.Depth``
          - Optional[np.ndarray]
          - Depth image, shape=(700, 400), unit in millimeters (mm)
        * - ``Sensor.OutputType.Force``
          - Optional[np.ndarray]
          - 3D force distribution, shape=(35, 20, 3)
        * - ``Sensor.OutputType.ForceNorm``
          - Optional[np.ndarray]
          - Normal force component, shape=(35, 20, 3)
        * - ``Sensor.OutputType.ForceResultant``
          - Optional[np.ndarray]
          - 6-dimensional resultant force, shape=(6,)
        * - ``Sensor.OutputType.Marker2D``
          - Optional[np.ndarray]
          - Tangential displacement, shape=(26,14,2)   
        * - ``Sensor.OutputType.Mesh3D``
          - Optional[np.ndarray]
          - Current frame 3D mesh, shape=(35, 20, 3)
        * - ``Sensor.OutputType.Mesh3DInit``
          - Optional[np.ndarray]
          - Initial 3D mesh, shape=(35, 20, 3)
        * - ``Sensor.OutputType.Mesh3DFlow``
          - Optional[np.ndarray]
          - Mesh deformation vector, shape=(35, 20, 3)
        * - ``Sensor.OutputType.TimeStamp``
          - Optional[np.ndarray]
          - Sensor timestamp, shape=(35, 20, 3)

    :return: Requested sensor data with quantity and order matching input parameters.
    :rtype: Corresponding ``np.ndarray`` or ``None`` (when data is unavailable)

.. note::
  
    If you need to retrieve multiple types of data simultaneously, use a single function call as shown in the example. This ensures all data comes from the same frame and optimizes calculation speed.
    

Example Code
-----------------
.. container:: step-block

  .. code-block:: python

    from xensesdk import Sensor

    # Create sensor instance
    sensor = Sensor.create('OP000064')

    # Retrieve specified types of sensor data
    rectify, depth, force = sensor.selectSensorInfo(
        Sensor.OutputType.Rectify,
        Sensor.OutputType.Depth,
        Sensor.OutputType.Force
    )

    # Output data shapes (example)
    print("Rectified image shape:", rectify.shape)       # (700, 400, 3)
    print("Depth image shape:", depth.shape)             # (700, 400)
    print("3D force distribution shape:", force.shape)   # (35, 20, 3)

    # Release resources
    sensor.release()