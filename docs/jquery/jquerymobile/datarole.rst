datarole - описание функциональности элемента
=============================================


.. code-block:: js
    
    <div data-role="page">
        <div data-role="header"></div>
        <div data-role="content"></div>
    </div>

Возможные значения атрибута:
----------------------------

* `button` - кнопка

    * `data-corners` - определяет скругленность углов, true/false

    * `data-icon` - определяет значок кнопки

    * `data-iconpos` - позиция значка кнопки, left/top/rigth/bottom/notext

    * `data-inline` - размер кнопки определяется размером содержимого, true/false

    * `data-shadow` - тень, true/false


* `collapsible` - сворачиваемый блок, вызывает соответсвующие события, которые можно перехватить

    * `data-collapsed` - отображать блок свернутым, true/false

    * `data-content-theme` - тема оформления для области содержимого сворачиваемого блока

    .. code-block:: js
        
        <div data-role='collapsible'>
            <h1>Заголовок</h1>
            <p>содержимое</p>
        </div>


* `collapsible-set` - виджет акордион

    * `data-content-theme` - тема оформления для области содержимого сворачиваемого блока


* `content` - содержимое страницы


* `controlgroup` - управляющая группа

    * `data-type` - ориентация группы, horizontal


* `fieldcontain` - элемент формы и его подпись должны выстраиваться в линию    
    
    .. code-block:: js
        
        <form method='get'>
            <div data-role='fieldcontain'>
                <label for='address'>address</label>
                <input id='address'>
            </div>
            <input type='submit' data-inline='true'>
        </form>

    Аттрибуты данных для элементов select

        * `data-icon` - иконка

        * `data-iconpos` - позиция значка кнопки, left/top/rigth/bottom/notext

        * `data-inline` - размер кнопки определяется размером содержимого, true/false

        * `data-native-menu` - true/false - нативное меню

        * `data-overlay-theme` - тема оформления

        * `data-placeholder` - явным образом идентифицирует элемент options в качесвтве заместителя

    Програмное управление списком select

        * `open` - открывает список

        * `close` - закрывает список

        * `refresh` - обновляет виджет

        .. code-block:: js
            
            $('#select').selectmenu('open');


* `footer` - нижняя часть страницы

* `header` - заголовок страницы


* `listview` - списки

    * `data-filter` - true/false, отобразить текстовое поле для поиска

    * `data-filter-placeholder` - строка замениститель, которая будет отображаться в фильтре

    * `data-filter-theme` - тема для фильтра

    * `data-inset` - включить скругление углов

    * `data-split-icon` - определяет значок разделителя между кнопками

    Атрибуты для форматирования элементов списка

        * `list-divider` - элемент списка - разделитель    

        * `data-icon` - значок для элемента списка

        * `data-theme` - тема

        * `data-divider-theme` - тема разделителя
        
        .. code-block:: js
            
            <ul 
                data-role='listview' 
                data-theme='c'
                data-divider-theme='b'>

                <li data-role='list-divider'>A</li>
                ...
            </ul>

    Програмное управление 

        .. code-block:: js
            
            $('ul').listview('option', 'filterCallback', function(listItem, filter){
                var pattern = new RegExp();
                return !pattern.test(listItem)
            })  

    CSS атрибуты

        * `ui-li-count` - счетчик

            .. code-block:: js
                
                <li>
                    <a href='#roses'>
                        Roses
                        <div class='ui-li-count'>32</div>
                    </a>
                </li>

        * `ui-li-aside`

            .. code-block:: js
                
                <a href='#roses'>
                    <h1>Roses<h1>
                    <p>Roses description</p>
                    <p class='ui-li-aside'>Rose <strong>$4.99</strong><p>
                </a>

    Двухуровневый список

        .. code-block:: js

            <a href='#roses'>
                <h1>Roses</h1>
                <p>Rose description</p>
            </a>
                
                









* `none` - выключает автоматическое создание виджетов

* `page` - страница

* `slider` - слайдер




Примеры
-------

Две страницы на странице

    .. code-block:: js
        
        <div id="page1" data-role="page1">
            <a href="#page2" data-transition="pop">перейти на страницу 2</a>
        </div>
        
        <div id="page2" data-role="page2">
            <a href="#page1" data-transition="pop">перейти на страницу 1</a>
        </div>


Select с ползунком

    .. code-block:: js
        
        <form>
            <div data-role='fieldcontain'>
                <label for='speed'>speed</label>
                <select 
                    id='speed' 
                    name='speed'
                    data-role='slider'>
                    <option value='fast'>fast</option>
                    <option value='slow'>sloe</option>
                </select>
            </div>
        </form>