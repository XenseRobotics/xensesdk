.. _tag_call_service:

call_service 方法
=======================

.. container:: step-block

    .. py:function:: call_service(master_ip: str, service_name: str, action_name: str, *args, **kwargs) -> dict

        调用算力板上的服务。

        :param master_ip: 算力板 IP 地址，例如: ``192.168.99.2``
        :type master_ip: str
        :param service_name: 服务名称
        :type service_name: str
        :param action_name: 服务支持的 action 名称
        :type action_name: str
        :param args: 传递给服务的可变参数
        :param kwargs: 传递给服务的关键字参数
        :return: 字典结构为:
            ``{"success": True, "ret": ret}``，其中：
            - ``success``: 布尔值，表示调用是否成功
            - ``ret``: 服务返回的具体结果数据
        :rtype: dict