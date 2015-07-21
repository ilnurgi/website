WebCam
======


.. py:method:: cameraStartPreview([int resolutionLevel=0, int jpegQuality=0...20...100, str filepath])

    запускаем отображатель


.. py:method:: cameraStopPreview()

    останавливает предпросмотр


.. py:method:: webcamAdjustQuality([int resolutionLevel=0, int jpegQuality=0...20...100])

    Adjusts the quality of the webcam stream while it is running.


.. py:method:: webcamStart([int resolutionLevel=0, int jpegQuality=0...20...100, int port])

    Starts an MJPEG stream and returns a Tuple of address and port for the stream.


.. py:method:: webcamStop()

    Stops the webcam stream.