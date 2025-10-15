.. _tagcreate_method:

create Method
==================

.. container:: step-block

    .. py:method:: Sensor.create(cam_id=0, use_gpu=True, config_path=None, api=None, check_serial=True, rectify_size=None, ip_address=None, video_path=None)
        :module: xensesdk

        Creates a sensor instance. After use, call :meth:`~Sensor.release` to free up resources.

        :param cam_id: Sensor ID, serial number, or video path. Defaults to 0.
        :type cam_id: int | str, optional
        
        :param use_gpu: Whether to use GPU for inference.
        :type use_gpu: bool, optional
        
        :param config_path: Path or directory of the configuration file. If it is a directory, it must contain a calibration file with the same name as the sensor serial number.
        :type config_path: str | Path, optional
        
        :param api: Camera API type (e.g., OpenCV backend), used to specify the camera access method.
        :type api: Enum, optional
        
        :param check_serial: Whether to check the sensor serial number.
        :type check_serial: bool, optional
        
        :param rectify_size: Rectified image size (width, height).
        :type rectify_size: tuple[int, int], optional
        
        :param mac_address: Camera MAC address used for remote connection.
        :type mac_address: str, optional
        
        :param video_path: Video path for offline simulation.
        :type video_path: str, optional
        
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

        .. tab-item:: Example 3: Open Stored Offline Data

            .. code-block:: python

                from xensesdk import Sensor

                # Load local data via video_path (set cam_id to None)
                sensor = Sensor.create(None, video_path=r"data.h5")

                # Release resources after use
                sensor.release()

        .. tab-item:: Example 4: Connect to Sensor on Remote Computing Board

            .. code-block:: python

                from xensesdk import Sensor

                # Specify the IP address to connect to the remote sensor
                sensor = Sensor.create('OP000064', ip_address="192.168.66.66")

                # Release resources after use
                sensor.release()

.. admonition:: tips
    :class: tip

        The mac_address parameter in Example 4 is compatible with the device IP address. For instructions on how to obtain the device MAC address, refer to
        `EzROS </home/xense/projects/docs-en/xensesdk/docs/docs/source//GripperSDK/user/EzROS/ezros_example.html>`_.