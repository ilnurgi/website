Анимации
========

alpha
-----

Меняет прозрачность

.. code-block:: xml

    <alpha
        xmlns:android= "http://schemas.android.com/apk/res/android"

        android:fromAlpha="0.0"
        android:toAlpha="1.0"
        android:duration="3000" />


rotate
------

Поворот

.. code-block:: xml

    <rotate
        xmlns:android="http://schemas.android.com/apk/res/android"

        android:fromDegrees="0"
        android:toDegrees="360"
        android:duration="3000" />

set
---

Комбиниррование анимации

.. code-block:: xml

    <set
        xmlns:android="http://schemas.android.com/apk/res/android" >

        <rotate />
        <scale />
    </set>

scale
-----

Изменяет размеры

.. code-block:: xml

    <scale
        xmlns:android="http://schemas.android.com/apk/res/android"

        android:fromXScale="0.1"
        android:toXScale="1.0"
        android:fromYScale="0.1"
        android:toYScale="1.0"
        android:pivotX="50%"
        android:pivotY="50%"
        android:duration="3000" />


translate
---------

Перемещение

.. code-block:: xml

    <translate
        xmlns:android="http://schemas.android.com/apk/res/android"

        android:fromXDelta="-150"
        android:toXDelta="0"
        android:fromYDelta="-200"
        android:toYDelta="0"
        android:duration="3000" />