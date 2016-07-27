.. py:module:: android.view

View - базовый компонент интерфейса
===================================


.. py:class:: View()

    Базовый класс для всех компонентов интерфейса

    Наследник :py:class:`java.lang.Object`


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

    .. py:method:: setOnClickListener(callback)

        Устанавливает обработчик клика, для кликабельных объектов: :py:class:`android.widget.Button`

        * callback - :py:class:`android.view.View.OnClickListener`

        .. code-block:: java

            import android.view.View;
            import android.view.View.OnClickListener;

            btnLogin.setOnClickListener(new OnClickListener(){

                @Override
                public void onClick(View v){
                    ...
                }
            })


    .. py:class:: OnClickListener()

        Интерфейс, обработчик нажатий кнопок

        .. py:method:: onClick(view)

            Обработчик кнопки

            * view - :py:class:`android.view.View`

        .. code-block:: java

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