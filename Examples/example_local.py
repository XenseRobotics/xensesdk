"""Local connection sensor visualization example, needed pip install xensesdk[viz,onnx] or xensesdk[full]。"""

from xensesdk import ExampleView, Sensor


def main() -> None:

    # 1. Create a Sensor instance
    sensor = Sensor.create(cam_id=0)

    # 2. ui Statement
    view = ExampleView(sensor, title="xensesdk ExampleView demo")
    view2d = view.create2d(
        Sensor.OutputType.Rectify,
        Sensor.OutputType.Difference,
        Sensor.OutputType.Depth,
        Sensor.OutputType.Marker2D,
    )
    force_plot = view.createPlot("Force", ["Fx", "Fy", "Fz"], y_label="force")
    torque_plot = view.createPlot("Torque", ["Tx", "Ty", "Tz"], y_label="torque")

    # 3. Acquire data from the sensor for visualization in each frame
    def update() -> None:
        rectify, difference, depth, force, force6d = sensor.selectSensorInfo(
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
        view.setForceFlow(force, force6d)
        force_plot.setData(force6d[:3])
        torque_plot.setData(force6d[3:])

    view.setCallback(update)

    try:
        view.show()
    finally:
        sensor.release()


if __name__ == "__main__":
    main()
