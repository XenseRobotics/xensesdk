.. _tag_create_timer_:

create_timer方法
=====================

.. container:: step-block

   .. py:method:: Node.create_timer(self, interval_ms: int, callback: callable, start: bool = True, delay_ms: int = 0) -> Timer
       :module: ezros

       创建定时器，按指定间隔周期性执行回调函数。

       :param interval_ms: 执行间隔（毫秒）
       :type interval_ms: int
       
       :param callback: 定时执行的回调函数
       :type callback: callable
       
       :param start: 是否立即启动,默认True
       :type start: bool, optional
       
       :param delay_ms: 启动后延迟执行时间(毫秒),默认0
       :type delay_ms: int, optional
       
       :return: 定时器对象
       :rtype: ezros.Timer
       
       
示例代码
--------
.. container:: step-block

    .. code-block:: python

        import ezros
        
        def timer_callback():
            print("定时器触发")
        
        node = ezros.Node("timer_node")
        timer = node.create_timer(1000, timer_callback, delay_ms=500)
        ezros.spin(node)
        node.shutdown()