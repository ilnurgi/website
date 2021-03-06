tabs
====

виджет Tabs

.. py:function:: tabs([methodName, option, value])
.. py:function:: tabs([methodName, param_obj])
.. py:function:: tabs([param_obj])

    .. code-block:: html
        
        <div id="tabs">            
            <ul>
                <li><a href="#tabflowers.html">Содержимое Ajax</a></li>
                <li>
                    <a href="mydata.json">
                        <span>
                            JSON данные которые потом преобразуются в шаблон
                            в аякс настройках
                        </span>
                    </a>
                </li>
                <li><a href="#tab1">Ряд 1</a></li>
                <li><a href="#tab2">Ряд 2</a></li>
                <li><a href="#tab3">Ряд 3</a></li>
            </ul>
            <div id="tab1"></div>
            <div id="tab2"></div>
            <div id="tab3"></div>
        </div>

    .. code-block:: js

        $('#tabs').tabs({
            add: function(event, ui){ 
                // index - Индекс (номер) активной вкладки
                // panel - Объект HTMLElement, в котором находится
                // содержимое активной вкладки
                // tab - URL-адрес источника содержимого для активной вкладки
            },
            select: function(event, ui){
                ...
            },
            load: function(event, ui){
                ...
            },

            ajaxOptions: {
                dataType: 'html',
                dataFilter: function(result){
                    var data = $.parseJson(result).slice(0, 3);
                    return $(
                        '<div></div'
                    ).append(
                        $('#flowerTmpl').tmpl(data)
                    ).html();
                },
                error: function(jqxr, status, index, anchor){
                    $(anchor.hash).text('Ошибка');
                }
            },
            fx: {
                opacity: 'toggle',
                duration: 'normal'
            }
            panelTemplate: "<div>содержимое пo умолчанию</div>"
        });

    * `methodName`

        * `destroy` - Полностью удаляет функциональность виджета Tabs
          из базового HTML-элемента

        * `disable` - Приостанавливает работу всего виджета или отдельных вкладок. 

        * `enable` - Возобновляет работу ранее приостановленного виджета или
          отдельных вкладок

        * `option` - Позволяет изменить одну или несколько опций. 

        * `add` - Добавляет новую вкладку

        * `remove` - Удаляет вкладку

        * `select` - Активизирует вкладку

        * `load` - Осуществляет принудительную загрузку содержимого вкладки

        * `url` - Изменяет URL-адрес источника содержимого дистанционной вкладки

        * `length` - Возвращает количество вкладок в виджете

        * `abort` - Отменяет все активные Ajax-запросы для дистанционных вкладок

        * `rotate` - Указывает виджету Tabs на необходимость циклического обхода
          вкладок

    * `param_obj`

        * `add` - обработчик добавления таба

        * `ajaxOptions` - Позволяет устанавливать и
          получать значения конфигурационных параметров для Ajax-запросов

            * `dataType`

            * `dataFilter` - возвращает шаблон для вкладки

            * `error` - обрабботчик ошибки

        * `cache` - Если эта опция равна true,
          то полученное в результате Ajax запроса содержимое будет кешироваться,
          так что при следующем открытии вкладки запрос
          не будет повторно выполняться.

            Значение по умолчанию — false, которое означает,
            что содержимое дистанционной вкладки будет загружаться с сервера
            при каждом ее открытии

        * `collapsible` - Если эта опция равна true,
          то пользователь не будет иметь возможности оставить невыбранными
          все вкладки.

            Значение по умолчанию — false, которое означает,
            что одна из вкладок всегда должна быть активна (открыта)
        
        * `create` - обработчик когда виджет Tabs применяется к базовому
          HTML-элементу

        * `disable` - обработчик при отключении вкладки

        * `disabled` - Установка значения true или false означает
          соответственно отключение или включение функциональности вкладок.

            Если в качестве значения задан массив чи­сел,
            то они указывают индексы отключаемых вкладок

        * `enable` - обработчик при включении функциональных возможностей вкладки

        * `event` - Позволяет получить или задать событие,
          которое делает вкладку активной.

            По умолчанию таким событием является ciick,
            т.е. вкладка активизируется после выполнения на ней щелчка

        * `fx` - Определяет эффекты,
          которые должны использоваться при анимации процессов открытия и
          закрытия вкладок.

            Значение по умолчанию — null, означающее, что эффекты не используются.

            * `opacity`

            * `duration`

        * `load` - обработчик загрузки шаблона вкладки

        * `panelTemplate` - Определяет шаблон,
          в соответствии с которым должны генерироваться элементы содержимого,
          создаваемые программным путем.

            По умолчанию для этого исполь­зуется элемент div.

        * `remove` - обработчик при удалении вкладки из виджета

        * `select` - обработчик выбора вкладки

        * `selected` - Позволяет получить или задать индекс активной вкладки

        * `show` - обработчик когда вкладка отображается для пользователя

        * `spinner` - Позволяет получить или задать текст,
          отображаемый для пользователя во время загрузки содержимого
          дистанционных вкладок.

        * `tabTemplate` - Определяет шаблон,
          в соответствии с которым должны генерироваться структурные элементы,
          создаваемые программным путем.
