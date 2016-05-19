Методы модулей
==============

.. code-block:: js

    var app = angular.module('myModule', []);


config
------

.. js:function:: app.config(function)

    Конфигурирует модуль

    .. code-block:: js

        app.config(function($routeProvider){
            $routeProvider
                .otherwise({redirectTo: '/'})
        });


constant
--------

.. js:function:: app.constant(key, value)

    Объявляет константу модуля

    .. code-block:: js

        app.constant('CONST', 123);



controller
----------

.. js:function:: app.controller(name, constructor)

    Объявляет контроллер в модуле

    .. code-block:: js

        app.controller(
            'myController',
            function(){
                ...
            }
        )


directive
---------

.. js:function:: app.directive(name, constructor)

    Объявляет директиву в модуле.

    Обработчик может вернуть объект со следующими свойствами, или просто какойто обработчик

        * `compile` - метод(либо ссылка на метод) с инструкциями по компиляции шаблона

            Функция компиляции compile (используется довольно редко) трансформирует HTML шаблон.

            Функция принимает следующие аргументы:

                * шаблон элемента

                * шаблон атрибутов

                * связывающая функция

            Функция может возвращать функцию или объект.

        * `controller` - метод (либо ссылка на метод) где описано поведение(логика)

            Необходима в случае, когда логика директивы выходит за пределы одного метода и нам уже необходимма группа методов.

            Такую группу методов мы можем объединить в функцию-контроллер.

            Это будет специальный тип контроллера "связанный с директивой",
            которые должен взаимодействать только с данной директивой.

        * `link` - основной параметр фабрики – метод(либо ссылка на метод) по связыванию директивы с приложением

            После компиляции функция линковки link регистрирует обработчики событий на DOM обновленного HTML.

            метод принимает следующие атрибуты:

            * scope

            * element

            * attrs

            * ctrl

            * transclude - функция для трансклуда

                .. code-block:: js

                    transclude(scope, function(clone, scope){
                        // scope - скоуп клинируемого элемента
                        // если не хочется использовать transclude: true,
                        element.append(clone);
                    });

        * `name` – имя текущей области видимости (scope).

            Не обязательный и по умолчанию это имя заданное при регистрации директивы.

        * `priority` - приоритет выполнения, для случая когда на одном элементе несколько директив

        * `replace`

            * `true` – шаблон директивы заменит элемент

            * `false` – произойдет append

        * `restrict` - задает способ встраивания

            * `E` - тэг(имя элемента)

            * `A` - атрибут

            * `C` - класс

            * `M` - комментарий

        * `require` - требовать от других контроллеров передавать в текущую директиву связывающую функцию.

        * `scope` - Определяет способ передачи scope в директиву

            В зависимости от типа переданного параметра ведёт себя по разному:

            * `true` – создается новый scope конкретно для этой директивы

            * `{}` - задается конкретный изолированный scope – т.е. scope не унаследованный от родительского

                Может влючать в себе ссылки на элементы родительского scope при использоварнии нетривиального синтаксиса
                (специальный префикс символ (@, =, & ) перед имеем метода/переменой)

                * `@` или `@attr` – связывает переменную локального scope со значением DOM аттрибута

                * `=` или `=attr` – двустороннее связывание значения атрибута и переменной

                * `&` или `&attr`– позволяет выполнять выражения из аттрибута в рамках родительского scope

            * `false` - используется scope ближайшего контроллера (default)

        * `template` - шаблон HTML

        * `templateUrl` - ссылка на файл шаблона

        * `terminal`

            * true - текущий приоритет будет установлен на последующие директивы

        * `transclude` - компилирует контент элемента и делает возможные его вставку внутрь шаблона (по средством ngTransclude )

            * `true` - не потерять содержимое директивы

            * `'element'`

    .. code-block:: js

        // простая директива
        app.directive(
            'pane',
            function(){
                return function(){
                    ...
                }
            }
        );

        // директива с настройками
        app.directive(
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

                    }
                };
            };
        });


factory
-------

.. js:function:: app.factory(name, providerFunction)

    Фабрика

    .. code-block:: js

        app.factory(
            'some_factory',
            function(){
                return {
                    some_var: 'some_var_description'
                }
            });

filter
------

.. js:function:: app.filter(name, constructor)

    .. code-block:: js

        app.filter(
            'first_filter',
            function(){
                return function(value){
                    return '2,' + value;
                };
        })


name
----

.. js:attribute:: name

    Имя модуля


provider
--------

.. js:function:: app.provider(name, constructor)


run
---

.. js:function:: app.run()

    .. code-block:: js

        app.run(function($rootScope){
            // эта штука иногда перехвататывает ошибки,
            // которые не отображаются в консоли
            $rootScope.$on('$stateChangeError', function(){
                throw arguments[5];
            });
            ...
        });


requires
--------

.. js:attribute:: requires

    Зависимости модуля


service
-------

.. js:function:: service(name, constructor)


value
-----

.. js:function:: app.value(key, value)

    Объявляет переменную в модуле