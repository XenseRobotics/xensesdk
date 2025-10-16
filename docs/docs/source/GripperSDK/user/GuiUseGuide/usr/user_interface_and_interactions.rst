.. _tag_user_interface_and_interactions:

四、界面与交互
=================

1、 选择夹爪IP  
------------------

.. figure:: ../../images/Data_or_Record_control_area.jpg
    :alt: 夹爪IP选择区
    :align: center
    :scale: 100%
    :name: _gs-sensor_selection

    图 1 夹爪IP选择区

当前夹爪IP选择区的“更改”选项下，可选择在局域网内所有的夹爪IP，实现对不同IP夹爪的连接。
 

传感器状态提示
#######################

.. |online_icon| image:: ../../images/online_icon.png
    :alt: 在线图标
    :align: middle
    :width: 16px
    :height: 16px

.. |offline_icon| image:: ../../images/offline_icon.png
    :alt: 离线图标
    :align: middle
    :width: 16px
    :height: 16px

.. |error_icon| image:: ../../images/error_icon.png
    :alt: 错误图标
    :align: middle
    :width: 16px
    :height: 16px

.. |resetup| image:: ../../images/resetup.png
    :alt: 重新扫描图标
    :align: middle
    :width: 64px
    :height: 16px

|online_icon| :表示设备已上线

|offline_icon| :表示设备已离线

|error_icon| :表示传感器异常，鼠标悬浮会显示异常信息（传感器config文件读取失败）。

拔掉/插入夹爪后，需要点击 |resetup| ，重新连接扫描传感器。



触觉信息显示
#################

.. figure:: ../../images/touch_infromation_new.png
    :alt: 触觉信息显示
    :align: center
    :scale: 100%
    :name: _gs-touch_infromation_new

    图 2 触觉信息显示

.. container:: content-paragraph
    
    夹爪传感器可感知触觉并生成对应图像，同时能实时显示多维度的力数据，助力对夹爪的状态与受力情况进行精准监测和控制。

.. |calibration_button| image:: ../../images/calibration_button.jpg
    :alt: 校准按钮
    :align: middle
    :width: 16px
    :height: 16px
    
触觉图像信息失真时，或遇到传感器数据滞留时，在空载情况下点击正下方 |calibration_button| 校准按钮，
可以重新校准传感器，以刷新显示。



2、 夹爪传感器配置区
----------------------

.. figure:: ../../images/conf_zhua.png
    :alt: 夹爪配置区
    :align: center
    :scale: 100%
    :name: conf_zhua

    图 3 夹爪配置区

.. |target| image:: ../../images/target.png
    :alt: 切换目标位置
    :align: middle
    :width: 16px
    :height: 16px

.. |vmax| image:: ../../images/vmax.png
    :alt: 设置最大速度
    :align: middle
    :width: 16px
    :height: 16px

.. |fmax| image:: ../../images/fmax.png
    :alt: 设置最大接触力
    :align: middle
    :width: 16px
    :height: 16px

.. |set_color| image:: ../../images/set_color.png
    :alt: 设置状态灯颜色
    :align: middle
    :width: 16px
    :height: 16px
    

|target| 移动目标位置：点击后传感器可移动到目标位置

|vmax| 设置传感器最大速度：可以调节传感器移动的速度

|fmax| 设置传感器最大接触力：可以调节传感器与物体的接触力大小

|set_color| 设置夹爪状态灯的颜色：点击颜色按钮，可以设置状态灯的颜色



3、 工具栏
----------------

.. figure:: ../../images/toolbar.png
    :alt: 工具栏
    :align: center
    :scale: 100%
    :name: _gs-toolbar

    图 4 工具栏

.. |theme_switch| image:: ../../images/settings.png
    :alt: 设置按钮
    :align: middle
    :width: 16px
    :height: 16px

.. |help| image:: ../../images/help.png
    :alt: 帮助按钮
    :align: middle
    :width: 16px
    :height: 16px

.. |about| image:: ../../images/about.png
    :alt: 关于按钮
    :align: middle
    :width: 16px
    :height: 16px

.. |minimization| image:: ../../images/minimization.png
    :alt: 最小化按钮
    :align: middle
    :width: 16px
    :height: 16px
    
.. |maximization| image:: ../../images/maximization.png
    :alt: 最大化按钮
    :align: middle
    :width: 16px
    :height: 16px    

.. |exit| image:: ../../images/exit.png
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
