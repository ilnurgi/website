.. py:module:: warnings

warnings - предупреждения
=========================

* `Warning` - Базовый класс для всех предупреждений. Является производным от класса Exception.
* `UserWarning` - Универсальное предупреждение, определяемое пользователем. Является производным от класса Warning.
* `DeprecationWarning` - Предупреждение на случай использования нерекомендуемых возможностей. Является производным от класса Warning.
* `SyntaxWarning` - Предупреждение на случай использования нерекомендуемого синтаксиса. Является производным от класса Warning.
* `RuntimeWarning` - Предупреждение на случай использования особенностей, которые могут привести к проблемам во время выполнения. Является производным от класса Warning.
* `FutureWarning` - Предупреждение о том, что поведение используемой возможности изменится в будущем. Является производным от класса Warning.

.. py::method:: warn(message[, category=UserWarning[, stacklevel=1]])

    Возбуждает предупреждение. 

    :param str message: текст предупреждения
    :param class category: класс предупреждения (такой как DeprecationWarning)
    :param int stacklevel: кадр стека, в котором должно возбуждаться предупреждение. 


.. py::method:: warn_explicit(message, category, filename, lineno[, module[, registry]])

    Низкоуровневая версия функции :py:meth:`warn()`. 

    :param str message: текст предупреждения
    :param class category: класс предупреждения (такой как DeprecationWarning)
    :param str filename:  имя файла где возбуждается предуцпреждение
    :param int lineno: номер строки. где возбуждается исключение
    :param registry: объект, представляющий все активные фильтры. Если аргумент registry опущен, вывод предупреждения не подавляется.


.. py::method:: showwarning(message, category, filename, lineno[, file=sys.stderr])

    Выводит предупреждение в файл. 
    
    :param str message: текст предупреждения
    :param class category: класс предупреждения (такой как DeprecationWarning)
    :param str filename:  имя файла где возбуждается предуцпреждение
    :param int lineno: номер строки. где возбуждается исключение
    :param file: файловый объект


.. py::method:: formatwarning(message, category, filename, lineno)

    Создает форматированную строку, которая выводится при возбуждении предупреждения.
    
    :param str message: текст предупреждения
    :param class category: класс предупреждения (такой как DeprecationWarning)
    :param str filename:  имя файла где возбуждается предуцпреждение
    :param int lineno: номер строки. где возбуждается исключение

.. py::method:: filterwarnings(action[, message[, category[, module[, lineno[, append]]]]])

    Добавляет новый элемент в список фильтров. 

    :param str action: ‘error’, ‘ignore’, ‘always’, ‘default’, ‘once’ или ‘module
    :param str message: регулярное выражение, которое сравнивается с текстом сообщения
    :param class category: класс предупреждения (такой как DeprecationWarning)
    :param str modeule:  регулярное выражение, которое сравнивается с названием модуля
    :param int lineno: номер строки. где возбуждается исключение, 0 - все строки
    :param append: добавить фильтр в конец, иначе добавляется в начало

.. py::method:: resetwarnings()

    Сбрасывает все фильтры предупреждении.

.. py::attribute:: filters

    Список активных фильтров

