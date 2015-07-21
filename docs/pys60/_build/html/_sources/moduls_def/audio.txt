audio
=====

.. py:module:: audio

Модуль для работы с аудио

.. py:method:: say(text) 
    
    Произносит текст text

    >>> audio.say(u'hello')

Sound()
-------

.. py:class:: Sound()
    
    .. code-block:: python

        import audio
        s = audio.Sound.open('e:\\1.wav')
        s.play()
        s.close()

.. py:method:: Sound.close() 
    
    Закрыть открытый файл
    
    >>> s.close()

.. py:method:: Sound.current_volume() 
    
    Возвращает текущий уровень громкости.
    
    >>> s.current_volume()
    9

.. py:method:: Sound.current_position() 
    
    Возвращает текущую позицию в микросекундах. 

.. py:method:: Sound.duration() 
    
    Возвращает длину аудио-файла в микросекундах. 

.. py:method:: Sound.max_volume() 
    
    Возвращает максимальный уровень громкости.

    >>> s.max_volume()
    10

.. py:method:: Sound.open() 
    
    Открывает файл и возвращает объект Sound

    >>> s = audio.Sound.open('e:\\1.wav')

.. py:method:: Sound.play([times=1, interval=0, callback=None]) 
    
    :param times: количество повторов (audio.KMdaRepeatForever, бесконечно)
    :param interval: длительность паузы между повторами в микросекундах.
    :param callback: обработчик старта и окончания воспроизведения аудио-файла. Ей передается три аргумента: предыдущее состояние, текущее состояние и код возможной ошибки.
        
    Проигрывает мелодию

    >>> s.play()

.. py:method:: Sound.record() 
    
    Начинает запись
    
    >>> s.record()

.. py:method:: Sound.set_volume(volume) 
    
    Устанавливает уровень громкости volume в диапазоне от нуля до значения полученного методом :py:meth:`max_volume()`

    >>> s.set_volume(10)

.. py:method:: Sound.set_position(microseconds) 
    
    Устанавливает позицию воспроизведения. 

.. py:method:: Sound.state() 
    
    Возвращает состояние объекта:
        
        * audio.ENotReady - объект создан успешно, но файл не открыт;
        * audio.EOpen - файл открыт успешно, но воспроизвести его или осуществить запись в него невозможно;
        * audio.EPlaying - файл воспроизводится;
        * audio.ERecording - в файл осуществляется запись.

.. py:method:: Sound.stop() 
    
    Остановить воспроизведение

    >>> s.stop()
