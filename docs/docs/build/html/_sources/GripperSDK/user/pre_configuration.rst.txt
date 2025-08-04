.. _tag_Gripperpre_configuration:

硬件连接与网络配置
=====================

将服务器端与上位机连接于同一局域网内,使得二者可以进行通信。

.. raw:: html

    <style>
    .custom-h2 {
        font-size: 1.5em !important; /* 更大的字号 */
        font-weight: 700 !important;
        color: #2c3e50 !important; /* 深色更有质感 */
        border-bottom: 1px solid #fffdfdff !important; /* 更粗的下边框 */
        padding-bottom: 10px !important;
        margin-top: 1.5em !important;
        margin-bottom: 0.8em !important;
        font-family: "Microsoft YaHei", sans-serif !important; /* 换成更适配的中文字体 */
        text-shadow: 0 2px 3px rgba(0,0,0,0.1); /* 增加文字阴影 */
        background: linear-gradient(to right, #3498db, #9b59b6); /* 背景渐变（可选） */
        -webkit-background-clip: text;
        color: transparent; /* 文字渐变效果（需配合背景渐变） */
    }
    </style>

.. raw:: html

    <div class="custom-h2">方法一:使用交换机</div>

.. container:: step-block

    此时夹爪的IP地址使用 ``dhcp`` 自动获取,后续需利用 `zeroros_cli <./Zeroros/usr/Zeroros>`_ 进行扫描。

.. raw:: html

    <div class="custom-h2">方法二:直连电脑网口</div>

.. container:: step-block

    **步骤 1:** 配置PC的以太网

    此时夹爪为静态 IP ``192.168.99.2`` ,电脑端需要在和夹爪同一网段内设置自身 IP (打开网络设置 -> 有线设置 -> IPv4)。
    设置参考如下:

    .. list-table::
        :widths: 15 20 35
        :header-rows: 1  

        * - 参数项  
          - 示例/固定值 
          - 配置说明  
            
        * - IP 地址  
          - ``192.168.99.10`` 
          - 格式为 ``192.168.99.X`` (``X`` 的取值范围为 1-254,避开夹爪 IP)    
        * - 子网掩码  
          - ``255.255.255.0`` 
          - 固定配置，无需变动  
   
.. container:: step-block

    **步骤 2:** 连接以太网

        使用以太网线将PC的以太网接口与夹爪设备的网口直接连接,确保PC端网线接口牢固插入

.. container:: step-block

    **步骤 3:** 连接夹爪设备电源

        1.将夹爪设备的电源适配器插曲市电插座

        2.等待夹爪完成初始化：

        - 观察到状态灯常亮

        - 听到夹爪的复位声或观察到夹爪的机械复位

.. container:: step-block

    **步骤 4:** 测试网络连通性

        1. 打开PC的命令提示符(Windows系统:按下 ``Win+R`` ，输入 ``cmd`` 后回车;Linux:打开终端)。

        2. 在命令行中输入以下命令并回车：

        .. code-block:: bash

            ping 192.168.99.2

        3. 结果判断:
   
        .. tabs::

            .. tab:: 网络连通成功
                
                若显示 **"Reply from 192.168.99.2"** 等类似信息,可直接继续后续操作。

            .. tab:: 连接超时

                若显示 **"Request timed out"** ,请依次排查以下项:

                - 以太网IP配置是否正确(重新核对步骤 1)
                - 以太网线是否松动或损坏
                - 夹爪设备是否已完成初始化（状态灯是否常亮）

 




    
