.. _tag_shutdown_:

shutdown方法
=====================

.. container:: step-block

   .. py:method:: Node.shutdown(self)
       :module: ezros

       终止节点运行，释放相关资源。

示例代码
--------
.. container:: step-block

    .. code-block:: python
        
        import ezros
        
        node = ezros.Node("example_node")
        # 节点相关操作...
        node.shutdown()  # 关闭节点
        print("节点已终止")