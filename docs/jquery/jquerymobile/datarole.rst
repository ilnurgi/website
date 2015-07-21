datarole - описание функциональности элемента
=============================================


.. code-block:: js
    
    <div data-role="page">
        <div data-role="header"></div>
        <div data-role="content"></div>
    </div>

Возможные значения атрибута:
----------------------------

* `content` - содержимое страницы

* `footer` - нижняя часть страницы

* `header` - заголовок страницы

* `page` - страница


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