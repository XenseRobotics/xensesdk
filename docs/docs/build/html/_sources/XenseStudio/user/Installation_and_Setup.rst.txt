.. _tag_installation_and_setup:

III. Installation and Setup
================================

1. Installation Steps
-------------------------

**Windows Platform：**
The XenseStudio.exe installer is provided. Double-click the file and follow the on-screen prompts to complete the installation. After installation, a shortcut named "Xense Studio" will be displayed on the desktop.

**Linux Platform：**
The xensestudio.deb installer is provided. Use the sudo command to install it:

.. code-block:: bash

    sudo dpkg -i /path/to/your/XenseStudio_v1.1.4.deb
.. raw:: html

    <div class="download-button-container" style="text-align: center; margin: 2em 0;">
        <a href="https://pan.baidu.com/s/1pifsPkFevYTWBEq1PUNwDQ?pwd=yjcd"
           class="download-button"
           style="
               display: inline-flex;
               align-items: center;
               justify-content: center;
               padding: 0.75rem 2rem;
               background-color: #3B82F6;
               color: white;
               font-weight: 500;
               border-radius: 0.5rem;
               text-decoration: none;
               box-shadow: 0 4px 6px -1px rgba(59, 130, 246, 0.4);
               transition: all 0.3s ease;
           ">
            <i class="fa fa-download" style="margin-right: 0.5rem;"></i>
            Install XenseStudio
        </a>
    </div>

    <style>
        .download-button:hover {
            background-color: #1E40AF;
            transform: translateY(-2px);
            box-shadow: 0 10px 15px -3px rgba(59, 130, 246, 0.4);
        }
    </style>

2. Initial Configuration
-----------------------------
After the program starts, the software interface will be displayed as shown in Figure 1:

.. raw:: html

    <style>
        /* 强制制强制图片比例保持原始比例 */
        .preserve-aspect-ratio img {
            max-width: 100%;    /* 最大宽度不超过容器 */
            height: auto !important;  /* 强制高度自适应，!important覆盖默认样式 */
            object-fit: contain;      /* 保持比例，不裁剪 */
            display: block;
            margin: 0 auto;
        }
    </style>

.. figure:: ../images/initial_setup.png
    :alt: Software Initial Configuration
    :align: center
    :scale: 100%
    :name: _xs-initial_setup
    :class: preserve-aspect-ratio

    Figure 1: Software Initial Configuration
