Работа с файлами, каталогами и данными
======================================

.. js:function:: app.ClearData(file)

    Очищает пользовательскую память от данных, сохраненных с помощью :js:func:`SaveText` и т.п.


.. js:function:: app.CopyFile(src, dst)

    Копирует укзанный файл в новое место

        :js:func:`CopyFolder`, :js:func:`DeleteFile`, :js:func:`deleteFolder`, :js:func:`FileExists`, :js:func:`FolderExists`


.. js:function:: app.CopyFolder(src, dst, overwrite)

    Копирует указанный католог в новое место


.. js:function:: app.CreateFile(file, mode)

    Возвращает :js:class:`File`, файловый объект


.. js:function:: app.CreateZipUtil()

    Возвращает :js:class:`ZipUtil`
    

.. js:function:: app.DeleteDatabase(name)

.. js:function:: app.DeleteFile(fileName)

    Удаляет файл по указанному пути

    .. code-block:: js
        
        app.DeleteFile('/sdcard/file.txt');


.. js:function:: app.DeleteFolder(folderName)

    Удаляет папку по указанному пути

    .. code-block:: js
        
        app.DeleteFile('/sdcard/files');


.. js:function:: app.ExtractAssets(src, dest, overwrite)    

    Copy content from one folder to another. If overwrite = true, then existing files in destination folder will be overwritten.


.. js:function:: app.FileExists(fileName)

    Возвращает булево, существет ли файл по указанному пути

    .. code-block:: js
        
        app.FileExists('/sdcard/file.txt')


.. js:function:: app.FolderExists(folderName)

    Возвращает булево, существет ли папка по указанному пути

    .. code-block:: js
        
        app.FolderExists('/sdcard/files')


.. js:function:: app.GetExternalFolder()    

    Возвращает путь до флешки, microsd карточки

    .. code-block:: js
        
        external_path = app.GetExternalFolder()


.. js:function:: app.GetFileDate( file ) 

    Returns the date of a file (file needs the full path).  


.. js:function:: app.GetFileSize( file ) 

    Returns the size of a file in bytes (file needs the full path).


.. js:function:: app.GetFreeSpace( option )

    Returns the free space in gigabytes. Parameter option can be: “internal” or “external”. 


.. js:function:: app.GetInternalFolder()


.. js:function:: app.GetPrivateFolder(fldrName)

    Создает и возвращает путь до приватной папки, доступной только для приложения

    .. code-block:: js
         
        fldr = app.GetPrivateFolder('myfolder');    


.. js:function:: app.GetSharedFiles()

.. js:function:: app.GetSharedText(p1)

.. js:function:: app.GetSpecialFolder( name )    

    'DCIM','Pictures','Movies','Downloads' etc  1.29


.. js:function:: Lapp.istFolder(path, filter, limit, options)

    Возвращает список файлов в указанной папке

    .. code-block:: js
        
        files = app.ListFolder('/sdcard/');
        files = app.ListFolder('/sdcard/', '.mp3');
        files = app.ListFolder('/sdcard/', '.mp4', 10);
        files = app.ListFolder('/sdcard/', '.mp4', 10, 'FillPath,alphasort');


.. js:function:: app.LoadBoolean(valueName, default, id)

    Загружает параматеры из пользовательской памяти, для сохранения используйте :js:func:`SaveBoolean`

    * `valueName` - имя параметра

    * `default` - значение по умолчанию

    * `id` - идентификатор, для расшаривания атрибута между прилоэениями

    .. code-block:: js
        
        bol = app.LoadBoolean('MyName', true);


.. js:function:: app.LoadNumber(valueName, default, id)

    Загружает параматеры из пользовательской памяти, для сохранения используйте :js:func:`SaveNumber`

    * `valueName` - имя параметра

    * `default` - значение по умолчанию

    * `id` - идентификатор, для расшаривания атрибута между прилоэениями

    .. code-block:: js
        
        num = app.LoadNumber('MyName', 42);


.. js:function:: app.LoadText(valueName, default, id)

    Загружает параматеры из пользовательской памяти, для сохранения используйте :js:func:`SaveText`

    * `valueName` - имя параметра

    * `default` - значение по умолчанию

    * `id` - идентификатор, для расшаривания атрибута между прилоэениями

    .. code-block:: js
        
        name = app.LoadText('MyName', 'Bill');


.. js:function:: app.MakeFolder(folder_path)

    Создает папку по указанному пути

    .. code-block:: js
        
        app.MakeFolder('/sdcard/ilnurgi/')


.. js:function:: app.OpenDatabase(dbName)

    Возвращает :js:class:`Database`

    .. code-block:: js
        
        db = app.OpenDatabase('MyDB');


.. js:function:: app.OpenFile(fileName, type, promt)

    Открыват файл в другой программе

    .. code-block:: js
        
        app.OpenFile('/sdcard/text/txt', 'text/plain', 'Choose Editor')


.. js:function:: app.ReadFile(fileName, options)

    Возвращает содержимое файла

    * `options`

        * `windows-1252`
        * `ISO-8859-1`
        * `US-ASCII`
        * `UTF-16`
        * `UTF-16BE`
        * `UTF-16LE`
        * `UTF-8`

    .. code-block:: js
        
        txt = app.ReadFile('/sdcard/text.txt');


.. js:function:: app.RenameFile(fileName, newFileName)

    Переименовывает файл

    .. code-block:: js
        
        app.RenameFile('/sdcard/text.txt', '/sdcard/newtext.txt');


.. js:function:: app.RenameFolder(folderName, newFolderName)

    Переименовывает папку

    .. code-block:: js
        
        app.RenameFolder('/sdcard/text', '/sdcard/newtext');


.. js:function:: app.SaveBoolean(valueName, value, id)

    Сохраняет параматеры в пользовательскую память, для получения используйте :js:func:`LoadBoolean`

    * `valueName` - имя параметра

    * `value` - значение

    * `id` - идентификатор, для расшаривания атрибута между прилоэениями

    .. code-block:: js
        
        app.SaveBoolean('MyName', true);


.. js:function:: app.SaveNumber(valueName, value, id)

    Сохраняет параматеры в пользовательскую память, для получения используйте :js:func:`LoadNumber`

    * `valueName` - имя параметра

    * `value` - значение

    * `id` - идентификатор, для расшаривания атрибута между прилоэениями

    .. code-block:: js
        
        app.SaveNumber('MyName', 42);


.. js:function:: app.SaveText(valueName, value, id)

    Сохраняет параматеры в пользовательскую память, для получения используйте :js:func:`LoadText`

    * `valueName` - имя параметра

    * `value` - значение

    * `id` - идентификатор, для расшаривания атрибута между прилоэениями

    .. code-block:: js
        
        app.SaveText('MyName', '123');


.. js:function:: app.SendFile(filenam, dstName, title)

    Send a file to another App (users choice).

    .. code-block:: js
        
        app.SendFile( file, "sftest.txt", "Send File" );

        
.. js:function:: app.WriteFile(fileName, text, mode)

    Пишет данные в файл

    .. code-block:: js
        
        app.WriteFile('/sdcard/text.txt', 'Hello', 'Append');