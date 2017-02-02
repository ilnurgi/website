.. py:module:: configparser

configparser
============

.. py:class:: ConfigParser()

    Парсер cfg файлов

    .. code-block:: cfg

        [english]
        greeting = Hello
        [french]
        greeting = Bonjour
        [files]
        home = /usr/local
        # simple interpolation:
        bin = %(home)s/bin

    .. code-block:: py

        cfg = ConfigParser()
        cfg.read("file.cfg")

        cfg['french']
        # <Section: french>

        cfg['french']['greeting']
        # 'Bonjour'

        cfg['files']['bin']
        # '/usr/local/bin'


    .. py:method:: read(file_path)

        Читает указанный конфиг

        .. code-block:: py

            cfg.read("file.cfg")