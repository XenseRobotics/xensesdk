.. _tag_all_info:

查看zeroros服务信息
===================================

.. container:: step-block

    如果我们想要查看zeroros服务信息,可通过以下命令来实现:

    .. tabs::

        .. tab:: 不指定IP

            .. code-block:: python

                zeroros_cli -a

                #或者zeroros_cli --all_info.

        .. tab:: 指定IP

            .. code-block:: python

                zeroros_cli -i 192.168.99.2 -a

                #或者zeroros_cli --master_ip {master_ip} -a
    
    
    以下为打印信息：

    .. tabs::

        .. tab:: 不指定IP 成功

            .. code-block:: python

                === All Information ===
                Node: OG000266
                - IP: 192.168.99.2
                - Services:
                    * OG000266 : [...]
                - Topics:
                    * OG000266

                Node: gripper_9a14e81bb832
                - IP: 192.168.99.2
                - Services:
                    * gripper_9a14e81bb832 : ['control_gripper_pos']
                - Topics:
                    * gripper_9a14e81bb832

                Node: Master
                - IP: 192.168.99.2:11411
                - Services:
                    * MasterService : [...]

        .. tab:: 不指定IP 失败

            .. code-block:: python

                INFO:root:No master found via broadcast, using default master IP.

                WARNING:Node-169.254.224.187-12260-0:Failed to send message to 169.254.224.187:11411, retrying 0...


                === All Information ===

        .. tab:: 指定IP 成功

            .. code-block:: python

                === All Information ===
                Node: OG000266
                - IP: 192.168.99.2
                - Services:
                    * OG000266 : ['get_img',...]
                - Topics:
                    * OG000266

                Node: gripper_9a14e81bb832
                - IP: 192.168.99.2
                - Services:
                    * gripper_9a14e81bb832 : ['control_gripper_pos']
                - Topics:
                    * gripper_9a14e81bb832

                Node: Master
                - IP: 192.168.99.2:11411
                - Services:
                    * MasterService : [...]

        .. tab:: 指定IP 失败

            .. code-block:: python

                WARNING:Node-169.254.224.187-18964-0:Failed to send message to 192.168.99.2:11411, retrying 0...


                === All Information ===

.. admonition:: tips
    :class: tip

    用例中虽然有指定IP,但是和不指定IP的成功打印信息相同:
    
    因为用例背景仅连接了一个夹爪,且如果查询服务不指定IP,则默认使用扫描到的第一个节点。


        
