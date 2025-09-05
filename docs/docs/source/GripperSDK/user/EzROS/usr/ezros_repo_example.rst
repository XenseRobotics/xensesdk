.. _tag_ezros_repo_example:

更多命令行工具与示例程序
========================
.. container:: step-block

    **一、EzROS 命令行工具(CLI):**  
    通过命令行工具可快速查看网络节点信息、监听话题数据、调用服务，无需编写额外代码。


    .. container:: step-block

        **1. 查看所有节点、话题和服务：**  
        全局查看 EzROS 网络中的节点、节点关联的话题与服务，支持短参数 `-a` 或长参数 `--all`。

        .. code-block:: bash

            python -m ezros -a  # 短参数
            python -m ezros --all  # 长参数


    .. container:: step-block

        **2. 监听指定话题：**  
        指定话题名称和监听时长，实时获取话题发布的数据。

        .. code-block:: bash

            python -m ezros topic -e chatter -t 30

        **参数说明**:
        - `e`：话题名称(如 `chatter`)
        - `t`：监听时长(秒，如 `30`)


    .. container:: step-block

        **3. 调用指定服务：**  
        指定服务名称和动作，传递参数并获取服务响应。

        .. code-block:: bash

            python -m ezros service -n math_service -c add:=10,20

        **参数说明**:
        - `n`：服务名称(如 `math_service`)
        - `c`：动作与参数(格式：`动作名:=参数1,参数2`)


    **二、示例程序快速体验**  
    项目提供配套示例代码，可通过以下命令快速运行并验证功能：

    .. code-block:: bash
        # 1. 启动话题发布（持续发送数据）
        python examples/publisher_example.py &
        
        # 2. 同时启动订阅者接收数据（新终端）
        python examples/subscriber_example.py
        
        # 3. 启动服务端提供计算能力（新终端）
        python examples/service_server_example.py &
        
        # 4. 运行客户端调用服务（新终端）
        python examples/service_client_example.py

        示例代码路径：`examples/` 目录下，涵盖话题通信、服务调用核心场景，可结合 CLI 工具（如 `python -m ezros -a`）查看节点运行状态。