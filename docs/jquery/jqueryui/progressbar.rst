progressbar - виджет прогрессбара
=================================


.. js:function:: progressbar([methodName, option, value])
.. js:function:: progressbar([methodName, param_obj])
.. js:function:: progressbar([param_obj])


    * `methodName` - название метода


        * `destroy` - Возвращает базовый элемент в первоначальное состояние, полностью удаляя из него функциональность виджета

            .. code-block:: js
                
                $('progrssDiv').progressbar('destroy');

        * `disable` - Отключает

            .. code-block:: js
                
                $('progrssDiv').progressbar('disable');

        * `enable` - Включает кнопку

            .. code-block:: js
                
                $('progrssDiv').progressbar('enable');

        * `option` - Устанавливает одно или несколько значений свойств


            .. code-block:: js

                $('progrssDiv').progressbar(
                    'option',    // имя метода
                    'disabled',  // свойство
                    false        // значение
                );

                $('progrssDiv').progressbar(
                    'option', 
                    {
                        label: 'Merge',
                        disabled: true
                    }
                );

        * `value` - получает или устанавливает значение

            .. code-block:: js
                
                $('button').button('value', 21);


    * `param_obj` - объект

        * `create` - обработчик создания элемента

        * `change` - обработчик изменения значения

        * `complete` - обработчик, когда значение равно 100
        
        * `disable` - индикатор включен/выключен

        * `value` - процент выполнения задачи


    .. code-block:: js
        
        $('progrssDiv').progressbar({
            value: 21
        })