Исключения
==========

Error
-----

.. py:class:: Error([message])

    Наследник :py:class:`Object`


    .. py:attribute:: message

        Сообщение об ошибке


    .. py:attribute:: name

        Тип ошибки


EvalError
---------


.. py:class:: EvalError([message])

    Исключение, генрируемое функцией eval

    Наследник :py:class:`Error`


RangeError
----------


.. py:class:: RangeError([message])

    Генерируется, когда число выходит из допустимого диапазона

    Наследник :py:class:`Error`


ReferenceError
--------------


.. py:class:: ReferenceError([message])

    Генерируется при попытке чтения несуществующей переменной

    Наследник :py:class:`Error`


SyntaxError
-----------


.. py:class:: SyntaxError([message])

    Генерируется при синтаксической ошибке

    Наследник :py:class:`Error`


TypeError
---------


.. py:class:: TypeError([message])

    Генерируется, когда значение имеет неверный тип

    Наследник :py:class:`Error`


URIError
--------


.. py:class:: URIError([message])

    Генерируется методами кодирования и декодирования

    Наследник :py:class:`Error`
