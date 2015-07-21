AJAX - Asynchronous Javascript and XML - «асинхронный JavaScript и XML»
=======================================================================


.. code-block:: js

    function ajaxTest(input) {
        var request = new XMLHttpRequest();
        request.open('GET‘, 'ajax.php?input=' + input);
        request.send();
        request.onreadystatechange = function() {
            if (request.readyState == 4 && request.status == 200)
            processResult(request.responseText);
        }
    }


.. js:class:: XMLHttpRequest()

    
    .. js:attribute:: onreadystatechange

        Обработчик изменения статуса

        .. code-block:: js

            xhr.onreadystatechange = function(){
                if (xhr.readyState == 4)
                ...
            }

    .. js:attribute:: readyState

        Статус обработки запрос

        * 0 - open еще не вызывался
        * 1 - open вызван, send ещё не вызван
        * 2 - send вызван, но ответа пока нет
        * 3 - идет прием данных
        * 4 - ответ от сервера получен


    .. js:attribute:: status

        HTML статус код ответа
                 

    .. js:attribute:: responseText

        Ответ запроса


    .. js:function:: abort()

        Отменить загрузку

        
    .. js:function:: open(str method, str url, bool assynchrone=true)

        Открывает запрос


    .. js:function:: send()

        Отправляет запрос


    .. js:function:: setRequestHeader(key, value)

        Устанавливает заголовки для запроса




    