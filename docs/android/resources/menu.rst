menu - меню
===========

.. code-block:: xml

    <menu>
        <item
            android:id="@+id/menu_copy"
            android:orderInCategory="1"
            android:title="copy">
        </item>
        <group android:id="@+id/group1">
            <item
                android:id="@+id/menu_copy"
                android:orderInCategory="1"
                android:title="copy">
            </item>
        </group>
    </menu>