GoProController
===============

.. js:class:: GoProController

    .. code-block:: js
        
        app.LoadPlugin( "GoProController" );
        goprocontroller = app.CreateObject( "GoProController" );


    .. js:function:: Connect(ip)
    .. js:function:: Disconnect()

    .. js:function:: SetOnConnect(gopro_OnConnect);
    
    .. js:function:: SetOnError(gopro_OnError);

    .. js:function:: StartShutter();

    .. js:function:: StopShutter();

    .. js:function:: LoadStatus(callback)

        * status

            =================== =======================================================
            Status              Description
            =================== =======================================================
            AutoPowerOff        Auto power off duration in seconds
            BatteryLevel        Battery level, 0 - 100
            BeepVolume          Camera beep volume
            BurstRate           Photo burst rate
            BurstRecording      Indicates if the camera is currently taking a photo burst
            CameraMode          Current camera mode
            DefaultCameraMode   Startup camera mode
            LEDs                Indicates how many of the status indicator lights are active
            Locate              Indicates if the camera is currently Locating (See the Locate Mode section)
            Orientation         Camera orientation
            OSD                 Indicates if the On Screen Display is on
            PhotoCount          Number of photos taken
            PhotoMode           Photo mode, includes the resolution and field of view, e.g. 5mpWide
            PhotosAvailable     Number of photos available to take
            Protune             Indicates if Protune mode on
            SDCard              Indicates if there is currently an SD card in the camera
            SpotMeter           Indicates if the spot meter is on
            TimelapseInterval   Timelapse interval in seconds
            VideoAvailableTime  Time in seconds remaining for video
            VideoCount          Number of videos recorded
            VideoFOV            Video field of view
            VideoFPS            Video framerate
            VideoMode           Video mode, e.g. 720, 1080, etc
            VideoStandard       PAL or NTSC
            VideoRecording      Indicates if video is currently recording
            VideoRecordingTime  Duration in seconds of the currently recording video
            =================== =======================================================

        .. code-block:: js
            
            gopro.LoadStatus(function(status){})


    .. js:function:: SetOption(options)

        ================= ============================
        Параметр          Описание
        ================= ============================
        AutoPowerOff      Never, 60, 120, 300 (seconds)
        BeepVolume        0, 70, 100
        BurstRate         3/1s, 5/1s, 10/1s, 10/2s, 30/1s, 30/2s, 30/3s
        CameraMode        Video, Photo, Burst, Timelapse
        DefaultCameraMode Video, Photo, Burst, Timelapse
        LEDs              Off, 2, 4
        Orientation       Up, Down
        OSD               On, Off
        PhotoMode         5mpWide, 5mpMedium, 7mpWide, 7mpMedium, 8mpMedium, 11mpWide, 12mpWide
        Protune           On, Off
        SpotMeter         On, Off
        TimelapseInterval 0.5, 1, 2, 5, 10, 20, 60 (seconds)
        VideoFOV          Wide, Medium, Narrow
        VideoFPS          12, 15, 12.5, 24, 25, 30, 48, 50, 60, 100, 120, 240
        VideoMode         WVGA, 720, 960, 1080, 1440, 2.7k, 4K, 2.7KCinema, 4KCinema, 720SuperView, 1080SuperView
        VideoStandard     PAL, NTSC
        ================= ============================

        .. code-block:: js
            
            gopro.SetOptions({CameraMode: 'Video'});

    .. js:function:: GetModel()

    .. js:function:: IsPowerOn()

    .. js:function:: PowerOn()

    .. js:function:: PowerOff()

    .. js:function:: StartLocate()

    .. js:function:: StopLocate()