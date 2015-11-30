Email - электронная почта
=========================

.. js:class:: Email

    :js:func:`CreateEmail`


    .. js:function:: Recive(type, limit, subject)

        .. code-block:: js
            
            email.Recive('Inbox', 20, '')

            
    .. js:function:: Send(title, msg, from, to, attach)


    .. js:function:: SetIAMP(host)

        .. code-block:: js
            
            email.SetSMTP('smtp.gmail.com', 465);


    .. js:function:: SetOnMessage(callback)

        Устанавливает обработчик прихода сообщения

        .. code-block:: js
            
            .. code-block:: js
                
                email.SetOnMessage(function(msg){
                    /*
                     * msg.from
                     * msg.to
                     * msg.Subject
                     * msg.body
                     */
                })


    .. js:function:: SetOnStatus(callback)

        .. code-block:: js
            
            email.SetOnStatus(function(status){})


    .. js:function:: SetSMTP(host, port)

        .. code-block:: js
            
            email.SetSMTP('smtp.gmail.com', 465);


Email.Receive( p1,p2,p3 )   
Email.Send( subject,body,sender,recipients,attach )     
Email.SetIMAP( p1,p2 )  
Email.SetOnMessage( p1 )    
Email.SetOnStatus( p1 )     
Email.SetSMTP( p1,p2 ) 