.. _tag_Gripperconnect_sensor:

Sensor Connection
=========================

This article describes how to quickly connect sensors in Gripper-related device development.

1. Scan Sensor List
------------------------
Import modules and scan for available sensors. You need to replace the actual master control service identifier:

.. container:: step-block

  .. code-block:: python

    import sys
    from xensesdk import ExampleView, Sensor, call_service

    MASTER_SERVICE = "master_d672f584b17a"
    ret = call_service(MASTER_SERVICE, "scan_sensor_sn")
    if ret is None:
        print("Scan failed, check master control service")
        sys.exit(1)
    serial_number = list(ret.keys())[0]

2. Create Sensor Instance
---------------------------------
Create a sensor object using the serial number and extracted MAC address:

.. container:: step-block

  .. code-block:: python

    mac_address = MASTER_SERVICE.split("_")[-1]
    sensor = Sensor.create(serial_number, mac_addr=mac_address)

3. Configure Data Processing (Optional)
---------------------------------------------
If visualization is required, create a view and define data callback:

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

4. Start and Release Resources
----------------------------------------
Start the display and release resources when finished:

.. container:: step-block

  .. code-block:: python

    sensor.release()
    sys.exit()

Notes
--------
- Ensure the master control service identifier is correct, the sensor is powered on and on the same network
- For multiple sensors, you can loop through all serial numbers in `ret`
- `release()` must be called to avoid device occupation conflicts