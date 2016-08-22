values
======

Константы

color
-----

Цвета

.. code-block:: xml

    <resources>
        <color name="my_color">#001100</color>
    </resources>


dimen
-----

Размеры

.. code-block:: xml

    <resources>
        <dimen name="standard_border">5dp</dimen>
    </resources>


.. _res_values_string:

string
------

Строки

.. code-block:: xml

    <resources>
        <string name="app_name">MyCalculator</string>
    </resources>


string-array
------------

.. code-block:: xml

    <resources>
        <string-array name="names">
            <item>item 1</item>
            <item>item 2</item>
        </string>
    </resources>


style
-----

Стили

.. code-block:: xml

    <resources>
        <style name="StyleName" parent="ParentStyleName">
            <item name="attributeName">value</item>
            <item name="android:textSize">14sp</item>
        </style>
    </resources>