Глобальные методы
=================


.. js:function:: OnAlarm(id)

    Обработчик, если приложение развернуто будильником :js:func:`SetAlarm`


.. js:function:: OnBack()

    Обработчик кнопки назад, если стандратное поведение выключено :js:func:`EnableBackKey`

    .. code-block:: js
        
        function OnBack(){
            ...
        }


.. js:function:: OnConfig()

    Обработчик системных измененний, например при смене ориентации


.. js:function:: OnData()

    Обработчик приема данных из других источников


.. js:function:: OnMenu(menu)
    
    Обработчик кнопки меню



.. js:function:: OnPause()

    Обработчик сворачивания приложения



.. js:function:: OnResume()

    Возвращение к свернтуому приложению


.. js:function:: OnStart()

    Вызывается при старте приложения

    .. code-block:: js
        
        function OnStart(){
            ...
        }


