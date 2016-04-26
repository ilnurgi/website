Создание и установка плагинов
============================


Установим зависимости
---------------------
    
.. code-block:: sh
    
    sudo apt-get install createrepo rpm dpkg-dev ruby ruby-dev
    sudo pip install fuel-plugin-builder
    sudo gem install fpm
    yum install graphviz


Создадим шаблон плагина
-----------------------

.. code-block:: sh
    
    fpb --create plugin_name


Собираем пакет плагина
----------------------

.. code-block:: sh
    
    fpb --build plugin_name