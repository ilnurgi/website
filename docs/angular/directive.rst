Директивы
=========

Директивы являются одной из ключевых возможностей Angular.JS.

Они позволяют разработчику описать поведение отдельных элементов и расширить синтаксис HTML.

В js коде директивы принято называть camelCase-ом `ngApp`, а в шаблонах писать их через тире `ng-app`

Стандартные директивы
---------------------

.. js:attribute:: ng-app

    Главная директива приложения, задает область ангуляр приложения или создает область для модуля.
    
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


.. js:attribute:: ng-bind

    Связывание компонента с объектом из скоупа

    .. code-block:: html

        Hello <span ng-bind="name"><span>


.. js:attribute:: ng-change

.. js:attribute:: ng-checked

.. js:attribute:: ng-class

    Задает новый класс элементу

    .. code-block:: html

        <li ng-class="{'actie':(currPath == 'main')}"></li>


.. js:attribute:: ng-class-even

    Задает новый класс каждому четному элементу


.. js:attribute:: ng-class-odd

    Задает новый класс каждому нечетному элементу


.. js:attribute:: ng-click

    Обработчик клика по элементу


.. js:attribute:: ng-controller

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


.. js:attribute:: ng-disabled

.. js:attribute:: ng-hide

    Скрывает элемент

.. js:attribute:: ng-href

.. js:attribute:: ng-dbl-click

    Обработчик двойного клика по элементу


.. js:attribute:: ng-form

    Связывает элементы формы


.. js:attribute:: ng-include

    подключает отдельный файлы

    .. code-block:: html

        <div ng-include='/index.html'></div>


.. js:attribute:: nginit

    Директива, инициализация начальных данных

    .. code-block:: html

        <div ng-init="name='world'">
            Hello {{ name }}
        </div>


.. js:attribute:: ng-mousedown

.. js:attribute:: ng-mouseenter

.. js:attribute:: ng-mouseleave

.. js:attribute:: ng-mousemove

.. js:attribute:: ng-mouseover

.. js:attribute:: ng-mouseup

.. js:attribute:: ng-model

    Задает модель для связывания


.. js:attribute:: ng-read-only

.. js:attribute:: ng-repeat

    Цикл перебора массива

    .. code-block: html

        <ul>
            <li ng-repeat="phone in phones">
                {{phone.name}}
            </li>
        </ul>


.. js:attribute:: ng-selected

.. js:attribute:: ng-show

    Показывает/скрывает html элемент, в зависимости от результата выражения

    .. code-block:: html

        <!-- когда $scope.myValue истина, элемент отображается -->
        <div ng-show="myValue"></div>

        <input type='checkbox' ng-model='ShowValue'>
        <div ng-show='ShowValue'>текст, который отобразится при клике по checkbox</div>


.. js:attribute:: ng-src

.. js:attribute:: ng-style

.. js:attribute:: ng-submit

    Позволяет забиндить действие, которое будет выполняться при отправке данных из формы.


.. js:attribute:: ng-transclude

    используется внутри кастомных директив для вывода контета заданого снаржу при объявлении директивы



Как написать свою директиву
---------------------------

.. code-block:: js

    // простая директива
    angular.module('app', [])
        .directive(
            'pane',
            function(){
                return function(){
                    ...
                }
            }
        );

    // директива с настройками
    angular.module('app', [])
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
                              '</div>',
                    link: function(scope, element, attrs, ctrl, transclude){
                        /*
                         * scope -
                         * elemnt - 
                         * attrs -
                         * ctrl -
                         * transclude - функция для трансклуда
                           transclude(scope, function(clone, scope){
                                // scope - скоуп клинируемого элемента
                                // если не хочется использовать transclude: true,
                                element.append(clone);
                            });
                         */
                    }
                };
            };
        });
        
        
Описание параметров директив

* `priority` - приоретива выполения(для случая когда на одном элементе несколько директив)

* `replace` - если `true` – то шаблон директивы заменит элемент, `false` – произойдет append

* `restrict` - задает способ встраивания

    * `E` - тэг(имя элемента)

    * `A` - атрибут

    * `C` - класс

    * `M` - комментарий

* `scope` - Определяет способ передачи scope в директиву

    В зависимости от типа переданного параметра ведёт себя по разному:

    * `true` – создается новый scope конкретно для этой директивы

    * `{}` - задается конкретный изолированный scope – т.е. scope не унаследованный от родительского

        Может влючать в себе ссылки на элементы родительского scope при использоварнии нетривиального синтаксиса
        (специальный префикс символ (@, =, & ) перед имеем метода/переменой)

        * `@` – переменную локального scope со значением DOM аттрибута

        * `=` – двустороннее связывание значения атрибута и переменной

        * `&` – позволяет выполнять выражения из аттрибута в рамках родительского scope

    * `false` - используется scope ближайшего контроллера (default)

* `template` - шаблон HTML

* `templateUrl` - ссылка на файл шаблона

* `transclude` - компилирует контент элемента и делает возможные его вставку внутрь шаблона (по средством ngTransclude )
    
    * `true` - не потерять содержимое директивы

    * `'element'`

* `controller` - метод (либо ссылка на метод) где описано поведение(логика) `dialogDirectiveController`
    
    Необходима в случае, когда логика директивы выходит за пределы одного метода и нам уже необходимма группа методов.
    
    Такую группу методов мы можем объединить в функцию-контроллер.
    
    Это будет специальный тип контроллера "связанный с директивой",
    которые должен взаимодействать только с данной директивой.

* `compile` - метод(либо ссылка на метод) с инструкциями по компиляции шаблона

    Функция компиляции compile (используется довольно редко)  трансформирует HTML шаблон.

* `link` - основной параметр фабрики – метод(либо ссылка на метод) по связыванию директивы с приложением

    После компиляции функция линковки link регистрирует обработчики событий на DOM обновленного HTML.