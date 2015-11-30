app - главный объект для работы
===============================

.. js:class:: app

    Глобальный объект, приложение.


    .. js:function:: _Extract(p1)

    .. js:function:: AddLayout(layout)

        Добавляет в приложение контейнер, для удаления используйте :js:func:`RemoveLayout`

        * `layout` - :js:class:`Layout`


    .. js:function:: Alert(text, title)

        Отображает информационное окно

        .. code-block:: js
            
            app.Alert('Hello World!', 'Message');


    .. js:function:: BluetoothList(p1)

        Возвращает :js:class:`BluetoothList`


    .. js:function:: BluetoothSerial(mode)

        :js:class:`BluetoothSerial`


    .. js:function:: Broadcast(p1, p2)

    .. js:function:: Call(number)

    .. js:function:: CheckLicense()

        The app.CheckLicense( key ) method will trigger a standard Google Play license check for the running application (if it is a paid App).
        
        You need to pass in the long key which can be found in the “Services and API's” section of the developer console.
        
        If the App is not licensed (for example someone just got hold of a copy of your APK and installed it) then it will show them a dialog asking them to purchase the App from Google Play and then close the App


    .. js:function:: ClearData(file)

        clears app.SaveText/SaveNumber..etc 

    .. js:function:: CopyFile(src, dst)

        :js:func:`CopyFolder`, :js:func:`DeleteFile`, :js:func:`deleteFolder`, :js:func:`FileExists`, :js:func:`FolderExists`


    .. js:function:: CopyFolder(src, dst, overwrite)

    .. js:function:: CreateAudoRecorder()

        Возвращает :js:class:`AudioRecorder`, устройство для записи звуков

        .. code-block:: js
            
            recorder = app.CreateAudoRecorder()


    .. js:function:: CreateBluetoothSerial()

        :js:class:`BluetoothSerial`
    .. js:function:: CreateButton(text, width, height, options)

        Возвращает :js:class:`Button`

        * `text` - надпись на кнопке, для HTML кнопки можно прямо html писать

        * `width` - ширина кнопки, -1 если не надо учитывать

        * `height` - высота кнопки, -1 если не надо учитывать

        * `options` - доп опции кнопки

            * `Alum` - 

            * `Custom` - настриваемая иконка
            
            * `FillX` - расстянуть по ширине родителя

            * `FillY` - расстянуть по высоте родителя

            * `FillXY` - расстянуть по родителю

            * `Gray` - 

            * `HTML` - html кнопка
            * `NoSound`

        .. code-block:: js
            
            button = app.CreateButton('A', 0.2, 0.2)
            button = app.CreateButton('A', -1, -1, 'FillX')
            button = app.CreateButton('A', -1, -1, 'FillX,Gray')
            button = app.CreateButton('A', -1, -1, 'FillX,Alum')
            button = app.CreateButton('<b>Text</b>', -1, -1, 'HTML')


    .. js:function:: CreateCameraView(width, height, options)

        Возвращает :js:class:`CameraView`

        * `options`

            * `CIF`
            * `QVGA`
            * `SVGA`
            * `VGA`
            * `XGA`
            * `UXGA`


        .. code-block:: js
            
            cam = app.CreateCameraView()
            cam = app.CreateCameraView('Front')
            cam = app.CreateCameraView(0.5, 0.7, 'CIF')

            cam = app.CreateCameraView( 0.8, 0.4 );
            lay.AddChild( cam );
            setTimeout( "cam.StartPreview()", 1000 );


    .. js:function:: CreateCheckBox(text, width, height, options)

        Возвращает :js:class:`CheckBox`

        .. code-block:: js
            
            check_box = app.CreateCheckBox('CheckBox');


    .. js:function:: CreateCrypt(options)

        Возвращает :js:class:`Crypt`

        .. code-block:: js
            
            crypt = app.CreateCrypt()


    .. js:function:: CreateDebug(debug text)


    .. js:function:: CreateDialog(title, options)

        Возвращает :js:class:`Dialog`, компонент диалога.

        If you add the “NoCancel” in options to the CreateDialog method, it will prevent back keys and touches outside the dialog area from closing the dialog. You can then add a “OK” or “Close” button to the dialog, so you can close the dialog manually by calling the dlg.Hide() or dlg.Dismiss() methods. There is also a “NoTitle” option

        * `options`

            * `NoCancel`
            * `NoTitle`

        .. code-block:: js
            
            dlgL = app.CreateDialog('Chose item');


    .. js:function:: CreateDownloader()

        :js:class:`Downloader`


    .. js:function:: CreateEmail(login, password)

        Возвращает :js:class:`Email`

        .. code-block:: js
            
            email = app.CreateEmail('mail@gmail.com', '123')


    .. js:function:: CreateFile(file, mode)

        :js:class:`File`


    .. js:function:: CreateGLView(width, height, option)

        Возвращает :js:class:`GLView`

        .. code-block:: js
            
            glview = app.CreateGLView( 1, 1, "Fast2d" );            


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


    .. js:function:: CreateLayout(type, options)

        Возвращает :js:class:`Layout`

        По умлочанию:

            * контейнер прозрачный
            * объекты внутри контейнера будут уцентрироваться и заполняться сверху

        * `type` - тип контейнера

            * `Linear` - контейнер, объекты внутри контейнера размещаются линейно

                * `Vertical` - объекты внутри контейнера распологаются вертикально в линию

                * `Horizontal` - объекты внутри контейнера распологаются горизонтально в линию

            * `Frame` - контейнер, который используется при отображении данных впереди или позади чего-то

            * `Absolute` - абсолютный контейнер, игнорирует все настройки выранивания

        * `options` - доп настройки контейнера

            * `Bottom`

            * `Center`

            * `FillX`

            * `FillXY` - контейнер заполняет родителя по оси х, у.

            * `FillY`

            * `Horizontal`

            * `Left`        
            
            * `Right`        
                    
            * `Top`

            * `TopCenter` - default

            * `TouchThrough`

            * `VCenter` - объекты внутри контейнера центрируются вертикально  

        .. code-block:: js
            
            lay = app.CreateLayout('Linear', 'VCenter,FillXY');
            lay = app.CreateLayout('Linear', 'Vertical');
            lay = app.CreateLayout('Linear', 'Horizontal,FillXY');
            lay = app.CreateLayout('Frame');


    .. js:function:: CreateList(list, width, height, options)

        Возвращает :js:class:`List`

        Элемент списка может содержать различные компоненты, и тогда он должен описываться в виде `title:icon` или `title:body:extra:icon`. Иконка может быть как абсолютным путем, так и быть одним из зарезервированных слов `folder, audiofolder, photofolder, videofolder, audio, photo, video and playlist`

        Также можно создать список из кнопок, укзав доп параметры: `AlumButton, GreenButton, OrangeButton, WhiteGrad, FontAwesome`

        .. code-block:: js
            
            lst = app.CreateList('1,2,3', 0.8, 0.4)
            lst = app.CreateList('Folder:folder,Audio:audio,Photo:photo,Video:video', 0.8, 0.4)
            lst = app.CreateList( data, 0.8, 0.8, "OrangeButton" );

            var list = "[fa-file-text-o] Text, " +
                       "[fa-file-photo-o] Photo, " + 
                       "[fa-file-audio-o] Sound, " +
                       "[fa-file-video-o] Video";
            lst = app.CreateList( list, 0.8, 0.25, "FontAwesome" );


    .. js:function:: CreateListDialog(title, list, options)

        Возвращает :js:class:`ListDialog`

        .. code-block:: js
            
            dlg = app.CreateListDialog('Choises', 'Add,Remove')
            dlg = app.CreateListDialog('Choises', 'Add,Remove', 'Multi')


    .. js:function:: CreateListView(list, title, options)

        Возвращает :js:class:`ListView`

        .. code-block:: js
            
            lvw = app.CreateListView( "Mon,Tues,Wed,Thurs,Fri,Sat,Sun", "Days" );


    .. js:function:: CreateLocator(type, p2)

        Возвращает :js:class:`Locator`

        “GPS”
        “Network”
        “GPS,Network”


        .. code-block:: js
            
            loc = app.CreateLocator('GPS,Network');


    .. js:function:: CreateNetClient(type)

        Возвращает :js:class:`NetClient`

        .. code-block:: js
            
            net = app.CreateNetClient('TCP');
            net = app.CreateNetClient('TCP,Raw');
            net = app.CreateNetClient('UDP');


    .. js:function:: CreateNotification(options)

        Возвращает :js:class:`Notification`

        Ongoing     This option creats an ongoing notification in the status bar

        .. code-block:: js
            
            // простое уведомление
            notify = app.CreateNotification();

            // уведомление пропадет после прочтения
            notify = app.CreateNotification('AutoCancel');

            // ???
            notify = app.CreateNotification('AutoCancel,FullScreen');


    .. js:function:: CreateNxt()

        Creates the NXT object is used to manage the connection between your Android phone/tablet and the Lego Mindstorms NXT brick


    .. js:function:: CreateNxtRemote()
        
        Internal NXTRemote object. Use NXT object from app.CreateNXT()

        :js:class:`NxtRemote`

        
    .. js:function:: CreateMediaPleer()

        Возвращает :js:class:`MediaPlerr`, проигрывать музфкальных файлов

        .. code-block:: js
            
            player = app.CreateMediaPleer()


    .. js:function:: CreateMediaStore()

        Возвращает :js:class:`MediaStore`

        .. code-block:: js
            
            store = app.CreateMediaStore()


    .. js:function:: CreateObject( name )

    .. js:function:: CreatePlayStore()

        Возвращает :js:class:`PlayStore`

        .. code-block:: js
            
            playstore = app.CreatePlayStore()
            


    .. js:function:: CreateSeekBars(width, height)

        Возвращает :js:class:`SeekBars`

        .. code-block:: js
            
            sb = app.CreateSeekBars(0.8)


    .. js:function:: CreateSensor(type, options)

        Возвращает :js:class:`Sensor`

        * `type`

            * `Accelerometer` - 
            * `MagneticField` - 
            * `Light` - 
            * `Orientation` - 
            * `Proximity` - 

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


    .. js:function:: CreateScroller(width, height, options)

        Возвращает :js:class:`Scroller`

        .. code-block:: js
            
            function OnStart() {
              lay = app.CreateLayout( "Linear", "FillXY" );

              scroll = app.CreateScroller( 1.0, 1.0 );
              lay.AddChild( scroll );

              layScroll = app.CreateLayout( "Linear", "Left" );
              scroll.AddChild( layScroll );

              img = app.CreateImage( "/Sys/Img/Hello.png", 2.0, 2.0 );
              layScroll.AddChild( img );

              app.AddLayout( lay );
            }       

    .. js:function:: CreateSMS()

        Возвращает :js:class:`SMS`

        .. code-block:: js
            
            sms = app.CreateSMS()


    .. js:function:: CreateSpeechRec()

        Возвращает :js:class:`SpeechRec`, звукозапись

        .. code-block:: js

            speech = app.CreateSpeechRec();
            speech = app.CreateSpeechRec('NoBeep');            
            
            
    .. js:function:: CreateSpinner(list, width, height, options)

        Возвращает :js:class:`Spinner`

        .. code-block:: js
            
            spin = app.CreateSpinner( "Bilbo,Frodo,Gandalf", 0.4 );
            
    .. js:function:: CreateSynth()

        Возвращает :js:class:`Synth`, синтезатор

        .. code-block:: js
            
            synth = app.CreateSynth('VCF');
            synth = app.CreateSynth('Signal');


    .. js:function:: CreateTabs(tabs, width, height, options)

        Возвращает :js:class:`Tabs`, вкладки

        .. code-block:: js
            
            tabs = app.CreateTabs('FRED,BILL,MARK', 0.8, 0.8, 'VCenter');


    .. js:function:: CreateText(text, width, height, options)

        Возвращает :js:class:`Text`

        * `options` 

            * `Multiline`

            * `Left`

            * `Right`

        .. code-block:: js
            
            text = app.CreateText('Hello');
            text = app.CreateText('Hello', 0.8, 0.2, 'Multiline');
            txt = app.CreateText("[fa-cogs] Settings", 0.8, 0.1, "FontAwesome");
            txt = app.CreateText("[fa-heart] Settings", 0.8, 0.1, "FontAwesome");
            txt = app.CreateText("[fa-pause] Settings", 0.8, 0.1, "FontAwesome");
            txt = app.CreateText("[fa-facebook-square] Settings", 0.8, 0.1, "FontAwesome");
            txt = app.CreateText("[fa-google-plus-square] Settings", 0.8, 0.1, "FontAwesome");
            txt = app.CreateText("[fa-twitter] Settings", 0.8, 0.1, "FontAwesome");
            txt = app.CreateText("\uf04c Settings", 0.8, 0.1, "FontAwesome");
            txt = app.CreateText("<font color=#008800>[fa-check-square-o]</font> Done", 0.8, 0.1, "FontAwesome,HTML");
            txt = app.CreateText("<font color=#008800>[fa-square-o]</font> Done", 0.8, 0.1, "FontAwesome,HTML");


    .. js:function:: CreateTextEdit(text, width, height, options)

        Возвращает :js:class:`TextEdit`

        .. code-block:: js
            
            txtedit = app.CreateTextEdit('edit')


    .. js:function:: CreateToggle(text, width, height, options)

        Возвращает :js:class:`ButtonToggle`

        .. code-block:: js
            
            btn = app.CreateToggle('toggle me')


    .. js:function:: CreateUSBSerial()

        :js:class:`USBSerial`


    .. js:function:: CreateVideoView(widrh, heigth, options)

        Возвращает :js:class:`VideoView`. Проигрыватель видео

        .. code-block:: js
            
            video = app.CreateVideoView()


    .. js:function:: CreateWebServer(port, options)

        Возвращает :js:class:`WebServer`

        .. code-block:: js
            
            webserver = CreateWebServer(8080, 'Upload,ListDir');


    .. js:function:: CreateWebView(width, height)

        Возвращает :js:class:`WebView`

        .. code-block:: js
            
            web = app.CreateWebView()


    .. js:function:: CreateYesNoDialog(msg)

        Возвращает :js:class:`YesNoDialog`

        .. code-block:: js
            
            yesNo = app.CreateYesNoDialog('Yes?')


    .. js:function:: CreateZipUtil()

        Возвращает :js:class:`ZipUtil`


    .. js:function:: Exit()

        Завершает выполнение программы

        .. code-block:: js
            
            app.Exit()


    .. js:function:: DeleteFile(fileName)

        Удаляет файл по указанному пути

        .. code-block:: js
            
            app.DeleteFile('/sdcard/file.txt');


    .. js:function:: DeleteFolder(folderName)

        Удаляет папку по указанному пути

        .. code-block:: js
            
            app.DeleteFile('/sdcard/files');


    .. js:function:: EnableBackKey(enable)

        Включает/выключает стандартное поведение кнопки назад. Если стандартное поведение выключено, будет вызываться глобальный метод :js:func:`OnBack`

        .. code-block:: js
            
            function OnStart(){
                app.EnableBackKey(false);
            }

            function OnBack(){
                ...
            }


    .. js:function:: FileExists(fileName)

        Возвращает булево, существет ли файл по указанному пути

        .. code-block:: js
            
            app.FileExists('/sdcard/file.txt')


    .. js:function:: FolderExists(folderName)

        Возвращает булево, существет ли папка по указанному пути

        .. code-block:: js
            
            app.FolderExists('/sdcard/files')


    .. js:function:: GetAppName()

        Возвращает имя приложения

        .. code-block:: js
            
            name = app.GetAppName()


    .. js:function:: GetAppPath()

        Возвращает путь папки приложения

        .. code-block:: js
            
            app_path = app.GetAppPath()


    .. js:function:: GetClipboardText()

        Возвращает текст буфера обмена, для установки используйте :js:func:`SetClipboardText`

        .. code-block:: js
            
            text = app.GetClipboardText()


    .. js:function:: GetDefaultOrientation()            

        Возвращает стандртную ориентацию экрана: `Portrait` или `Landscape`, :js:func:`GetOrientation`, :js:func:`SetOrientation`

        .. code-block:: js
            
            orinet = app.GetDefaultOrientation()


    .. js:function:: GetDisplayHeight()    

        Возвращает доступную высоту экрана в пикселях для вашего приложения, исключается верхняя и нижняя информационные поля.

        .. code-block:: js
            
            height = app.GetDisplayHeight()


    .. js:function:: GetDisplayWidth()    

        Возвращает доступную ширину экрана в пикселях для вашего приложения, исключается верхняя и нижняя информационные поля.

        .. code-block:: js
            
            width = app.GetDisplayWidth()


    .. js:function:: GetExternalFolder()    

        Возвращает путь до флешки, microsd карточки

        .. code-block:: js
            
            external_path = app.GetExternalFolder()


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


    .. js:function:: GetLastButton()

        Возвращает :js:class:`Button`, последнюю нажатую кнопку

        .. code-block:: js
            
            btn = app.GetLastButton()


    .. js:function:: GetLastImage()

        Возвращает :js:class:`Image`, последнюю нажатую картинку

        .. code-block:: js
            
            image = app.GetLastImage()


    .. js:function:: GetLastToggle()

        Возвращает :js:class:`ButtonToggle`, последнюю нажатую toggle кнопку

        .. code-block:: js
            
            tglbutton = app.GetLastToggle()


    .. js:function:: GetMacAddress()

        Возвращает MAC адрес WiFi устройства

        .. code-block:: js
            
            mac = app.GetMacAddress()


    .. js:function:: GetModel()

        Возвращает идентификатор модели устройства

        .. code-block:: js
            
            model = app.GetModel()


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


    .. js:function:: GetPrivateFolder(fldrName)

        Создает и возвращает путь до приватной папки, доступной только для приложения

        .. code-block:: js
             
            fldr = app.GetPrivateFolder('myfolder');


    .. js:function:: GetRotation()

        Возвращает текущий угол поворота устройства: 0, 90, 180, 270

        .. code-block:: js
            
            rot = app.GetRotation()


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


    .. js:function:: GetSharedFiles()

    .. js:function:: GetSharedText()

    .. js:function:: GetUser()

        Возвращает email адрес для главного пользователя

        .. code-block:: js
            
            user = app.GetUser()


    .. js:function:: HideProgress()

        Скрывает показанные прогресс, :js:func:`ShowProgress`

        .. code-block:: js
            
            app.HideProgress();


    .. js:function:: HideProgressBar()

        Скрывает показанные прогрессбар, :js:func:`ShowProgressBar`, :js:func:`UpdateProgressBar`

        .. code-block:: js
            
            app.HideProgressBar();


    .. js:function:: IsTablet()

        Возвращает булево, планшет ии смартфон

        .. code-block:: js
            
            tablet = app.IsTablet();


    .. js:function:: IsBluetoothOn()

        Возвращает булево, включен ли bluetooth

        .. code-block:: js
            
            bthOn = app.IsBluetoothOn()


    .. js:function:: IsScreenOn()

        Возвращает булево, включен ли экран

        .. code-block:: js
            
            bthOn = app.IsScreenOn()


    .. js:function:: ListFolder(path, filter, limit)

        Возвращает список файлов в указанной папке

        .. code-block:: js
            
            files = app.ListFolder('/sdcard/');
            files = app.ListFolder('/sdcard/', '.mp3');
            files = app.ListFolder('/sdcard/', '.mp4', 10);


    .. js:function:: LoadBoolean(valueName, default, id)

        Загружает параматеры из пользовательской памяти, для сохранения используйте :js:func:`SaveBoolean`

        * `valueName` - имя параметра

        * `default` - значение по умолчанию

        * `id` - идентификатор, для расшаривания атрибута между прилоэениями

        .. code-block:: js
            
            bol = app.LoadBoolean('MyName', true);


    .. js:function:: LoadNumber(valueName, default, id)

        Загружает параматеры из пользовательской памяти, для сохранения используйте :js:func:`SaveNumber`

        * `valueName` - имя параметра

        * `default` - значение по умолчанию

        * `id` - идентификатор, для расшаривания атрибута между прилоэениями

        .. code-block:: js
            
            num = app.LoadNumber('MyName', 42);


    .. js:function:: LoadText(valueName, default, id)

        Загружает параматеры из пользовательской памяти, для сохранения используйте :js:func:`SaveText`

        * `valueName` - имя параметра

        * `default` - значение по умолчанию

        * `id` - идентификатор, для расшаривания атрибута между прилоэениями

        .. code-block:: js
            
            name = app.LoadText('MyName', 'Bill');


    .. js:function:: MakeFolder(folder_path)

        Создает папку по указанному пути

        .. code-block:: js
            
            app.MakeFolder('/sdcard/ilnurgi/')


    .. js:function:: OpenDatabase(dbName)

        Возвращает :js:class:`Database`

        .. code-block:: js
            
            db = app.OpenDatabase('MyDB');


    .. js:function:: OpenFile(fileName, type, promt)

        Открыват файл в другой программе

        .. code-block:: js
            
            app.OpenFile('/sdcard/text/txt', 'text/plain', 'Choose Editor')


    .. js:function:: OpenUrl(url)

        Открывает урл во внешенем web браузере

        .. code-block:: js
            
            app.OpenUrl('http://google.com');


    .. js:function:: PreventScreenLock(prevent)

        Разрешает/запрещает блокировку экрана

        .. code-block:: js
            
            app.PreventScreenLock(true);


    .. js:function:: ReadFile(fileName)

        Возвращает содержимое файла

        .. code-block:: js
            
            txt = app.ReadFile('/sdcard/text.txt');


    .. js:function:: RemoveLayout(layout)

        Удаляет указанный контейнер, для добавления используйте :js:func:`AddLayout`


    .. js:function:: RenameFile(fileName, newFileName)

        Переименовывает файл

        .. code-block:: js
            
            app.RenameFile('/sdcard/text.txt', '/sdcard/newtext.txt');


    .. js:function:: RenameFolder(folderName, newFolderName)

        Переименовывает папку

        .. code-block:: js
            
            app.RenameFolder('/sdcard/text', '/sdcard/newtext');


    .. js:function:: SaveBoolean(valueName, value, id)

        Сохраняет параматеры в пользовательскую память, для получения используйте :js:func:`LoadBoolean`

        * `valueName` - имя параметра

        * `value` - значение

        * `id` - идентификатор, для расшаривания атрибута между прилоэениями

        .. code-block:: js
            
            app.SaveBoolean('MyName', true);


    .. js:function:: SaveNumber(valueName, value, id)

        Сохраняет параматеры в пользовательскую память, для получения используйте :js:func:`LoadNumber`

        * `valueName` - имя параметра

        * `value` - значение

        * `id` - идентификатор, для расшаривания атрибута между прилоэениями

        .. code-block:: js
            
            app.SaveNumber('MyName', 42);


    .. js:function:: SaveText(valueName, value, id)

        Сохраняет параматеры в пользовательскую память, для получения используйте :js:func:`LoadText`

        * `valueName` - имя параметра

        * `value` - значение

        * `id` - идентификатор, для расшаривания атрибута между прилоэениями

        .. code-block:: js
            
            app.SaveText('MyName', '123');


    .. js:function:: SendFile(filenam, dstName, title)

        Send a file to another App (users choice).

        .. code-block:: js
            
            app.SendFile( file, "sftest.txt", "Send File" );


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


    .. js:function:: SetAlarm(type, id, callback, timeout, periodic)

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


    .. js:function:: SetClipboardText(text)

        Вставляет в буфер обмена текст, для получения используйте :js:func:`GetClipboardText`  

        .. code-block:: js
            
            app.SetClipboardText('my text');


    .. js:function:: SetDebugEnabled(enabled)

        Включает/выключает вывод в лог IDE отладочной информации

        .. code-block:: js
            
            app.SetDebugEnabled(false);


    .. js:function:: SetMenu(menuList)

        Устанавливает элементы в меню, обработчиком выбора при этом будет :js:func:`OnMenu`, в который будет передаваться выбраннный элемент. 

        На некоторых устройствах кнопки меню нет, при необходимости можно нарисовать кнопку меню и при нажатии на него вызывать :js:func:`ShowMenu`

        .. code-block:: js
            
            function OnStart() {
                app.SetMenu( "Start,Stop,Pause" );
            }

            function OnMenu( item ) {
              app.ShowPopup( item, "Short" );
            }   


    .. js:function:: SetOrientation(orientation, callback)

        Устанавливает ориентацию экрана: Portrait или Landscape. :js:func:`GetDefaultOrientation`, :js:func:`GetOrientation`

        .. code-block:: js

            app.SetOrientation("Landscape");
            
    
    .. js:function:: SetScreenBrightness(brightness)

        Устанавливает яркость экрана

        .. code-block:: js
            
            app.SetScreenBrightness(0.25);
            
    
    .. js:function:: SetScreenMode(mode)

        Устанавливает тип экрана: `Full`, `Game`

        .. code-block:: js
            
            app.SetScreenMode('Full');


    .. js:function:: SetVolume(type, val)

        Устанавливает уровень громкости

        .. code-block:: js
            
            app.SetVolume('System', 1);


    .. js:function:: ShowPopup(text, options)

        Отображает всплывающее сообщение

        * `options`

            * `Short`
            * `Bottom`

        .. code-block:: js
            
            app.ShowPopup('Hello World', 'Bottom,Short');


    .. js:function:: ShowProgress(text)

        Отображает прогресс с текстом, :js:func:`HideProgress`

        .. code-block:: js
            
            app.ShowProgress('Loading ...');
            setTimeout('app.HideProgress()', 3000);


    .. js:function:: ShowProgressBar(text)

        Отображает прогрессбар с текстом, :js:func:`HideProgressBar`, :js:func:`UpdateProgressBar`

        .. code-block:: js
            
            app.ShowProgressBar('Loading ...');
            setTimeout('app.HideProgressBar()', 3000);


    .. js:function:: TextToSpeech(text, pitch, speed, callback)

        Произносит указанный тект

        .. code-block:: js
            
            app.TextToSpeech('Hello World', 1.0, 1.0, function(){});


    .. js:function:: UpdateProgressBar(progress)

        Включает вибрацию по указанному паттерну, :js:func:`ShowProgressBar`, :js:func:`HideProgressBar`

        .. code-block:: js
            
            app.UpdateProgressBar(60);


    .. js:function:: Vibrate(pattern)

        Включает вибрацию по указанному паттерну

        .. code-block:: js
            
            app.Vibrate('0,100,30,100,50,300')


    .. js:function:: WriteFile(fileName, text, mode)

        Пишет данные в файл

        .. code-block:: js
            
            app.WriteFile('/sdcard/text.txt', 'Hello', 'Append');