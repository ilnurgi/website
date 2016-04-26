Canvas - канвас
===============

Канвас (холст) - элемент , с помощью которого производится работа с изображениями.


.. js:class:: Canvas()

    
    .. js:attribute:: height

        Высота холста


    .. js:attribute:: weight

        Ширина холста


    .. js:function:: getContext(str contextid[, args])

        Возвращает контекст канваса

        Если contextid == '2d', вернет :js:class:`CanvasRenderingContext2D`


    .. js:function:: toDataURL([str type='image/png', [args]])

        Возвращает растровое изображение холста в виде URL-адреса `data://`

        * `type` - MIME-тип или графический формат

        .. code-block:: js

            // Ско­пи­ро­вать со­дер­жи­мое хол­ста в эле­мент <img> и до­ба­вить его в до­ку­мент
            var canvas = document.getElementById("my_canvas");
            var image = document.createElement("img");
            image.src = canvas.toDataURL();
            document.body.appendChild(image);