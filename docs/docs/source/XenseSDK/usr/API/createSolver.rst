.. _tag_createSolver:

createSlover 方法
==========================

.. container:: step-block

    .. py:method:: SensorSolver.createSolver(runtime_path)
        :module: xensesdk
        :classmethod:

        从加密的运行时配置文件创建 SensorSolver 实例。

        :param runtime_path: 加密的运行时配置文件路径，支持字符串或 Path 对象。
        :type runtime_path: Union [str, Path]

        :return: 成功时返回 SensorSolver 实例，失败时返回 False。
        :rtype: SensorSolver | bool

        :raises AssertionError: 解密后的数据格式不正确或缺少必要的 "ConfigManager" 键时触发。
        :raises Exception: 读取文件、解密过程中发生错误时触发（具体错误信息会被捕获并打印）。

示例方法
----------------

.. container:: step-block

    .. code-block:: python

        import sys
        from xensesdk import ExampleView
        from xensesdk import Sensor


        def main():
            sensor_1 = Sensor.create('OG000232')
            sensor_0 = Sensor.createSolver("/home/msi/hongzhan_ws/gitlab/xensesdk/xensesdk/examples/xxxx")
            View = ExampleView(sensor_0)
            View2d = View.create2d(Sensor.OutputType.Rectify, Sensor.OutputType.Marker2D, Sensor.OutputType.Depth)

            def callback():
                rec = sensor_1.selectSensorInfo(Sensor.OutputType.Rectify)
                force, res_force, mesh_init, diff, depth = sensor_0.selectSensorInfo(
                    Sensor.OutputType.Force, 
                    Sensor.OutputType.ForceResultant,
                    Sensor.OutputType.Mesh3DInit,
                    Sensor.OutputType.Difference, 
                    Sensor.OutputType.Depth,
                    rectify_image=rec
                )
                marker_img = sensor_0.drawMarkerMove(diff)
                View2d.setData(Sensor.OutputType.Rectify, rec)
                View2d.setData(Sensor.OutputType.Marker2D, marker_img)
                View2d.setData(Sensor.OutputType.Depth, depth)
                View.setForceFlow(force, res_force, mesh_init)
                View.setDepth(depth)

            View.setCallback(callback)
            View.show()
            sensor_0.release()
            sys.exit()

        if __name__ == '__main__':
            main()
