Создание графического интерфейса
================================

Большинство объектов создаются одинаково. 

Можно задать высоту и ширину объекта, либо указать -1, для игнорирования параметра.

В качестве доп опции задаются: :ref:`component_align`


.. js:function:: app.CreateButton(text, width, height, options)

    Возвращает :js:class:`Button`, кнопка

    * `options` - :ref:`component_align`

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


.. js:function:: app.CreateCameraView(width, height, options)

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


.. js:function:: app.CreateCheckBox(text, width, height, options)

    Возвращает :js:class:`CheckBox`

    .. code-block:: js
        
        check_box = app.CreateCheckBox('CheckBox');


.. js:function:: app.CreateGLView(width, height, option)

    Возвращает :js:class:`GLView`

    .. code-block:: js
        
        glview = app.CreateGLView( 1, 1, "Fast2d" ); 


.. js:function:: app.CreateList(list, width, height, options)

    Возвращает :js:class:`List`

    Элемент списка может содержать различные компоненты, и тогда он должен описываться в виде `title:icon` или `title:body:extra:icon`. 

    Иконка может быть как абсолютным путем, так и быть одним из зарезервированных слов `folder, audiofolder, photofolder, videofolder, audio, photo, video and playlist`

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


.. js:function:: app.CreateListView(list, title, options)

    Возвращает :js:class:`ListView`

    .. code-block:: js
        
        lvw = app.CreateListView( "Mon,Tues,Wed,Thurs,Fri,Sat,Sun", "Days" );


.. js:function:: app.CreateScroller(width, height, options)

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
        

.. js:function:: app.CreateSeekBars(width, height, options)

    Возвращает :js:class:`SeekBars`

    .. code-block:: js
        
        sb = app.CreateSeekBars(0.8)


.. js:function:: app.CreateSpinner(list, width, height, options)

    Возвращает :js:class:`Spinner`

    .. code-block:: js
        
        spin = app.CreateSpinner( "Bilbo,Frodo,Gandalf", 0.4 );
        

.. js:function:: app.CreateTabs(tabs, width, height, options)

    Возвращает :js:class:`Tabs`, вкладки

    .. code-block:: js
        
        tabs = app.CreateTabs('FRED,BILL,MARK', 0.8, 0.8, 'VCenter');


.. js:function:: app.CreateText(text, width, height, options)

    Возвращает :js:class:`Text`, текстовое поле для отображения.

    В тексте можно указать иконку :ref:`icons`

    * `options` - :ref:`component_align`

        * `Multiline` - многострочный

    .. code-block:: js
        
        text = app.CreateText('Hello');
        text = app.CreateText('Hello', 0.8, 0.2, 'Multiline');
        txt = app.CreateText("[fa-cogs] Settings", 0.8, 0.1, "FontAwesome");        
        txt = app.CreateText("\uf04c Settings", 0.8, 0.1, "FontAwesome");
        txt = app.CreateText("<font color=#008800>[fa-check-square-o]</font> Done", 0.8, 0.1, "FontAwesome,HTML");


.. js:function:: app.CreateTextEdit(text, width, height, options)

    Возвращает :js:class:`TextEdit`

    * `options`
        * `AutoScale` - reduces text size to fit if needed
        * `Bold` - Write bold Text
        * `FontAwesome` - Use this to display Icons 
        * `from` - this inbuilt font
        * `Html` -     
        * `Left` -     
        * `Multiline` -    
        * `Right` - 

    .. code-block:: js
        
        txtedit = app.CreateTextEdit('edit')


.. js:function:: app.CreateToggle(text, width, height, options)

    Возвращает :js:class:`ButtonToggle`

    .. code-block:: js
        
        btn = app.CreateToggle('toggle me')


.. js:function:: app.CreateVideoView(widrh, heigth, options)

    Возвращает :js:class:`VideoView`. Проигрыватель видео

    .. code-block:: js
        
        video = app.CreateVideoView()


.. js:function:: app.CreateWebView(width, height, options, zoom)

    Возвращает :js:class:`WebView`

    * `options`
        * `IngoreErrors`
        * `NoScrollBars`
        * `ScrollFade`

    .. code-block:: js
        
        web = app.CreateWebView()


.. js:function:: app.GetLastButton()

    Возвращает :js:class:`Button`, последнюю нажатую кнопку

    .. code-block:: js
        
        btn = app.GetLastButton()


.. js:function:: app.GetLastCheckBox()


.. js:function:: app.GetLastImage()

    Возвращает :js:class:`Image`, последнюю нажатую картинку

    .. code-block:: js
        
        image = app.GetLastImage()


.. js:function:: app.GetLastToggle()

    Возвращает :js:class:`ButtonToggle`, последнюю нажатую toggle кнопку

    .. code-block:: js
        
        tglbutton = app.GetLastToggle()


.. js:function:: app.SetMenu(menuList, p2)

    Устанавливает элементы в меню, обработчиком выбора при этом будет :js:func:`OnMenu`, в который будет передаваться выбраннный элемент. 

    На некоторых устройствах кнопки меню нет, при необходимости можно нарисовать кнопку меню и при нажатии на него вызывать :js:func:`ShowMenu`

    .. code-block:: js
        
        function OnStart() {
            app.SetMenu( "Start,Stop,Pause" );
        }

        function OnMenu( item ) {
          app.ShowPopup( item, "Short" );
        }  