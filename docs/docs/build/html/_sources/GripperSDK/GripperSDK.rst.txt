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

    <div class="custom-h2">核心功能</div>

.. container:: step-block

    .. list-table:: 
        :header-rows: 1
        :widths: 20 60

        * - 功能模块
          - 说明
        * - 夹爪控制
          - 支持以 200 Hz 频率接收夹爪数据，同时可对夹爪运动进行精准控制。  
        * - 传感器控制
          - 提供传感器启动、关闭操作接口，支持读取传感器实时数据，满足不同场景下的数据采集需求。  
        * - 服务联网自启动
          - 无论设备是直连电脑，还是通过交换机接入网络，实现 “即插即用” 。  
        * - 服务自动发现
          - SDK 可自动扫描可连接的服务节点，简化人工配置流程，提升系统部署效率。  
        * - 休眠模式
          - 若传感器 10 min 未被使用，自动关闭传感器以降低功耗，仅保留主服务节点持续运行，保障基础服务不中断。  
        * - CLI 调试工具
          - 通过 ``EzROS`` 命令行工具，可快速测试服务状态，便于开发与运维阶段排查问题。  

.. raw:: html

    <div class="custom-h2">系统架构</div>

.. raw:: html

    <div class="custom-h2">主目录</div>

.. container:: step-block
 
    .. list-table::
        :width: 30
        
        * - :ref:`硬件连接与网络配置 <tag_Gripperpre_configuration>`
        
        * - :ref:`安装指南 <tag_Gripperinstallation>`
        
        * - :ref:`API文档 <tag_Grippermethodlist>`
        
        * - :ref:`EzROS调试工具 <tag_ezros>` 

.. toctree::
   :maxdepth: 3
   :caption: 目录
   :hidden:
   
   user/pre_configuration

   user/Installation

   user/methodlist
   
   user/Zeroros/Zeroros
