.. py::module:: types

types
=====

В модуле types объявляются имена встроенных типов, которые соответствуют функциям, модулям, генераторам, кадрам стека и другим элемен-там программ. Имена, объявленные в этом модуле, часто используются при обращении к встроенной функции `isinstance()` и в других операциях
над типами.

==================== =====================
Переменная           Описание
==================== =====================
BuiltinFunctionType  Тип встроенных функций
CodeType             Тип объектов с программным кодом
FrameType            Тип кадра стека выполняемых объектов
FunctionType         Тип пользовательских функций и lambda-выражений
GeneratorType        Тип объектов генераторов и итераторов
GetSetDescriptorType Тип объектов дескрипторов методов getset
LambdaType           Альтернативное имя типа FunctionType
MemberDescriptorType Тип объектов дескрипторов атрибутов
MethodType           Тип методов пользовательских классов
ModuleType           Тип модулей
TracebackType        Тип объектов с трассировочной информацией
==================== =====================

.. py::class:: FunctionType(code, globals [, name [, defarags [, closure]]])

    Создает новый объект функции.


.. py::class:: CodeType(argcount, nlocals, stacksize, flags, codestring, constants, names, varnames, filename, name, firstlineno, lnotab [, freevars [, cellvars ]])

    Создает новый объект с программным кодом.


.. py::class:: MethodType(function, instance, class)

    Создает новый связанный метод объекта.


.. py::method:: ModuleType(name [, doc])

    Создает новый объект модуля.