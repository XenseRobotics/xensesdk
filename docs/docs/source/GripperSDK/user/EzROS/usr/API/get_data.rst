.. _tag_get_data_:

get_data方法
=====================

.. container:: step-block

   .. py:method:: ezros.BytesMessage.get_data()
       :module: ezros

       用于从序列化的字节流中提取并还原原始数据，自动处理压缩数据的解压缩过程。

       :return: 与创建 ``BytesMessage`` 时传入的原始数据完全一致的内容,支持字典、列表、字符串、NumPy数组等多种数据类型。
       :rtype: Any
       
       :raises ValueError: 若消息数据损坏或序列化格式异常，可能触发此异常。
       :raises ImportError: 若创建消息时使用了特定压缩算法（如 ``lz4``），但当前环境未安装对应解压库，会触发此异常。
       
       :note: 
           1. 无论创建 ``BytesMessage`` 时是否启用压缩（`compression` 参数），``get_data()`` 都会自动适配解压逻辑，无需手动处理。
           2. 反序列化后的数据类型与原始数据严格一致（如原始数据为字典，返回结果也为字典），确保数据完整性。


示例代码
--------
.. container:: step-block

    .. code-block:: python

        import ezros

        # 1. 基本用法：无压缩数据的反序列化
        raw_data = {
            "key": "value",
            "numbers": [1, 2, 3],
            "status": True,
            "score": 95.5
        }
        # 创建BytesMessage对象（自动序列化）
        msg = ezros.BytesMessage(raw_data)
        # 调用get_data()反序列化，恢复原始数据
        recovered_data = msg.get_data()
        print("原始数据:", raw_data)
        print("恢复数据:", recovered_data)
        print("数据类型是否一致:", type(recovered_data) == type(raw_data))  # 输出 True


    