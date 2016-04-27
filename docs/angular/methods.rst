Стандартные методы модуля
=========================

Вспомогательные методы
----------------------


.. js:function:: angular.bind(self, fn, args)

    карринг для функции fn


.. js:function:: angular.bootstrap(element[, modules])

    используется для старта фреймфорка вручную


.. js:function:: angular.callbacks

    объект-коллекция колбэков для JSONP


.. js:function:: angular.copy(source, destination)

    полное копирование(deep copy) объекта


.. js:function:: angular.element(selector)

    Селектор из jQuery


.. js:function:: angular.equals(o1, o2)

    сравнение значений/объектов


.. js:function:: angular.extend(dst, src[,src2[,src3...]])

    расширение объекта


.. js:function:: angular.forEach(array, callback, [context])

    Цикл по массиву

    :param array array: массив
    :param callback: обработчик

   .. code-block:: js

        angular.forEach(['1', '2'], function(item){
            console.log(item);
        })

        // 1
        // 2


.. js:function:: angular.fromJson

    конвертация из JSON


.. js:function:: angular.identity(value)

    создает функцию, которая вернет значение(используется как обертка для мест, где нужно передавать строго функцию)


.. js:function:: angular.injector(modules)

    создает функцию-инжектор, которая может быть использована для получения сервисов


.. js:function:: angular.isUndefined, isDefined, isString, isFunction, isObject, isNumber, isElement, isArray, isDate

    методы проверки принадлежности типу


.. js:function:: angular.lowercase

    перевод в нижний регистр


.. js:function:: angular.noop()

    функция “пустышка”, которую можно использовать как заглушку для колбэков


.. js:function:: angular.toJson

    конвертация в JSON


.. js:function:: angular.uppercase

    перевод в верхний регистр


.. js:function:: angular.version

    версия продукта


Методы работы с модулем приложений
----------------------------------


.. js:function:: angular.module(name, requires)

    Объявляет модуль в приложений и возвращает его экземпляр

    :param str name: название модуля
    :param array requires: список зависимостей

    .. code-block:: jjs

        var app = angular.module('muModule', [])


.. js:function:: app.controller(name, callback)

    Объявляет контроллер в модуле

    :param str name: название модуля
    :param callback: обработчик

    .. code-block:: js

        app.controller(
            'myController',
            function(){
                ...
            }
        )


.. js:function:: app.constant(key, value)

    Объявляет константу модуля

    .. code-block:: js

        app.constant('CONST', 123);


.. js:function:: app.config(function)

    Конфигурирует модуль

    .. code-block:: js

        app.config(function($routeProvider){
            $routeProvider
                .otherwise({redirectTo: '/'})
        });


.. js:function:: app.directive(name, callback)

    Объявляет директиву в модуле

    :param str name: название
    :param callback: обработчик

    .. code-block:: js

        app.directive(
            'myController',
            function(){
                restrict: 'A'
            }
        )

.. js:function:: app.run()

    .. code-block:: js

        angular
        .module('app', [])
        .run(function($rootScope){
            // эта штука иногда перехвататывает ошибки,
            // которые не отображаются в консоли
            $rootScope.$on('$stateChangeError', function(){
                throw arguments[5];
            });
            ...
        });


.. js:function:: app.value(key, value)

    Объявляет переменную в модуле