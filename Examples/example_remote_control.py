import time 
from threading import Thread

from xensegripper import XenseGripper


def data_fetch():
    while True:
        status = gripper.get_gripper_status()
        if isinstance(status, dict):
            info_str = "\rGripper Status: {"
            for key, value in status.items():
                info_str += f"{key}:{value:+8.4f}, "
            info_str += "}"
            print(info_str, end="", flush=True)
        time.sleep(0.05)

if __name__=="__main__":

    gripper = XenseGripper.create("d672f584b17a")
    data_fetch_thread = Thread(target=data_fetch, daemon=True)
    data_fetch_thread.start()

    flag = True
    while True:
        if flag:
            gripper.set_position(80, 80, 20)
            flag = not flag
        else:
            gripper.set_position(10, 80, 20)
            flag = not flag
        time.sleep(1)
