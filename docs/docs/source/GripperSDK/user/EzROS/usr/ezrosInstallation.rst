.. _tag_ezrosinstallation:

***************
快速安装
***************

安装指南
-------------
.. container:: step-block

    **步骤 1:** 安装指定版本的 CycloneDDS nightly build


    .. code-block:: bash
        
        # 安装 2025.7.29 版本的 CycloneDDS nightly build（确保兼容性）
        pip install cyclonedds-nightly==2025.7.29

.. container:: step-block

    **步骤 2:** 安装依赖包


    .. code-block:: bash
        
        # 安装 numpy（数据处理）和 lz4（BytesMessage 数据压缩）依赖
        pip install numpy lz4

依赖版本说明
-------------
.. note:: 

    cyclonedds-nightly固定使用 2025.7.29 版本，以保障与相关组件的兼容性；
    numpy最低版本要求为 1.20.0,满足数据处理场景的基础依赖；
    lz4核心用于 BytesMessage 类型数据的压缩，提升数据传输与存储效率。