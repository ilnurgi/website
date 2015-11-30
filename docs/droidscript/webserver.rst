WebServer
=========

.. js:class:: WebServer


    .. js:function:: AddServlet(url, callback);

        Добавляет обработичк запроса

        .. code-block:: js
            
            server.AddServlet('/message', OnServlet);

            function OnServlet(request, info){
                /*
                 * info.remoteAddress
                 * request.msg
                 */
            }


    .. js:function:: SetFolder(fldrName);

        .. code-block:: js
            
            server.SetFolder('/sdcard/DroidScript');


    .. js:function:: SetResponse(text)

        .. code-block:: js
            
            server.SetResponse('Go!')


    .. js:function:: GetWebSockClients()   
    
    .. js:function:: SendText( txt, ip )   
    
    .. js:function:: SetOnReceive( callback)   
    
    .. js:function:: Start()
    
