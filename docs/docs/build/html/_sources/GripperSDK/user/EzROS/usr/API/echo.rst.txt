.. _tag_echo:

监控话题
============

.. container:: step-block

    当要对特定 Topic 查询时，可使用如下命令：

    .. tabs::
        .. tab:: 监听 Sensor
            .. code-block:: bash

                ezros topic -e OG000285 -t 30

        .. tab:: 监听 Gripper
            .. code-block:: bash

                ezros topic -e gripper_d672f584b17a -t 30


    终端打印信息如下：

    .. tabs::
        .. tab:: 监听 Sensor 输出
            .. code-block:: text

                监听话题: OG000285
                持续时间: 30 秒
                按 Ctrl+C 停止
                ============================================================
                成功订阅话题 OG000285 (类型: BytesMessage)
                开始监听话题 OG000285...

                [02:51:54] [OG000285]: {<OutputType.Depth: 3>: array([[0.        , 0.        , 0.        , ..., 0.        , 0.        ,
                        0.        ],
                    [0.        , 0.        , 0.        , ..., 0.        , 0.        ,
                        0.        ],
                    [0.        , 0.        , 0.        , ..., 0.        , 0.        ,
                        0.        ],
                    ...,
                    [0.        , 0.        , 0.        , ..., 0.00699991, 0.00700688,
                        0.00700688],
                    [0.        , 0.        , 0.        , ..., 0.00699412, 0.00703006,
                        0.00703006],
                    [0.        , 0.        , 0.        , ..., 0.00699401, 0.00703049,
                        0.00703049]], dtype=float32), <OutputType.Difference: 2>: array([[[109, 110, 107],
                        [108, 110, 108],
                        [107, 111, 108],
                        ...,
                        [111, 112, 113],
                        [118, 114, 120],
                        [121, 115, 123]],

                        ...

                    [[107, 106, 109],
                        [108, 107, 110],
                        [110, 109, 110],
                        ...,
                        [110, 110, 108],
                        [110, 110, 110],
                        [110, 109, 110]]], dtype=uint8)}
                [02:51:54] [OG000285]: {<OutputType.Depth: 3>: array([[0.        , 0.        , 0.        , ..., 0.        , 0.        ,
                        1.        ],
                    [0.        , 0.        , 0.        , ..., 0.        , 0.        ,
                        2.        ],
                    [0.        , 0.        , 0.        , ..., 0.        , 0.        ,
                        3.        ],
                    ...,
                    [0.        , 0.        , 0.        , ..., 0.00699991, 0.00700688,
                        0.00700688],
                    [0.        , 0.        , 0.        , ..., 0.00699412, 0.00703006,
                        0.00703006],
                    [0.        , 0.        , 0.        , ..., 0.00699401, 0.00703049,
                        0.00703049]], dtype=float32), <OutputType.Difference: 2>: array([[[109, 110, 107],
                        [108, 110, 108],
                        [107, 111, 108],
                        ...,
                        [110, 110, 108],
                        [110, 110, 110],
                        [110, 109, 110]]], dtype=uint8)}

        .. tab:: 监听 Gripper 输出
            .. code-block:: text

                监听话题: gripper_d672f584b17a
                持续时间: 30 秒
                按 Ctrl+C 停止
                ============================================================
                成功订阅话题 gripper_d672f584b17a (类型: BytesMessage)
                开始监听话题 gripper_d672f584b17a...

                [02:52:30] [gripper_d672f584b17a]: {'position': 0.0, 'velocity': 0.0, 'force': 2.37, 'temperature': 46}
                [02:52:30] [gripper_d672f584b17a]: {'position': 0.0, 'velocity': 0.0, 'force': 2.37, 'temperature': 46}
                [02:52:30] [gripper_d672f584b17a]: {'position': 0.0, 'velocity': 0.0, 'force': 2.37, 'temperature': 46}
                [02:52:30] [gripper_d672f584b17a]: {'position': 0.0, 'velocity': 0.0, 'force': 2.37, 'temperature': 48}
                [02:52:30] [gripper_d672f584b17a]: {'position': 0.0, 'velocity': 0.0, 'force': 2.37, 'temperature': 46}
                [02:52:30] [gripper_d672f584b17a]: {'position': 0.0, 'velocity': 0.0, 'force': 2.27, 'temperature': 46}
                [02:52:30] [gripper_d672f584b17a]: {'position': 0.0, 'velocity': 0.0, 'force': 2.27, 'temperature': 46}
                [02:52:30] [gripper_d672f584b17a]: {'position': 0.0, 'velocity': 0.0, 'force': 2.27, 'temperature': 46}
                [02:52:30] [gripper_d672f584b17a]: {'position': 0.0, 'velocity': 0.0, 'force': 2.37, 'temperature': 46}
                [02:52:30] [gripper_d672f584b17a]: {'position': 0.0, 'velocity': 0.0, 'force': 2.37, 'temperature': 46}
                [02:52:30] [gripper_d672f584b17a]: {'position': 0.0, 'velocity': 0.0, 'force': 2.37, 'temperature': 46}
                [02:52:30] [gripper_d672f584b17a]: {'position': 0.0, 'velocity': 0.0, 'force': 2.37, 'temperature': 46}
                [02:52:31] [gripper_d672f584b17a]: {'position': 0.0, 'velocity': 0.0, 'force': 2.37, 'temperature': 46}
                [02:52:31] [gripper_d672f584b17a]: {'position': 0.0, 'velocity': 0.0, 'force': 2.41, 'temperature': 46}
                [02:52:31] [gripper_d672f584b17a]: {'position': 0.0, 'velocity': 0.0, 'force': 2.41, 'temperature': 46}
                [02:52:31] [gripper_d672f584b17a]: {'position': 0.0, 'velocity': 0.0, 'force': 2.37, 'temperature': 46}

                监听被用户中断

        .. tab:: 未能检测话题
            .. code-block:: text

                监听话题: gripper_d672f584b18a
                持续时间: 30 秒
                按 Ctrl+C 停止
                ============================================================
                未能检测到话题类型,话题可能不存在或无发布者/订阅者


.. admonition:: tips
    :class: tip

    - `topic` 子命令，表明本次操作是调用某个话题；
    - `--echo/-e` 必选参数，指定要监听的 Topic 名称；
    - `--timeout/-t` 可选参数，指定监听的持续时间，默认为 30 秒。