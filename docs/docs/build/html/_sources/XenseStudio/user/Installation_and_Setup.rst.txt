.. _tag_installation_and_setup:

三、安装与设置
=================

1、 安装步骤
-------------

**Windows平台：**
提供XenseStudio.exe安装程序。双击以后，按照提示操作。安装完毕后将在桌面显示其快捷方式：Xense Studio。

**Linux平台：**
提供安装程序xensestudio.deb，使用sudo命令进行安装：

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
            下载 XenseStudio
        </a>
    </div>

    <style>
        .download-button:hover {
            background-color: #1E40AF;
            transform: translateY(-2px);
            box-shadow: 0 10px 15px -3px rgba(59, 130, 246, 0.4);
        }
    </style>

2、 初始配置
-----------------
程序启动以后软件显示界面如图1所示：

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
    :alt: 软件初始设置
    :align: center
    :scale: 100%
    :name: _xs-initial_setup
    :class: preserve-aspect-ratio 

    图 1 软件初始设置
