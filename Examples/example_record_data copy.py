import sys
from xensesdk import ExampleView
from xensesdk import Sensor

def main():
    sensor  = Sensor.create("OG000102")
    sensor.exportRuntimeConfig("./")
    sensor_solver = sensor.createSolver("./runtime_OG000102")
    View = ExampleView(sensor_solver)
    View2d = View.create2d(Sensor.OutputType.Difference, Sensor.OutputType.Depth, Sensor.OutputType.Marker2D)
    def callback():
        force, res_force, mesh_init, src, diff, depth = sensor_solver.selectSensorInfo(
            Sensor.OutputType.Force, 
            Sensor.OutputType.ForceResultant,
            Sensor.OutputType.Mesh3DInit,
            Sensor.OutputType.Rectify, 
            Sensor.OutputType.Difference, 
            Sensor.OutputType.Depth,
            rectify_image = "OG000102.png"
        )


        marker_img = sensor_0.drawMarkerMove(src)   
        View2d.setData(Sensor.OutputType.Marker2D, marker_img)
        View2d.setData(Sensor.OutputType.Difference, diff)
        View2d.setData(Sensor.OutputType.Depth, depth)
        View.setForceFlow(force, res_force, mesh_init)
        View.setDepth(depth)
    View.setCallback(callback)

    View.show()
    sensor_solver.release()
    sys.exit()

if __name__ == '__main__':
    main()