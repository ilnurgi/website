Reflect - исследование и обаботка свойств объектов
==================================================

.. note:: EcmaScript6

.. js:class:: Reflect()

    .. js:function:: apply(function, this, args)

        Вызов функции с заданным контекстом.

        Аналогичен методу apply :js:class:`Function`

        .. code-block:: js

            function s(a, b){
                return this.value + a + b;
            }
            Reflect.apply(s, {value: 100}, [10, 30]);
            // 140


    .. js:function:: construct(constructor, args, prototype)

        Вызов функции в качестве конструктора

        Аналогичен оператору :ref:`new`, отличается:

            * передача в свойстве `prototype`

        .. code-block:: js

            function const1(a, b){};
            function const2(){};
            var newObj = Reflect.construct(const1, [1, 2], const2);


    .. js:function:: defineProperty(object, property, descriptor)

        Опеределяет новое или изменяет существующее свойство объекта. Возвращает логическое значение, была ли операция успешной.

        Аналогичен методу defineProperty :js:class:`Object`, отличается:

            * возвращает логическое значение, а не модифицированный объект

        .. code-block:: js

            // создание свойств данных
            var obj = {};
            Reflect.defineProperty(obj, 'name', {
                // значение свойства
                value: 'Ilnurgi',
                // значение может быть изменено
                writable: true,
                // атриубты свойства могут быть изменены и свойство может быть удалено
                configurable: true,
                // свойство может быть использовано в цикле for ... in
                enumerable: true
            })

            // создание свойства со средствами доступа
            var obj = {
                __name__: 'ilnurgi'
            }
            Reflect.defineProperty(obj, 'name', {
                get: function(){
                    return this.__name__;
                },
                set: function(value){
                    this.__name__ = value;
                },
                // свойства дескриптора могут быть изменены и свойство может быть удалено
                configurable: true,
                // свойство может быть использовано в цикле for ... in
                enumerable: true
            })


    .. js:function:: deleteProperty(object, property)

        Удаление свойства объекта.

        Аналогичен :ref:`delete`

        .. code-block:: js

            Reflect.deleteProperty(obj, 'name');


    .. js:function:: enumerate(object)

        Возвращает итератор, перечисляемые свойства объекта.

        Аналогичен циклу for ... in

        .. code-block:: js

            var iter = Reflect.enumerate(obj);
            iter.next().value;


    .. js:function:: get(object, property, this)

        Возвращает значение свойства объекта


    .. js:function:: getOwnPropertyDescriptor(object, property)

        Возвращает дескриптор свойства объекта

        Аналогичен getOwnPropertyDescriptor :js:class:`Object`

        .. code-block:: js

            var descriptor = Reflect.getOwnPropertyDescriptor(obj, 'name');


    .. js:function:: getPrototypeOf(object)

        Извлекает прототип объекта

        Аналогичен getPrototypeOf :js:class:`Object`

        .. code-block:: js

            var obj2 = Reflect.getPrototypeOf(obj1);


    .. js:function:: has(object, property)

        Используется для проверки существования свойства в объекте.

        Аналогичен оператору :ref:`in`

        .. code-block:: js

            Reflect.has(obj, 'name');


    .. js:function:: isExtensible(object)

        Проверяет возможность расширения объекта, возможность добавления новых свойств в объект

        Аналогичен isExtensible :js:class:`Object`

        .. code-block:: js

            Reflect.isExtensible(obj);


    .. js:function:: ownKeys(object)

        Возвращает массив ключей свойств объекта, игнорируя наследуемые свойства.

        .. code-block:: js

            Reflect.ownKeys(obj);
            

    .. js:function:: preventExtensions(object)

        Позволяет отметить объект как нерасширяемый, возвращает логическое значение, успешность операции.

        Аналогичен preventExtensions :js:class:`Object`

        .. code-block:: js

            Reflect.preventExtensions(obj);


    .. js:function:: set(object, property, value, this)

        Задает значение свойства объекта


    .. js:function:: setPrototypeOf(object, prototype)

        Установка значения прототипа

        .. code-block:: js

            Reflect.setPrototypeOf(obj, {
                name: 'ilnurgi'
            })
