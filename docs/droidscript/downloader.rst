DownLoader
==========

.. js:class:: DownLoader

    :js:func:`CreateDownloader`


    .. js:function:: Download(sourceURI,destPath)     

        Start download. You can pass a comma seperated list of file urls to download. destPath should be a valid and accessible folder on the device
    
    .. js:function:: GetProgress()    

        returns fract value 0..1, but “NaN” if not yet started
    
    .. js:function:: GetSize()    
    
    .. js:function:: IsComplete()     

        returns true/false
    
    .. js:function:: SetOnComplete(callback)  

        Should be done before starting the download. 