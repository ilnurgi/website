android.content.SharedPreferences
=================================

.. py:class:: android.content.SharedPreferences()

    Настройки приложения.

    Файлы настроек хранятся в /data/data/ru.ilnurgi1/shared_prefs/activity.xml

    .. code-block:: java

        SharedPreferences sharedPreferences = context.getPreferences(MODE_PRIVATE);


    .. py:method:: edit()

        Возвращает редактор настроек, :py:class:`android.content.SharedPreferences.Editor`

        .. code-block:: java

            Editor editor = sharedPreferences.edit();


    .. py:method:: getString(String key, String default)

        Возвращает строку, значение по ключю

        .. code-block:: java

            String value = sharedPreferences.getString("key");


Editor
------

.. py:class:: android.content.SharedPreferences.Editor()

    Редактор настроек

    .. code-block:: java

        Editor editor = sharedPreferences.edit();


    .. py:method:: commit()

        Фиксирует изменения настроек

        .. code-block:: java

            editor.commit();


    .. py:method:: putString(String key, String value)

        Добавляет значение по указанному ключю

        .. code-block:: java

            editor.putString("key", "value");

