Исключения
==========

Error
-----

.. js:class:: Error([message])

    Наследник :js:class:`Object`


    .. js:attribute:: message

        Сообщение об ошибке


    .. js:attribute:: name

        Тип ошибки


EvalError
---------


.. js:class:: EvalError([message])

    Исключение, генрируемое функцией eval

    Наследник :js:class:`Error`


RangeError
----------


.. js:class:: RangeError([message])

    Генерируется, когда число выходит из допустимого диапазона

    Наследник :js:class:`Error`


ReferenceError
--------------


.. js:class:: ReferenceError([message])

    Генерируется при попытке чтения несуществующей переменной

    Наследник :js:class:`Error`


SyntaxError
-----------


.. js:class:: SyntaxError([message])

    Генерируется при синтаксической ошибке

    Наследник :js:class:`Error`


TypeError
---------


.. js:class:: TypeError([message])

    Генерируется, когда значение имеет неверный тип

    Наследник :js:class:`Error`


URIError
--------


.. js:class:: URIError([message])

    Генерируется методами кодирования и декодирования

    Наследник :js:class:`Error`
