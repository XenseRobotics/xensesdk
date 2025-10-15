.. _tag_echo:

Monitoring Topics
=====================

.. container:: step-block

    When you need to query a specific Topic, use the following commands:

    .. tab-set::

        .. tab-item:: Monitor Sensor

            .. code-block:: bash

                ezros topic -e OG000285 -t 30

        .. tab-item:: Monitor Gripper

            .. code-block:: bash

                ezros topic -e gripper_d672f584b17a -t 30


    The terminal will print the following information:

    .. tab-set::

        .. tab-item:: Sensor Monitoring Output

            .. code-block:: text

                Monitoring Topic: OG000285
                Duration: 30 seconds
                Press Ctrl+C to stop
                ============================================================
                Successfully subscribed to topic OG000285 (Type: BytesMessage)
                Start monitoring topic OG000285...

                [02:51:54] [OG000285]: {<OutputType.Depth: 3>: array([[0.        , 0.        , 0.        , ..., 0.        , 0.        ,    0.        ],
                    [0.        , 0.        , 0.        , ..., 0.        , 0.        ,0.        ],
                    [0.        , 0.        , 0.        , ..., 0.        , 0.        ,0.        ],
                    ...,
                    [0.        , 0.        , 0.        , ..., 0.00699991, 0.00700688,0.00700688],
                    [0.        , 0.        , 0.        , ..., 0.00699412, 0.00703006,0.00703006],
                    [0.        , 0.        , 0.        , ..., 0.00699401, 0.00703049,0.00703049]],
                    dtype=float32), <OutputType.Difference: 2>: array([[[109, 110, 107],
                    [108, 110, 108],
                    [107, 111, 108],
                    ...,
                    [111, 112, 113],
                    [118, 114, 120],
                    [121, 115, 123]],

                    [[107, 106, 109],
                    [108, 107, 110],
                    [110, 109, 110],
                    ...,
                    [110, 110, 108],
                    [110, 110, 110],
                    [110, 109, 110]]], dtype=uint8)}
                [02:51:54] [OG000285]: {<OutputType.Depth: 3>: array([[0.        , 0.        , 0.        , ..., 0.        , 0.        , 1.        ],
                    [0.        , 0.        , 0.        , ..., 0.        , 0.        , 2.        ],
                    [0.        , 0.        , 0.        , ..., 0.        , 0.        , 3.        ],
                    ...,
                    [0.        , 0.        , 0.        , ..., 0.00699991, 0.00700688, 0.00700688],
                    [0.        , 0.        , 0.        , ..., 0.00699412, 0.00703006, 0.00703006],
                    [0.        , 0.        , 0.        , ..., 0.00699401, 0.00703049, 0.00703049]],
                    dtype=float32), <OutputType.Difference: 2>: array([[[109, 110, 107],
                    [108, 110, 108],
                    [107, 111, 108],
                    ...,
                    [110, 110, 108],
                    [110, 110, 110],
                    [110, 109, 110]]], dtype=uint8)}


        .. tab-item:: Gripper Monitoring Output

            .. code-block:: text

                Monitoring Topic: gripper_d672f584b17a
                Duration: 30 seconds
                Press Ctrl+C to stop
                ==========================================================================
                Successfully subscribed to topic gripper_d672f584b17a (Type: BytesMessage)
                Start monitoring topic gripper_d672f584b17a...

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

                Monitoring interrupted by user

        .. tab-item:: Topic Not Detected
            
            .. code-block:: text

                Monitoring Topic: gripper_d672f584b18a
                Duration: 30 seconds
                Press Ctrl+C to stop
                =====================================================================================
                Failed to detect topic type; the topic may not exist or has no publisher/subscriber


.. admonition:: tips
    :class: tip

    - The `topic` subcommand indicates that this operation is to call a specific topic;
    - The `--echo/-e` parameter is mandatory and specifies the name of the Topic to monitor;
    - The `--timeout/-t` parameter is optional and specifies the duration of monitoring, with a default of 30 seconds.