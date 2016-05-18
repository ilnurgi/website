Promise - асинхронная операция
==============================

.. note:: EcmaScript6

.. js:class:: Promise()

    Асинхронная операция.

    Состояния операции:

    * fulfilled - выполнено - вызвана функция `resolve` с аргументом, не являющимся объектом :js:class:`Promise` или без аргументов

    * rejected - отклонено - вызвана функция `reject` или возникло исключение внутри исполнителя

    * pending - ожидание - `resolve` или `reject` не вызваны

    * settled - завершено - выполнена или отклонена и не находится в режиме ожидания

    .. code-block:: js

        var promise = new Promise(
            function(resolve, reject){
                var request = new XMLHttpRequest();
                request.open("GET", "data.json");
                request.addEventListener("load", function(){
                    if (request.status === 200){
                        resolve(request.responseText);
                    } else {
                        reject(request.status);
                    }
                }, false);
                request.addEventListener("error", function(){
                    reject("Error");
                }, false);
                request.send();
            }
        );


    .. js:function:: all(iterable)

        Возвращает объект Promiseб когда все объекты в итерируемом объекте будут выполнены.

        Если один из объектов будет отклонен, он немедленно вернется.

        .. code-block:: js

            var p1 = new Promise(...);
            var p2 = new Promise(...);
            Promise.all([p1, p2]).then(...);


    .. js:function:: catch(onRejected)    

        Используется для обработки ошибок и исключений

        .. code-block:: js

            promise.catch(function(reason){
                ...
            });


    .. js:function:: race(iterable)

        Возвращает объект Promise сразу, как только один из объектов будет выполнен или отклонен

        
    .. js:function:: reject(value)

        Преобразует значение в отклоненный объект Promise.

        .. code-block:: js

            var p1 = Promise.reject(5);
            p1.then(null, function(value){
                console.log(value);
            });
            // 5


    .. js:function:: resolve(value)

        Преобразует значение в возвращаемый объект Promise.

        .. code-block:: js

            var p1 = Promise.resolve(5);
            p1.then(function(value){
                console.log(value);
            });
            // 5


    .. js:function:: then(onFulfilled, onRejected)

        Позволяет выполнить некоторые действия после того, как асинхронная операция будет выполнена или отклонена.

        .. code-block:: js

            promise.then(
                function(value){
                    ...
                },
                function(reason){
                    ...
                });