link
====

Ссылка на различные доп файлы документа.

Должен находится внутри тега head

href
----

ссылка на файл

.. code-block:: html

    <link rel='stylesheet' href='main.css'>


media
-----

тип медиа документа

* all - все устройства
* aural
* braille - устройства с тактильной обратной связью
* handled - портативные устройства
* print - режим вывода на печать
* projection - проекторы
* screen - цветные компьютерные экраны
* tty - моноширинная символьная сетка
* tv - телевизоры
* orientation - ориентация экрана
* (min/max)-width - ширина области просмотра
* (min/max)-height - высота области просмотра
* (min/max)-aspect-ratio - соотношение сторон области просмотра
* (min/max)-device-width - ширина экрана
* (min/max)-device-height - высота экрана
* (min/max)-device-aspect-ratio - соотношение сторон экрана

.. code-block:: html

    <link rel="stylesheet" media="screen and (max-width: 960px)" />


rel
---

отношение к актуальному документу

* alternate - альтернативная версия документа
* contents - оглавление документа или сайта
* copyright - авторские права
* glossary - термины
* help - справочный документ
* icon - иконка страницы
* index - индекс документа
* next - ссылка на следующий документ
* prev - ссылка на предыдущую страницу
* stylesheet - стили

.. code-block:: html

    <link rel="stylesheet" media="screen and (max-width: 960px)" />


hreflang
--------

язык медиаинформации

sizes
-----

размер пиктограммы

