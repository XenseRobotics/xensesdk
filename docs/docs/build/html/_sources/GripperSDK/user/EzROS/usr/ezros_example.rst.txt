.. _tag_ezros_example:

Using the EzROS Command-Line Tool
=====================================

.. container:: ezros-tool-guide

    For first-time use, you can quickly learn about ezros's functions through the following command.

    .. code-block:: bash

        ezros -h
        # or ezros --help

    The terminal will print the following information:

    .. code-block:: text

        usage: ezros [-h] [-d DOMAIN_ID] [-q] [-a] [-t TIMEOUT] [-f FILTER] {service,topic} ...

        EzROS CLI - A simple network tool

        positional arguments:
          {service,topic}       Commands
            service             Call a service
            topic               Listen to a topic

        optional arguments:
          -h, --help            show this help message and exit
          -d DOMAIN_ID, --domain-id DOMAIN_ID
                                DDS domain ID
          -q, --quiet           Quiet mode
          -a, --all             Display all node information
          -t TIMEOUT, --timeout TIMEOUT
                                Scan timeout in seconds, default 2 seconds
          -f FILTER, --filter FILTER
                                Filter node names containing the specified string, default matches all nodes

    .. container:: ezros-cmd-catalog-section

        For more detailed usage, please refer to the debugging commands in the EzROS directory:

        .. container:: command-catalog

            - :ref:`Viewing EzROS Service Information <tag_all_info>`
            - :ref:`Monitoring Topics <tag_echo>`
            - :ref:`Calling Services <tag_service>`

.. toctree::
   :maxdepth: 2
   :caption: Table of Contents
   :hidden:

   API/all_info
   API/echo
   API/service