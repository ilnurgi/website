Object - объект
===============


.. js:class:: Object()

    Объект, является прототипом для всех объектов языка

    .. code-block:: js

        var obj = {};
        var obj2 = new Object();

        var person = {
            'name': 'Alex',
            'age': 25
        };

        person.name;
        // 'Alex'

        person['name'];
        // 'Alex'

        delete person.age;

        // создание дочерних объектов
        var Megaperson = Object.create(person);


    .. js:attribute:: constructor

        Ссылка на конструктор

        .. code-block:: js

            a = new Array(1,2,3);  
            a.constructor == Array;
            // true


    .. js:function:: hasOwnProperty(name)

        Определяет, обладает ли объект свойством. 

        .. code-block::

            var o = new Object();         // Соз­дать объ­ект
            o.x = 3.14;                   // Оп­ре­де­лить не­унас­ле­до­ван­ное свой­ст­во
            o.hasOwnProperty("x");        // Вер­нет true: x – это ло­каль­ное свой­ст­во o
            o.hasOwnProperty("y");        // Вер­нет false: o не име­ет свой­ст­ва y
            o.hasOwnProperty("toString"); // Вер­нет false: свой­ст­во toString унас­ле­до­ва­но

    .. js:function:: isPrototypeOf(obj)

        Яв­ля­ет­ся ли дан­ный объ­ект про­то­ти­пом для ука­зан­но­го объ­ек­та

        .. code-block:: js

            var o = new Object();                         // Соз­дать объ­ект
            Object.prototype.isPrototypeOf(o)             // true: o – объ­ект
            Function.prototype.isPrototypeOf(o.toString); // true: toString – функ­ция
            Array.prototype.isPrototypeOf([1,2,3]);       // true: [1,2,3] – мас­сив
            // Ту же про­вер­ку мож­но вы­пол­нить дру­гим спо­со­бом
            (o.constructor == Object); // true: o соз­дан с по­мо­щью кон­ст­рук­то­ра Object()
            (o.toString.constructor == Function);         // true: o.toString – функ­ция
            // Объ­ек­ты-про­то­ти­пы са­ми име­ют про­то­ти­пы. Сле­дую­щий вы­зов вер­нетtrue, по­ка­зы­вая, что
            // объ­ек­ты-функ­ции на­сле­ду­ют свой­ст­ва от Function.prototype, а так­же от Object.prototype.
            Object.prototype.isPrototypeOf(Function.prototype);


    .. js:function:: propertyIsEnumerable(var)

        Су­ще­ст­ву­ет ли свой­ст­во с ука­зан­ным име­нем и бу­дет ли оно пе­ре­чис­ле­но цик­лом for/in

        .. code-block:: js

            var o = new Object();               // Соз­дать объ­ект
            o.x = 3.14;                         // Оп­ре­де­лить свой­ст­во
            o.propertyIsEnumerable("x");        // true: x - ло­каль­ное и пе­ре­чис­ли­мое
            o.propertyIsEnumerable("y");        // false: o не име­ет свой­ст­ва y
            o.propertyIsEnumerable("toString"); // false: toString унас­ле­до­ван­ное свой­ст­во
            Object.prototype.propertyIsEnumerable("toString"); // false: не­пе­ре­чис­ли­мое

    .. js:function:: toLocaleString()

        Локализованное строчное представление объекта


    .. js:function:: toString()

        Возвращает строковое представление объекта


    .. js:function:: valueOf()

        Возвращает значение объекта

Методы, доступные только в объекте Object
-----------------------------------------

.. js:function:: create(prototype[, descriptors]) 

    Соз­да­ет но­вый объ­ект с ука­зан­ным про­то­ти­пом и свой­ст­ва­ми.

    .. versionadded:: ECMAScript5

    .. code-block:: js

        // Соз­дать объ­ект, ко­то­рый име­ет соб­ст­вен­ные свой­ст­ва x и y и на­сле­ду­ет свой­ст­во z
        var p = Object.create({z:0}, {
            x: { 
                value: 1, 
                writable: false, 
                enumerable:true, 
                configurable: true
            },
            y: { 
                value: 2, 
                writable: false, 
                enumerable:true, 
                configurable: true
            },
        });


.. js:function:: defineProperties(obj, descriptors) 

    Соз­да­ет или на­страи­ва­ет од­но или бо­лее свойств в ука­зан­ном объ­ек­те.

    .. versionadded:: ECMAScript5

    .. code-block:: js

        // До­ба­вить в но­вый объ­ект свой­ст­ва
        var p = Object.defineProperties({},
            x: { 
                value: 0, 
                writable: false, 
                enumerable:true, 
                configurable: true
            },
            y: { 
                value: 1, 
                writable: false, 
                enumerable:true, 
                configurable: true
            },
        });


.. js:function:: defineProperty(obj, name, value) 

    Соз­да­ет или на­страи­ва­ет свой­ст­во в ука­зан­ном объ­ек­те.

    .. versionadded:: ECMAScript5

    .. code-block:: js

        Object.defineProperty({}, 'n', { 
            value: v, 
            writable: false,
            enumerable: true, 
            configurable:false
        });


.. js:function:: freeze(obj) 

    Де­ла­ет ука­зан­ный объ­ект не­из­ме­няе­мым.

    .. versionadded:: ECMAScript5


.. js:function:: getOwnPropertyDescriptor(obj, name) 

    Воз­вра­ща­ет ат­ри­бу­ты ука­зан­но­го свой­ст­ва в ука­зан­ном объ­ек­те.

    .. versionadded:: ECMAScript5


.. js:function:: getOwnPropertyNames(obj, name) 

    Воз­вра­ща­ет мас­сив имен всех не­унас­ле­до­ван­ных свойств в  ука­зан­ном объ­ек­те, вклю­чая свой­ст­ва, не ­пе­ре­чис­ляе­мые цик­лом for/in.

    .. versionadded:: ECMAScript5

    
.. js:function:: getPrototypeOf(obj) 

    Воз­вра­ща­ет про­то­тип ука­зан­но­го объ­ек­та.

    .. versionadded:: ECMAScript5

    .. code-block:: js

        var p = {};              // Обыч­ный объ­ект
        Object.getPrototypeOf(p) // => Object.prototype
        var o = Object.create(p) // Объ­ект, на­сле­дую­щий объ­ект p
        Object.getPrototypeOf(o) // => p


.. js:function:: isExtensible(obj) 

    Оп­ре­де­ля­ет, мо­гут ли до­бав­лять­ся но­вые свой­ст­ва в ука­зан­ный объ­ект.

    .. versionadded:: ECMAScript5

    .. code-block:: js

        var o = {};                  // Соз­дать но­вый объ­ект
        Object.isExtensible(o)       // => true: он яв­ля­ет­ся рас­ши­ряе­мым
        Object.preventExtensions(o); // Сде­лать не­рас­ши­ряе­мым
        Object.isExtensible(o)       // => false: те­перь он не­рас­ши­ряе­мый


.. js:function:: isFrozen(obj) 

    Оп­ре­де­ля­ет, яв­ля­ет­ся ли ука­зан­ный объ­ект фик­си­ро­ван­ным.

    .. versionadded:: ECMAScript5


.. js:function:: isSealed(obj) 

    Оп­ре­де­ля­ет, яв­ля­ет­ся ли ука­зан­ный объ­ект не­рас­ши­ряе­мым, а его свой­ст­ва не­дос­туп­ны­ми для на­строй­ки.

    .. versionadded:: ECMAScript5


.. js:function:: keys(obj) 

    Воз­вра­ща­ет мас­сив имен не­унас­ле­до­ван­ных пе­ре­чис­ли­мых свойств в ука­зан­ном объ­ек­те.

    .. versionadded:: ECMAScript5

    .. code-block:: js

        Object.keys({x:1, y:2}) // => ["x", "y"]

    
.. js:function:: preventExtensions(obj) 

    Пре­дот­вра­ща­ет воз­мож­ность до­бав­ле­ния но­вых свойств в ука­зан­ный объ­ект.

    .. versionadded:: ECMAScript5


.. js:function:: seal(obj) 

    Пре­дот­вра­ща­ет воз­мож­ность до­бав­ле­ния но­вых и уда­ле­ния су­ще­ст­вую­щих свойств в ука­зан­ном объ­ек­те.

    .. versionadded:: ECMAScript5


Дескрипторы свойств
-------------------
Де­ск­рип­тор свой­ст­ва – это обыч­ный Ja­va­Script-объ­ект, опи­сы­ваю­щий ат­ри­бу­ты (и ино­гда зна­че­ние) свой­ст­ва. 

В язы­ке Ja­va­Script су­ще­ст­ву­ет два ти­па свойств. 

Свой­ст­ва-дан­ные, имею­щие зна­че­ние и три ат­ри­бу­та: enumerable, writable и  configurable.
        
    .. code-block:: js

        {
            value:        /* лю­бое зна­че­ние, до­пус­ти­мое в язы­ке Ja­va­Script */,
            writable:     /* true или false */,
            enumerable:   /* true или false */,
            configurable: /* true или false */
        }

Свой­ст­ва с ме­то­да­ми дос­ту­па, имею­щие ме­тод чте­ния и/или ме­тод за­пи­си, а так­же
ат­ри­бу­ты enumerable и configurable.

    .. code-block:: js

        {
            get:          /* функ­ция или undefined: вза­мен свой­ст­ва value */,
            set:          /* функ­ция или undefined: вза­мен ат­ри­бу­та writable */,
            enumerable:   /* true или false */,
            configurable: /* true или false */
        }