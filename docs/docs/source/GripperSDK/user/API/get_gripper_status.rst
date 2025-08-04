.. _tag_Gripper_get_gripper_status_:

get_gripper_status 方法
=========================

.. container:: step-block

    .. py:method:: XenseGripper.get_gripper_status(self)
        :module: xensegripper

        获取夹爪当前的状态信息。

        该方法通过读取夹爪客户端的缓冲区数据，返回包含夹爪状态的字典（如位置、速度、力等实时信息）。

        :return: 夹爪当前状态的字典，具体键值根据实际缓冲区数据定义。
        :rtype: dict

示例代码
--------

.. container:: step-block

    .. code-block:: python

        from xensegripper import XenseGripper
        import time
        import threading

        def get_status_continuously(gripper, stop_event):
            """持续获取夹爪状态的线程函数"""
            while not stop_event.is_set():  # 当停止事件未触发时持续运行
                status = gripper.get_gripper_status()
                print(f"当前夹爪状态: {status}")
                time.sleep(1)  # 每秒获取一次

        if __name__ == "__main__":
            # 创建夹爪实例
            gripper = XenseGripper.create("9a14e81bb832")
            
            # 创建停止事件（用于控制线程退出）
            stop_event = threading.Event()
            
            # 创建并启动状态获取线程
            status_thread = threading.Thread(
                target=get_status_continuously,
                args=(gripper, stop_event),
                daemon=True  # 主线程退出时自动结束子线程
            )
            status_thread.start()
            
            try:
                # 打开夹爪（与状态获取并行执行）
                print("开始打开夹爪...")
                gripper.open_gripper()
                time.sleep(3)  # 等待打开完成
                
                # 关闭夹爪（与状态获取并行执行）
                print("开始关闭夹爪...")
                gripper.close_gripper()
                time.sleep(3)  # 等待关闭完成
                
            finally:
                # 触发停止事件，结束状态获取线程
                stop_event.set()
                # 等待线程安全退出
                status_thread.join()
                print("程序结束")
