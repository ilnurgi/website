app - Основной объект для работы, создания новых элементов
==========================================================

.. toctree::
   
   layout
   ui
   ui_dialog
   contacts_sms
   files_data

.. js:class:: app

    Глобальный объект, предоставляющий API для работы с Android устройством

    .. js:function:: _Extract(p1)


    .. js:function:: BluetoothList(p1)

        Возвращает :js:class:`BluetoothList`


    .. js:function:: BluetoothSerial(mode)

        :js:class:`BluetoothSerial`


    .. js:function:: Broadcast(p1, p2)
    

    .. js:function:: CheckLicense()

        The app.CheckLicense( key ) method will trigger a standard Google Play license check for the running application (if it is a paid App).
        
        You need to pass in the long key which can be found in the “Services and API's” section of the developer console.
        
        If the App is not licensed (for example someone just got hold of a copy of your APK and installed it) then it will show them a dialog asking them to purchase the App from Google Play and then close the App


    .. js:function:: CreateAudoRecorder()

        Возвращает :js:class:`AudioRecorder`, устройство для записи звуков

        .. code-block:: js
            
            recorder = app.CreateAudoRecorder()


    .. js:function:: CreateBluetoothSerial()

        :js:class:`BluetoothSerial`


    .. js:function:: CreateCrypt(options)

        Возвращает :js:class:`Crypt`

        .. code-block:: js
            
            crypt = app.CreateCrypt()


    .. js:function:: CreateDebug(debug text)    


    .. js:function:: CreateDownloader()

        :js:class:`Downloader`


    .. js:function:: CreateEmail(login, password)

        Возвращает :js:class:`Email`

        .. code-block:: js
            
            email = app.CreateEmail('mail@gmail.com', '123')


    .. js:function:: CreateImage(file, width, height, options, bitmapx, bitmapy)

        Возвращает :js:class:`Image`

        * `options`
            * `async` - FontAwesome Use this option to write icons as Text on your image

            * `Resize` - The Resize option internally scales down the original image to the display size, so it uses up less memory than the full size image (useful if you are lots of thumbnail images)

            * `ScaleCenter` - you can use the option to keep the image at it's original size and centered within the Image object

        .. code-block:: js
            
            // картинка из assets
            img = app.CreateImage('Img/myimage.png');
            
            // пустая картинка
            img = app.CreateImage(null, 0.8, 0.8);

            // с граниченным bitmap, 480-800
            canvas = app.CreateImage( null, 1.0, 1.0, "fix", 480, 800 );


    .. js:function:: CreateIOIO(p1)

        :js:class:`IOIO`


    .. js:function:: CreateLocator(type, p2)

        Возвращает :js:class:`Locator`

        “GPS”
        “Network”
        “GPS,Network”


        .. code-block:: js
            
            loc = app.CreateLocator('GPS,Network');

        
    .. js:function:: CreateMediaPleer()

        Возвращает :js:class:`MediaPlerr`, проигрывать музфкальных файлов

        .. code-block:: js
            
            player = app.CreateMediaPleer()


    .. js:function:: CreateMediaStore()

        Возвращает :js:class:`MediaStore`

        .. code-block:: js
            
            store = app.CreateMediaStore()


    .. js:function:: CreateNetClient(type)

        Возвращает :js:class:`NetClient`

        .. code-block:: js
            
            net = app.CreateNetClient('TCP');
            net = app.CreateNetClient('TCP,Raw');
            net = app.CreateNetClient('UDP');


    .. js:function:: CreateNxt()

        Creates the NXT object is used to manage the connection between your Android phone/tablet and the Lego Mindstorms NXT brick

        :js:class:`Nxt`


    .. js:function:: CreateNxtRemote()
        
        Internal NXTRemote object. Use NXT object from app.CreateNXT()

        :js:class:`NxtRemote`


    .. js:function:: CreateObject( name )

    .. js:function:: CreatePlayStore()

        Возвращает :js:class:`PlayStore`

        .. code-block:: js
            
            playstore = app.CreatePlayStore()


    .. js:function:: CreateSensor(type, options)

        Возвращает :js:class:`Sensor`

        * `type`

            * `Accelerometer` - 
            * `MagneticField` - 
            * `Light` - 
            * `Orientation` - 
            * `Proximity` - 
            * `Temperature`
            * `GameRotation`
            * `GeomagneticRotation`
            * `Gravity`
            * `Gyroscope`
            * `HeartRate`
            * `Acceleration`
            * `Pressure`
            * `Humidity`
            * `RotationMotion`
            * `StepCounter`
            * `StepDetector`

        * `options`

            * `Fast` - 
            * `Fastest` - 
            * `Medium` - 
            * `Slow` - 

        .. code-block:: js
            
            sns = app.CreateSensor( "Accelerometer" );
            sns.SetOnChange(function(x, y, z, time){});
            sns.Start();

            sns = app.CreateSensor( "Orientation" );
            sns.SetOnChange(function(azimuth, pitch, roll, time){});
            sns.Start();

            sns = app.CreateSensor( "Light" );
            sns.SetOnChange(function(lux){});
            sns.Start();  


    .. js:function:: CreateService( packageName, classname, callback, options )

        :js:class:`Service` 


    .. js:function:: CreateSmartWatch( p1 )

        :js:class:`SmartWatch`


    .. js:function:: CreateSpeechRec(options)

        Возвращает :js:class:`SpeechRec`, звукозапись

        .. code-block:: js

            speech = app.CreateSpeechRec();
            speech = app.CreateSpeechRec('NoBeep'); 


    .. js:function:: CreateSynth(p1)

        Возвращает :js:class:`Synth`, синтезатор

        .. code-block:: js
            
            synth = app.CreateSynth('VCF');
            synth = app.CreateSynth('Signal');


    .. js:function:: CreateSysProc(shell)

        :js:class:`Sys`


    .. js:function:: CreateUSBSerial(baudRate,dataBits,stopBits,parity)

        :js:class:`USBSerial`


    .. js:function:: CreateWebServer(port, options)

        Возвращает :js:class:`WebServer`

        .. code-block:: js
            
            webserver = CreateWebServer(8080, 'Upload,ListDir');
            webserver = CreateWebServer(8080, 'Reflect');


.. js:function:: Debug(text)

    .. js:function:: DisableKeys(keyList)

    .. js:function:: EnableBackKey(enable)

        Включает/выключает стандартное поведение кнопки назад. Если стандартное поведение выключено, будет вызываться глобальный метод :js:func:`OnBack`

        .. code-block:: js
            
            function OnStart(){
                app.EnableBackKey(false);
            }

            function OnBack(){
                ...
            }


    .. js:function:: Execute(code)

        This function is intended for use inside a WebView control to execute functions in the main script

        .. note:: 

            You should put quotes around the code you want executing too:
            
            .. code-block:: js
                
                app.Execute( "Alert( 'Hi' )" );
                app.Execute( "Alert( \"Hi\" )" );

    
    .. js:function:: Exit(p1)

        Завершает выполнение программы

        .. code-block:: js
            
            app.Exit()


    .. js:function:: GetAccounts()

    .. js:function:: GetAppName()

        Возвращает имя приложения

        .. code-block:: js
            
            name = app.GetAppName()


    .. js:function:: GetAppPath()

        Возвращает путь папки приложения

        .. code-block:: js
            
            app_path = app.GetAppPath()


    .. js:function:: GetBatteryLevel()

    .. js:function:: GetBuildNum()

    .. js:function:: GetClipboardText()

        Возвращает текст буфера обмена, для установки используйте :js:func:`SetClipboardText`

        .. code-block:: js
            
            text = app.GetClipboardText()

    .. js:function:: GetCountry()        

    .. js:function:: GetCountryCode()        

    .. js:function:: GetData( p1 )    

    .. js:function:: GetDatabaseFolder()

    .. js:function:: GetDefaultOrientation()            

        Возвращает стандртную ориентацию экрана: `Portrait` или `Landscape`, :js:func:`GetOrientation`, :js:func:`SetOrientation`

        .. code-block:: js
            
            orinet = app.GetDefaultOrientation()


    .. js:function:: GetDeviceId()

    .. js:function:: GetDisplayHeight()    

        Возвращает доступную высоту экрана в пикселях для вашего приложения, исключается верхняя и нижняя информационные поля.

        .. code-block:: js
            
            height = app.GetDisplayHeight()


    .. js:function:: GetDisplayWidth()    

        Возвращает доступную ширину экрана в пикселях для вашего приложения, исключается верхняя и нижняя информационные поля.

        .. code-block:: js
            
            width = app.GetDisplayWidth()


    .. js:function:: GetDSVersion()

    .. js:function:: GetEnv()

    .. js:function:: GetIntent()

        .. code-block:: js
    
            intent = app.GetIntent()
            /*
             * intent.action
             * intent.type
             * intent.data
             * intent.extras
             */

    
    .. js:function:: GetIPAddress()    

        Возвращает ip адрес вашего устройства, если включен WiFi

        .. code-block:: js
            
            ip = app.GetIPAddress()


    .. js:function:: GetJoystickName(joyNum)    

        Возвращает имя джойстика, подключенного к устройству через OTG

        .. code-block:: js
            
            joy_name = app.GetJoystickName(0)


    .. js:function:: GetJoystickState(joyNum, keyNum)    

        Возвращает состояние кнопки указанного джойстика, подключенного к устройству через OTG.

        1 - кнопка нажата, 0 - кнопка не нажата

        -1,0 ... 1,0 - для axis устройств. Например если для оси-х вернется -1,0 то значит влево, 1,0 -> вправо.
        
        axis - кнопки, могут быть от axis-0 до axis-9

        ============= ========
        Кнопка        Описание
        ============= ========
        "Up"          DPad Up
        "Down"        DPad Down
        "Left"        DPad Left
        "Right"       DPad Right
        "Center"      DPad Center
        "X", "Y", "Z" X, Y and Z Buttons
        "A", "B", "C" A, B and C Buttons
        "Start"       Start Button
        "ThumbLeft"   Left Thumb Buttons
        "ThumbRight"  Right Thumb Buttons
        ============= ========
        
        .. code-block:: js
            
            abtn = app.GetJoystickState( 0, "A" );
            bbtn = app.GetJoystickState( 0, "B" );
            xaxis = app.GetJoystickState( 0, "axis-0" );
            yaxis = app.GetJoystickState( 0, "axis-1" );


    .. js:function:: GetLanguage()       

    .. js:function:: GetLanguageCode()

    .. js:function:: GetMacAddress()

        Возвращает MAC адрес WiFi устройства

        .. code-block:: js
            
            mac = app.GetMacAddress()

    .. js:function:: GetMediaFile(“MyApp”,“.png”)

    .. js:function:: GetMetadata( file,keys )

    .. js:function:: GetModel()

        Возвращает идентификатор модели устройства

        .. code-block:: js
            
            model = app.GetModel()

    .. js:function:: GetName()       

    .. js:function:: GetObjects()    

        Returns all Objects of your App 

    .. js:function:: GetOptions()


    .. js:function:: GetOrientation()

        Возвращает текущую ориентацию экрана: `Portrait` или `Landscape`, :js:func:`GetDefaultOrientation`, :js:func:`SetOrientation`

        .. code-block:: js
            
            orient = app.GetOrientation()


    .. js:function:: GetOSVersion()

        Возвращает версию операционной системы

        =================== ============== =========
        Кодовое имя         Версия         API level
        =================== ============== =========
        (no code name)      1.0 API        level 1
        (no code name)      1.1 API        level 2
        Cupcake             1.5 API        level 3
        Donut               1.6 API        level 4
        Eclair              2.0 API        level 5
        Eclair              2.0.1          API level 6
        Eclair              2.1            API level 7
        Froyo               2.2.x          API level 8
        Gingerbread         2.3 - 2.3.2    API level 9
        Gingerbread         2.3.3 - 2.3.7  API level 10
        Honeycomb           3.0            API level 11
        Honeycomb           3.1            API level 12
        Honeycomb           3.2.x          API level 13
        Ice Cream Sandwich  4.0.1 - 4.0.2  API level 14
        Ice Cream Sandwich  4.0.3 - 4.0.4  API level 15
        Jelly Bean          4.1.x          API level 16
        Jelly Bean          4.2.x          API level 17
        Jelly Bean          4.3.x          API level 18
        KitKat              4.4 - 4.4.4    API level 19
        =================== ============== =========

        .. code-block:: js
            
            version = app.GetOSVersion()


    .. js:function:: GetPackageName()        

    .. js:function:: GetPath()

    .. js:function:: GetRingerMode()

    .. js:function:: GetRotation()

        Возвращает текущий угол поворота устройства: 0, 90, 180, 270

        .. code-block:: js
            
            rot = app.GetRotation()

    .. js:function:: GetRunningApps()

    .. js:function:: GetRunningServices()


    .. js:function:: GetScreenDensity()

        Возвращает плотность экрана устройства, dpi

        .. code-block:: js
            
            dpi = app.GetScreenDensity()


    .. js:function:: GetScreenHeight()

        Возвращает высоту экрана устрйоства

        .. code-block:: js
            
            dpi = app.GetScreenHeight()


    .. js:function:: GetScreenWidth()

        Возвращает ширину экрана устрйоства

        .. code-block:: js
            
            dpi = app.GetScreenWidth()


    .. js:function:: GetTop()

    .. js:function:: GetUser()

        Возвращает email адрес для главного пользователя

        .. code-block:: js
            
            user = app.GetUser()

    .. js:function:: GetUser()       

    .. js:function:: GetVersion()        

    .. js:function:: GetVolume(stream)   

        streams: alarm,dtmf,music,notification,ring,system,voicecall    1.25b

    .. js:function:: GoToSleep()

    .. js:function:: HideKeyboard( p1 )


    .. js:function:: IsBluetoothEnabled()


    .. js:function:: IsBluetoothOn()

        Возвращает булево, включен ли bluetooth

        .. code-block:: js
            
            bthOn = app.IsBluetoothOn()

    .. js:function:: IsBluetoothOn() Checks if Bluetooth is on.  

    .. js:function:: IsChrome()  detects running in arc welded chrome    1.23b

    .. js:function:: IsFolder( folder )  Checks if folder is a file or folder.   

    .. js:function:: IsKeyboardShown()       1.29

    .. js:function:: IsNewVersion()      

    .. js:function:: IsPro()


    .. js:function:: IsScreenOn()

        Возвращает булево, включен ли экран

        .. code-block:: js
            
            bthOn = app.IsScreenOn()
    
    .. js:function:: IsTablet()

        Возвращает булево, планшет ии смартфон

        .. code-block:: js
            
            tablet = app.IsTablet();

    .. js:function:: IsWifiEnabled()

    .. js:function:: KillApp( file )

    .. js:function:: LoadPlugin( url )

    .. js:function:: LoadScript( url, callback )

    .. js:function:: Odroid(p1,p2,p3)

    .. js:function:: OpenUrl(url)

        Открывает урл во внешенем web браузере

        .. code-block:: js
            
            app.OpenUrl('http://google.com');


    .. js:function:: PreventScreenLock(prevent)

        Разрешает/запрещает блокировку экрана

        .. code-block:: js
            
            app.PreventScreenLock(true);

    .. js:function:: PreventWifiSleep( p1 )

 
    .. js:function:: SendIntent(packageName, className, action, category, uri, type, extras )

        .. code-block:: js

            {
                var packageName = "com.google.android.gm";
                var className = "com.google.android.gm.ComposeActivityGmail";
                var action = "android.intent.action.VIEW";
                var category = null;
                var uri = "myfriend@gmail.com";
                var type = "message/rfc822";
                
                var extras = [ 
                    {name:"android.intent.extra.EMAIL", type:"list", value:"fred@gmail.com"},
                    {name:"android.intent.extra.SUBJECT", type:"string", value:"My subject"},
                    {name:"android.intent.extra.TEXT", type:"string", value:"Hello!"} 
                ];
                extras = JSON.stringify( extras );

                app.SendIntent( packageName, className, action, category, uri, type, extras ); 
            }
        
        
    .. js:function:: SendMail(address, subject, body, attachment)

        Отправляет email сообщение из доступного email аккаунта

        .. code-block:: js
            
            app.SendMail('ilnurgi87@gmail.com', 'MySubject', 'Hello', '/sdcard/file.txt')


    .. js:function:: SendMessage(msg)

    .. js:function:: SetAlarm(type, id, callback, time, interval)

        Вызывает указанный обработчик, в указанное время, миллисекунды, даже если приложение свернуто. 

        В обработчик передается указанный идентификатор.

        Все будильники выключается при перезагрузке

        .. code-block:: js
            
            // устанавливает однократный будильник
            app.SetAlarm("Set", 1, function(id){}, 12345645675);

            // устанавливает периодический будильник
            app.SetAlarm("Repeat", 1, function(id){}, 12345645675б 10000);

            // выключает будильник
            app.SetAlarm("Cancel", 1);


    .. js:function:: SetAutoBoot(TrueFalse) 

        Calling app.SetAutoBoot( true ) method will cause DroidScript to be started automatically when your device boots. 
        
        The method will also work in your own apps if you build APKs.   

    .. js:function:: SetAutoWifi(TrueFalse)  

        The app.SetAutoWifi( true ) method will cause DroidScript to turn on the WiFi editor automatically  

    .. js:function:: SetBluetoothEnabled(enable)

    .. js:function:: SetClipboardText(text)

        Вставляет в буфер обмена текст, для получения используйте :js:func:`GetClipboardText`  

        .. code-block:: js
            
            app.SetClipboardText('my text');


    .. js:function:: SetData( name,value )

    .. js:function:: SetDebugEnabled(enabled)

        Включает/выключает вывод в лог IDE отладочной информации

        .. code-block:: js
            
            app.SetDebugEnabled(false);


    .. js:function:: SetJoystickOptions( options )

    .. js:function:: SetOnBroadcast( callback )      

    .. js:function:: SetOnError( callback )      

    .. js:function:: SetOnKey(callback)  reports key changes, including volume key   1.29

    .. js:function:: SetOptions(options)


    .. js:function:: SetOrientation(orientation, callback)

        Устанавливает ориентацию экрана: Portrait или Landscape. :js:func:`GetDefaultOrientation`, :js:func:`GetOrientation`

        .. code-block:: js

            app.SetOrientation("Landscape");
            
    
    .. js:function:: SetRingerMode( mode )  

        use Normal, Vibrate or Silent to set the model

    .. js:function:: SetScreenBrightness(brightness)

        Устанавливает яркость экрана

        .. code-block:: js
            
            app.SetScreenBrightness(0.25);
            
    
    .. js:function:: SetScreenMode(mode)

        Устанавливает тип экрана: `Full`, `Game`, Normal, Default

        .. code-block:: js
            
            app.SetScreenMode('Full');

    .. js:function:: SetSharedApp( p1 )      

    .. js:function:: SetTitle( p1 )  This method is obsolete

    .. js:function:: SetVolume(type, val)

        Устанавливает уровень громкости

        .. code-block:: js
            
            app.SetVolume('System', 1);


    .. js:function:: SetWifiEnabled(enable)      

    .. js:function:: ShowDebug( p1 )     

    .. js:function:: ShowKeyboard( ctrl )    ctrl must already have focus    1.29

    .. js:function:: ShowMenu( p1,p2 )   This Sample demonstrates how to show the menu

    .. js:function:: SimulateTouch( obj,x,y,dir )    This Sample shows how to use SimulateTouch  

    .. js:function:: StartApp( file,options )    Starts DroidScript application from script in file. File is the fullpath to the app. Parameter options is optional. 

    .. js:function:: StartDebugServer()      

    .. js:function:: StartService(packageName,className)     

    .. js:function:: StopApp( file ) Stops DroidScript application from script in file. File is the fullpath to the app. 

    .. js:function:: StopService()


    .. js:function:: TextToSpeech(text, pitch, speed, callback)

        Произносит указанный тект

        .. code-block:: js
            
            app.TextToSpeech('Hello World', 1.0, 1.0, function(){});


    .. js:function:: ToBack()

        Сврпачивает приложение 


    .. js:function:: Try(p1, p2, p3)


    .. js:function:: Vibrate(pattern)

        Включает вибрацию по указанному паттерну

        .. code-block:: js
            
            app.Vibrate('0,100,30,100,50,300')


    .. js:function:: Wait(secs)

        is not recomendedee