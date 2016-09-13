jQuery
======

.. py:class:: jQuery(selector [, context=document])
.. py:class:: jQuery(elts)
.. py:class:: jQuery(html, [props])
.. py:class:: jQuery(f)

    * selector - селектор для выбора, :ref:`selector`
    * elts - эле­мен­т до­ку­мен­та, мас­сив или объ­ект, по­доб­ный мас­си­ву
      (NodeList или дру­гой объ­ект jQuery, со­дер­жа­щим эле­мен­ты до­ку­мен­та).
    * html - строка для син­так­си­че­ского ана­лиза
    * f - функ­ция, ко­то­рая долж­на быть вы­зва­на по­сле то­го,
      как до­ку­мент бу­дет за­гру­жен и ста­нет дос­ту­пен для вы­пол­не­ния опе­ра­ций с ним.

      Ес­ли до­ку­мент уже го­тов к вы­пол­не­нию опе­ра­ций,
      функ­ция f бу­дет вы­зва­на не­мед­лен­но, как ме­тод объ­ек­та document.

    Элемент документа.

    .. code-block:: js

        var jq_elem = $("body");


    .. py:method:: attr()

        Задает атрибуты

        .. code-block:: js

            jq_elem.attr("src", "image.png");


    .. py:method:: click()

        Добавляет обработчик клика

        .. code-block:: js

            jq_elem.click(function() {});


    .. py:method:: css()

        Задает css стили

        .. code-block:: js

            jq_elem.css("color", "red");