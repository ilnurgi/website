.. py:module:: QtCore

QtCore - модуль содержит классы, не связанные с реализацией графического интерфейса.
====================================================================================

Список классов модуля
---------------------

.. toctree::
   :maxdepth: 1

   qt
   qobject
   qpoint
   qpointf
   qrect
   qrectf
   qsize
   qsizef
   qtimer

Базовые типы данных фреймворка
------------------------------

QString
-------

.. py:class:: QString()

    юникод строка


QChar
-----

.. py:class:: QChar()

    юникод символ


QStringList
-----------

.. py:class:: QStringList()

    массив юникод строк


QByteArray
----------

.. py:class:: QByteArray()

    массив байтов


QVariant
--------

.. py:class:: QVariant()

    может хранить данные любого типа


    .. py:method:: toPyObject()

        возвращает, преобразованные в python тип, данные


QPyNullVariant
--------------

.. py:class:: QPyNullVariant(<тип>)

    пустой объект, определенного типа


    ::

        a = QPyNullVariant(int)
        a.isNull(), a.typeName()
        True, 'int'

        a = QPyNullVariant('QString')
        a.isNull(), a.typeName()
        True, 'QString'


    .. py:method:: isNull()

        возвращает истину или ложь, объект пустой


    .. py:method:: typeName()

        возвращает тип объекта


QDate
-----

.. py:class:: QDate()

    представление даты


QTime
-----

.. py:class:: QTime()

    представление времени


QDateTime
---------

.. py:class:: QDateTime()

    представление даты и времени


QTextStream
-----------

.. py:class:: QTextStream()

    текстовый поток


QUrl
----

.. py:class:: QUrl()

    url-адрес


.. py:method:: pyqtSignal(*types[, name])

  Регистрирует пользовательские сигналы в системе

  * args - названия типов данных, которые принимает метод. 

    * Если тип из с++, его указывает в виде строки

    * Если сигнал имеет несколько перегруженных методов, то типы указываются в виде списка
  
  * name - имя сигнала

  .. code-block:: py

    mysignal = QtCore.pyqtSignal([int], [str], name='mysignal')


.. py:method:: pyqtSlot(*types, name=None, result=None)

  Декоратор, устанавливает пользовательский метод как слот. Чтобы создать перегруженную версию слота, декоратор указывается несколько раз

  * args - названия типов данных, которые принимает метод. 

    * Если тип из с++, его указывает в виде строки   
  
  * name - имя слота, если не задан то соответсвует имени слота
  
  * result - тип возвращаемых данных

  .. code-block:: py

    mysignal = QtCore.pyqtSignal([int], [str], name='mysignal')