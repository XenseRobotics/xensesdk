"""solver 可视化示例，需要 xensesdk[viz,onnx] 或 xensesdk[full]。"""

from xensesdk import ExampleView, Sensor


def main() -> None:
    # 1. 创建 Sensor 和 Solver 实例， 导出 runtime config
    sensor = Sensor.create("OG000237")
    sensor.exportRuntimeConfig(save_dir=".")

    # 2. 从 runtime config 创建 solver 实例， 使用 Sensor 的图像数据进行校准和推理
    solver = Sensor.createSolver("./runtime_OG000237")

    rectify = sensor.selectSensorInfo(Sensor.OutputType.Rectify)
    solver.calibrateSensor(rectify_image=rectify)  # 校准 solver
    
    # 2. ui 声明
    view = ExampleView(solver, title="xensesdk ExampleView demo")
    view2d = view.create2d(
        Sensor.OutputType.Rectify,
        Sensor.OutputType.Difference,
        Sensor.OutputType.Depth,
        Sensor.OutputType.Marker2D,
    )
    force_plot = view.createPlot("Force", ["Fx", "Fy", "Fz"], y_label="force")
    torque_plot = view.createPlot("Torque", ["Tx", "Ty", "Tz"], y_label="torque")

    # 3. 每一帧先从 sensor 获取 rectify 图像, 再传入 solver 进行推理, 最后可视化 solver 的输出结果
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
