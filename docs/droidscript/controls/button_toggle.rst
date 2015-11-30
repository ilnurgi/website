ButtonToggle
============

.. js:class:: ButtonToggle()

    :js:func:`CreateToggle`, :js:func:`GetLastToggle`

    Также имеет аналогичные методы:

        * :js:func:`GetChecked`

        * :js:func:`GetHeight`

        * :js:func:`GetText`

        * :js:func:`GetTextSize`

        * :js:func:`GetVisibility`

        * :js:func:`GetWidth`

        * :js:func:`SetChecked`

        * :js:func:`SetMargins`

        * :js:func:`SetOnTouch` - в обработчик передается состояние

            .. code-block:: js
                
                btn.SetOnTouch(function(event){
                    app.ShowPopup(event.action); // Down, Up, Move
                    app.ShowPopup(event.x); 
                    app.ShowPopup(event.y); 

                });

        * :js:func:`SetPadding`

        * :js:func:`SetPosition`

        * :js:func:`SetSize`

        * :js:func:`SetText`

        * :js:func:`SetTextColor`

        * :js:func:`SetTextSize`

        * :js:func:`SetVisibility` 