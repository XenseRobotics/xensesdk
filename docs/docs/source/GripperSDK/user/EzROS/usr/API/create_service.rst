.. _tag_create_service_:

create_service方法
=====================

.. container:: step-block

   .. py:method:: Node.create_service(self, service_name: str) -> ServiceServer
       :module: ezros

       在当前节点上创建一个服务端，用于提供指定名称的服务并处理客户端请求。

       :param service_name: 服务名称(字符串),需符合ROS服务命名规范;
                           建议使用斜杠分隔的层次结构(如"robot/calculate"),
                           客户端需通过相同名称调用服务。
       :type service_name: str
       
       :return: 新创建的服务端对象，需通过其`register_callback()`方法注册具体动作的处理函数。
       :rtype: ezros.ServiceServer
       
      
示例代码
--------
.. container:: step-block

    .. code-block:: python
        
        import ezros
        
        # 定义加法服务的回调函数
        def add_callback(a, b):
            return a + b
        
        # 创建节点
        node = ezros.Node("math_service_node")
        
        # 创建名为"math_service"的服务端
        service = node.create_service("math_service")
        
        # 为服务注册"add"动作的处理回调
        service.register_callback("add", add_callback)
        
        ezros.spin(node)  # 启动节点事件循环，等待客户端调用
        node.shutdown()