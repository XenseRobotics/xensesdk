.. _tag_ezrosprogramexample:

********************
EzROS编程示例
********************

1. 话题通信（发布/订阅）
----------------------------
.. container:: step-block
   
    发布者示例:

    .. code-block:: python

        import ezros

        ezros.init()
        node = ezros.Node("publisher")
        pub = node.create_publisher(ezros.StringMessage, "chatter")
        rate = ezros.create_rate(1.0)  

        count = 0
        while ezros.ok():
            msg = ezros.StringMessage()
            msg.data = f"Hello, EzROS! {count}"
            pub.publish(msg)
            node.logger.info(f"发布: {msg.data}")
            count += 1
            rate.sleep()

    订阅者示例:

    .. code-block:: python

        import ezros

        def callback(msg):
            print(f"收到消息: {msg.data}")

        ezros.init()
        node = ezros.Node("subscriber")
        sub = node.create_subscriber(ezros.StringMessage, "chatter", callback)
        ezros.spin()


2. 服务通信（请求/响应）
------------------------

.. container:: step-block

    服务端示例:

    .. code-block:: python

        import ezros

        def add_callback(a, b):
            return a + b

        ezros.init()
        node = ezros.Node("add_server")
        service = node.create_service("math_service")
        service.register_callback("add", add_callback)
        ezros.spin()

    客户端示例:

    .. code-block:: python

        import ezros

        ezros.init()
        node = ezros.Node("add_client")
        client = node.create_client("math_service")

        # 方法1: 使用 call 方法
        result = client.call("add", 5, 3, timeout_sec=5.0)

        # 方法2: 使用魔法方法（推荐）
        result = client.add(5, 3, timeout_sec=5.0)

        if result:
            print(f"计算结果: {result}")
        else:
            print("服务调用失败")

        # 或者使用全局便捷函数
        result = ezros.call_service("math_service", "add", 5, 3, timeout_sec=5.0)


3. 复杂数据传输
-----------------

.. container:: step-block

    .. code-block:: python

        import ezros
        import numpy as np
        import time

        # 发布复杂数据
        complex_data = {
            "timestamp": time.time(),
            "sensor_array": np.random.rand(100, 100),
            "metadata": {"sensor_id": "cam_01", "version": "1.0"}
        }

        msg = ezros.BytesMessage(complex_data)
        pub.publish(msg)

        # 订阅复杂数据
        def complex_callback(msg):
            data = msg.get_data()
            print(f"时间戳: {data['timestamp']}")
            print(f"数组形状: {data['sensor_array'].shape}")


4. 消息类型
----------------

.. container:: step-block

    EzROS 提供了多种内置消息类型：

    StringMessage: 字符串消息
   
    BytesMessage: 字节流消息（支持复杂数据和压缩）
   
    IntMessage: 整数消息
   
    FloatMessage: 浮点数消息
   
    BoolMessage: 布尔消息

    BytesMessage 支持自动序列化复杂数据和多种压缩算法：

    .. code-block:: python

        # 基本用法
        data = {"key": "value", "numbers": [1, 2, 3]}
        msg = ezros.BytesMessage(data)

        # 指定压缩算法
        msg = ezros.BytesMessage(data, compression='lz4')  
        # 获取数据
        recovered_data = msg.get_data()