menu - меню
===========

.. code-block:: xml

    <menu
        xmlns:android= "http://schemas.android.com/apk/res/android">

        <item
            android:id="@+id/menu_copy"
            android:orderInCategory="1"
            android:title="copy" />

        <group
            android:id="@+id/group1">

            <item
                android:id="@+id/menu_copy"
                android:orderInCategory="1"
                android:title="copy" />
        </group>
    </menu>