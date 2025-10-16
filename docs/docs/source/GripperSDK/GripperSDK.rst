GripperSDK
=================

.. raw:: html

    <style>
    .custom-h2 {
        font-size: 1.5em !important; /* 更大的字号 */
        font-weight: 700 !important;
        color: #2c3e50 !important; /* 深色更有质感 */
        border-bottom: 1px solid #fffdfdff !important; /* 更粗的下边框 */
        padding-bottom: 10px !important;
        margin-top: 1.5em !important;
        margin-bottom: 0.8em !important;
        font-family: "Microsoft YaHei", sans-serif !important; /* 换成更适配的中文字体 */
        text-shadow: 0 2px 3px rgba(0,0,0,0.1); /* 增加文字阴影 */
        background: linear-gradient(to right, #3498db, #9b59b6); /* 背景渐变（可选） */
        -webkit-background-clip: text;
        color: transparent; /* 文字渐变效果（需配合背景渐变） */
    }
    </style>

.. raw:: html

    <div class="custom-h2">Core Functions</div>

.. container:: step-block

    .. list-table:: 
        :header-rows: 1
        :widths: 20 60

        * - Function Module
          - Description
        * - Gripper Control
          - Supports receiving gripper data at a frequency of 200 Hz, while enabling precise control of gripper movement.  
        * - Sensor Control
          - Provides interfaces for sensor startup and shutdown operations, and supports reading real-time sensor data to meet data collection needs in different scenarios.  
        * - Service Auto-Startup on Network Connection
          - Enables "plug-and-play" functionality regardless of whether the device is directly connected to a computer or accessed via a switch.  
        * - Service Auto-Discovery
          - The SDK can automatically scan for connectable service nodes, simplifying manual configuration processes and improving system deployment efficiency.  
        * - Sleep Mode
          - If the sensor is not used for 10 minutes, it will automatically turn off to reduce power consumption, while only keeping the main service node running continuously to ensure uninterrupted basic services.  
        * - CLI Debugging Tool
          - Through the ``EzROS`` command-line tool, you can quickly test the service status, facilitating problem troubleshooting during development and operation phases.  


.. raw:: html

    <div class="custom-h2">Main Directory</div>

.. container:: step-block
 
    .. list-table::
        :width: 30
        
        * - :ref:`Hardware Connection & Network Configuration <tag_Gripperpre_configuration>`
        
        * - :ref:`Installation Guide <tag_Gripperinstallation>`
        
        * - :ref:`API Documentation <tag_Grippermethodlist>`

        * - :ref:`Sensor Connection <tag_Gripperconnect_sensor>`
        
        * - :ref:`EzROS Debugging Tool <tag_ezros>` 

        * - :ref:`GUI User Guide <tag_guiUseGuide>` 

.. toctree::
   :maxdepth: 3
   :caption: Table of Contents
   :hidden:
   
   user/pre_configuration

   user/Installation

   user/methodlist

   user/connect_sensor
   
   user/EzROS/EzROS
  
   user/GuiUseGuide/GuiUseGuide