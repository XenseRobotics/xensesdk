.. _tag_wait_for_service_:

wait_for_service方法
=====================

.. container:: step-block

   .. py:method:: Node.wait_for_service(self, service_name: str, timeout: float = None) -> bool
       :module: ezros

       阻塞等待指定服务就绪，直到服务可用或超时。

       :param service_name: 服务名称
       :type service_name: str
       
       :param timeout: 最大等待时间(秒),默认None(无限期等待)
       :type timeout: float, optional
       
       :return: 服务就绪返回True,超时返回False
       :rtype: bool
       

示例代码
--------
.. container:: step-block

    .. code-block:: python

        import ezros
        
        node = ezros.Node("service_wait_node")
        client = node.create_client("data_service")
        
        # 最多等待3秒
        if node.wait_for_service("data_service", timeout=3.0):
            print("服务已就绪，可调用")
        else:
            print("等待服务超时")
        
        node.shutdown()