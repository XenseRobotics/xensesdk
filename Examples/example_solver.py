"""Solver visualization example, needed xensesdk[viz,onnx] or xensesdk[full]。"""

from xensesdk import ExampleView, Sensor


def main() -> None:

    sensor = Sensor.create("OG000237")
    sensor.exportRuntimeConfig(save_dir=".")

    solver = Sensor.createSolver("./runtime_OG000237")

    rectify = sensor.selectSensorInfo(Sensor.OutputType.Rectify)
    solver.calibrateSensor(rectify_image=rectify)  # 校准 solver
    
    view = ExampleView(solver, title="xensesdk ExampleView demo")
    view2d = view.create2d(
        Sensor.OutputType.Rectify,
        Sensor.OutputType.Difference,
        Sensor.OutputType.Depth,
        Sensor.OutputType.Marker2D,
    )
    force_plot = view.createPlot("Force", ["Fx", "Fy", "Fz"], y_label="force")
    torque_plot = view.createPlot("Torque", ["Tx", "Ty", "Tz"], y_label="torque")

    def update() -> None:
        rectify = sensor.selectSensorInfo(
            Sensor.OutputType.Rectify,
        )
        rectify, difference, depth, force, force_resultant = solver.selectSensorInfo(
            Sensor.OutputType.Rectify,
            Sensor.OutputType.Difference,
            Sensor.OutputType.Depth,
            Sensor.OutputType.Force,
            Sensor.OutputType.ForceResultant,
            rectify_image=rectify,
        )

        marker_move = solver.drawMarkerMove(rectify)
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
