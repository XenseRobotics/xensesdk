.. _tag_service_is_ready_:

service_is_ready方法
======================

.. container:: step-block

   .. py:method:: Node.service_is_ready(self, service_name: str, action_name: str = None) -> bool
       :module: ezros

       检查指定服务是否就绪，可用于判断服务是否可被调用。

       :param service_name: 服务名称
       :type service_name: str
       
       :param action_name: 服务动作名称，可选参数
       :type action_name: str, optional
       
       :return: 服务就绪返回True,否则返回False
       :rtype: bool
       
示例代码
--------
.. container:: step-block

    .. code-block:: python

        import ezros
        
        node = ezros.Node("service_check_node")
        client = node.create_client("math_service")
        
        if node.service_is_ready("math_service", "add"):
            print("加法服务已就绪")
        else:
            print("加法服务未就绪")
        
        node.shutdown()