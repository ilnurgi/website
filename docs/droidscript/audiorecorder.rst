AudioRecorder - звукозапись
===========================

.. js:class:: AudioRecorder

    :js:func:`CreateAudioRecorder`


    .. js:function:: GetRMS()

    .. js:function:: GetType()


    .. js:function:: Pause()

        Приостанавливает запись

        .. code-block:: js
            
            recorder.Pause()


    .. js:function:: SetFile(fileName)

        Устанавливает файл. в котороый будет записываться

        .. code-block:: js
            
            recorder.SetFile('/sdcard/sound.wav');


    .. js:function:: Start(p1)

        Начинает запись

        .. code-block:: js
            
            recorder.Start()


    .. js:function:: Stop()

        Прекращает запись

        .. code-block:: js
            
            recorder.Stop()