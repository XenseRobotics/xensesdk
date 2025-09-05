.. _tag_bytesmessage_:

BytesMessage方法
=====================

.. container:: step-block

   .. py:class:: ezros.BytesMessage(data, compression='none')
       :module: ezros

       EzROS 提供的字节流消息类型,用于序列化复杂数据(如字典、列表、NumPy数组等)并支持数据压缩，适用于需要高效传输或存储复杂结构数据的场景（如话题发布/订阅、服务请求/响应）。通过 `get_data()` 方法可反序列化恢复原始数据。

       :param data: 待序列化的原始数据,支持多种数据类型,如字典、列表、字符串、NumPy数组等。
       :type data: Any

       :param compression: 数据压缩算法，可选值为 `'none'`（无压缩，默认）、`'lz4'`(LZ4压缩,高效快速)、`'zlib'`(Zlib压缩,压缩率更高)；需确保环境中已安装对应压缩库（如使用 `'lz4'` 需先安装 `lz4` 包）。
       :type compression: str, optional
       

示例代码
--------
.. container:: step-block

    .. code-block:: python

        import ezros

        # 基本用法：创建BytesMessage（默认无压缩）
        # 定义复杂结构原始数据（支持字典、列表等混合类型）
        raw_data = {
            "key": "value",
            "numbers": [1, 2, 3],
            "status": True,
            "score": 95.5
        }
        # 用原始数据创建BytesMessage对象（自动序列化）
        msg1 = ezros.BytesMessage(raw_data)
        
       