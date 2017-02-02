.. _android_view_menu:

android.view.Menu
=================

.. py:class:: android.view.Menu()

    Меню


    .. py:method:: add(String title)
    .. py:method:: add(int groupId, int itemId, int order, String title)

        Добавляет элемент в меню

        * title - текст, который будет отображен
        * groupId - идентификатор группы, частью которой является пункт меню
        * itemId - ID пункта меню
        * order - для задания последовательности показа пунктов меню


    .. py:method:: setGroupVisible(int groupId, bool enable)

        Скрывает отображает элементы в меню
        
        * groupId - идентификатор группы
        * enable - видимость элемента

