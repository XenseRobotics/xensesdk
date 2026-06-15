"""Lightweight Remote Connection Sensor Example"""

import time

from xensesdk import Sensor, call_service


def main() -> None:
    master_service = "master_000000000000"
    ret = call_service(master_service, "scan_sensor_sn", timeout_sec=1)
    if ret is None:
        raise RuntimeError("Failed to call service")

    print(f"Found sensors: {ret}, using the first one.")
    serial_number = list(ret.keys())[0]
    sensor = Sensor.create(serial_number, mac_addr=master_service.split("_")[-1])

    last_report_time = 0.0
    try:
        while True:
            started_at = time.time()
            rectify = sensor.selectSensorInfo(Sensor.OutputType.Rectify)
            if started_at - last_report_time >= 2.0:
                print(f"serial={serial_number}, rectify={rectify.shape}, dtype={rectify.dtype}")
                last_report_time = started_at

            elapsed = time.time() - started_at
            if elapsed < 0.016:
                time.sleep(0.016 - elapsed)
    except KeyboardInterrupt:
        pass
    finally:
        sensor.release()


if __name__ == "__main__":
    main()
