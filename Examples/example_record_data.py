from xensesdk import Sensor
import time 

if __name__ == '__main__':
    sensor  = Sensor.create("OG000018")

    sensor.startSaveSensorInfo(r"D:\gitlab\xensesdk\xensesdk\examples\data3", [Sensor.OutputType.Difference, Sensor.OutputType.Rectify])
    time.sleep(5)
    sensor.stopSaveSensorInfo()
    print("save ok")
    
    sensor.release()
