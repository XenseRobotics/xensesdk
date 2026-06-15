"""Lightweight solver example"""

import tempfile
from pathlib import Path
import cv2

from xensesdk import Sensor


def main() -> None:
    sensor = Sensor.create(cam_id=0, overrides={"dev.disable_infer": True})
    try:
        serial_number = sensor.ctx.get("dev", "serial_number")
        with tempfile.TemporaryDirectory() as temp_dir:
            sensor.exportRuntimeConfig(save_dir=temp_dir)
            runtime_path = Path(temp_dir) / f"runtime_{serial_number}"

            solver = Sensor.createSolver(
                runtime_path,
                overrides={"dev.disable_infer": True},
            )
            try:
                rectify = sensor.selectSensorInfo(Sensor.OutputType.Rectify)
                diff = solver.selectSensorInfo(
                    Sensor.OutputType.Difference,
                    rectify_image=rectify,
                )
                cv2.imwrite("diff.png", diff)
                print(f"Difference image saved to: ./diff.png")
            finally:
                solver.release()
    finally:
        sensor.release()


if __name__ == "__main__":
    main()
