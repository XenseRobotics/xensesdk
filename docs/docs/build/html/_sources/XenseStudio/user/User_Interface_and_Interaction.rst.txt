.. _tag_user_interface_and_interaction:

四、界面与交互
=================

1、 选择传感器   
------------------

.. figure:: ../images/Data_or_Record_control_area.png
    :alt: 数采控制区
    :align: center
    :scale: 100%
    :name: _xs-sensor_selection

    图 1 数采控制区

当前数采控制区的“选择传感器”选项下，可实时监测传感器多模态感知信息，且支持对传感器反馈信息进行录制，以便后期“打开数据流”进行回溯，复盘，分析。
 
 .. figure:: ../images/elements_selection_area.png
    :alt: 设备选择区
    :align: center
    :scale: 100%
    :name: _xs-device_selection

    图 2 设备选择区

.. |select_button| image:: ../images/select_button.png
    :alt: 选择按钮
    :align: middle
    :width: 16px
    :height: 16px

软件支持同时连接多路传感器，并可以在各传感器之间快速切换。
设备选择区可显示所有传感器名称，通过单击 |select_button| ，
从已检测到的传感器列表快速切换至目标传感器，并将其采集信息显示在可视化区域中。

传感器状态提示
#######################

.. |online_icon| image:: ../images/online_icon.png
    :alt: 在线图标
    :align: middle
    :width: 16px
    :height: 16px

.. |offline_icon| image:: ../images/offline_icon.png
    :alt: 离线图标
    :align: middle
    :width: 16px
    :height: 16px

.. |error_icon| image:: ../images/error_icon.png
    :alt: 错误图标
    :align: middle
    :width: 16px
    :height: 16px

.. |resetup| image:: ../images/resetup.png
    :alt: 重新扫描图标
    :align: middle
    :width: 64px
    :height: 16px

|online_icon| :表示设备已上线

|offline_icon| :表示设备已离线

|error_icon| :表示传感器异常，鼠标悬浮会显示异常信息（传感器config文件读取失败）。

拔掉/插入传感器后，需要点击 |resetup| ，重新扫描传感器。

感知模态配置
####################

.. |Perception_Mode_Configuration_Area| image:: ../images/Perception_Mode_Configuration_Area.png
    :alt: 感知模态配置区
    :align: middle

.. |default(selected)| image:: ../images/default(selected).png
    :alt: 默认选中图标
    :align: middle
    :width: 16px
    :height: 16px

.. |default(unselected)| image:: ../images/default(unselected).png
    :alt: 默认未选中图标
    :align: middle
    :width: 16px
    :height: 16px

.. |contactforce(selected)| image:: ../images/contactforce(selected).png
    :alt: 接触力选中图标
    :align: middle
    :width: 16px
    :height: 16px

.. |contactforce(unselected)| image:: ../images/contactforce(unselected).png
    :alt: 接触力未选中图标
    :align: middle
    :width: 16px
    :height: 16px

.. |video(selected)| image:: ../images/video(selected).png
    :alt: 视频选中图标
    :align: middle
    :width: 16px
    :height: 16px

.. |video(unselected)| image:: ../images/video(unselected).png
    :alt: 视频未选中图标
    :align: middle
    :width: 16px
    :height: 16px

.. |record_button| image:: ../images/record_button.png
    :alt: 录制按钮
    :align: middle
    :width: 16px
    :height: 16px

.. |pause_button| image:: ../images/pause_button.png
    :alt: 暂停按钮
    :align: middle
    :width: 16px
    :height: 16px

.. container:: row

    .. container:: perception-image

        |Perception_Mode_Configuration_Area|

    .. container:: perception-options
        
        |default(selected)| / |default(unselected)| 默认: 新启动程序或者点击感知模态配置区左侧的“默认”图标，
        可视化区将显示传感器触觉图像信息
        
        |contactforce(selected)| / |contactforce(unselected)| 接触力: 点击感知模块配置区左侧的“接触力”图标，
        可视化区将显示接触力重建结果和曲面变形场
    
        |video(selected)| / |video(unselected)| 录制：点击感知模块配置区左侧的“录制”图标,
        点击右下角 选择数据流存放位置，随后点击正下方 |record_button| 开始录制，点击 |pause_button| 停止录制并将文件保存至目标路径
    
.. container:: caption
    
    图 3 感知模态配置区

视图切换
#################

.. figure:: ../images/views_switch.png
    :alt: 视图切换
    :align: right
    :class: right-figure

    图 4 视图切换

.. container:: content-paragraph
    
    视图切换可实现传感器反馈的触觉及接触力信息在二维平面与三维立体空间的灵活转换，并以触觉图像、接触力、曲面变形场等多模态形式予以呈现

|
|
|

 .. figure:: ../images/touch_infromation_new.jpg
    :alt: 触觉信息
    :align: center
    :width: 500px
    :height: 450px
    :name: touch_info

    图 5 触觉信息

|

.. |calibration_button| image:: ../images/calibration_button.png
    :alt: 校准按钮
    :align: middle
    :width: 16px
    :height: 16px
    
触觉图像信息失真时，或遇到传感器数据滞留时，在空载情况下点击正下方 |calibration_button| 校准按钮，
可以重新校准传感器，以刷新显示。

|

 .. figure:: ../images/contactforce_new.jpg
    :alt: 接触力
    :align: center
    :width: 500px
    :height: 450px
    :name: contactforce_info

    图 6 接触力信息

|

三维视图上的箭头，即为接触力重建的结果箭头方向表示力的方向，箭头的长度表示力的大小，箭头之下的曲面部分，
显示了接触变形场的感知结果。二维视图下，由于可视化维度的限制，只显示曲面变形场。

2、 打开数据流
----------------

.. |open_videos| image:: ../images/open_videos.png
    :alt: 打开数据流按钮
    :align: middle
    :width: 80px
    :height: 16px

.. |name_of_the_sensor| image:: ../images/name_of_the_sensor.png
    :alt: 传感器名称
    :align: middle
    :width: 80px
    :height: 16px


在数采控制区点击“打开数据流”，点击 |open_videos| ，可以加载之前录制的数据流文件。加载以后，软件将循环展示从数据流文件中获取的信息，并展示计算结果。
传感器选择区显示保存的数据流文件名称 |name_of_the_sensor| ，虚拟传感器的名称来自数据流文件名。加载数据流以后，详见3.1默认模式和接触力模式，但没有录制模式。
感知模式配置可参考3.1.2（ |video(selected)| / |video(unselected)| 录制），视图切换可参考3.1.3。

3、 工具栏
----------------

.. figure:: ../images/toolbar.png
    :alt: 工具栏
    :align: center
    :scale: 100%
    :name: _xs-toolbar

    图 7 工具栏

.. |theme_switch| image:: ../images/settings.png
    :alt: 设置按钮
    :align: middle
    :width: 16px
    :height: 16px

.. |help| image:: ../images/help.png
    :alt: 帮助按钮
    :align: middle
    :width: 16px
    :height: 16px

.. |about| image:: ../images/about.png
    :alt: 关于按钮
    :align: middle
    :width: 16px
    :height: 16px

.. |minimization| image:: ../images/minimization.png
    :alt: 最小化按钮
    :align: middle
    :width: 16px
    :height: 16px

.. |maximization| image:: ../images/maximization.png
    :alt: Maximize Button
    :align: middle
    :width: 16px
    :height: 16px
    
.. |exit| image:: ../images/exit.png
    :alt: 退出按钮
    :align: middle
    :width: 16px
    :height: 16px

|theme_switch| 设置：设置界面的主题外观与语言类型

|help| 帮助：打开帮助文档、常见问题解答

|about| 关于：展示应用信息

|minimization| 最小化：将应用最小化至后台

|maximization| 最大化：将应用程序最大化以占据整个屏幕

|exit| 退出：关闭当前应用
