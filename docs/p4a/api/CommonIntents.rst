CommonIntents - общедоступные действия
======================================

.. py:method:: pick(str uri)

    Display content to be picked by URI (e.g. contacts)


.. py:method:: scanBarcode()

    включает сканер баркода. возвращает результат в в иде словаря


.. py:method:: search(str query)

    включает поиск по запросу


.. py:method:: view(str uri[ , str type, dict extras])

    :param str uri:
    :param str type: не обязательный, MIME type/subtype of the URI,
    :param dict extras: не обязательный, доп параметры

    запускает указанный активити


.. py:method:: viewContacts()

    запускает приложение, контакты


.. py:method:: viewHtml(str path)

    открывает в браузере указанный файл


.. py:method:: viewMap(str query)

    открывает поиск по карте по запросу