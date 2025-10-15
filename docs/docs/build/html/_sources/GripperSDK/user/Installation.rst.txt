.. _tag_Gripperinstallation:

Installing GripperSDK
===========================

.. raw:: html

    <style>
    /* 步骤标题样式（外显，无边框） */
    .step-title {
        font-size: 1.3em !important;
        font-weight: 700 !important;
        color: #2c3e50 !important;
        margin-top: 1.8em !important;
        margin-bottom: 0.5em !important;
        font-family: "Microsoft YaHei", sans-serif !important;
    }
    
    /* 步骤内容容器（带边框） */
    .step-content {
        border: 1px solid #ddd !important;
        border-radius: 6px !important;
        padding: 15px 20px !important;
        background-color: #f9f9f9 !important;
        margin-bottom: 1em !important;
    }

    /* 自定义代码块样式 - 蓝色字体 */
    .step-content .highlight pre {
        color: #2980b9 !important; /* 蓝色字体 */
        font-weight: 500 !important; /* 略微加粗 */
        background-color: #f0f7ff !important; /* 浅蓝色背景衬托 */
        padding: 10px 15px !important;
        border-radius: 4px !important;
        border: 1px solid #bed6e3 !important; /* 浅蓝色边框 */
    }
    </style>


.. rubric:: Step 1: Prepare the Python Development Environment
   :class: step-title

.. container:: step-content

    GripperSDK depends on XenseSDK, so a Python development environment needs to be installed. Please refer to the Python development environment preparation in `XenseSDK <../../XenseSDK/usr/Installation.html>`_.


.. rubric:: Step 2: Install the GripperSDK Package
   :class: step-title

.. container:: step-content

    .. code-block:: bash
        
        pip install xensegripper

.. admonition:: tips
   :class: tip

   For the latest version of GripperSDK, please obtain it from the `official Github website <https://github.com/XenseRobotics/xensesdk/releases>`_.
