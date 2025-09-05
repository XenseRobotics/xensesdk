.. _tag_create_client_:

create_client方法
=====================

.. container:: step-block

   .. py:method:: Node.create_client(self, service_name: str) -> ServiceClient
       :module: ezros

       在当前节点上创建一个服务客户端，用于调用指定名称的服务端提供的功能。

       :param service_name: 要调用的服务名称(字符串),必须与服务端创建时使用的名称完全一致(区分大小写),符合ROS服务命名规范。
       :type service_name: str
       
       :return: 新创建的服务客户端对象，通过该对象可调用服务端提供的具体动作。
       :rtype: ezros.ServiceClient
       

示例代码
--------
.. container:: step-block

    .. code-block:: python

        import ezros
        
        # 创建节点
        node = ezros.Node("math_client_node")
        
        # 创建服务客户端，连接到"math_service"服务
        client = node.create_client("math_service")
        
        # 等待服务端就绪
        if node.wait_for_service("math_service", timeout=5.0):
            # 调用服务的"add"动作
            result = client.add(3, 5)  # 等价于 client.call("add", 3, 5)
            print(f"3 + 5 = {result}")
        else:
            print("服务端未就绪，无法调用服务")
        
        node.shutdown()