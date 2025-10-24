.. _tag_createSolver:

createSolver 方法
==========================

.. container:: step-block

    .. py:method:: SensorSolver.createSolver(runtime_path)
        :module: xensesdk
        :classmethod:

        工厂方法（类方法），用于从给定的 runtime 配置路径创建一个 SensorSolver 实例。

        :param runtime_path: - 指向 runtime 配置文件的路径
        :type runtime_path: Union [str, Path]

        :return: 成功时返回 SensorSolver 实例，失败时返回 False。
        :rtype: SensorSolver | bool

        :raises AssertionError: 解密后的数据格式不正确或缺少必要的 "ConfigManager" 键时触发。
        :raises Exception: 读取文件、解密过程中发生错误时触发（具体错误信息会被捕获并打印）。

示例方法
----------------

.. container:: step-block

    .. code-block:: python

        from pathlib import Path
        SCRIPT_DIR = Path(__file__).resolve().parent
        SAVE_DIR = Path(SCRIPT_DIR / "test_dir")  # 存放目录
        SAVE_DIR.mkdir(parents=True, exist_ok=True)
        import cv2
        import time
        import numpy as np

        from xensesdk import Sensor

        sensor_id = 'OG000232'

        def save_data():
            fps = 30
            duration = 3   # 秒
            frame_interval = 1.0 / fps
            total_frames = fps * duration

            sensor_0 = Sensor.create(sensor_id)
            for i in range(total_frames):
                start_time = time.time()

                # 采集一帧
                rec = sensor_0.selectSensorInfo(Sensor.OutputType.Rectify)

                # 生成文件名
                filename = SAVE_DIR / f"{sensor_id}_{i:03d}.png"

                # 保存图片
                cv2.imwrite(str(filename), rec)
                print(f"Saved {filename}")

                # 控制帧率（30Hz）
                elapsed = time.time() - start_time
                sleep_time = frame_interval - elapsed
                if sleep_time > 0:
                    time.sleep(sleep_time)

            # 导出配置
            sensor_0.exportRuntimeConfig(SAVE_DIR)

            sensor_0.release()

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
                    depth_vis = np.clip(depth*200, 0, 255)
                    cv2.imwrite(SAVE_DIR / f"{png_file.stem}_depth.png", depth_vis)

            sensor_solver.release()

        if __name__ == '__main__':
            save_data()
            replay_data()
            print("Data saved and replayed successfully.")