.. _tag_scanSerialNumber:

scanSerialNumber Method
============================

.. container:: step-block

    .. py:method:: Sensor.scanSerialNumber() -> dict
        :module: xensesdk
        :noindex:

        Scans and returns information about all connected sensors on the current device.

        This method detects sensor devices connected to the system and returns the mapping between their serial numbers and corresponding camera IDs, facilitating the creation of sensor instances via serial numbers later.

        :return: A dictionary containing all connected sensors, where keys are sensor serial numbers (``serial_number``) and values are corresponding camera IDs (``camera_id``)
        :rtype: dict