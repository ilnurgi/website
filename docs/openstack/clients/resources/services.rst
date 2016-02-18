Services - ресурс, для управления сервисами, запущенными на хостах
==================================================================

Имеет следующие методы, для управления сервисами:

.. py:method:: list(host=None, binary=None)

    Возвращает список сервисов, запущенных на хостах.

    Без аргументов вернет полную информацию о запущенных сервисах на всех хостах.

    :param host: название хоста
    :param binary: название сервиса
    :rtype: Service

    .. code-block:: py

        services = nova_client.services.list()


.. py:method:: enable(host, binary)

    Включает указанный сервис на хосте

    :param host: название хоста
    :param binary: название сервиса

    .. code-block:: py

        service = nova_client.services.enable(host='my_host', binary='nova-compute')


.. py:method:: disable(host, binary)

    Выключает указанный сервис на хосте

    :param host: название хоста
    :param binary: название сервиса

    .. code-block:: py

        service = nova_client.services.disable(host='my_host', binary='nova-compute')


.. py:method:: disable_log_reason(host, binary, reason)

    Выключает указанный сервис на хосте

    :param host: название хоста
    :param binary: название сервиса
    :param reason: причина выключения

    .. code-block:: py

        service = nova_client.services.disable(host='my_host', binary='nova-compute')


.. py:method:: force_down(host, binary, force_down)

    Выключает указанный сервис на хосте, форсированно

    :param host: название хоста
    :param binary: название сервиса
    :param force_down:

    .. code-block:: py

        service = nova_client.services.disable(host='my_host', binary='nova-compute')


Service
=======

.. py:class:: Service()

    Сервис, запущенный на хосте

    .. py:attribute:: binary

        Название сервиса

    .. py:method:: disabled_reason

        Причина выключения

    .. py:method:: forced_down

        .. note::

            доступно для клиента версии старше 2.11

    .. py:attribute:: host

        Название хоста

    .. py:attribute:: id

        Идентификатор запущенного сервиса

    .. py:attribute:: status

        Статус сервиса, включен или выключен: 'up', 'down'

    .. py:attribute:: updated_at

        Дата обновления сервиса

    .. py:attribute:: zone

        Зона сервиса





