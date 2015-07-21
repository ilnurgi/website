.. py:module:: ensymble

ensymble
========

Данный модуль позволяет работать с sis файлами.

Использование
-------------

Для linux систем модуль необходмо просто установить в систему.

Для windows необходимо доустановить openssl.exe, а также libssl32.dll, libeay32.dll, и положить эти файлы рядом с ensymble.py

На ПК возможно использование данного модуля из консоли.

>>> $ ensymble.py command options...

Команды

    * altere32 - добавляет права доступа в приложения или библиотеки. (Alter the IDs and capabilities of e32image files (EXEs, DLLs))
    * genuid - генератор uid (Generate a new test-range UID from a name)
    * infoe32- показывает права доступа приложении или библиотек. (Show the IDs and capabilities of e32image files (EXEs, DLLs))
    * mergesis - сливает два sis файла в один. (Merge several SIS packages into one)
    * py2sis - создает sis приложение. (Create a SIS package for a "Python for S60" application)
    * signsis - подписывает приложение (Sign a SIS package)
    * simplesis - создает sis приложение по структуре папок. (Create a SIS package from a directory structure)
    * version - выводит версию библиотеки. (Print Ensymble version)

    Также эти команды доступны в интерпретаторе, первым параметром в них необходимо передать строку, она ни на что не влияет, а вторым, список строк с параметрами.

    >>> from ensymble.actions import altere32

Общие параметры
    
    Кодировка
    
        --encoding=terminal,filesystem

        -e terminal,filesystem

    Выводит информацию
    
        --verbose

        -v

    Справка, помощь

        --help

        -h

altere32
--------

>>> $ ensymble.py altere32
        [--uid=0x01234567] [--secureid=0x01234567] [--vendorid=0x01234567]
        [--caps=Cap1+Cap2+...] [--encoding=terminal,filesystem] [--verbose]
        --inplace <infile>...

Данная команда добавляет права в Symbian EXEs and DLLs. 

    * infile - путь к исходному файлу
    * outfile - путь к результирующему файлу
    * --inplace, -i - путь к папке с файлами
    * --uid=0x01234567, -u 0x01234567 - юид приложения, если не задан то uid не изменится
    * --secureid=0x01234567, -s 0x01234567 - аналогично uid
    * --vendorid=0x01234567б -r 0x01234567 - аналогично uid
    * --caps=Cap1+Cap2+..., -b Cap1+Cap2+..., --caps=0x12345. -b 0x12345 - права доступа
    * --heapsize=min,max, -H min,max - ограничения использования ОЗУ

    >>> $ ensymble.py altere32
        --caps=LocalServices+Location+NetworkServices+PowerMgmt+ProtServ+
        ReadUserData+SurroundingsDD+SWEvent+UserEnvironment+WriteUserData+
        ReadDeviceData+TrustedUI+WriteDeviceData
        myextension_orig.pyd myextension.pyd

    >>> $ ensymble.py altere32 --caps=0xff1b4 --inplace *.dll

    >>> $ ensymble.py altere32 --heapsize=4k,4M myapp_orig.exe myapp.exe

.. note:: When modifying the UID, the secure ID should be modified accordingly. Modifying UIDs of application EXEs is generally not possible, because applications usually include the UID in program code as well.

genuid
------

>>> $ ensymble.py genuid
    [--encoding=terminal,filesystem] [--verbose]
    <name>...


Генератор uid для приложений

    * name - название приложения

    >>> $ ensymble.py genuid myapplication myextension
    myapplication: 0xe0942bea
    myextension: 0xe325ed58

infoe32
-------

>>> $ ensymble.py infoe32
    [--encoding=terminal,filesystem] [--verbose]
    <infile>...


Возвращает информацию о Symbian EXEs and DLLs

    * infile - пути к исходным файлам

    >>> $ ensymble.py infoe32 myprogram.exe somelibrary.dll
    myprogram.exe:
        UID1          0x1000007a
        UID2          0x100039ce
        UID3          0x12345678
        Secure ID     0x12345678
        Vendor ID     0x00000000
        Capabilities  0x0 (NONE)
    somelibrary.dll:
        UID1          0x10000079
        UID2          0x00000000
        UID3          0x00000000
        Secure ID     0x00000000
        Vendor ID     0x00000000
        Capabilities  0xff7be (ALL-TCB-DRM-AllFiles)

mergesis
--------

>>> $ ensymble.py mergesis
        [--cert=mycert.cer] [--privkey=mykey.key] [--passphrase=12345]
        [--encoding=terminal,filesystem] [--verbose]
        <infile> [mergefile]... <outfile>


Сливает sis файлы в один sis файл

.. note:: The "mergesis" command will only work with SIS files that do not already contain other embedded SIS files.

    * infile - путь к базовому sis
    * mergefile - пути к сливаемым файлам
    * outfile - выходной файл
    * --cert=mycert.cer, -a mycert.cer - сертификаты для подписи
    * --privkey=mykey.key, -k mykey.key - ключи для подписи
    * --passphrase=12345, -p 12345 - пароли

.. note:: Using command line options to give the pass phrase is insecure. Any user of the computer will be able to see command lines of started programs and thus will see the pass phrase in plain view. Instead, standard input should be used (see examples below).

    >>>$ ensymble.py mergesis
        --cert=mycert.cer --key=mykey.key --passphrase=12345
        myapp_v1_0_0.sis PythonForS60_1_3_17_3rdEd_selfsigned.SIS
        myapp_standalone_v1_0_0.sis

    >>> $ echo "12345" | ensymble.py mergesis
        --cert=mycert.cer --key=mykey.key
        basefile.sis addon1.sis addon2.sis

        # 12345 пароль сертификата

py2sis
------

>>> $ ensymble.py py2sis
        [--uid=0x01234567] [--appname=AppName] [--version=1.0.0]
        [--lang=EN,...] [--icon=icon.svg] [--shortcaption="App. Name",...]
        [--caption="Application Name",...] [--drive=C]
        [--textfile=mytext.txt] [--cert=mycert.cer] [--privkey=mykey.key]
        [--passphrase=12345] [--caps=Cap1+Cap2+...]
        [--vendor="Vendor Name",...] [--autostart]
        [--encoding=terminal,filesystem] [--verbose]
        <src> [sisfile]

Собирает sis

    * src - путь к файлу или папке
    * sisfile - выходной файл, если указать папку, то в папку пложится файл с именем приложения и с версией
    * --appname=AppName, -n AppName - название приложения
    * --uid=0x01234567, -u 0x01234567 - uid
    * --version=1.0.0, -r 1.0.0
    * --lang=EN,..., -l EN,...
    * --icon=icon.svg, -i icon.svg
    * --shortcaption="App. Name",..., -s "App. Name",...
    * --caption="Application Name",..., -c "Application Name",...
    * --drive=C, -f C
    * --extrasdir=root, -x root
    * --textfile=mytext_%.txt, -t mytext_%.txt
        * %% - literal %
        * %n - language number (01 - 99)
        * %c - two-character language code in lowercase letters
        * %C - two-character language code in capital letters
        * %l - language name in English, using only lowercase letters
        * %l - language name in English, using mixed case letters

    * --cert=mycert.cer, -a mycert.cer
    * --privkey=mykey.key, -k mykey.key
    * --passphrase=12345, -p 12345
    * --caps=Cap1+Cap2+..., -b Cap1+Cap2+..., --caps=0x12345, -b 0x12345
    * --vendor=Name,..., -d Name,...
    * --autostart, -g
    * --runinstall, -R
    * --heapsize=min,max, -H min,max

    >>> $ ensymble.py py2sis myprog.py

    >>> $ echo "12345" | ensymble.py py2sis
        --cert mycert.cer --privkey mykey.key
        myprog.py

signsis
-------


    >>> ensymble.py signsis
        [--unsign]
        [--cert=mycert.cer] [--privkey=mykey.key] [--passphrase=12345]
        [--execaps=Cap1+Cap2+...] [--dllcaps=Cap1+Cap2+...]
        [--encoding=terminal,filesystem] [--verbose]
        <infile> [outfile]


Подписывает приложения

    * infile
    * outfile
    * --unsign, -u - удаляет сертификат из файла
    * --cert=mycert.cer, -a mycert.cer
    * --privkey=mykey.key, -k mykey.key
    * --passphrase=12345, -p 12345
    * --execaps=Cap1+Cap2+..., -b Cap1+Cap2+..., --execaps=0x12345, -b 0x12345
    * --dllcaps=Cap1+Cap2+..., -d Cap1+Cap2+..., --dllcaps=0x12345, -d 0x12345

    >>> $ ensymble.py signsis
        --dllcaps=LocalServices+Location+NetworkServices+PowerMgmt+ProtServ+
        ReadUserData+SurroundingsDD+SWEvent+UserEnvironment+WriteUserData+
        ReadDeviceData+TrustedUI+WriteDeviceData
        --cert=mycert.cer --key=mykey.key --passphrase=12345
        coolextension_nocert.sis coolextension_mycert.sis

    >>> $ echo "12345" | ensymble.py signsis
        --dllcaps=0xff1b4 --cert=mycert.cer --key=mykey.key
        coolextension_nocert.sis coolextension_mycert.sis


simplesis
---------

    >>> $ ensymble.py simplesis
        [--uid=0x01234567] [--version=1.0.0] [--lang=EN,...]
        [--caption="Package Name",...] [--drive=C] [--textfile=mytext_%C.txt]
        [--cert=mycert.cer] [--privkey=mykey.key] [--passphrase=12345]
        [--vendor="Vendor Name",...] [--encoding=terminal,filesystem]
        [--verbose]
        <srcdir> [sisfile]


Создает sis приложение по структуре папок

    * srcdir
    * sisfile
    * --uid=0x01234567, -u 0x01234567
    * --version=1.0.0, -r 1.0.0
    * --lang=EN,..., -l EN,...
    * --caption="Application Name",..., -c "Application Name",...
    * --drive=C, -f C
    * --textfile=mytext_%C.txt, -t mytext_%C.txt
        * %% - literal %
        * %n - language number (01 - 99)
        * %c - two-character language code in lowercase letters
        * %C - two-character language code in capital letters
        * %l - language name in English, using only lowercase letters
        * %l - language name in English, using mixed case letters
    * --cert=mycert.cer, -a mycert.cer
    * --privkey=mykey.key, -k mykey.key
    * --passphrase=12345, -p 12345

    >>> $ ls -R mymodule
    mymodule:
    resource/sys/
    mymodule/resource:
    apps/mymodule.py
    mymodule/resource/apps:
    mymodule.rsc
    mymodule/sys:
    bin/
    mymodule/sys/bin:
    _mymodule.pyd
    
    >>> $ ensymble.py simplesis mymodule

    >>> $ echo "12345" | ensymble.py py2sis
        --cert mycert.cer --privkey mykey.key
        mymodule

version
---------------------

    >>> $ ensymble.py version