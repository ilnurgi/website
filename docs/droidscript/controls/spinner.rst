Spinner
=======

.. js:class:: Spinner

    :js:class:`CreateSpinner`

    Также имеет аналогичные методы:

        * :js:func:`GetHeight`

        * :js:func:`GetText`

        * :js:func:`GetTextSize`

        * :js:func:`GetVisibility`

        * :js:func:`GetWidth`

        * :js:func:`SetMargins`

        * :js:func:`SetPadding`

        * :js:func:`SetPosition`

        * :js:func:`SetSize`

        * :js:func:`SetTextColor`

        * :js:func:`SetTextSize`

        * :js:func:`SetVisibility`       


    .. js:function:: GetTextSize( mode )

    .. js:function:: SelectItem( item )
    
    .. js:function:: SetList( list )
    
    .. js:function:: SetOnChange( callback )

        Устанавливает обработчик события, выбор элемента. В обработчик передается выбранный элемент.

        .. code-block:: js
            
            spin.SetOnChange(function(item){
                app.ShowPopup( "Selected = " + item );
            });

    