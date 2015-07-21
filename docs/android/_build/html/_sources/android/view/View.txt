.. _android_view_View:

android.view.View
=================

.. py:class:: android.view.View

    пустая область экрана размером 100 х 100 пикселов

    .. py:method:: getId()

        возвращает id объекта

    .. py:method:: setBackgroundResource(R.color.name)

        устанавливает фоновый цвет

    .. py:method:: setOnCreateContextMenuListener(obj)

        утсанавливает обработчик контекстного меню, obj например this - Activity


    .. py:method:: onMeasure(width, height)

        задает размер области для вью

        :param width: int
        :param height: int
        :rtype: void

    .. py:method:: setMeasuredDimension(measuredHeight, measuredWidth);

        устанавливает размер области

        :param measuredHeight: int
        :param measuredWidth: int


.. _android_view_View_OnClickListener:

android.view.View.OnClickListener
---------------------------------

.. py:class:: android.view.View.OnClickListener

    интерфейс, обработчик нажатий кнопок

    .. py:method:: onClick(view)

        обработчик кнопки

        :param view: :ref:`android_view_View`

    ::

        OnClickListener oclBtnOk = new OnClickListener() {

            @Override
            publick void onClick(View v){
                ...
            };
        };


.. _android_view_View_MeasureSpec:

android.view.View.MeasureSpec
---------------------------------

.. py:class:: android.view.View.MeasureSpec



    .. py:method:: getMode(?)
    .. py:method:: getSize(?)

    .. py:attribute:: UNSPECIFIED