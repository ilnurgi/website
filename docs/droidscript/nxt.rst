Nxt
===

.. js:class:: Nxt

    .. js:function:: Beep( frequency, duration ) 

        Commands the NXT brick to play a tone of a given frequency for a given duration in milliseconds.

        .. code-block:: js
            
            nxt.Beep( 100, 500 );


    .. js:function:: Brake( motors ) 

        Commands the NXT brick to Brake one or more of it's motors.
        
        The motors parameter can be a single motor, for example just “A” or a combination of motors such as “ABC”.
        
        Unlike the Stop function, this function actively brakes the motors using power from the battery.

        .. code-block:: js
            
            nxt.Brake('BC');


    .. js:function:: CheckConnection()   

        Returns true if the NXT brick is currently connected to the phone/tablet but it will show a popup warning message and return false if no brick is currently connected.
    
        This function is useful if you want to warn the user that he/she have no connection.

        .. code-block:: js
            
            ok = nxt.CheckConnection()


    .. js:function:: Connect( name ) 

        Connects to the Bluetooth device with given name.


    .. js:function:: Disconnect()    

        Disconnects the Bluetooth link between your phone and the NXT brick.


    .. js:function:: Drive( motors, power, rotation )    

        Commands the NXT brick to drive one or more of it's motors with a given power and number of rotations.
    
        The motors parameter can be a single motor, for example just “A” or a combination of motors such as “ABC”.
        
        Power is given as a percentage value and negative values make the motor reverse.
        
        If the number of rotations is set to zero, then the motor will continue until the Stop function is called.
    
    .. js:function:: FileFindFirst( p1 ) 
    
    .. js:function:: FileFindNext( p1 )  
    
    .. js:function:: GetBtAddress( obj ) 

        Returns Bluetooth address of a connected NXT brick or NXT brick address given as optional obj parameter.
    
    .. js:function:: GetBtName( obj )   

         Returns Bluetooth name of a connected NXT brick or NXT brick name given as optional obj parameter.
    
    .. js:function:: GetCurrentProgram() 

        Gets the name of the NXT-G program currently running on the NXT brick.
    
    .. js:function:: GetRotationCount( motor)    
    
    .. js:function:: IsBluetoothEnabled()    

        Checks if Bluetooth is enabled on the phone/tablet. Returns true if Bluetooth is enabled and false if it is disabled. This is alias for function IsEnabled.

    .. js:function:: IsConnected()   

        Returns true if the NXT brick is currently connected to the phone/tablet. Unlike CheckConnection method, it will not show a popup warning message and return false if no brick is currently connected.
    
    .. js:function:: IsEnabled() 

        Checks if Bluetooth is enabled on the phone/tablet. Returns true if Bluetooth is enabled and false if it is disabled. This is the same function as IsBluetoothEnabled.


    .. js:function:: IsMotorIdle( motor )    

        Checks if the specified motor (“A”,“B”,“C”) is currently powered. This can be useful in order to check if a previously sent motor command has completed.

    .. js:function:: IsPaired( name )    

        Checks if Bluetooth device with name is on the paired devices list of our phone/tablet. Returns “true” or “false”.

    .. js:function:: PlaySoundFile( file, repeat )   

        Commands the NXT brick to play a sound file (.rso) file which is available on the brick.
    
        The file parameter should be the name of the sound file and the repeat parameter should be number of times you want the sound to repeat.

    .. js:function:: ReadColorSensor( input, mode )  

        Reads the color currently being 'seen' by the NXT color sensor. (Note: brick firmware 1.28 or greater is required for this function)
        
        The input parameter should be an NXT input port number between 1 and 4 (which the color sensor is plugged into).
        
        The mode parameter should be one of the following values:- “ColorDetect”, “LightSense”, “RedSense”, “GreenSense”, “BlueSense”.
        
        If the mode ColorDetect is chosen, then the returned values will be a number between 1 and 6 which represent the following colors: black, blue, green, yellow, red, white.
        
        You can use the ToColorName function to convert from these six values to a color name.
        
        If any of the other modes are chosen, then the result will be a color intensity value between 0 and 1023.

    .. js:function:: ReadDistanceSensor( input ) 

        Reads the distance measured by the ultrasonic sensor in centimeters.

        The input parameter should be an NXT input port number between 1 and 4 (which the ultrasonic sensor is plugged into).

    .. js:function:: ReadMail( mailbox, type, remove )   

        Reads a message from the NXT brick's mail box. This message can be written using a normal NXT-G program running on the brick. This allows you to read values from NXT-G programs with your phone or tablet.
        
        The mailbox parameter is the target mailbox number and can be a value between 1 and 10.
        
        The type parameter should be one of the following values:- “Text”, “Number” or “Logic” depending on what type of value you wish to read from the brick's mailbox.
        
        The remove parameter should be true if you wish to remove the message from the NXT's mailbox after reading it or false if you wish to leave the message in the mailbox.

    .. js:function:: ReadLightSensor( input, active )    

        Reads the intensity of the light currently being 'seen' by the NXT light sensor.
        
        The input parameter should be an NXT input port number between 1 and 4 (which the light sensor is plugged into).
        
        The active parameter should be set to true if you want the white light to be turned on during sensing and false if the light is not required.
        
        The returned value will be a light level value between 0 and 100.

    .. js:function:: ReadTouchSensor( input )    

        Reads the state of the NXT touch sensor, which will be true if the switch is currently pushed in and false otherwise.
        
        The input parameter should be an NXT input port number between 1 and 4 (which the touch sensor is plugged into).
        
        ReadSoundSensor(input,mode) Reads the sound pressure level (loudness) of the sound currently being 'heard' by the sound sensor (Note: Sound sensors are not included with the standard NXT kit)
        
        The input parameter should be an NXT input port number between 1 and 4 (which the sound sensor is plugged into).
        
        The mode parameter should be one of the following values:- “DB” or “DbA” depending if you want the returned value in standard Decibels or A-weighted Decibels.

    .. js:function:: RequestEnable() 

        Invokes system dialog box which could enable Bluetooth on tablet/phone when Bluetooth is disabled. If Bluetooth is enabled, this function doesn't invoke any visible dialog box.
        
        Be careful when checking Bluetooth state immediately after this function by calling IsEnabled or IsBluetoothEnabled, while RequestEnable doesn't stop program execution, and there is no SetOnRequestEnabled method called after this function invoke. This function is internally invoked by ShowDevices method when Bluetooth is disabled.

    .. js:function:: SendMail( mailbox, type, message)    

        Sends a message to the NXT brick's mail box. This message can be read using a normal NXT-G program running on the brick. This allows you to communicate with NXT-G programs from your phone or tablet.
        
        The mailbox parameter is the target mailbox number and can be a value between 1 and 10.
        
        The type parameter should be one of the following values:- “Text”, “Number” or “Logic” depending on what type of value you wish to send to the brick's mailbox.
    
    .. js:function:: SetInvert( boolean )    

        Provides a convenient way to invert the direction of the motor commands.
    
    .. js:function:: SetLampColor( input, color )    

        Commands the NXT brick to set the color sensor lamp to one of the following: 'White', 'Red', 'Green', 'Blue', 'Off'.
        
        The input parameter should be an NXT input port number between 1 and 4 (which the color sensor is plugged into).

    .. js:function:: SetOnConnect( myfunc )  

        The SetOnConnect function allows you to set the name of a function that you would like to be called when the NXT has been successfully connected via Bluetooth. Callback function returns status of connection (true if connection is successful, and false, if connection failed) and caller nxt object.
    
    .. js:function:: SetOnConnected( myfunc )    

        Allows you to set the name of a function that you would like to be called when the NXT has been successfully connected via Bluetooth.

    .. js:function:: ShowDevices()   

        Shows the user a dialog box that contains a list of NXT bricks which are paired with the phone. The user can then select the brick to connect to via Bluetooth.

    .. js:function:: StartProgram( program ) 

        Starts an NXT-G program (.rxe file) on the NXT brick (if the program is available on the brick).
        
        Note: This function will also launch .rso sound files.

    .. js:function:: Stop( motors )  

        Commands the NXT brick to Stop powering one or more of it's motors and allow them to coast to a halt.
        
        The motors parameter can be a single motor, for example just “A” or a combination of motors such as “ABC”.

    .. js:function:: StopProgram()   

        Stops the NXT-G program (.rxe file) which is currently running on the NXT brick.
    
    .. js:function:: ToColorName( colorNum ) 

        Function returns string with one of the six colors: black, blue, green, yellow, red, white converted from colorNum parameter.
        
        You can use the ToColorName function to convert value obtained from color sensor by method ReadColorSensor with mode set to ColorDetect.