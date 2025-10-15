.. _tag_set_control_param_:

set_control_param Method
==============================

.. container:: step-block

   .. py:method:: XenseGripper.set_control_param(self, stiffness: float = None, kp: float = None, ki: float = None, kd: float = None) -> None
       :module: xensegripper

       Sets the controller parameters (PID control parameters) in SAFE mode.

       :param stiffness: Target force parameter, optional.
       :type stiffness: float, optional
       
       :param kp: Proportional gain (Kp) of the PID controller, optional.
       :type kp: float, optional
       
       :param ki: Integral gain (Ki) of the PID controller, optional.
       :type ki: float, optional
       
       :param kd: Derivative gain (Kd) of the PID controller, optional.
       :type kd: float, optional