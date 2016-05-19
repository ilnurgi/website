Стандартные сервисы
===================


anchorScroll
------------

.. js:function:: $anchorScroll()

    Автоматический скрол к конкретному элементу

    .. code-block:: js

        $anchorScroll();


browser
-------

.. js:attribute:: $browser


cacheFactory
------------

.. js:function:: $cacheFactory(cacheId[, options])

    Фабрика, которая создает объект кеша и возвращает его.

    Кеш обладает следующими свойствами и методами

    * info() - возвращает идентификатор, размер и настройки для кэша.
    * put(key, value) - добавляет новую пару ключ-значение в кэш.
    * get(key) - возвращает кэшированное значение для ключа или undefined если значения нет.
    * remove(key) - удаляет пару ключ-значение из кэша.
    * removeAll() - полностью очищает кэш, удаляя все пары ключ-значение.
    * destroy() - удаляет ссылку на кэш из $cacheFactory.

compile
-------

.. js:attribute:: $compile(element, transclude, maxPriority)

    Компилирует шаблон, обрабатывает директивы, связывает события.
    Использует $interpolate


controller
----------

.. js:attribute:: $controller(constructor, locals)

    Создает и возвращает контроллер


document
--------

.. js:attribute:: $document

    jQuery обертка элемента window.document


exceptionHandler
----------------

.. js:attribute:: $exceptionHandler(exception[, cause])

    Любое не перехваченное исключение в angular выражениях обрабатывается этим сервисом


filter
------

.. js:attribute:: $filter(name)

    Создает и возвращает фильтр


http
----

.. js:attribute:: $http(config)

    сервис взаимодействия по протоколу HTTP (XMLHttpRequest/JSONP)

    .. code-block:: js

        $http({
            method: $scope.method,
            url: $scope.url,
            cache: $templateCache}
        ).success(
            function(data, status) {
                $scope.status = status;
                $scope.data = data;
            }
        ).error(
            function(data, status) {
                $scope.data = data || "Request failed";
                $scope.status = status;
        });

    .. js:function:: delete(url, [config])
    .. js:function:: get(url, [config])
    .. js:function:: head(url, [config])
    .. js:function:: jsonp(url, [config])
    .. js:function:: patch(url, data, [config])
    .. js:function:: post(url, data, [config])
    .. js:function:: put(url, data, [config])
    .. js:function:: success(callback)

        Обработчик успешного запроса

        .. code-block:: js

            $http.get('phones/phones.json')
                .success(function(data, status, headers, config) {
                    $scope.phones = data;
                });
            });


httpBackend
-----------

.. js:attribute:: $httpBackend

    низкоуровневый аналог $http (может быть использован в тестах)


interpolate
-----------

.. js:attribute:: $interpolate(text[, mustHaveExpression])

    перерабатывает тект содержащий выражения(для этого использует $parse)


locale
------

.. js:function:: locale()


location
--------

.. js:attribute:: $location

    Сервис, предоставляет доступ к объекту location

    .. js:function:: absUrl()

    .. js:function:: hash([hash])

    .. js:function:: host()

    .. js:function:: path([path])

    .. js:function:: port()

    .. js:function:: protocol()

    .. js:function:: replace()

    .. js:function:: search([search, [paramValue]])

    .. js:attribute:: url([url])


log
---

.. js:attribute:: $log

    логирование

    .. js:function:: error()
    .. js:function:: info()
    .. js:function:: log()
    .. js:function:: warn()


parse
-----

.. js:attribute:: $parse(expression)

    конвертирует Ангулар-выражение(expression) в функцию


q
-

.. js:attribute:: $q

    сервис работы с асинхронными операциями (promise/deferred)


rootElement
-----------

Корневой элемент приложения

rootScope
---------

.. js:attribute:: $rootScope

    сервис получения доступа к root scope


route
-----

.. js:attribute:: $route

    сервис роутинга-связывания URL и контроллеров приложения


routeParams
-----------

.. js:attribute:: $routeParams

    сервис доступа к параметрам из URL


routeProvider
-------------

.. js:attribute:: $routeProvider

    сервис настройки роутинга

    .. code-block:: js

        var app = angular.module('myApp', ['ngRoute']);
        app.config([
            '$routeProvide',
            function($routeProvider){
                $routeProvider
                    .when('/', {
                        'templateUrl': 'url',
                        'controller': 'ctrl'
                    })
                    .when('/phones/phoneId', {
                        ...
                    })
            }
        ])

    .. js:function:: when(url, {args})

        роутниг по урлу

        * url - адрес роутинга
        * templateUrl - адрес
        * controller - адрес

    .. js:function:: otherwise({args})

        дефолтный редирект

        * redirectTo - адрес редиректа


sniffer
-------

.. js:attribute:: $sniffer


templateCache
-------------

.. js:attribute:: $templateCache

    сервис кеширования шаблонов


timeout
-------

.. js:attribute:: $timeout(fn[, delay][, invokeApply])

    обертка для метода window.setTimeout


window
------

.. js:attribute:: $window 

    ссылка на глобальный объект window