CameraView
==========

.. js:class:: CameraView

    :js:func:`CreateCameraView`

    Также имеет следующие методы:

        * :js:func:`GetHeight`

        * :js:func:`GetVisibility`

        * :js:func:`GetWidth`

        * :js:func:`SetMargins`

        * :js:func:`SetPosition`

        * :js:func:`SetSize`

        * :js:func:`SetVisibility`


    .. js:function:: AutoCapture( folder, fileName, maxCount )

    .. js:function:: Destroy()
    
    .. js:function:: FindFaces( maxFaces )
    
    .. js:function:: Focus()
    
    .. js:function:: GetAbsHeight()

    .. js:function:: GetAbsWidth()

    .. js:function:: GetCameraCount()
    
    .. js:function:: GetColorEffects()

    .. js:function:: GetImageHeight()     

    .. js:function:: GetImageWidth()  

    .. js:function:: GetMaxZoom()     

    .. js:function:: GetParameters()     

    .. js:function:: GetPictureSizes()

    .. js:function:: GetPixelData( format,left,top,width,height ) 

        format can be “rawbase64”, “pngbase64” or “jpgbase64”
    
    .. js:function:: GetPosition()

    .. js:function:: GetType()

    .. js:function:: GetZoom()

    .. js:function:: IsRecording()
    
    .. js:function:: MotionMosaic( xtiles, ytiles, sensitivity, minPeriod, imageObj )
    
    .. js:function:: Record(fileName, seconds);

    .. js:function:: Release()

    .. js:function:: ReportColors( list, callback, sampSize, maxRate )

        .. code-block:: js
            
            cam.ReportColors('0.5,0.5', OnColor, 16, 300);

            function OnColor(colors){
                color = colors[0]
                /*
                 * red = color[0]
                 * green = color[1]
                 * blue = colors[2]
                 */
            }

    
    .. js:function:: SetBackGradient(color1,color2,color3,p4,p5,p6,p7)

    .. js:function:: SetBackGradientRadial( x,y,r,color1,color2,color3,p7 )   

    .. js:function:: SetBackground( imagefile,options )   

    .. js:function:: SetColorEffect( effect )     

        use in SetOnReady

    .. js:function:: SetDuplicateImage( img1,img2 ) 

    .. js:function:: SetFlash( onoff )
    
    .. js:function:: SetFocusMode( mode )

        * `mode`

            * Video    

    .. js:function:: SetOnFocus( callback )
    
    .. js:function:: SetOnMotion( callback )

        .. code-block:: js
            
            cam.SetOnMotion(function(data){});

    
    .. js:function:: SetOnPicture( callback )
    
    .. js:function:: SetOnReady( callback )
    
    .. js:function:: SetPadding(...)

    .. js:function:: SetParameter( name,value ) 

    .. js:function:: SetPictureSize( width, height )

    .. js:function:: SetPosition(...)
    
    .. js:function:: SetPreviewImage( imageObj )
    
    .. js:function:: SetScale(x, y)

    .. js:function:: SetSound( onoff )

    .. js:function:: SetZoom(level)
    
    .. js:function:: StartPreview()
    
    .. js:function:: Stop()

    .. js:function:: StopPreview()
    
    .. js:function:: Stream( ip, port, quality, fps, mtu )
    
    .. js:function:: TakePicture( fileName )
    
