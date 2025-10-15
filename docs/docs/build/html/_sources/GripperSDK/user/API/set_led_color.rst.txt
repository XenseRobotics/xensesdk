.. _tag_set_led_color_:

set_led_color Method
=========================

.. container:: step-block

   .. py:method:: XenseGripper.set_led_color(self, r, g, b)
       :module: xensegripper

       Sets the color of the gripper's LED light, controlled via RGB color values.

       :param r: Red channel value, ranging from 0 to 255.
       :type r: int
       
       :param g: Green channel value, ranging from 0 to 255.
       :type g: int
       
       :param b: Blue channel value, ranging from 0 to 255.
       :type b: int
       
       :raises ValueError: Triggered when any color channel value is outside the 0-255 range.

Example Code
----------------
.. container:: step-block

    .. code-block:: python

        from xensegripper import XenseGripper

        # Create a gripper instance
        gripper = XenseGripper.create("9a14e81bb832")

        # Set LED color (RGB 0-255)
        gripper.set_led_color(255, 0, 0)    # Red
        gripper.set_led_color(0, 255, 0)    # Green
        gripper.set_led_color(0, 0, 255)    # Blue
        

        # Error example: Color value out of range
        try:
            gripper.set_led_color(300, 0, 0)  # 300 exceeds the maximum limit of 255
        except ValueError as e:
            print(e)

        try:
            gripper.set_led_color(-10, 0, 0)  # -10 is below the minimum limit of 0
        except ValueError as e:
            print(e)