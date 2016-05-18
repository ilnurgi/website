audio
=====

Звуковой файл на странице

autobuffer
----------


autoplay
--------

Включает автовоспроизведение


controls
--------

Включает элементы управления


crossorigin
-----------

* anonymous - по умолчанию

* use-credentials

Проверка полномочия для файла


loop
----

Включает повторное воспроизведение


mediagroup
----------

Связывает несколько элементов в группу


mited
-----

Приглушает звук


preload
-------

* none

* metadata

* auto

Буферизация при загрузке страницы


src
---

Местоположение файла


.. code-block:: html

    <audio src="ilnurgi.mp3" autoplay controls>
        Ваш браузер не поддерживает встроенный звук, <a href="ilnurgi.mp3">скачать трек</a>
    </audio>

    <audio id="soundtrack" controls preload="auto">
        <source src="track.mp3" type="audio/mp3">
        <source src="track.ogg" type="audio/ogg">
    </audio>