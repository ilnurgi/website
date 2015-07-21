mobile - объект, хранящий настройки мобильного приложения
=========================================================

.. code-block:: js
    
    $(document).bind('mobileinit', function(){
        $.mobile.defaultPageTransition = 'fade';
    })

.. js:class:: mobile


    .. js:attribute:: ajaxEnable

        вкл/выкл навигацию между страницами через ajax

    .. js:attribute:: defaultPageTransition

        анимационный эффект, применяемый ко всем навигационным переходам

        * `slide`

        * `pop`

        * `slideup`

        * `slidedown`

        * `fade`

        * `flip`

