class - классы
==============


.. code-block:: py

    class MyClass(object):

        # укзаывает, какие атрибуты и методы унаследуют экземпляры

        __slots__ = ()

        def __init__(self):
            """
            1. данный метод инициализирует атрибуты объекта для создания экземпляра
            2. метод экземпляра класса
            3. self - экземпляр класса
            """

            # вызов родительского метода
            super(MyClass, self).__init__()

        def __call__(self):
            """
            позволяет обрабатывать вызов экземпляра класса как вызов функции
            """

        @classmethod
        def class_method(cls):
            """
            1. метод класса
            2. cls - сам класс
            """
            pass

        @staticmethod
        def static_method()
            """
            1. статический метод
            """
            pass

Создание и уничтожение объектов
-------------------------------

.. py:method:: __init__(self, *args, **kwargs)

    Инициализация экземпляра класса

.. py:method:: __new__(self, *args, **kwargs)

    Создание экземпляра класса

.. py:method:: __del__(self)

    Уничтожение экземпляра класса. Уменьшает счетчик ссылок на объект

Строковое представление объектов
--------------------------------

.. py:method:: __format__(self, format_spec)

    Создает форматированное строковое представление объекта

.. py:method:: __repr__(self, *args, **kwargs)

   Строковое представление объекта, строка с выражением, которое может использоваться для воссоздания объекта с помощью функции eval()

.. py:method:: __str__(self)

    Строковое представление объекта

Сравнение и упорядочивание объектов
-----------------------------------

.. py:method:: __bool__(self)

    Истинность объекта

.. py:method:: __hash__(self)

   Хеш сумма объекта

.. py:method:: __lt__(self,other)

    self < other

.. py:method:: __le__(self,other)

    self <= other

.. py:method:: __gt__(self,other)

    self > other

.. py:method:: __ge__(self,other)

    self >= other

.. py:method:: __eq__(self,other)

    self == other

.. py:method:: __ne__(self,other)

    self != other

Проверка типа
-------------

.. py:method:: __instancecheck__(cls,object)

.. py:method:: __subclasscheck__(cls, sub)

Доступ к атрибутам
------------------

.. py:method:: __getattribute__(self, name)

    Возвращает атрибут self.name.

.. py:method:: __getattr__(self, name)

    Возвращает атрибут self.name, который не может быть найден обычным способом,
    или возбуждает исключение AttributeError.

.. py:method:: __setattr__(self, name, value)

    Изменяет значение атрибута при выполнении операции self.name = value.
    Переопре деляет механизм присваивания, исполь зуемый по умолчанию.

.. py:method:: __delattr__(self, name)

    Удаляет атрибут self.name.

Дескрипторы
-----------

.. py:method:: __get__(self, instance, cls)

    Возвращает значение атрибута или возбуждает исключение AttributeError

.. py:method:: __set__(self, instance, value)

    Записывает в атрибут значение value

.. py:method:: __delete__(self, instance)

    Удаляет атрибут


Последовательности
------------------

.. py:method:: __len__(self)

    Возвращает длину объекта self

.. py:method:: __getitem__(self, key)

    Возвращает self[key]

.. py:method:: __setitem__(self, key, value)

    Реализует присваивание self[key] = value

.. py:method:: __delitem__(self, key)

    Удаляет self[key]

.. py:method:: __contains__(self, obj)

    Возвращает True, если obj присутствует в self; в противном случае возвращает False


Итераторы
---------

.. py:method:: __iter__(self)

    Возвращает объект итератор, который должен иметь метод next() или __next__(), возвразающий следующий объект,
    или возбуждать исключение StopIteration

Математические операции
-----------------------

.. py:method:: __add__(self,other)

    self + other

.. py:method:: __sub__(self,other)

    self - other

.. py:method:: __mul__(self,other)

    self * other

.. py:method:: __div__(self,other)

    self / other (только в Python 2)

.. py:method:: __truediv__(self,other)

    self / other (Python 3)

.. py:method:: __floordiv__(self,other)

    self // other

.. py:method:: __mod__(self,other)

    self % other

.. py:method:: __divmod__(self,other)

    divmod(self,other)

.. py:method:: __pow__(self,other [,modulo])

    self ** other, pow(self, other, modulo)

.. py:method:: __lshift__(self,other)

    self << other

.. py:method:: __rshift__(self,other)

    self >> other

.. py:method:: __and__(self,other)

    self & other

.. py:method:: __or__(self,other)

    self | other

.. py:method:: __xor__(self,other)

    self ^ other

.. py:method:: __radd__(self,other)

    other + self

.. py:method:: __rsub__(self,other)

    other - self

.. py:method:: __rmul__(self,other)

    other * self

.. py:method:: __rdiv__(self,other)

    other / self (только в Python 2)

.. py:method:: __rtruediv__(self,other)

    other / self (Python 3)

.. py:method:: __rfloordiv__(self,other)

    other // self

.. py:method:: __rmod__(self,other)

    other % self

.. py:method:: __rdivmod__(self,other)

    divmod(other,self)

.. py:method:: __rpow__(self,other)

    other ** self

.. py:method:: __rlshift__(self,other)

    other << self

.. py:method:: __rrshift__(self,other)

    other >> self

.. py:method:: __rand__(self,other)

    other & self

.. py:method:: __ror__(self,other)

    other | self

.. py:method:: __rxor__(self,other)

    other ^ self

.. py:method:: __iadd__(self,other)

    self += other

.. py:method:: __isub__(self,other)

    self -= other

.. py:method:: __imul__(self,other)

    self \*= other

.. py:method:: __idiv__(self,other)

    self /= other (только в Python 2)

.. py:method:: __itruediv__(self,other)

    self /= other (Python 3)

.. py:method:: __ifloordiv__(self,other)

    self //= other

.. py:method:: __imod__(self,other)

    self %= other

.. py:method:: __ipow__(self,other)

    self \*\*= other

.. py:method:: __iand__(self,other)

    self &= other

.. py:method:: __ior__(self,other)

    self \|= other

.. py:method:: __ixor__(self,other)

    self ^= other

.. py:method:: __ilshift__(self,other)

    self <<= other

.. py:method:: __irshift__(self,other)

    self >>= other

.. py:method:: __neg__(self)

    –self

.. py:method:: __pos__(self)

    +self

.. py:method:: __abs__(self)

    abs(self)

.. py:method:: __invert__(self)

    ~self

.. py:method:: __int__(self)

    int(self)

.. py:method:: __long__(self)

    long(self) (только в Python 2)

.. py:method:: __float__(self)

    float(self)

.. py:method:: __complex__(self)

    complex(self)

.. py:method:: __round__(self)

    round(self)

.. py:method:: __index__(self)

    вызывается при использовании функции `bin()`, `hex()`, `oct()`

Контексты (with)
----------------

Начиная с версии 2.6, язык поддерживает протокол менеджеров контекста. Этот протокол гарантирует выполнение завершающих действий (например, закрытие файла) вне зависимости от того, произошло исключение внутри блока кода или нет. Для работы с протоколом предназначена инструкuия with ... as. 

>>> with <выражение>[ as <переменная>][, <выражение2>[ as <переменная2>]]:
        ...

Вначале вычисляется <выражение>, которое должно возвращать объект, поддерживающий протокол.
Этот объект должен иметь два метода: __enter__ и __exit__.

.. py:method:: __enter__(self)

    Вызывается при входе в новый контекстный блок. Возвращаемое значение помещается в переменную,
    указанную в спецификаторе as инструкции with.

.. py:method:: __exit__(self, type, value, tb)

    Вызывается, когда поток выполнения покидает контекстный блок.
    Если в процессе выполнения инструкций в блоке было возбуждено исключение, в аргументах type, value и tb
    передаются тип исключения, его значение и объект с трассировочной информацией.
    В первую очередь инструкция with предназначена для упрощения управления системными ресурсами,
    такими как открытые файлы, сетевые соединения и блокировки.
    Благодаря реализа ции этого интерфейса объект может безопасно освобождать ресурсы после выхода потока выполнения
    за пределы контекста, в котором этот объект используется.


Сохранение и востановление объектов. `pickle`, 'shelve'
-------------------------------------------------------

.. py:method:: __getstate__(self)

    возвращает представление объекта для сохранения

.. py:method:: __setstate__(self, value)

    возвращает востановленный объект по аргументу

::

    import socket

    class Client(object):

        def __init__(self,addr):
            self.server_addr = addr
            self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.sock.connect(addr)

        def __getstate__(self):
            return self.server_addr
            
        def __setstate__(self,value):
            self.server_addr = value
            self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.sock.connect(self.server_addr)

Атрибуты классов

===================== ========
атрибут               описание
===================== ========
t.__doc__             Строка документирования
t.__name__            Имя класса
t.__bases__           Кортеж с базовыми классами
t.__dict__            Словарь, содержащий методы и атрибуты класса
t.__module__          Имя модуля, в котором определен класс
t.__abstractmethods__ Множество имен абстрактных методов (может быть неопределен, если абстрактные методы отсутствуют в классе)
===================== ========


Атрибуты экземпляров классов

============== ========
атрибут        описание
============== ========
ш.__class__    Класс, которому принадлежит экземпляр
m.__dict__     Словарь, содержащий данные экземпляра
============== ========


Атрибуты методов

============== ========
атрибут        описание
============== ========
m.__class__    Класс, в котором определен данный метод
m.__doc__      Строка документирования
m.__func__     Объект функции, реализующей данный метод
m.__name__     Имя метода
m.__self__     Ссылка на экземпляр, ассоциированный с данным методом (None – для несвязанных методов)
============== ========