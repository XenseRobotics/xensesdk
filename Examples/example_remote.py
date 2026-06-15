"""远程连接传感器可视化示例，需要 pip install xensesdk[viz]。"""

from xensesdk import ExampleView, Sensor
from xensesdk import call_service


def main() -> None:
    # --------------------
    # 1. connect to remote sensor:
    # 将 master_service 替换为实际的服务名称，通常格式为 "master_{mac_address}"，
    # 可以通过调用 "scan_sensor_sn" 服务获取可用的服务列表和对应的序列号。
    # --------------------
    master_service = "master_000000000000"
    ret = call_service(master_service, "scan_sensor_sn", timeout_sec=1)
    if ret is None:
        raise RuntimeError("Failed to call service")

    print(f"Found sensors: {ret}, using the first one.")
    serial_number = list(ret.keys())[0]

    sensor = Sensor.create(serial_number, mac_addr=master_service.split("_")[-1])

    # --------------------
    # 2. visualize
    # --------------------
    view = ExampleView(sensor, title="xensesdk ExampleView demo")
    view2d = view.create2d(
        Sensor.OutputType.Rectify,
        Sensor.OutputType.Difference,
        Sensor.OutputType.Depth,
        Sensor.OutputType.Marker2D,
    )
    force_plot = view.createPlot("Force", ["Fx", "Fy", "Fz"], y_label="force")
    torque_plot = view.createPlot("Torque", ["Tx", "Ty", "Tz"], y_label="torque")

    def update() -> None:
        rectify, difference, depth, force, force_resultant = sensor.selectSensorInfo(
            Sensor.OutputType.Rectify,
            Sensor.OutputType.Difference,
            Sensor.OutputType.Depth,
            Sensor.OutputType.Force,
            Sensor.OutputType.ForceResultant,
        )
        marker_move = sensor.drawMarkerMove(rectify)
        view2d.setData(Sensor.OutputType.Rectify, rectify)
        view2d.setData(Sensor.OutputType.Difference, difference)
        view2d.setData(Sensor.OutputType.Depth, depth)
        view2d.setData(Sensor.OutputType.Marker2D, marker_move)
        view.setDepth(depth)
        view.setForceFlow(force, force_resultant)
        force_plot.setData(force_resultant[:3])
        torque_plot.setData(force_resultant[3:])

    view.setCallback(update)

    try:
        view.show()
    finally:
        sensor.release()


if __name__ == "__main__":
    main()
