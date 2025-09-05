.. _tag_wait_for_condition_:

wait_for_condition方法
========================

.. container:: step-block

   .. py:method:: ezros.wait_for_condition(callback, timeout=None, interval=0.5)
       :module: ezros

       周期性检查回调函数返回值，阻塞等待条件满足或超时退出，用于流程同步控制。

       :param callback: 条件判断回调函数,需返回布尔值(True/False);
                         当返回True时表示条件满足,将立即退出等待。
       :type callback: Callable[[], bool]
       
       :param timeout: 最大等待时间（单位：秒）；
                       若为None(默认),则无限期等待直到条件满足;
                       若设定数值，超过该时间后将强制退出。
       :type timeout: float | None, optional
       
       :param interval: 条件检查的时间间隔(单位:秒),默认0.5秒；
                        表示每间隔指定时间调用一次回调函数进行条件判断。
       :type interval: float, optional
       
       :return: 若条件满足则返回True,若超时则返回False。
       :rtype: bool
       
       :note:
           回调函数应避免包含耗时操作，以免影响检查周期的准确性；
           需在ezros.init()初始化后使用，依赖框架的时间管理机制。
         
       