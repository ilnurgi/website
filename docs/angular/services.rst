Сервисы
=======

Базовые сервисы
---------------

.. js:attribute:: $window 

    ссылка на глобальный объект window
    
    
.. js:attribute:: $document

    jQuery обертка элемента window.document
    
    
.. js:attribute:: $location

    Сервис, предоставляет доступ к объекту location

    .. js:attribute:: hash()

        возвращает часть документа

    .. js:attribute:: path()
    .. js:attribute:: search()

        возвращает объект, данные гет запроса

    .. js:attribute:: url()
    
    
.. js:attribute:: $timeout(fn[, delay][, invokeApply])

    обертка для метода window.setTimeout
    
    
.. js:attribute:: $sniffer, $browser

    "приватные" сервисы для внутреннего использования
    
    
.. js:attribute:: $q

    сервис работы с асинхронными операциями (promise/deferred)
    
    
.. js:attribute:: $rootScope

    сервис получения доступа к root scope


.. js:attribute:: $http(config)

    сервис взаимодействия по протоколу HTTP (XMLHttpRequest/JSONP)

    .. js:function:: delete(url, [config])
    .. js:function:: get(url, [config])
    .. js:function:: head(url, [config])
    .. js:function:: jsonp(url, [config])
    .. js:function:: patch(url, data, [config])
    .. js:function:: post(url, data, [config])
    .. js:function:: put(url, data, [config])

        Запрос на сервер

        .. js:function:: success(callback)

            Обработчик успешного запроса

        .. code-block: js

            $http.get('phones/phones.json')
                .success(function(data, status, headers, config) {
                    $scope.phones = data;
                });
            });


.. js:attribute:: $httpBackend

    низкоуровневый аналог $http (может быть использован в тестах)


.. js:attribute:: $route

    сервис роутинга-связывания URL и контроллеров приложения


.. js:attribute:: $routeParams

    сервис доступа к параметрам из URL


.. js:attribute:: $routeProvider

    сервис настройки роутинга

    .. code-block: js

        var app = angular.module('myApp', ['ngRoute']);
        app.config([
            '$routeProvide',
            function($routeProvider){
                $routeProvide
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

        :param url: адрес роутинга
        :param templateUrl: адрес
        :param controller: адрес

    .. js:function:: otherwise({args})

        дефолтный редирект

        :param redirectTo: адрес редиректа


.. js:attribute:: $cacheFactory(cacheId[, options])

    создания создания и получения доступа к кэш-хранилищам


.. js:attribute:: $templateCache

    сервис кеширования шаблонов


.. js:attribute:: $controller(constructor, locals)

    вызов контроллера


.. js:attribute:: $anchorScroll

    автоматический скрол к конкретному элементу(до сих пор думаю зачем это было вынесено в сервис)


.. js:attribute:: $filter(name)

    создание фильтров используемых во вью


.. js:attribute:: $parse(expression)

    конвертирует Ангулар-выражение(expression) в функцию


.. js:attribute::.. $interpolate(text[, mustHaveExpression])

    перерабатывает тект содержащий выражения(для этого использует $parse)


.. js:attribute:: $compile(element, transclude, maxPriority)

    копилирует шаблон, обрабатывает директивы, связывает события. Использует $interpolate


.. js:attribute:: $exceptionHandler(exception[, cause])

    сервис эксепшенов


.. js:attribute:: $log

    логирование