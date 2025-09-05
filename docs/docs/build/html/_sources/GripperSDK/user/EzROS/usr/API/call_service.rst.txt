.. _tag_call_service_:

call_service方法
=====================

.. container:: step-block

   .. py:method:: ezros.call_service(service_name, action_name, *args, timeout_sec=5.0)
       :module: ezros

       EzROS 提供的全局便捷函数，用于直接调用指定服务的目标动作并获取响应，无需先创建客户端实例，简化服务调用流程。

       :param service_name: 待调用的服务名称,需与服务端注册的服务名完全一致。
       :type service_name: str

       :param action_name: 服务下的目标动作名称,需与服务端注册的动作名完全一致。
       :type action_name: str

       :param `*args`: 传递给服务动作的参数，参数数量和类型需与服务端动作的参数要求匹配。
       :type `*args`: Any

       :param timeout_sec: 服务调用超时时间，单位为秒，默认值为 5.0 秒。
       :type timeout_sec: float, optional
       
       :return: 服务执行后的响应结果,格式由服务端定义，如字典、数值等。
       :rtype: Any | None
       
       :note: 
           1. 调用前需确保EzROS框架已通过ezros.init()初始化，且服务端已启动并注册对应服务与动作。
          
示例代码
--------
.. container:: step-block

    .. code-block:: python

        import ezros

        # 1. 初始化EzROS框架（服务调用前必须执行）
        ezros.init()

        # 2. 创建节点（作为服务调用的功能载体）
        node = ezros.Node("add_client_node")

        # 创建客户端，关联目标服务 "math_service"
        client = node.create_client("math_service")
        result1 = client.call("add", 5, 3, timeout_sec=5.0)
       
        if result1:
            print(f"方式1(client.call)计算结果: {result1}")
        else:
            print("方式1:服务调用失败（超时/服务不存在/参数错误）")

        