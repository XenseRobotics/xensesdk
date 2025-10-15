.. _tag_exportRuntimeConfig:

exportRuntimeConfig Method
==================================

.. container:: step-block

    .. py:method:: Sensor.exportRuntimeConfig(self, save_dir=".", binary=False)
        :module: xensesdk

        Exports the current sensor's runtime configuration to the specified directory.

        :param save_dir: Directory for saving the configuration file, defaults to the current directory.
        :type save_dir: Union[str, Path], optional

        :param binary: Whether to return binary encrypted data instead of saving to a file, defaults to False.
        :type binary: bool, optional

        :return: None

        :raises RuntimeError: Thrown when configuration export fails in remote connection mode.

        :note:

            The saved file name follows the format "runtime_<serial_number>".

Example Method
-----------------

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

        if __name__ == '__main__':
            save_data()
            replay_data()
            print("Data saved and replayed successfully.")