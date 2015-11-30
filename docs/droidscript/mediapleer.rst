MediaPleer - проигрывать музыкальных файлов
===========================================

.. js:class:: MediaPleer

    
    .. js:function:: Close()


    .. js:function:: GetDuration()


    .. js:function:: GetPosition()


    .. js:function:: IsLooping()


    .. js:function:: IsPlaying()


    .. js:function:: IsReady()


    .. js:function:: Pause()


    .. js:function:: Play()    


    .. js:function:: SeekTo(pos)

        Переходит на указанную позицию в файле, указывается в секундах.


    .. js:function:: SetFile(fileName)

        Задает путь к проигрываемому файлу. После добавления выполнит обработчик, установленный методом :js:func:`SetOnReady`.

        .. code-block:: js
            
            player.SetFile('/sdcard/muzon.mp3')
            player.SetFile('Snd/muzon.mp3')


    .. js:function:: SetLooping( loop )


    .. js:function:: SetOnComplete()

        Устанавливает обработчик, который вызывается после проигрывания медиа файла


    .. js:function:: SetOnReady(callback)

        Устанавливает обработчик, который вызывается после :js:func:`SetFile`


    .. js:function:: SetOnSeekDone( callback )


    .. js:function:: SetVolume( left, right )


    .. js:function:: Stop()




    
Mediaplayer.Close()     
Mediaplayer.GetDuration()   
Mediaplayer.GetType()   
Mediaplayer.IsLooping()     
Mediaplayer.IsPlaying()     
Mediaplayer.IsReady()   
Mediaplayer.Pause()     
Mediaplayer.Play()  
Mediaplayer.Release()   
Mediaplayer.SeekTo( seconds )   
Mediaplayer.SetFile( filename )     
Mediaplayer.SetLooping( loop )  
Mediaplayer.SetOnComplete( callback )   
Mediaplayer.SetOnReady( callback )  
Mediaplayer.SetOnSeekDone( callback )   
Mediaplayer.SetVolume( left,right )     
Mediaplayer.Stop() 
    

    

    
