Стандартные методы модуля
=========================


bind
----

.. js:function:: angular.bind(self, fn, args)

    карринг для функции fn


bootstrap
---------

.. js:function:: angular.bootstrap(element[, modules])

    Ручная инициализация фреймворка

    .. code-block:: js

        angular.element(document).ready(function() {
            angular.bootstrap(document);
        });


callbacks
---------

.. js:function:: angular.callbacks

    объект-коллекция колбэков для JSONP


copy
----

.. js:function:: angular.copy(source, destination)

    полное копирование(deep copy) объекта


element
-------

.. js:function:: angular.element(selector)

    Селектор из jQuery


equals
------

.. js:function:: angular.equals(o1, o2)

    сравнение значений/объектов


extend
------

.. js:function:: angular.extend(dst, src[,src2[,src3...]])

    расширение объекта


forEach
-------

.. js:function:: angular.forEach(array, callback, [context])

    Цикл по массиву

   .. code-block:: js

        angular.forEach(['1', '2'], function(item){
            console.log(item);
        })

        // 1
        // 2


fromJson
--------

.. js:function:: angular.fromJson

    конвертация из JSON


identity
--------

.. js:function:: angular.identity(value)

    создает функцию, которая вернет значение(используется как обертка для мест, где нужно передавать строго функцию)


injector
--------

.. js:function:: angular.injector(modules)

    создает функцию-инжектор, которая может быть использована для получения сервисов


isArray
-------

.. js:function:: angular.isArray


isDate
------

.. js:function:: angular.isDate


isDefined
---------

.. js:function:: angular.isDefined


isElement
---------

.. js:function:: angular.isElement


isFunction
----------

.. js:function:: angular.isFunction


isNumber
--------

.. js:function:: angular.isNumber


isObject
--------

.. js:function:: angular.isObject


isString
--------

.. js:function:: angular.isString


isUndefined
-----------

.. js:function:: angular.isUndefined


lowercase
---------

.. js:function:: angular.lowercase

    перевод в нижний регистр


module
------

.. js:function:: angular.module(name, requires)

    Объявляет модуль в приложений и возвращает его экземпляр

    .. code-block:: jjs

        var app = angular.module('myModule', [])


noop
----

.. js:function:: angular.noop()

    функция “пустышка”, которую можно использовать как заглушку для колбэков


toJson
------

.. js:function:: angular.toJson

    конвертация в JSON


uppercase
---------

.. js:function:: angular.uppercase

    перевод в верхний регистр


version
-------

.. js:function:: angular.version

    версия продукта