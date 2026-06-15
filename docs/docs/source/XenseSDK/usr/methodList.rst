.. _tag_xensesdkmethodlist:

********************
使用XenseSDK API
********************
.. container:: step-block

    本文件提供了用于处理传感器图像的各类方法，包含深度图生成、差异图计算、标记检测以及传感器数据的综合聚合。
    
    .. list-table::
        :widths: 30
        :header-rows: 1

        * - API目录

        * - :ref:`create 方法 <tagcreate_method>`

        * - :ref:`selectSensorInfo 方法 <tagselect_sensor_info_method>`

        * - :ref:`getCameraID 方法 <tagget_camera_id_method>`

        * - :ref:`release 方法 <tagrelease_method>`

        * - :ref:`calibrateSensor 方法 <tag_calibrateSensor>`

        * - :ref:`scanSerialNumber 方法 <tag_scanSerialNumber>`
        
        * - :ref:`createSolver 方法 <tag_createSolver>`
        
        * - :ref:`exportRuntimeConfig 方法 <tag_exportRuntimeConfig>`  

        * - :ref:`call_service 方法 <tag_call_service>`

    更多代码示例请跳转至项目主页查看：
    
    .. raw:: html

        <div style="margin: 20px 0; text-align: center;">
            <a href="https://github.com/XenseRobotics/xensesdk/tree/main/Examples" target="_blank"
            style="display: inline-block; width: 100%; max-width: 600px; padding: 18px 0;
                    background-color: #f0f0f0; color: #333; text-decoration: none;
                    border-radius: 4px; font-size: 16px; border: 1px solid #e0e0e0;">
                查看更多示例代码 <i class="fa fa-github"></i>
            </a>
        </div>

    如果您在示例中遇到了问题，欢迎在仓库的 Issues 区分享您的使用场景，帮助我们完善示例！

.. toctree:: 
    :maxdepth: 1
    :hidden:
    :caption: API目录

    API/create
    API/selectSensorInfo
    API/getCameraID
    API/release
    API/calibrateSensor
    API/scanSerialNumber
    API/createSolver
    API/exportRuntimeConfig
    API/call_service