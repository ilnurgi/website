android.content.res.Configuration
=================================


.. py:class:: Configuration()

    Конфигурация приложения


android.content.res.Resources
=============================


.. py:class:: android.content.res.Resources()

    Таблица ресурсов приложения

    .. code-block:: java

        Resources resource = activity.getResources()


    .. py:method:: getColor(R.color.id)

        Возвращает ресурс цвет по идентификатору


    .. py:method:: getDimension(R.dim.id)

        Возвращает ресурс размер по идентификатору


    .. py:method:: getDrawable(R.drawable.id)

        Возвращает ресурс изображение по идентификатору


    .. py:method:: getStringArray(int arrayId)

        Возвращает ресурс массив по идентификатору

        .. code-block:: java

            String[] names = resource.getStringArray(R.array.names);


    .. py:method:: getText(id)

        возвращает текст по идентификатору

        .. code-block:: java

            CharSequence styledText = myResources.getText(R.string.stop_message);


Resources.NotFoundException
---------------------------

.. py:class:: android.content.res.Resources.NotFoundException()

