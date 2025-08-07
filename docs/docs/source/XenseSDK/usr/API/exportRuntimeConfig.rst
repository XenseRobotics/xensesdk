.. _tag_exportRuntimeConfig:

exportRuntimeConfig 方法
==============================

.. container:: step-block

    .. py:method:: Sensor.exportRuntimeConfig(self, save_dir=".", binary=False)
        :module: xensesdk

        导出运行时配置并加密保存，支持本地保存或返回二进制数据。

    :param save_dir: 配置文件保存目录，默认为当前目录。
    :type save_dir: str, 可选

    :param binary: 是否返回二进制加密数据而非保存到文件，默认为 False。
    :type binary: bool, 可选

    :return: 当 binary=True 时返回加密的二进制数据，否则无返回值。
    :rtype: bytes | None

    :raises RuntimeError: 远程连接模式下导出配置失败时抛出。

    :note:

        保存的文件名格式为 "runtime_<序列号>"

示例方法
-----------------

.. container:: step-block

    .. code-block:: python

        import sys
        from xensesdk import ExampleView
        from xensesdk import Sensor


        def main():
            sensor_0 = Sensor.create('OG000232')
            sensor_0.exportRuntimeConfig("/home/msi/hongzhan_ws/gitlab/xensesdk/xensesdk/examples")
            sensor_0.release()
        if __name__ == '__main__':
            main()
