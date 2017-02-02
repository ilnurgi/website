Deffered
========

.. js:class:: Deffered()

    Отсроченный объект


    .. py:function:: always(function)

        Регистрирует функцию, которая выполнится вне зависимости от состояния объекта


    .. py:function:: done(function)

        Регистрация функция обратного вызова при успешном завершнеии


    .. py:function:: fail(function)

        Регистрация функции обратного вызова при ошибках


    .. py:function:: notify()

        Отправляет сведения в объект о ходе выполнения


    .. py:function:: progress(function)

        Регистрирует функцию для сведении о ходе работы


    .. py:function:: reject()

        Метод переводит объект в состояние - ошибка при выполнении.


    .. py:function:: resolve()

        Метод переводит отсроченный объект в состояние - успешно выполнено (resolved)


    .. py:function:: state()

        Возвращает состнояние объекта

        * `pending` - в работе

        * `resolved` - принят

        * `rejected` - отклонен


    .. py:function:: then(done_function, fil_function)

        Регистрирует функции вызова для ошибок и успещного выполнения




    .. code-block:: js
        
        var def = $.Deffered()