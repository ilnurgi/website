WebView
=======

.. js:class:: WebView

    :js:func:`CreateWebView`

    Также поддерживает слудующие методы:

        * `GetHeight`

        * `GetVisibility`

        * `GetWidth`

        * `SetBackground`

        * `SetBackColor`

        * `SetBackGradient`

        * `SetBackGradientRadial`

        * `SetMargins`

        * `SetPadding`

        * `SetPosition`

        * `SetSize`

        * `SetVisibility`

    
    .. js:function:: Back()
    
    .. js:function:: Forward()
    
    .. js:function:: CanGoBack()
    
    .. js:function:: CanGoForward()
    
    .. js:function:: Execute(text)

        Выполняет js код внутри страницы в webview

        .. code-block:: js
            
            webview.Execute('alert();');
            

    .. js:function:: LoadHtml(html, baseFolder, options)

        Загружает локальную html страницу.

        Доп параметры:

            * `allowzoom`

            * `autozoom`

            * `nolongtouch`

            * `wide`

        .. code-block:: js
            
            var html = '<html>...</html>'
            web.LoadHtml(html, 'file://Sys/')

 
    .. js:function:: LoadUrl(url, options)

        .. code-block:: js
            
            web.LoadUrl('http://gogle.com')
            web.LoadUrl('file:///Sys/Html/Page.html')


    .. js:function:: SetOnProgress(callback)

        Устанавливает обработчик процесса загрузки

        .. code-block:: js
            
            web.SetOnProgress(function(progress){});