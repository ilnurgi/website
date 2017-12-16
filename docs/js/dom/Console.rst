Console 
=======

Консоль браузера

.. py:class:: Console()

    .. py:method:: assert(expr, message)

        Выводит сообщение об ошибке в консоли если условие ложно


    .. py:method:: count([string title])
        
        Выводит строку title вместе со счетчиком вызовов данного метода с этой же строкой.


    .. py:method:: debug(any message...)
        
        Действует подобно методу console.log(), но помечает вывод,
        как отладочную информацию.


    .. py:method:: dir(any object)
        
        Выводит в консоли информацию об объекте в виде,
        по­зво­ляю­щем раз­ра­бот­чи­ку про­ве­рить свой­ст­ва или эле­мен­ты и
        в ин­те­рак­тив­ном ре­жи­ме ис­сле­до­вать вло­жен­ные объ­ек­ты и эле­мен­ты мас­си­вов.


    .. py:method:: dirxml(any node)
        
        Вы­во­дит в кон­соль раз­мет­ку XML или HTML уз­ла до­ку­мен­та.


    .. py:method:: error(messages)
        
        Выводит сообщения об ошибке

        .. code-block:: js

            console.error('error');
            // error


    .. py:method:: group(messages)
        
        Создает группу для группировки последующих сообщений в лог.

        Все последующие операции вывода в консоль будут помещать сообщения в эту группу, 
        пока не будет вызван метод groupEnd().


    .. py:method:: groupCollapsed(messages)
        
        Создает группу для группировки последующих сообщений в лог, но в свернутом виде.


    .. py:method:: groupEnd()
        
        Закрывает самую последнюю группу отладочных сообщений,
        созданную вызовом метода group() или groupCollapsed().


    .. py:method:: info(messages)
        
        Выводит информационные сообщения в консоль.

        .. code-block:: js

            console.info('message1', 'message2');
            // message1, message2


    .. py:method:: log(string format, messages)
        
        Выводит сообщения в консоль, возможно форматирование

        * format - строка с форматированием

            * %s - форматируются как строки

            * %d, %i - форматируются как целые числа

            * %f - форматируются как вещественные числа

            * %o - элементы дом

            * %O - объекты

            * %c - применяет заданные css свойства

        .. code-block:: js

            console.log('log information');
            // log information


    .. py:method:: profile([string title])
        
        Запускает профилировщик JavaScript и в начале отчета отображает строку title.


    .. py:method:: profileEnd()
        
        Останавливает профилировщик и выводит отчет с результатами профилирования
        программного кода.


    .. py:method:: time(name)
        
        Запускает таймер с именем name

        .. code-block:: js

            console.time('timer');


    .. py:method:: timeEnd(name)
        
        Останавливает указанный таймер и выводит имя и время,
        прошедшее с момента вызова метода time().

        .. code-block:: js

            console.time('timer');
            console.timeEnd('timer');
            // timer: 5495.19384765625ms


    .. py:method:: trace()
        
        Выводит трассировку стека.


    .. py:method:: warn(messages)
        
        Выводит предупреждающие сообщения в консоли.

        .. code-block:: js

            console.warn('warning');
            // warning