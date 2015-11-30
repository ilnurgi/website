FtpClient
=========

.. js:function:: FtpClient

    .. code-block:: js
        
        app.LoadPlugin('FtpClient');
        ftp = app.CreateFtpClient()


    .. js:function:: Connect(user, pass, server)

    .. js:function:: GetError()

    .. js:function:: Disconnect()

    .. js:function:: IsConnected()

    .. js:function:: SetPort(port)

    .. js:function:: SetServerTimeout(seconds)

    .. js:function:: SetOnResponse(callback)

    .. js:function:: GetCurrentDirrectory()

    .. js:function:: ChangeWorkingDirrectory(path)

    .. js:function:: GetDirectoryList(path)

    .. js:function:: CreateDirectory(path)

    .. js:function:: RemoveDirectory(path)

    .. js:function:: DirectoryExists(path)

    .. js:function:: SetOnStatus(callback)

    .. js:function:: DownloadDirectory(remote, local, mode)

    .. js:function:: UploadDirectory(local, remote, mode)

    .. js:function:: ForceDeleteDirectory(directory)

    .. js:function:: GetFilesDetail(file)

    .. js:function:: DownloadFile(remote, local, mode)

    .. js:function:: UploadFiel(local, remote, mode)

    .. js:function:: DeleteFile(file)

    .. js:function:: RenameFile(file, newName)

    .. js:function:: FileExists(file)

    .. js:function:: GetVersion()

    
