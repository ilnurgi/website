MediaPlayer
===========


.. py:method:: mediaIsPlaying([str tag='default'])

    проверяет, играет ли сейчас эта медиа


.. py:method:: mediaPlay(str url[ , str tag='default', bool play])
    
    открывает медию и при необходимости сразу проигрывает


.. py:method:: mediaPlayClose([str tag='default'])

    закрывает медию


.. py:method:: mediaPlayInfo([str tag='default']))

    информация об открытом ресурсе


.. py:method:: mediaPlayList()

    список открытых медиа ресурсов


.. py:method:: mediaPlayPause([str tag='default'])

    ставит на паузу проигрываем медиа


.. py:method:: mediaPlaySeek(int msec[ , str tag])

    продолжает проигрывание с указанной позиции


.. py:method:: mediaPlaySetLooping([bool enabled=true, str tag='default'])
 
    Set Looping


.. py:method:: mediaPlayStart([str tag='default'])

    начинает проигрывание медиа файла