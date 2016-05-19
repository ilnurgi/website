Стандартные директивы
=====================

Директивы являются одной из ключевых возможностей Angular.JS.

Они позволяют разработчику описать поведение отдельных элементов и
расширить синтаксис HTML.

В js коде директивы принято называть camelCase-ом `ngApp`,
а в шаблонах писать их через тире `ng-app`

a
-

Заменяет стандартный html тег - якорь,
т.к. в стандартном href является обязательным и
стандартны перезагружает страницу.

.. code-block:: html

    <a ng-click="model.$save()">Save</a>


form
----

Форма :js:class:`FormController`

* name - необязательный параметр

.. code-block:: html

    <form name="myForm"></form>


input[checkbox]
---------------

* :ref:`ngModel`

* name - имя свойства, под которым элемент управления будет доступен в области видимости

* ng-true-value

* ng-false-value

* :ref:`ngChange`

.. code-block:: html

    <input
        type="checkbox"
        ng-model="value1">

    <input
        type="checkbox"
        ng-model="value2"
        ng-true-value="YES"
        ng-false-value="NO">


input[email]
------------

* :ref:`ngModel`

* name - имя свойства, под которым элемент управления будет доступен в области видимости

* required

* :ref:`ngRequired`

* ng-minlength

* ng-maxlength

* :ref:`ngPattern`

.. code-block:: html

    <input
        type="email"
        name="input"
        ng-model="text"
        required>


input[number]
-------------

* :ref:`ngModel`
* name
* min
* max
* required
* :ref:`ngRequired`
* ng-minlength
* ng-maxlength
* :ref:`ngPattern`
* :ref:`ngChange`


.. code-block:: html

    <input
        type="number"
        name="input"
        ng-model="value"
        min="0"
        max="99"
        required>


input[radio]
------------

* :ref:`ngModel`
* value
* name
* :ref:`ngChange`

.. code-block:: html

    <input
        type="radio"
        ng-model="color"
        value="red"> Red <br/>

    <input
        type="radio"
        ng-model="color"
        value="green"> Green <br/>

    <input
        type="radio"
        ng-model="color"
        value="blue"> Blue <br/>


input[text]
-----------

* :ref:`ngModel`

* name - имя свойства, под которым элемент управления будет доступен в области видимости

* required

* :ref:`ngRequired`

* ng-minlength

* ng-maxlength

* :ref:`ngPattern`

* :ref:`ngChange`

.. code-block:: html

    <input
        type="text"
        name="userName"
        ng-model="user.name"
        required>

    <input
        type="text"
        name="lastName"
        ng-model="user.last"
        ng-minlength="3"
        ng-maxlength="10">

    <input
        type="text"
        name="input"
        ng-model="text"
        ng-pattern="word"
        required>


input[url]
----------

* :ref:`ngModel`

* name - имя свойства, под которым элемент управления будет доступен в области видимости

* required

* :ref:`ngRequired`

* ng-minlength

* ng-maxlength

* :ref:`ngPattern`

* :ref:`ngChange`

.. code-block:: html

    <input
        type="url"
        name="input"
        ng-model="text"
        required>


ng-app
------

Главная директива приложения, задает область ангуляр приложения или
создает область для модуля.

Можно указать дополнительный атрибут, название приложения.

1. создается инжектор(injector), который будет использоваться для dependency injection
2. инжектор создает root scope, что является контекстом для модели нашего приложения
3. AngularJS “компилирует” DOM начиная с ngApp.

.. code-block:: html

    <body ng-app></body>

.. code-block:: html

    <script type="text/javascript">
        var app = angular.module('myApp', []);
    </script>

    <body ng-app='myApp'></body>


ng-bind
-------

Связывание компонента с объектом из скоупа

.. code-block:: html

    Hello <span ng-bind="name"><span>


ng-bind-html-unsafe
-------------------

Создает привязку через свойство `innerHTML`.

.. code-block:: html

    Hello <span ng-bind-html-unsafe="name"><span>


ng-bind-template
----------------

Множественная привязка

.. code-block:: html

    <pre ng-bind-template="{{salutation}} {{name}}!"></pre>


.. _ngChange:

ng-change
---------

Вызывает определенную функция, приизменении значения.

.. code-block:: html

    <input
        type="checkbox"
        ng-model="confirmed"
        ng-change="change()"
        id="ng-change-example1" />


ng-checked
----------

.. code-block:: html

    <input
        id="checkSlave"
        type="checkbox"
        ng-checked="master">


ng-class
--------

Задает новый класс элементу

.. code-block:: html

    <li ng-class="{'active':(currPath == 'main')}"></li>

    <span ng-class="myVar">Sample Text</span>


ng-class-even
-------------

Задает новый класс каждому четному элементу,
используется совместно с :ref:`ngRepeat`

.. code-block:: html

    <li ng-repeat="name in names">
        <span ng-class-odd="'odd'" ng-class-even="'even'">
            {{name}}
        </span>
    </li>


ng-class-odd
------------

Задает новый класс каждому нечетному элементу,
используется совместно с :ref:`ngRepeat`


ng-click
--------

Обработчик клика по элементу

.. code-block:: html

    <button
        ng-click="count = count + 1"
        ng-init="count=0">


ng-cloak
--------

Предотвращение показа в браузере шаблона angular при загрузке приложения

.. code-block:: html

    <div
        id="template1"
        ng-cloak>{{ 'hello' }}</div>

ng-controller
-------------

Связывание элемента c контроллером

.. code-block:: html

    <script type="text/javascript">
        angular
        .module('myapp, []')
        .controller('myController', function myController($scope){
            ...
        })
        .controller('myController', ['$scope', function myController($scope){
            // для корректной минификации
            ...
        }])
    </script>

    <div ng-controller='myController'>
        {{ myValue }}
    </div>

.. code-block:: js

    <script type="text/javascript">
        angular
        .module('myapp, []')
        .controller('myController', MyCtrl);

        // для корректной минификации
        MyCtrl.$inject = ['$scope'];

        function MyCtrl($scope){
            ...
        });
    </script>

    <div ng-controller='myController'>
        {{ myValue }}
    </div>


ng-csp
------

Включает поддержку CSP

.. code-block:: html

    <html ng-csp>...</html>


ng-dblclick
-----------

Обработчик двойного клика по элементу

.. code-block:: html

    <button ng-dblclick="count = count + 1" ng-init="count=0">


ng-disabled
-----------

Включает/выключает элемент

.. code-block:: html

    <button
        ng-model="button"
        ng-disabled="checked">Button</button>


ng-form
-------

Форма, позволяет создавать вложенные формы


ng-hide
-------

Скрывает элемент

.. code-block:: html

    <span ng-hide="checked">I hide when you checkbox is checked?</span>


ng-href
-------

.. code-block:: html

    <a
        id="link-1"
        href
        ng-click="value = 1">link 1</a> (link, don't reload)

    <a
        id="link-2"
        href=""
        ng-click="value = 2">link 2</a> (link, don't reload)

    <a
        id="link-3"
        ng-href="/{{'123'}}">link 3</a> (link, reload!)

    <a
        id="link-4"
        href=""
        name="xx"
        ng-click="value = 4">anchor</a> (link, don't reload)

    <a
        id="link-5"
        name="xxx"
        ng-click="value = 5">anchor</a> (no link)

    <a
        id="link-6"
        ng-href="{{value}}">link</a> (link, change location)


ng-include
----------

Подключает отдельный файлы

* src
* onload - выполнится, когда новая часть будет загружена
* autoscroll - прокрутка отображения к загруженному контенту

.. code-block:: html

    <div
        ng-include='/index.html'
        onload=""
        autoscroll=""></div>


ng-init
-------

Директива, инициализация начальных данных

.. code-block:: html

    <div ng-init="name='world'">
        Hello {{ name }}
    </div>


ng-list
-------

Конвертирует входной текст, разделенный заданным знаком разделителем, в массив строк

.. code-block:: html

    <input name="namesInput" ng-model="names" ng-list required>

.. _ngModel:

ng-model
--------

Задает модель для связывания


ng-mousedown
------------

Обработчик события `mousedown`, нажата кнопка мыши


ng-mouseenter
-------------

Обработчик события `mouseenter`, курсов вошел в область


ng-mouseleave
-------------

Обработчик события `mouseleave`, курсов вышел из области


ng-mousemove
------------

Обработчик события `mousemove`, перемещение мыши в элементе


ng-mouseover
------------

Обработчик события `mouseover`, мышь сверху


ng-mouseup
----------

Обработчик события `mouseup`


ng-multiple
-----------

.. code-block:: html

    <select id="select" ng-multiple="checked">


ng-non-bindable
---------------

Не интерпретировать фреймворку содержимое элемента

.. code-block:: html

    <div ng-non-bindable>Ignored: {{1 + 2}}</div>


.. _ngOptions:

ng-options
----------


.. _ngPattern:

ng-pattern
----------


ng-pluralize
------------

Локализация

* count - значение
* offset
* when - карта значений
    * one - первый элемент
    * other - другой элемент

.. code-block:: html

    <ng-pluralize
        count="personCount"
        when="{'0': 'Nobody is viewing.',
               'one': '1 person is viewing.',
               'other': '{} people are viewing.'}">
    </ng-pluralize>

    <ng-pluralize
        count="personCount"
        offset=2
        when="{'0': 'Nobody is viewing.',
               '1': '{{person1}} is viewing.',
               '2': '{{person1}} and {{person2}} are viewing.',
               'one': '{{person1}}, {{person2}} and one other person are viewing.',
               'other': '{{person1}}, {{person2}} and {} other people are viewing.'}">
    </ng-pluralize>


ng-readonly
-----------

.. code-block:: html

    <input type="text" ng-readonly="checked" value="I'm Angular"/>


.. _ngRepeat:

ng-repeat
---------

Цикл перебора массива

* $index - номер текущей итерации
* $first - первая итерация
* $middle - не первая и не последняя итерация
* $last - полседняя итерация

.. code-block:: html

    <ul>
        <li ng-repeat="phone in phones">
            {{$index}}. {{phone.name}}
        </li>
    </ul>


.. _ngRequired:

ng-required
-----------


ng-selected
-----------

.. code-block:: html

    <option id="greet" ng-selected="selected">Greetings!</option>


ng-show
-------

Показывает/скрывает html элемент, в зависимости от результата выражения

.. code-block:: html

    <!-- когда $scope.myValue истина, элемент отображается -->
    <div ng-show="myValue"></div>

    <input type='checkbox' ng-model='ShowValue'>
    <div ng-show='ShowValue'>текст, который отобразится при клике по checkbox</div>


ng-src
------

.. code-block:: html

    <img ng-src="http://www.gravatar.com/avatar/{{hash}}"/>


ng-style
--------

Задает стили в зависимости от условии

.. code-block:: html

    <span ng-style="myStyle">Sample Text</span>


ng-submit
---------

Позволяет забиндить действие, которое будет выполняться при отправке данных из формы.

.. code-block:: html

    <form ng-submit="submit()" ng-controller="Ctrl">
    </form>


ng-switch
---------

.. code-block:: html

    <div ng-switch on="selection" >
        <div ng-switch-when="settings">Settings Div</div>
        <span ng-switch-when="home">Home Span</span>
        <span ng-switch-default>default</span>
    </div>


ng-transclude
-------------

Вставляет содержимое dom элемента в месте применения директивы

Используется внутри кастомных директив
для вывода контета заданого снаржу при объявлении директивы


ng-view
-------

Отображение шаблона для текущего пути.

.. code-block:: html

    <div ng-view></div>


script[type='text/ng-template']
-------------------------------

.. code-block:: html

    <script type="text/ng-template" id="/tpl.html">
        Content of the template.
    </script>


select
------

* :ref:`ngModel`
* name
* required
* :ref:`ngRequired`
* :ref:`ngOptions`

.. code-block:: js

    /* когда источник данных - массив:
     * label for value in array
     * select as label for value in array
     * label group by group for value in array
     * select as label group by group for value in array
     *
     * когда источник данных - объект:
     * label for (key , value) in object
     * select as label for (key , value) in object
     * label group by group for (key, value) in object
     * select as label group by group for (key, value) in object
     */

.. code-block:: html

    <select
        ng-model="color"
        ng-options="c.name for c in colors"></select>

    <select
        ng-model="color"
        ng-options="c.name group by c.shade for c in colors"></select>


textarea
--------

* :ref:`ngModel`

* name - имя свойства, под которым элемент управления будет доступен в области видимости

* required

* :ref:`ngRequired`

* ng-minlength

* ng-maxlength

* :ref:`ngPattern`

* :ref:`ngChange`