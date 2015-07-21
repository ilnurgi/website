MediaRecorder
=============

.. py:method:: recorderCaptureVideo(str targetPath[ , int duration=0, bool recordAudio=true])

    записывает видео с/без аудио в указанный файл указанное время


.. py:method:: recorderStartMicrophone(str targetPath)

    записывает звук в указанный файл


.. py:method:: recorderStartVideo(str targetPath[ , int duration=0, int videoSize=1])

    записывает видео в указанный файл, укзанное время, с указанным разрешением (0=160x120, 1=320x240, 2=352x288, 3=640x480, 4=800x480)


.. py:method:: recorderStop()

    останавливает запись


.. py:method:: startInteractiveVideoRecording(str targetPath)

    записывает видео в файл