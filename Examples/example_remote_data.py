import sys
from xensesdk import ExampleView
from xensesdk import Sensor
from xensesdk import call_service


def main():
    MASTER_SERVICE = "master_6ebbc5f53240"
    # find all sensors
    ret = call_service(MASTER_SERVICE, "scan_sensor_sn")
    if ret is None:
        print(f"Failed to scan sensors")
        sys.exit(1)
    else:
        print(f"Found sensors: {ret}, using the first one.")
    serial_number = list(ret.keys())[0]

    # create a sensor
    sensor_0 = Sensor.create(serial_number, mac_addr=MASTER_SERVICE.split("_")[-1])
    View = ExampleView(sensor_0)
    View2d = View.create2d(Sensor.OutputType.Difference, Sensor.OutputType.Depth)
    
    def callback():
        diff, depth = sensor_0.selectSensorInfo(Sensor.OutputType.Difference, Sensor.OutputType.Depth)
        View2d.setData(Sensor.OutputType.Difference, diff)
        View2d.setData(Sensor.OutputType.Depth, depth)
        View.setDepth(depth)
    View.setCallback(callback)

    View.show()
    sensor_0.release()
    sys.exit()


if __name__ == '__main__':
    main()
