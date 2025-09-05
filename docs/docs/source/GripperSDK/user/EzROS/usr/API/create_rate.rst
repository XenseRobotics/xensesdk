.. _tag_create_rate_:

create_rate方法
=====================

.. container:: step-block

   .. py:method:: ezros.create_rate(frequency)
       :module: ezros

       创建频率控制器，用于控制循环执行的频率。

       :param frequency: 设定的循环频率,单位为赫兹(Hz),表示每秒执行的次数；
                            支持整数或浮点数，例如 `1.0` 代表每秒1次,`5` 代表每秒5次。
       :type frequency: int | float
       
       :return: 频率控制器对象,通过该对象的sleep()方法触发延时，使循环频率贴合设定值。
       :rtype: ezros.Rate
       
       :note: 频率控制器依赖ezros.init()初始化后的框架环境，需在调用ezros.init()之后使用。


示例代码
--------
.. container:: step-block

    .. code-block:: python

        import ezros

        # 初始化EzROS框架（必须在创建频率控制器前执行）
        ezros.init()

        # 创建节点（用于话题发布、日志输出等功能载体）
        node = ezros.Node("publisher_node")

        # 创建StringMessage类型的话题发布者，话题名称为"chatter"
        pub = node.create_publisher(ezros.StringMessage, "chatter")

        # 创建频率控制器：设定循环频率为1.0Hz（即每秒执行1次循环）
        rate = ezros.create_rate(1.0)

        count = 0
        while ezros.ok():
            # 构造StringMessage消息，填充数据
            msg = ezros.StringMessage()
            msg.data = f"Hello, EzROS! Count: {count}"

            # 发布消息到"chatter"话题
            pub.publish(msg)
            count += 1
            rate.sleep()