Директивы
=========

Директивы являются одной из ключевых возможностей Angular.JS.
Они позволяют разработчику описать поведение отдельных элементов и расширить синтаксис HTML.
В js коде директивы принято называть camelCase'ом `ngApp`, а в шаблонах писать их через тире `ng-app`

Стандартные директивы
---------------------

.. js:attribute:: ngApp

    Главная директива приложения, задает область ангуляр приложения или создает область для модуля.
    Можно указать дополнительный атрибут, название приложения.

    1. создается инжектор(injector), который будет использоваться для dependency injection
    2. инжектор создает root scope, что является контекстом для модели нашего приложения
    3. AngularJS “компилирует” DOM начиная с ngApp.

    ::

        <body ng-app></body>

        // или

        <body ng-app='myApp'></body>

        var app = angular.module('myApp', []);


.. js:attribute:: ngBind

    Связывание компонента с объектом из скоупа

    .. code-block:: js

        Hello <span ng-bind="name"><span>


.. js:attribute:: ngChange

.. js:attribute:: ngChecked

.. js:attribute:: ngClass

    Задает новый класс элементу


.. js:attribute:: ngClassEven

    Задает новый класс каждому четному элементу


.. js:attribute:: ngClassOdd

    Задает новый класс каждому нечетному элементу


.. js:attribute:: ngClick

    Обработчик клика по элементу


.. js:attribute:: ngController

    Связывание элемента c контроллером

    .. code-block:: js

        <div ng-controller='myController'>
            {{ myValue }}
        </div>

        function myController($scope){
            /*
             * $scope - скоп контроллера, получается используя, dependence ingection
             */
            $scope.myValue = 'world';
        }
        app.controller('myController', myController)


.. js:attribute:: ngDisabled

.. js:attribute:: ngHide

    Скрывает элемент

.. js:attribute:: ngHref

.. js:attribute:: ngDblClick

    Обработчик двойного клика по элементу


.. js:attribute:: ngForm

    Связывает элементы формы


.. js:attribute:: ngInclude

    подключает отдельный файлы

.. js:attribute:: ngInit

    Директива, инициализация начальных данных

    .. code-block:: js

        <div ng-init="name='world'">
            Hello {{ name }}
        </div>


.. js:attribute:: ngMousedown

.. js:attribute:: ngMouseenter

.. js:attribute:: ngMouseleave

.. js:attribute:: ngMousemove

.. js:attribute:: ngMouseover

.. js:attribute:: ngMouseup

.. js:attribute:: ngModel

    Задает модель для связывания


.. js:attribute:: ngReadOnly

.. js:attribute:: ngRepeat

    Цикл перебора массива

    .. code-block: js

        <ul>
            <li ng-repeat="phone in phones">
                {{phone.name}}
            </li>
        </ul>


.. js:attribute:: ngSelected

.. js:attribute:: ngShow

    Показывает/скрывает html элемент, в зависимости от результата выражения

    .. code-block: js

        /*
         * когда $scope.myValue истина, элемент отображается
         */
        <div ng-show="myValue"></div>

    .. code-block:: js

        <input type='checkbox' ng-model='ShowValue'>
        <div ng-show='ShowValue'>текст, который отобразится при клике по checkbox</div>


.. js:attribute:: ngSrc

.. js:attribute:: ngStyle

.. js:attribute:: ngSubmit

    Позволяет забиндить действие, которое будет выполняться при отправке данных из формы.


.. js:attribute:: ngTransclude

    используется внутри кастомных директив для вывода контета заданого снаржу при объявлении директивы



Как написать свою директиву
---------------------------

.. code-block:: js

    // простая директива
    angular.module('transclude', [])
        .directive(
            'pane',
            function(){
                return function(){
                    ...
                }
            }
        );

    // директива с настройками
    angular.module('transclude', [])
        .directive(
            'pane',
            function(){
                return {
                    restrict: 'E',
                    transclude: true,
                    scope: {
                        title:'@'
                    },
                    template: '<div style="border: 1px solid black;">' +
                              '<div style="background-color: gray">{{title}}</div>' +
                              '<div ng-transclude></div>' +
                              '</div>'
                };
            };
        });
        
        
Описание параметров директив

* `priority` - приоретива выполения(для случая когда на одном элементе несколько директив) `1`
* `template` - шаблон HTML `<div ng-click=”doSomething()”></div>`
* `templateUrl` - ссылка на файл шаблона `./views/alert.html`
* `replace` - если `true` – то шаблон диретивы заменит элемент, `false` – произойдет append
* `transclude` - компилирует контект элемента и делает возможные его вставку внутрь шаблона (по средством ngTransclude )
* `restrict` - задает способ встраивания(смотри выше):
    * `E` - тэг(имя элемента)
    * `A` - атрибут
    * `C` - класс
    * `M` - комментарий
* `scope` - Определяет способ переда scope в директиву
    В зависимости от типа переданного параметра видет себя по разному:

    * `true` – создается новый scope конкретно для этой директивы
    * `{}` - задается конкретный изолированный scope – т.е. scope не унаследованный от родительского
        Может влючать в себе ссылки на элементы родительского scope при использоварнии нетривиального синтаксиса
        (специальный префикс символ (@, =, & )перед имеем метода/переменой):
        * `@` – переменную локального scope со значением DOM аттрибута
        * `=` – двустороннее связывание значения атрибута и переменной
        * `&` – позволяет выполнять выражения из аттрибута в рамках родительского scope
    * `false` - используется scope ближайшего контроллера (default)
* `controller` - метод (либо ссылка на метод) где описано поведение(логика) `dialogDirectiveController`
    Необходима в случае, когда логика директивы выходит за пределы одного метода и нам уже необходимма группа методов.
    Такую группу методов мы можем объединить в функцию-контроллер.
    Это будет специальный тип контроллера "связанный с директивой",
    которые должен взаимодействать только с данной директивой.
* `compile` - метод(либо ссылка на метод) с инструкциями по компиляции шаблона `function(tElement, tAttrs, transclude){ … }`
    Функция компиляции compile (используется довольно редко)  трансформирует HTML шаблон.
* `link` - основной параметр фаблири – метод(либо ссылка на метод) по связыванию директивы с приложением `function(scope, iElement, iAttrs){ … }`
    После компиляции функция линковки link регистрирует обработчики событий на DOM обновленного HTML.