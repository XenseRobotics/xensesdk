.. _tag_create_subscriber_:

create_subscriber方法
=====================

.. container:: step-block

   .. py:method:: Node.create_subscriber(self, msg_type, topic: str, callback, qos_depth: int = 10)
       :module: ezros

       在当前节点上创建一个话题订阅者，用于接收指定话题的消息并触发回调处理。

       :param msg_type: 消息类型类，需与发布该话题的发布者使用相同的消息类型，
                        用于解析接收到的消息数据。
       :type msg_type: Type[Message]
       
       :param topic: 要订阅的话题名称（字符串），需与发布者使用的话题名称完全一致
                     ,符合ROS话题命名规范。
       :type topic: str
       
       :param callback: 消息处理回调函数，当接收到新消息时自动调用；
                       函数需接收一个参数（即接收到的消息对象）。
       :type callback: Callable[[Message], None]
       
       :param qos_depth: QoS(服务质量)队列深度,默认值为10;
                         表示订阅者的消息缓存队列长度，超出后旧消息将被丢弃。
       :type qos_depth: int, optional
       
       :return: 新创建的订阅者对象，可用于管理订阅关系。
       :rtype: ezros.Subscriber
       
      
示例代码
--------
.. container:: step-block

    .. code-block:: python

        import ezros
        from std_msgs.msg import String  # 假设使用标准字符串消息类型
        
        # 定义消息处理回调函数
        def callback(msg):
            print(f"收到消息: {msg.data}")
        
        # 创建节点
        node = ezros.Node("listener_node")
        
        # 创建订阅者，订阅"chatter"话题的String类型消息
        subscriber = node.create_subscriber(String, "chatter", callback, qos_depth=5)
        
        ezros.spin(node)  # 启动节点事件循环，持续接收消息
        node.shutdown()