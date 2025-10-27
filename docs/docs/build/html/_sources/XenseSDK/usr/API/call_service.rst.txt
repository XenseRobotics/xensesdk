.. _tag_call_service:

call_service Method
=======================

.. container:: step-block

    .. py:function:: call_service(master_ip: str, service_name: str, action_name: str, *args, **kwargs) -> dict

        Calls the service on the computing board.

        :param master_ip: IP address of the computing board, e.g.: ``192.168.99.2``
        :type master_ip: str
        :param service_name: Name of the service
        :type service_name: str
        :param action_name: Name of the action supported by the service
        :type action_name: str
        :param args: Variable arguments passed to the service
        :param kwargs: Keyword arguments passed to the service
        :return: The dictionary structure is:
            ``{"success": True, "ret": ret}``, where:
            - ``success``: Boolean value indicating whether the call was successful
            - ``ret``: Specific result data returned by the service
        :rtype: dict