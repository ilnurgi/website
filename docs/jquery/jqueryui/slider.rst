slider
======

виджет слайдер

.. py:function:: slider([methodName, option, value])
.. py:function:: slider([methodName, param_obj])
.. py:function:: slider([param_obj])
    
    * `methodName` - название метода
        
        * `destroy` - Возвращает базовый элемент в первоначальное состояние, полностью удаляя из него функциональность виджета

            .. code-block:: js
                
                $('slider').slider('destroy');

        * `disable` - Отключает элемент

            .. code-block:: js
                
                $('slider').slider('disable');

        * `enable` - Включает элемент

            .. code-block:: js
                
                $('slider').slider('enable');

        * `option` - Устанавливает одно или несколько значений свойств

            .. code-block:: js

                $('slider').slider('option', 'value', 21);

                $('slider').slider(
                    'option', 
                    {
                        value: 21
                    }
                );

        * `value` - задает новое значение

            .. code-block:: js

                $('slider').slider('value', 21);

        * `values` - Устанавливает одно или несколько значений свойств

            .. code-block:: js

                $('slider').slider('values', 35, 65);

    * `param_obj` - объект с параметрами

        * `animate` -  включение/выключение анимации: true/false, slow, fast

        * `change` - обработчик, значение утсановлено

        * `create` - обработчик создания объекта

        * `disabled` - включение/выключение элемента

        * `max` - максимальное значение, по умолчанию 100

        * `min` - минимальное значение, по умолчанию 0

        * `orientation` - ориентация: vertical, horizontal

        * `range` - используется совместно со свойством values для создания ползунка с несколькими рукоятками

        * `slide` - обработчик, перемещения ползунка

        * `start` - обработчик, начинается перемещение ползунка

        * `step` - шаг пермещения

        * `stop` - обработчик, пользователь перестал передвигать ползунок
        
        * `value` - значение ползунка

        * `values` - используется совместно со свойством range для создания ползунка с несколькими рукоятками


    .. code-block:: js
        
        $('#slider').slider({
            values: [25, 65],
            range: true
        });