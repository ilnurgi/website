button - Виджет кнопка
======================


.. py:function:: button([methodName, option, value])
.. py:function:: button([methodName, param_obj])
.. py:function:: button([param_obj])

    * `methodName` - название метода


        * `destroy` - Возвращает базовый элемент в первоначальное состояние, полностью удаляя из него функциональность виджета

            .. code-block:: js
                
                $('button').button('destroy');

        * `disable` - Отключает кнопку

            .. code-block:: js
                
                $('button').button('disable');

        * `enable` - Включает кнопку

            .. code-block:: js
                
                $('button').button('enable');

        * `option` - Устанавливает одно или несколько значений свойств


            .. code-block:: js

                $('button').button(
                    'option',    // имя метода
                    'disabled',  // свойство
                    false        // значение
                );

                $('button').button(
                    'option', 
                    {
                        label: 'Merge',
                        disabled: true
                    }
                );

        * `refresh` - Обновляет состояние кнопки

            .. code-block:: js
                
                $('button').button('refresh');

    * `param_obj` - объект со свойствами
        
        * `create` - Обработчик события создания кнопки
        
        * `disabled` - Отключена кнопка

        * `text` - Текст кнопки

        * `icons` - Иконки, можно задать как объектом, так и просто строкой

            * `primary` - слева от текста

            * `secondary` - справа от текста

        * `label` - Текст кнопки


    .. code-block:: js
        
        $('button').button({
            label: 'Merge',
            disabled: true,
            icons: {
                primary: "ui-icon-star",
                secondary: "ui-icon-circle-arrow-e"
            }
        });