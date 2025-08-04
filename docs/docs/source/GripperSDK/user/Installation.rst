.. _tag_Gripperinstallation:

安装GripperSDK
===================

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

    <div class="custom-h2">安装指南</div>

.. container:: step-block

    **步骤 1:** 准备 Python 开发环境

    请参考
     `XenseSDK <../../XenseSDK/usr/Installation>`_ 中的 Python 开发环境准备。



.. container:: step-block

    **步骤 2:** 安装 CUDA 工具包和 cuDNN
    
    请参考
     `XenseSDK <../../XenseSDK/usr/Installation>`_ 中的 CUDA 工具包和 cuDNN 安装 。        

.. container:: step-block

    **步骤 3:** 安装 SDK 包
    将 SDK 包安装到您的环境中：

    .. code-block:: bash
        
        pip install xensesdk
        pip install xensegripper


    