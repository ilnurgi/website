Locator
=======

.. js:class:: Locator

    * :js:func:`SetOnChange` - устанавливает обработчик изменния данных, в обработчик придут новые данные

        .. code-block:: js
            
            loc.SetOnChange(function(data){
                /*
                 * data.provider
                 * data.latitude
                 * data.longitude 
                 * data.speed
                 * data.bearing
                 * data.altitude
                 * data.accuracy
                */
            })

    * :js:func:`Start` - запускает локатор


    .. js:function:: GetBearingTo()

        Возвращает расстояние до указанно точки

        .. code-block:: js

            //Calculate our distance in meters from Greenwich London.
            dist = loc.GetBearingTo( 51.4778, 0.0 );
            Log( "Bearing to London: "+bearing.toFixed(2)+" degrees\n" );


    .. js:function:: GetDistanceTo()

        Возвращает расстояние до указанно точки

        .. code-block:: js

            //Calculate our distance in meters from Greenwich London.
            dist = loc.GetDistanceTo( 51.4778, 0.0 );
            Log( "Distance to London: "+(dist/1000).toFixed(2)+" km" );
            
            
    .. js:function:: SetRate()

        Устанавливает время обновления

        .. code-block:: js
            
            loc.SetRate(10);



Locator.GetBearingTo()  Returns the approximate initial bearing in degrees East of true North when traveling along the shortest path between this location and the given location.
Locator.GetDistanceTo()     Returns the approximate distance in meters between this location and the given location.
Locator.SetOnChange(callback)   
Locator.SetRate(seconds)    Set Locator update frequency in seconds
Locator.Start()     
Locator.Stop() 