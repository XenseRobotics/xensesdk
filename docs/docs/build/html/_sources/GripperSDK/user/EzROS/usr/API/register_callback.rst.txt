.. _tag_register_callback_:

register_callback方法
=======================

.. container:: step-block

   .. py:method:: ServiceServer.register_callback(self, action: str, callback: Callable)
       :module: ezros

       为服务注册指定动作的处理回调函数。

       :param action: 服务动作名称
       :type action: str
       
       :param callback: 处理该动作的回调函数，接收客户端传入的参数并返回处理结果
       :type callback: Callable
       
示例代码
--------
.. container:: step-block

    .. code-block:: python

        import ezros
        
        def multiply_callback(a, b):
            return a * b
        
        node = ezros.Node("calc_server_node")
        service = node.create_service("calc_service")
        service.register_callback("multiply", multiply_callback)
        
        ezros.spin(node)
        node.shutdown()