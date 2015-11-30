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



    .. js:function:: Back()  
    
    .. js:function:: CanGoBack() 
    
    .. js:function:: CanGoForward()  
    
    .. js:function:: Capture(filename)   captures jpeg of visible page
    
    .. js:function:: ClearHistory()  
    
    .. js:function:: Execute( code ) 
    
    .. js:function:: Forward()   
    
    .. js:function:: GetAbsHeight()  
    
    .. js:function:: GetAbsWidth()   
    
    .. js:function:: GetHeight() 
    
    .. js:function:: GetPosition()   
    
    .. js:function:: GetType()   
    
    .. js:function:: GetUrl()    returns the current url
    
    .. js:function:: GetVisibility() 
    
    .. js:function:: GetWidth()  
    
    .. js:function:: LoadHtml( html,base,options )   
    
    .. js:function:: LoadUrl( url,options )  
    
    .. js:function:: Print() KitKat or later only
    
    .. js:function:: SetBackColor( color )   
    
    .. js:function:: SetBackGradient( color1,color2,color3,p4,p5,p6,p7 ) 
    
    .. js:function:: SetBackGradientRadial( x,y,r,color1,color2,color3,p7 )  
    
    .. js:function:: SetBackground( imagefile,options )  
    
    .. js:function:: SetMargins( left,top,right,bottom ) 
    
    .. js:function:: SetOnProgress( callback )   
    
    .. js:function:: SetPadding( width,height,top,bottom )   
    
    .. js:function:: SetPosition( left,top,width,height )    
    
    .. js:function:: SetScale( x,y ) 
    
    .. js:function:: SetSize( width,height ) 
    
    .. js:function:: SetVisibility( HideShow )   
    
