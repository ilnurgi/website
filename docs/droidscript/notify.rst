Notify - уведомления
====================

.. js:class:: Notify

    :js:func:`CreateNotify`


    .. js:function:: Cancel()

        Выключить/удалить уведомление

        .. code-block:: js
            
            notify.Cancel()

    .. js:function:: Notify()

        Отправить уведомление

        .. code-block:: js
            
            notify.Notify()


    .. js:function:: SetLargeImage(img)

        Установить изображение уведомления

        .. code-block:: js
            
            notify.SetLargeImage('/Img/hello.png');


    .. js:function:: SetLights(color, ?, ?)

        Включает индикатор уведомлени, включается если только экран выключен

        .. code-block:: js
            
            notify.SetLights('#00ffff', 500, 500);


    .. js:function:: SetMessage(message, title, details)

        .. code-block:: js
            
            notify.SetMessage('Notification', 'title', 'details');


Notification.Cancel(id)     id is optional and must match .Notify(id)
Notification.Destroy()  
Notification.GetType()  
Notification.Notify(id)     id is optional
Notification.Release()  
Notification.SetLargeImage( file )  
Notification.SetLights( color,onMs,offMs )  
Notification.SetMessage( ticker,title,text )    