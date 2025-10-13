
.. _tag_set_control_param_:

set_control_param方法
=====================

.. container:: step-block

   .. py:method:: XenseGripper.set_control_param(self, stiffness: float = None, kp: float = None, ki: float = None, kd: float = None) -> None
       :module: xensegripper

       设置 SAFE 模式下的控制器参数(PID 控制参数)。

       :param stiffness: 目标力参数，可选参数。
       :type stiffness: float, optional
       
       :param kp: PID 控制器的比例系数(Kp), 可选参数。
       :type kp: float, optional
       
       :param ki: PID 控制器的积分系(Ki), 可选参数。
       :type ki: float, optional
       
       :param kd: PID 控制器的微分系数(Kd), 可选参数。
       :type kd: float, optional
