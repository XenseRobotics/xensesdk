.. _tag_xensesdkmethodlist:

****************************
Using the XenseSDK API
****************************
.. container:: step-block

    This document provides various methods for processing sensor images, including depth map generation, difference map calculation, marker detection, and comprehensive aggregation of sensor data.

    .. list-table::
        :widths: 30
        :header-rows: 1

        * - API Directory

        * - :ref:`create Method <tagcreate_method>`

        * - :ref:`selectSensorInfo Method <tagselect_sensor_info_method>`

        * - :ref:`getCameraID Method <tagget_camera_id_method>`

        * - :ref:`release Method <tagrelease_method>`

        * - :ref:`calibrateSensor Method <tag_calibrateSensor>`

        * - :ref:`scanSerialNumber Method <tag_scanSerialNumber>`
        
        * - :ref:`createSolver Method <tag_createSolver>`
        
        * - :ref:`exportRuntimeConfig Method <tag_exportRuntimeConfig>`  

        * - :ref:`call_service Method <tag_call_service>`

    For more code examples, please visit the project homepage：

    .. raw:: html

        <div style="margin: 20px 0; text-align: center;">
            <a href="https://github.com/XenseRobotics/xensesdk/tree/main/Examples" target="_blank"
            style="display: inline-block; width: 100%; max-width: 600px; padding: 18px 0;
                    background-color: #f0f0f0; color: #333; text-decoration: none;
                    border-radius: 4px; font-size: 16px; border: 1px solid #e0e0e0;">
                View more example code <i class="fa fa-github"></i>
            </a>
        </div>

    If you encounter issues with the examples, please feel free to share your usage scenarios in the Issues section of the repository to help us improve the examples！
    
.. toctree:: 
    :maxdepth: 1
    :hidden:
    :caption: API Directory

    API/create
    API/selectSensorInfo
    API/getCameraID
    API/release
    API/calibrateSensor
    API/scanSerialNumber
    API/createSolver
    API/exportRuntimeConfig
    API/call_service