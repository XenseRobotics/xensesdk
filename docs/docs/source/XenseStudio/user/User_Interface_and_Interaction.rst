.. _tag_user_interface_and_interaction:

IV. Interface and Interaction
==================================

1. Sensor Selection   
-----------------------

.. figure:: ../images/Data_or_Record_control_area.png
    :alt: Data Acquisition Control Area
    :align: center
    :scale: 100%
    :name: _xs-sensor_selection

    Figure 1: Data Acquisition Control Area

Under the "Select Sensor" option in the current Data Acquisition Control Area, you can monitor the multimodal perception information of the sensor in real time. It also supports recording the sensor feedback information for later "opening data stream" to conduct review, recap, and analysis.
 
 .. figure:: ../images/elements_selection_area.png
    :alt: Device Selection Area
    :align: center
    :scale: 100%
    :name: _xs-device_selection

    Figure 2: Device Selection Area

.. |select_button| image:: ../images/select_button.png
    :alt: Select Button
    :align: middle
    :width: 16px
    :height: 16px

The software supports connecting multiple sensors simultaneously and enables quick switching between them.
The Device Selection Area displays the names of all sensors. By clicking |select_button| ,
you can quickly switch from the list of detected sensors to the target sensor, and its collected information will be displayed in the visualization area.

Sensor Status Indicators
##############################

.. |online_icon| image:: ../images/online_icon.png
    :alt: Online Icon
    :align: middle
    :width: 16px
    :height: 16px

.. |offline_icon| image:: ../images/offline_icon.png
    :alt: Offline Icon
    :align: middle
    :width: 16px
    :height: 16px

.. |error_icon| image:: ../images/error_icon.png
    :alt: Error Icon
    :align: middle
    :width: 16px
    :height: 16px

.. |resetup| image:: ../images/resetup.png
    :alt: Rescan Icon
    :align: middle
    :width: 64px
    :height: 16px

|online_icon| : Indicates the device is online

|offline_icon| : Indicates the device is offline

|error_icon| : Indicates a sensor error. Hovering the mouse over it will display the error message (sensor config file failed to load).

After unplugging/plugging in the sensor, you need to click |resetup| to rescan the sensors.

Perception Mode Configuration
##################################

.. |Perception_Mode_Configuration_Area| image:: ../images/Perception_Mode_Configuration_Area.png
    :alt: Perception Mode Configuration Area
    :align: middle

.. |default(selected)| image:: ../images/default(selected).png
    :alt: Default Selected Icon
    :align: middle
    :width: 16px
    :height: 16px

.. |default(unselected)| image:: ../images/default(unselected).png
    :alt: Default Unselected Icon
    :align: middle
    :width: 16px
    :height: 16px

.. |contactforce(selected)| image:: ../images/contactforce(selected).png
    :alt: Contact Force Selected Icon
    :align: middle
    :width: 16px
    :height: 16px

.. |contactforce(unselected)| image:: ../images/contactforce(unselected).png
    :alt: Contact Force Unselected Icon
    :align: middle
    :width: 16px
    :height: 16px

.. |video(selected)| image:: ../images/video(selected).png
    :alt: Recording Selected Icon
    :align: middle
    :width: 16px
    :height: 16px

.. |video(unselected)| image:: ../images/video(unselected).png
    :alt: Recording Unselected Icon
    :align: middle
    :width: 16px
    :height: 16px

.. |record_button| image:: ../images/record_button.png
    :alt: Record Button
    :align: middle
    :width: 16px
    :height: 16px

.. |pause_button| image:: ../images/pause_button.png
    :alt: Pause Button
    :align: middle
    :width: 16px
    :height: 16px

.. container:: row

    .. container:: perception-image

        |Perception_Mode_Configuration_Area|

    .. container:: perception-options
        
        |default(selected)| / |default(unselected)| Default: When the program is newly launched or the "Default" icon on the left side of the Perception Mode Configuration Area is clicked,
        the visualization area will display the sensor's tactile image information
        
        |contactforce(selected)| / |contactforce(unselected)| Contact Force: Click the "Contact Force" icon on the left side of the Perception Mode Configuration Area,
        and the visualization area will display the contact force reconstruction results and surface deformation field
    
        |video(selected)| / |video(unselected)| Recording: Click the "Recording" icon on the left side of the Perception Mode Configuration Area,
        click the bottom-right corner to select the data stream storage location, then click |record_button| at the bottom center to start recording, and click |pause_button| to stop recording and save the file to the target path
    
.. container:: caption
    
    Figure 3: Perception Mode Configuration Area

View Switching
##################

.. figure:: ../images/views_switch.png
    :alt: View Switching
    :align: right
    :class: right-figure

    Figure 4: View Switching

.. container:: content-paragraph
    
    View switching enables flexible conversion of the tactile and contact force information fed back by the sensor between 2D planar and 3D spatial views. It presents the information in multimodal forms such as tactile images, contact force, and surface deformation field.

|
|
|

 .. figure:: ../images/touch_infromation_new.jpg
    :alt: Tactile Information
    :align: center
    :width: 500px
    :height: 450px
    :name: touch_info

    Figure 5: Tactile Information

|

.. |calibration_button| image:: ../images/calibration_button.png
    :alt: Calibration Button
    :align: middle
    :width: 16px
    :height: 16px
    
When the tactile image information is distorted or sensor data retention occurs, click the |calibration_button| at the bottom center under no-load condition.
This allows recalibrating the sensor to refresh the display.

|

 .. figure:: ../images/contactforce_new.jpg
    :alt: Contact Force Information
    :align: center
    :width: 500px
    :height: 450px
    :name: contactforce_info

    Figure 6: Contact Force Information

|

The arrows in the 3D view are the results of contact force reconstruction. The direction of the arrow indicates the direction of the force, and the length of the arrow indicates the magnitude of the force. The curved surface area below the arrow
displays the perception result of the contact deformation field. In the 2D view, only the surface deformation field is displayed due to the limitation of visualization dimensions.

2. Open Data Stream
-----------------------

.. |open_videos| image:: ../images/open_videos.png
    :alt: Open Data Stream Button
    :align: middle
    :width: 80px
    :height: 16px

.. |name_of_the_sensor| image:: ../images/name_of_the_sensor.png
    :alt: Sensor Name
    :align: middle
    :width: 80px
    :height: 16px


Click "Open Data Stream" in the Data Acquisition Control Area, then click |open_videos| to load the previously recorded data stream file. After loading, the software will cyclically display the information obtained from the data stream file and present the calculation results.
The Sensor Selection Area displays the name of the saved data stream file |name_of_the_sensor| . The name of the virtual sensor is derived from the data stream file name. After loading the data stream, refer to 3.1 Default Mode and Contact Force Mode for details, but there is no Recording Mode.
For the perception mode configuration, refer to 3.1.2 ( |video(selected)| / |video(unselected)| Recording ). For view switching, refer to 3.1.3.

3. Toolbar
-------------

.. figure:: ../images/toolbar.png
    :alt: Toolbar
    :align: center
    :scale: 100%
    :name: _xs-toolbar

    Figure 7: Toolbar

.. |theme_switch| image:: ../images/theme_switch.png
    :alt: Theme Switch Button
    :align: middle
    :width: 16px
    :height: 16px

.. |help| image:: ../images/help.png
    :alt: Help Button
    :align: middle
    :width: 16px
    :height: 16px

.. |about| image:: ../images/about.png
    :alt: About Button
    :align: middle
    :width: 16px
    :height: 16px

.. |minimization| image:: ../images/minimization.png
    :alt: Minimize Button
    :align: middle
    :width: 16px
    :height: 16px
    
.. |exit| image:: ../images/exit.png
    :alt: Exit Button
    :align: middle
    :width: 16px
    :height: 16px

|theme_switch| Theme Switch: Click to select the interface theme

|help| Help: Open help documentation and FAQ (Frequently Asked Questions)

|about| About: Display application information

|minimization| Minimize: Minimize the application to the background

|exit| Exit: Close the current application