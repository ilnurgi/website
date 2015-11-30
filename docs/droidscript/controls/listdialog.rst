ListDialog
==========

.. js:class:: ListDialog

    :js:func:`CreateListDialog`

    Также имеет следующие методы:

        * :js:func:`SetOnTouch` - в обработчик которого передается выбранный элемент, в случае множественного выбора элемент и состояние выбора

            .. code-block:: js
                
                dlg.SetOnTouch(function(item){});
                dlg.SetOnTouch(function(item, isChecked){});

    .. js:function:: GetType