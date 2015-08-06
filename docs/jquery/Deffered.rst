Deffered
========

.. js:class:: Deffered()

    Отсроченный объект


    .. js:function:: always(function)

        Регистрирует функцию, которая выполнится вне зависимости от состояния объекта


    .. js:function:: done(function)

        Регистрация функция обратного вызова при успешном завершнеии


    .. js:function:: fail(function)

        Регистрация функции обратного вызова при ошибках


    .. js:function:: notify()

        Отправляет сведения в объект о ходе выполнения


    .. js:function:: progress(function)

        Регистрирует функцию для сведении о ходе работы


    .. js:function:: reject()

        Метод переводит объект в состояние - ошибка при выполнении.


    .. js:function:: resolve()

        Метод переводит отсроченный объект в состояние - успешно выполнено (resolved)


    .. js:function:: state()

        Возвращает состнояние объекта

        * `pending` - в работе

        * `resolved` - принят

        * `rejected` - отклонен


    .. js:function:: then(done_function, fil_function)

        Регистрирует функции вызова для ошибок и успещного выполнения




    .. code-block:: js
        
        var def = $.Deffered()