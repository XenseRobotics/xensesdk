.. _tag_service:

Service Call
================

.. container:: step-block

    When you need to call a specific Service, use the following commands:

    .. tab-set::

        .. tab-item:: Call Sensor Service

            .. code-block:: bash

                ezros service -n OG000285 -c get_img

        .. tab-item:: Call Gripper Service

            .. code-block:: bash

                ezros service -n gripper_d672f584b17a -c set_led_color:=255,0,0

    The following is the printed information:

    .. tab-set::

        .. tab-item:: Sensor Service Call Output

            .. code-block:: text

                Calling Service: OG000285
                Action: get_img
                Parameters: []
                ----------------------------------------
                Response:  [[[227 156  83]
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
                [ 75  44  31]]]

        .. tab-item:: Gripper Service Call Output
            
            .. code-block:: text

                Calling Service: gripper_d672f584b17a
                Action: set_led_color
                Parameters: [255, 0, 0]
                ----------------------------------------

.. admonition:: tips
    :class: tip

    - The `service` subcommand indicates that this operation is to call a specific service;
    - The `--name/-n` parameter is mandatory and specifies the name of the Service to call;
    - The `--call/-c` parameter is mandatory and specifies the service action and parameters to call, in the format of "action name:= parameters".