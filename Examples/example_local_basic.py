"""Lightweight local connection sensor example"""

import time
import cv2

from xensesdk import Sensor


REPORT_INTERVAL_SEC = 2.0


def main() -> None:
    sensor = Sensor.create(cam_id=0, disable_infer=True)
    report_started_at = time.time()
    frame_count = 0

    try:
        while True:
            raw, rectify, timestamp = sensor.selectSensorInfo(
                Sensor.OutputType.Raw,
                Sensor.OutputType.AugDifference,
                Sensor.OutputType.TimeStamp,
            )
            frame_count += 1
            cv2.imshow("Rectify", rectify)
            if cv2.waitKey(1) in (27, ord("q")):
                break

            now = time.time()
            report_elapsed = now - report_started_at
            if report_elapsed >= REPORT_INTERVAL_SEC:
                fps = frame_count / report_elapsed
                print(
                    f"raw={raw.shape}, rectify={rectify.shape}, "
                    f"dtype={rectify.dtype}, fps={fps:.1f}, timestamp={timestamp:.3f}"
                )
                report_started_at = now
                frame_count = 0

    except KeyboardInterrupt:
        pass
    finally:
        cv2.destroyAllWindows()
        sensor.release()


if __name__ == "__main__":
    main()
