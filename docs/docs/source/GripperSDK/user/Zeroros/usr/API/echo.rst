.. _tag_topic:

测试Topic
============

.. container:: step-block

    当要对特定Topic查询时,可使用如下命令:

    .. tabs::

        .. tab:: Sensor对应话题

              .. code-block:: python

                zeroros_cli  topic --echo OG000266
            
                #zeroros_cli topic --echo {topic_name}

        .. tab:: Gripper对应话题

                .. code-block:: python
                
                    zeroros_cli topic -e gripper_9a14e81bb832

                    #zeroros_cli topic -e {topic_name}

    .. tabs::

        .. tab:: Sensor对应话题 成功

            .. code-block:: python
            
                [OG000266]:
                {}
                [OG000266]:
                {}
                ...
                [OG000266]:
                {}
                [OG000266]:
                {}
               
             

        .. tab:: Sensor对应话题 失败

            .. code-block:: python
                
                ValueError: Topic OG000266 not found.

        .. tab:: Gripper对应话题 成功

            .. code-block:: python

                [gripper_9a14e81bb832]:
                {'position': 10.0, 'velocity': 0.0, 'force': -7.62, 'temperature': 57}
                [gripper_9a14e81bb832]:
                {'position': 10.0, 'velocity': 0.0, 'force': -7.62, 'temperature': 57}
                ...
                [gripper_9a14e81bb832]:
                {'position': 10.0, 'velocity': 0.0, 'force': -7.62, 'temperature': 57}
                [gripper_9a14e81bb832]:
                {'position': 10.0, 'velocity': 0.0, 'force': -7.62, 'temperature': 57}

        .. tab:: Grippper对应话题 失败

            .. code-block:: python

                ValueError: Topic gripper_9a14e81bb832 not found.
    
.. admonition:: tips
    :class: tip

    上述指令的参数参考
    `zeroros_cli -a <./all_info.html>`_ 的打印信息。