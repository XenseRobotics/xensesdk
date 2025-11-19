.. _tag_Gripperpre_configuration:

硬件连接与网络配置
=====================

将服务器端与上位机连接于同一局域网内，使得二者可以进行通信。

.. raw:: html

    <style>
    /* 步骤标题样式（外显，无边框） */
    .step-title {
        font-size: 1.3em !important;
        font-weight: 700 !important;
        color: #2c3e50 !important;
        margin-top: 1.8em !important;
        margin-bottom: 0.5em !important;
        font-family: "Microsoft YaHei", sans-serif !important;
    }
    
    /* 步骤内容容器（带边框） */
    .step-content {
        border: 1px solid #ddd !important;
        border-radius: 6px !important;
        padding: 15px 20px !important;
        background-color: #f9f9f9 !important;
        margin-bottom: 1em !important;
    }
    
    /* 方法标题样式 */
    .method-title {
        font-size: 1.1em !important;
        font-weight: 600 !important;
        color: #34495e !important;
        margin-top: 1.2em !important;
        margin-bottom: 0.6em !important;
        padding-left: 5px !important;
        border-left: 3px solid #3498db !important; /* 左侧装饰线 */
    }
    </style>


.. rubric:: 步骤 1: 连接夹爪设备电源
   :class: step-title  

.. container:: step-content

    1. 将夹爪设备的电源适配器插入市电插座。
    2. 等待夹爪完成初始化，观察到状态灯先闪烁后常亮。


.. rubric:: 步骤 2: 连接网络
   :class: step-title

.. container:: step-content

    .. rubric:: 方法一: 使用交换机
       :class: method-title  

    将夹爪与计算机分别接入交换机的不同网口并确保网络通路, 此时夹爪的IP地址使用 ``dhcp`` 自动获取，后续需利用 `ezros <./EzROS/usr/ezros_example.html>`_ 进行扫描。


    .. rubric:: 方法二: 直连电脑网口
       :class: method-title

    此时夹爪为静态 IP ``192.168.99.2``，电脑端需要在和夹爪同一网段内设置自身 IP(打开网络设置 -> 有线设置 -> IPv4)。
    设置参考如下:

    .. list-table::
        :widths: 15 20 35
        :header-rows: 1  

        * - 参数项  
          - 示例/固定值 
          - 配置说明  
            
        * - IP 地址  
          - ``192.168.99.10`` 
          - 格式为 ``192.168.99.X``, (x的取值范围为 1-254, 避开夹爪 IP)
        * - 子网掩码  
          - ``255.255.255.0`` 
          - 固定配置，无需变动  

    使用以太网线将PC的以太网接口与夹爪设备的网口直接连接, 确保PC端网线接口牢固插入。

    .. .. admonition:: tips
    ..     :class: tip

    ..     在使用sdk时，如果上位机既有线连接了夹爪，又连接了wifi，请在程序开头配置多网卡发现：

    ..     .. code-block:: python

    ..         from xensesdk import setup_multi_net_interface

    ..         setup_multi_net_interface()


.. rubric:: 步骤 3: 测试网络连通性
   :class: step-title

.. container:: step-content

    1. 打开PC的命令提示符 (Windows系统: 按下 ``Win+R``，输入 ``cmd`` 后回车; Linux: 打开终端)。
    2. 在命令行中输入以下命令并回车：

        .. code-block:: bash

            ping 192.168.99.2

    3. 结果判断:
   
        .. tab-set::

            .. tab-item:: 网络连通成功
                
                若显示 **"Reply from 192.168.99.2"** 等类似信息，可直接继续后续操作。

            .. tab-item:: 连接超时

                若显示 **"Request timed out"**，请依次排查以下项：

                - 以太网IP配置是否正确 (重新核对步骤 2)
                - 以太网线是否松动或损坏
                - 夹爪设备是否已完成初始化（状态灯是否常亮）
