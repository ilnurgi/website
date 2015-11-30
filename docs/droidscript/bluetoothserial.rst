BluetoothSerial
===============

.. js:class:: BluetoothSerial

    .. js:function:: Clear()     

    .. js:function:: Connect( name,channel )   

        .. code-block:: js
              
              bt.Connect( "HC-05" );  

    .. js:function:: Disconnect()    

    .. js:function:: IsBluetoothEnabled()    

    .. js:function:: IsConnected()   

    .. js:function:: IsPaired( p1 )  

    .. js:function:: RequestEnable()     

    .. js:function:: SetOnConnect( callback )    

        .. code-block:: js
            
            br.SetOnConnect(function(status){});


    .. js:function:: SetOnReceive( callback )   

        .. code-block:: js
             
             bt.SetOnReceive(fucntion(data){});


    .. js:function:: SetSplitMode( p1,p2,p3 )    

        .. code-block:: js
            
            bt.SetSplitMode( "End", "\n" ); 


    .. js:function:: SetTimeout( p1 )    

    .. js:function:: Write( p1 ) 
