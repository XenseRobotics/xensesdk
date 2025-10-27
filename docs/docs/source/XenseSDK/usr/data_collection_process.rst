.. _tag_data_collection_process:

数据采集与处理
===============

在传感器数据的采集与后处理流程中， ``exportRuntimeConfig`` 和 ``createSolver`` 是两个关键接口，分别承担配置导出和数据解析的核心作用，以下是接口说明及最佳实践方式。



一、 核心接口说明
-------------------------------
.. container:: step-content

    .. rubric:: 1. ``exportRuntimeConfig`` 接口
       :class: method-title  

    ``Sensor.exportRuntimeConfig(self, save_dir="", binary=False)`` 用于导出传感器运行时配置，将当前传感器的运行时参数（如校准数据、硬件特性等）持久化到指定目录，为后续离线数据解析提供配置依据。

    - **参数**:
    - ``save_dir`` (``Union[str, Path]``): 配置文件保存目录，默认为当前工作目录。
    - ``binary（bool）：是否以二进制加密格式返回数据（而非保存为文件），默认 False``。
    - **返回值**：``None``
    - **作用**：确保采集的原始数据在离线解析时，能使用与采集时一致的传感器配置，保证处理结果的准确性。

    .. rubric:: 2. ``createSolver`` 接口
       :class: method-title  

    ``Sensor.createSolver(runtime_path)`` 是工厂类方法，用于从指定的 runtime 配置路径创建 ``SensorSolver`` 实例，该实例是离线解析传感器数据的核心工具。

    - **参数**：
    - ``runtime_path（Union[str, Path]）：指向 runtime 配置文件的路径（由 exportRuntimeConfig`` 生成）。
    - **返回值**：成功时返回 ``SensorSolver`` 实例，失败时返回 ``False``。
    - **作用**：加载采集时导出的配置，基于原始数据计算深度图、力值等衍生数据，实现离线后处理。


.. .. rubric:: 2. 数据采集处理完整示例
..    :class: step-title  

二、 数据采集处理完整示例
--------------------------------

以下是结合两个接口的“数据采集-配置导出-离线处理”完整流程，包含代码实现与关键步骤说明。

.. container:: step-content

    .. rubric:: 1. 数据采集与配置导出（``save_data`` 函数）
       :class: method-title  


    .. container:: step-block

        .. code-block:: python

            from pathlib import Path
            SCRIPT_DIR = Path(__file__).resolve().parent
            SAVE_DIR = Path(SCRIPT_DIR / "test_dir")  # 数据保存目录
            SAVE_DIR.mkdir(parents=True, exist_ok=True)
            import cv2
            import time
            import numpy as np

            from xensesdk import Sensor

            sensor_id = 'OG000232'  

            def save_data():
                fps = 30  
                duration = 3  # 秒
                frame_interval = 1.0 / fps 
                total_frames = fps * duration  

                # 创建传感器实例
                sensor_0 = Sensor.create(sensor_id)
                
                for i in range(total_frames):
                    start_time = time.time()

                    # 采集一帧 rectify 类型图像（原始数据）
                    rec = sensor_0.selectSensorInfo(Sensor.OutputType.Rectify)

                    # 生成文件名
                    filename = SAVE_DIR / f"{sensor_id}_{i:03d}.png"

                    # 保存图片
                    cv2.imwrite(str(filename), rec)
                    print(f"Saved {filename}")

                    # 控制帧率（确保稳定30Hz）
                    elapsed = time.time() - start_time
                    sleep_time = frame_interval - elapsed
                    if sleep_time > 0:
                        time.sleep(sleep_time)

                # 导出运行时配置
                sensor_0.exportRuntimeConfig(SAVE_DIR)

                sensor_0.release()
    

    .. rubric:: 2. 离线数据解析与后处理（``replay_data`` 函数）
       :class: method-title  

    .. container:: step-block

        .. code-block:: python

            def replay_data():
                sensor_solver = Sensor.createSolver(SAVE_DIR / f"runtime_{sensor_id}")
                
                for png_file in sorted(SAVE_DIR.glob("*.png")):
                    if not png_file.name.endswith("_depth.png"):
                        img = cv2.imread(str(png_file), cv2.IMREAD_UNCHANGED)
                        
                        depth, force, diff = sensor_solver.selectSensorInfo(
                            Sensor.OutputType.Depth,
                            Sensor.OutputType.Force,
                            Sensor.OutputType.Difference,
                            rectify_image=img  
                        )
                        
                        depth_norm = cv2.normalize(depth, None, 0, 255, cv2.NORM_MINMAX)
                        depth_vis = np.uint8(depth_norm)
                        cv2.imwrite(SAVE_DIR / f"{png_file.stem}_depth.png", depth_vis)

                sensor_solver.release()
    

    .. rubric:: 3. 主流程执行
       :class: method-title  

    .. container:: step-block

        .. code-block:: python

            if __name__ == '__main__':
                save_data()    # 执行数据采集与配置导出
                replay_data()  # 执行离线数据解析与后处理
                print("Data saved and replayed successfully.")



.. rubric:: 三、流程说明
   :class: step-title

.. container:: step-content


    - **采集阶段**：通过 ``Sensor.create`` 初始化传感器，按固定帧率采集原始图像，并在结束后调用 ``exportRuntimeConfig`` 导出配置，确保“数据-配置”对应。
    - **后处理阶段**：通过 ``createSolver`` 加载导出的配置，创建解析器实例，对原始图像进行深度计算等处理，最终生成衍生数据（如深度图）。

    该流程保证了数据采集与解析的一致性，适用于需要离线分析传感器数据的场景（如算法验证、数据可视化等）。