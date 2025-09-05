.. _tag_create_publisher_:

create_publisher方法
======================

.. container:: step-block

   .. py:method:: Node.create_publisher(self, msg_type, topic: str, qos_depth: int = 10)
       :module: ezros

       在当前节点上创建一个话题发布者，用于向指定话题发布消息。

       :param msg_type: 消息类型类，定义了要发布的消息结构；
                        需与订阅该话题的订阅者使用相同的消息类型。
       :type msg_type: Type[Message]
       
       :param topic: 要发布的话题名称(字符串),需符合ROS话题命名规范;
                     建议使用斜杠分隔的层次结构（如"robot/position"）。
       :type topic: str
       
       :param qos_depth: QoS(服务质量)队列深度,默认值为10;
                         表示消息发布者的消息缓存队列长度，超出后旧消息将被丢弃。
       :type qos_depth: int, optional
       
       :return: 新创建的发布者对象，通过其`publish()`方法可发布消息。
       :rtype: ezros.Publisher
       
       
示例代码
--------
.. container:: step-block

    .. code-block:: python

        import ezros
        from std_msgs.msg import String  # 假设使用标准字符串消息类型
        
        # 创建节点
        node = ezros.Node("talker_node")
        
        # 创建发布者，向"chatter"话题发布String类型消息
        publisher = node.create_publisher(String, "chatter", qos_depth=5)
        
        # 发布消息
        msg = String()
        msg.data = "Hello EzROS!"
        publisher.publish(msg)
        
        ezros.spin(node)  # 启动节点事件循环
        node.shutdown()