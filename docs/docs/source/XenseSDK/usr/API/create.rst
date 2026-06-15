.. _tagcreate_method:

create Method
==================

.. container:: step-block

    .. py:method:: Sensor.create(cam_id=0, use_gpu=True, config_path=None, api=None, check_serial=True, rectify_size=None, mac_addr=None, video_path=None)
        :module: xensesdk

        Creates a sensor instance. After use, call :meth:`~Sensor.release` to free up resources.

        :param cam_id: Sensor ID, serial number, or video path. Defaults to 0.
        :type cam_id: int | str, optional
        
        :param config_path: Path or directory of the configuration file. If it is a directory, it must contain a calibration file with the same name as the sensor serial number.
        :type config_path: str | Path, optional
        
        :param api: Camera API type (e.g., OpenCV backend), used to specify the camera access method.
        :type api: Enum, optional
        
        :param check_serial: Whether to check the sensor serial number.
        :type check_serial: bool, optional
        
        :param rectify_size: Rectified image size (width, height).
        :type rectify_size: tuple[int, int], optional
        
        :param mac_addr: Camera MAC address used for remote connection.
        :type mac_addr: str, optional
        
        :return: Sensor instance, used for subsequent data collection and processing.
        :rtype: :class:`Sensor`

.. note::
    
    After use, be sure to call :meth:`~Sensor.release` to free up system resources.

Example Code
-------------------
.. container:: step-block

    .. tab-set::

        .. tab-item:: Example 1: Start Sensor via Serial Number (SN)

            .. code-block:: python

                from xensesdk import Sensor

                # Create an instance using the sensor serial number (SN)
                sensor = Sensor.create('OP000064')

                # Release resources after use
                sensor.release()

        .. tab-item:: Example 2: Start Sensor via Camera ID

            .. code-block:: python

                from xensesdk import Sensor

                # Create an instance using the camera ID (e.g., 0, 1)
                sensor = Sensor.create(0)

                # Release resources after use
                sensor.release()

        .. tab-item:: Example 3: Connect to Sensor on Remote Computing Board

            .. code-block:: python

                from xensesdk import Sensor

                # Specify the MAC address to connect to the remote sensor
                master_service = "master_000000000000"
                sensor = Sensor.create('OP000064', mac_addr="000000000000")

                # Release resources after use
                sensor.release()

.. admonition:: tips
    :class: tip

        You can refer to how to get the master_service in Example 3.
        `EzROS </home/xense/projects/docs-en/xensesdk/docs/docs/source//GripperSDK/user/EzROS/ezros_example.html>`_.