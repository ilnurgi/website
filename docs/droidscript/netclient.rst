NetClient
=========

.. js:class:: NetClient

        
    .. js:function:: AutoReceive();

        .. code-block:: js
            
            net.AutoReceive( ip, 11077, "UTF-16LE" );


    .. js:function:: Connect(host, port)

        .. code-block:: js
            
            net.Connect('http://google.com', 80);


    .. js:function:: Disconnect()

    .. js:function:: GetBroadcastAddress()

    .. js:function:: IsEnabled()

    .. js:function:: IsConnected()

    .. js:function:: ReceiveDatagram(encoding, port, timeout);

        .. code-block:: js
            
            net.ReceiveDatagram( "UTF-16LE", 11088, 300 );
            net.ReceiveDatagram( "UTF-8", port, 1 );


    .. js:function:: ReceiveBytes(type)
        
        .. code-block:: js
            
            bytes = net.ReceiveBytes('Hex');
            bytes = net.ReceiveBytes('Int');


    .. js:function:: ReceiveText(encode)

        Ожидает данные, для больших объекиов данных может потребоваться повторный вызов функции

        .. code-block:: js
            
            msg = net.ReceiveText('UTF-8')


    .. js:function:: SendBytes(bytes)

        .. code-block:: js
            
            net.SendBytes('47,45,54,20,2F,20,48,54,54,50,2F,31,2E,31,0D,0A,0D,0A', 'Hex');
            net.SendBytes([0x47,0x45,0x54,0x20,0x2F,0x20,0x48,0x54,0x54,0x50,0x2F,0x31,0x2E,0x31,0x0D,0x0A,0x0D,0x0A], "Int" );


    .. js:function:: SendDatagram();

        .. code-block:: js

            net.SendDatagram("wdemo:hello", "UTF-16LE", GetBroadcastAddress(), 11088);
        
        
    .. js:function:: SendText(text, mode)

        * `mode`

            * US-ASCII
            * UTF-16LE
            * UTF-16BE
            * UTF-16
            * UTF-8

        .. code-block:: js
            
            net.SendText('123', "UTF-16LE");


    .. js:function:: SetOnConnect(callback)

        .. code-block:: js

            net.SetOnConnect(function(connected){});
        

    .. js:function:: SetOnReceive(callback)

        .. code-block:: js
            
            net.SetOnReceive(function(text){});
        

NetClient.AutoReceive( server,port,mode )   
NetClient.Connect( address,port )   
NetClient.Disconnect()  
NetClient.DownloadFile( file )  
NetClient.GetBroadcastAddress()     
NetClient.IsConnected()     
NetClient.IsEnabled()   
NetClient.ReceiveDatagram( encoding, port, timeout )    
NetClient.ReceiveFile( file,wait )  
NetClient.ReceiveText( mode )   
NetClient.SendDatagram( packet, encoding, address, port )   
NetClient.SendText( text,mode )     
NetClient.SetOnConnect( callback )  
NetClient.SetOnDownload( callback )     
NetClient.SetOnReceive( callback )  
NetClient.SetTimeout( callback ) 