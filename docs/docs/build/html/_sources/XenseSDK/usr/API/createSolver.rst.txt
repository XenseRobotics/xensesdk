.. _tag_createSolver:

createSolver Method
==========================

.. container:: step-block

    .. py:method:: SensorSolver.createSolver(runtime_path)
        :module: xensesdk
        :classmethod:

        A factory method (class method) used to create a SensorSolver instance from a given runtime configuration path.

        :param runtime_path: Path pointing to the runtime configuration file
        :type runtime_path: Union [str, Path]

        :return: Returns a SensorSolver instance on success, or False on failure.
        :rtype: SensorSolver | bool

        :raises AssertionError: Triggered when the decrypted data format is incorrect or the necessary "ConfigManager" key is missing.
        :raises Exception: Triggered when errors occur during file reading or decryption (specific error information will be captured and printed).

Example Method
------------------

.. container:: step-block

    .. code-block:: python

        from pathlib import Path
        SCRIPT_DIR = Path(__file__).resolve().parent
        SAVE_DIR = Path(SCRIPT_DIR / "test_dir")  # Storage directory
        SAVE_DIR.mkdir(parents=True, exist_ok=True)
        import cv2
        import time
        import numpy as np

        from xensesdk import Sensor

        sensor_id = 'OG000232'

        def save_data():
            fps = 30
            duration = 3   # seconds
            frame_interval = 1.0 / fps
            total_frames = fps * duration

            sensor_0 = Sensor.create(sensor_id)
            for i in range(total_frames):
                start_time = time.time()

                # Capture one frame
                rec = sensor_0.selectSensorInfo(Sensor.OutputType.Rectify)

                # Generate filename
                filename = SAVE_DIR / f"{sensor_id}_{i:03d}.png"

                # Save image
                cv2.imwrite(str(filename), rec)
                print(f"Saved {filename}")

                # Control frame rate (30Hz)
                elapsed = time.time() - start_time
                sleep_time = frame_interval - elapsed
                if sleep_time > 0:
                    time.sleep(sleep_time)

            # Export configuration
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