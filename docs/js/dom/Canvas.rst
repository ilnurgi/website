Canvas - канвас
===============

Канвас (холст) - элемент , с помощью которого производится работа с изображениями.


.. py:class:: Canvas()

    
    .. py:attribute:: height

        Высота холста


    .. py:attribute:: weight

        Ширина холста


    .. py:function:: getContext(str contextid[, args])

        Возвращает контекст канваса

        Если contextid == '2d', вернет :py:class:`CanvasRenderingContext2D`


    .. py:function:: toDataURL([str type='image/png', [args]])

        Возвращает растровое изображение холста в виде URL-адреса `data://`

        * `type` - MIME-тип или графический формат

        .. code-block:: js

            // Ско­пи­ро­вать со­дер­жи­мое хол­ста в эле­мент <img> и до­ба­вить его в до­ку­мент
            var canvas = document.getElementById("my_canvas");
            var image = document.createElement("img");
            image.src = canvas.toDataURL();
            document.body.appendChild(image);