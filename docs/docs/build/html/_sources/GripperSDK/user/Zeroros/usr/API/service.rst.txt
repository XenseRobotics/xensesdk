.. _tag_service:

Service调用
==============

.. container:: step-block

    当要对特定Service服务调用时,可使用如下命令: 

    .. tabs::

        .. tab:: 调用Sensor服务

            .. code-block:: python

                ezros service -n OG000285 -c get_img

        .. tab:: 调用Gripper服务

            .. code-block:: python

                ezros service -n gripper_d672f584b17a -c set_led_color:=255.0.0

    以下为打印信息:

    .. tabs::

        .. tab:: 调用Sensor服务

            .. code-block:: python

                调用服务: OG000285
                动作: get_img
                参数: []
                ----------------------------------------
                响应:  [[[227 156  83]
                [230 151  85]
                [229 149  86]
                ...
                [201 110 112]
                [110  45  36]
                [ 74  44  34]]

                [[225 154  82]
                [228 150  85]
                [228 149  86]
                ...
                [225 131 137]
                [114  44  36]
                [ 75  44  31]]

        .. tab:: 调用Gripper服务

            .. code-block:: python

                调用服务: gripper_d672f584b17a
                动作: set_led_color
                参数: ['255.0.0']
                ----------------------------------------
                ...

.. admonition:: tips
    :class: tip

    service       子命令,表明本次操作是调用某个服务;

    --name/-n     必选参数,指定要调用的Service名称;

    --call/-c     必须参数,指定要调用的服务动作及参数，格式为 “动作名:= 参数”