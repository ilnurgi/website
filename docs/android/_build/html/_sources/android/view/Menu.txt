.. _android_view_Menu:

android.view.Menu
=================

.. py:class:: android.view.Menu

    объект меню


    .. py:method:: add(title)
    .. py:method:: add(groupId, itemId, order, title)

        добавляет элемент в меню

        :param title: :py:class:`String` - текст, который будет отображен
        :param groupId: :py:class:`int` - идентификатор группы, частью которой является пункт меню
        :param itemId: :py:class:`int` - ID пункта меню
        :param order: :py:class:`int`- для задания последовательности показа пунктов меню


    .. py:method:: setGroupVisible(groupId, enable)

        скрывает отображает элементы в меню
        
        :param groupId: :py:class:`int` - идентификатор группы
        :param enable: :py:class:`bool`- видимость элемента

