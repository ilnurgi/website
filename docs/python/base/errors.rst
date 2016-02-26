try/except - перехват исключений
================================

>>> try:
        5/0
    except ZeroDivisionError as err:
        print err

>>> raise RuntimeError(u'Ошибка какая то')

>>> class MyException(Exception): pass

>>> assert False, u'Данная строка возбудит исключение AssertionError'


.. py:class:: AttributeError

    Возбуждается при обращении к несуществующему атрибуту

    Наследник :py:class:`StandardError`


.. py:class:: ArithmeticError

    Базовый класс исключений, возбуждаемых арифметическими операциями

    Наследник :py:class:`StandardError`


.. py:class:: AssertionError

    Возбуждается инструкциями assert

    Наследник :py:class:`StandardError`


.. py:class:: BaseException

    Базовый класс всех исключений


.. py:class:: EnvironmentError

    Ошибка, обусловленная внешними причинами

    Наследник :py:class:`StandardError`


.. py:class:: EOFError

    Возбуждается по достижении конца файла

    Наследник :py:class:`StandardError`


.. py:class:: Exception

    Базовый класс для всех исключений, не связанных с завершением программы

    Наследник :py:class:`BaseException`


.. py:class:: FloatingPointError

    Ошибка в инструкции import

    Наследник :py:class:`ArithmeticError`


.. py:class:: GeneratorExit

    Возбуждается методом .close() генераторов

    Наследник :py:class:`BaseException`


.. py:class:: ImportError

    Ошибка в инструкции import

    Наследник :py:class:`SyntaxError`


.. py:class:: IndentationError

    Ошибка оформления отступов

    Наследник :py:class:`SyntaxError`


.. py:class:: IndexError

    Ошибка обращения по индексу за пределами последовательности.

    Наследник :py:class:`LookupError`


.. py:class:: IOError

    Ошибка ввода-вывода при работе с файлами

    Наследник :py:class:`EnvironmentError`


.. py:class:: KeyError

    Ошибка обращения к несуществующему ключу словаря

    Наследник :py:class:`LookupError`


.. py:class:: KeyboardInterrupt

    Возбуждается нажатием клавишей прерывания (обычно Ctrl-C)

    Наследник :py:class:`BaseException`


.. py:class:: LookupError

    Ошибка обращения по индексу или ключу

    Наследник :py:class:`Exception`


.. py:class:: MemoryError

    Нехватка памяти

    Наследник :py:class:`Exception`


.. py:class:: NameError

    Не удалось отыскать локальное или глобальное имя

    Наследник :py:class:`Exception`


.. py:class:: NotImplementedError

    Обращение к нереализованному методу или функции

    Наследник :py:class:`Exception`


.. py:class:: OSError

    Ошибка операционной системы

    Наследник :py:class:`EnvironmentError`


.. py:class:: ReferenceError

    Ошибка обращения к объекту, который уже был уничтожен

    Наследник :py:class:`Exception`


.. py:class:: RuntimeError

    Универсальное исключение

    Наследник :py:class:`Exception`


.. py:class:: StandardError

    Базовый класс для всех встроенных исключений (только в Python 2).

    В Python 3 – базовый класс всех исключений, наследующих класс Exception

    Наследник :py:class:`Exception`


.. py:class:: StopIteration

    Возбуждается для прекращения итераций

    Наследник :py:class:`Exception`


.. py:class:: SyntaxError

    Синтаксическая ошибка

    Наследник :py:class:`Exception`


.. py:class:: SystemError

    Нефатальная системная ошибка в интерпретаторе

    Наследник :py:class:`Exception`


.. py:class:: SystemExit

    Завершение программы

    Наследник :py:class:`BaseException`


.. py:class:: TabError

    Непоследовательное использование символа табуляции (генерируется при запуске интерпретатора с ключом –tt)

    Наследник :py:class:`IndentationError`


.. py:class:: TypeError

    Попытка выполнить операцию над аргументом недопустимого типа

    Наследник :py:class:`Exception`


.. py:class:: UnboundLocalError

    Ошибка обращения к локальной переменной, которой еще не было присвоено значение

    Наследник :py:class:`Exception`


.. py:class:: UnicodeError

    Ошибка при работе с символами Юникода

    Наследник :py:class:`ValueError`


.. py:class:: UnicodeDecodeError

    Ошибка декодирования символов Юникода

    Наследник :py:class:`ValueError`


.. py:class:: UnicodeEncodeError

    Ошибка кодирования символов Юникода

    Наследник :py:class:`ValueError`


.. py:class:: UnicodeTranslateError

    Ошибка трансляции символов Юникода

    Наследник :py:class:`ValueError`


.. py:class:: ValueError

    Недопустимый тип

    Наследник :py:class:`Exception`


.. py:class:: ZeroDivisionError

    Деление или деления по модулю на ноль

    Наследник :py:class:`ArithmeticError`
