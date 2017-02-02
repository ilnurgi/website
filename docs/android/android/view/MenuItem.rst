android.view.MenuItem
=====================

.. py:class:: android.view.MenuItem()

    Элемент меню

    .. py:method:: getGroupId()

        Возвращает int, идентификатор группы

        .. code-block:: java

            int groupId = menuItem.getGroupId();


    .. py:method:: getItemId()

        Возвращает int, идентификатор элемента

        .. code-block:: java

            int itemId = menuItem.getItemId();


    .. py:method:: getMenuInfo()

        Возвращает информацию о выбранном пункте :py:class:`android.widget.AdapterView.AdapterContextMenuInfo`

        .. code-block:: java

            AdapterContextMenuInfo acmi = (AdapterContextMenuInfo) item.getMenuInfo();


    .. py:method:: getOrder()

        Возвращает int, позицию элемента в списке

        .. code-block:: java

            int order = menuItem.getOrder();


    .. py:method:: getTitle()

        Возвращает текст элемента

        .. code-block:: java

            String title = menuItem.getTitle();