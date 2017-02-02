.. py:module:: android.app

Activity - активность
=====================


.. py:class:: Activity

    Активность, экран который отображается пользователю

    .. code-block:: java

        import android.app.Activity;
        import android.os.Bundle;

        public class MyActivity extends Activity {
            ...
        }


    .. py:method:: findViewById(id)

        Возвращает объект по иди

        .. code-block:: java

            Button btn = (Button)findViewById(R.id.btn);


    .. py:method:: getIntent()

        Возвращает интент, :py:class:`android.content.Intent`


    .. py:method:: getResources()

        Возвращает :py:class:`android.content.res.Resources`


    .. py:method:: onConfigurationChanged(config)

        Обработчик изменения конфигурации

        * config - :py:class:`android.content.res.Configuration`


    .. py:method:: onContextItemSelected(item)

        Обработчик выбора элемента в контекстном меню

        * item - :py:class:`android.view.MenuItem`

    
    .. py:method:: onCreate(savedInstanceState)

        Обработчик создания активности

        * savedInstanceState - :py:class:`android.os.Bundle`


        .. code-block:: java

            @Override
            public void onCreate(Bundle savedInstanceState) {
                super.onCreate(savedInstanceState);
                mCurrentIndex = savedInstanceState.getInt(KEY_INDEX, 0);
            }


    .. py:method:: onCreateContextMenu(menu, view, menuInfo)

        обработчик контекстного меню, вызывается каждый раз перед показом

        * menu - :py:class:`android.view.ContextMenu`

        * view - :py:class:`android_view_View`

        * menuInfo - :py:class:`android.view.ContextMenu.ContextMenuInfo`


    .. py:method:: onCreateOptionsMenu(menu)

        Обработчик создания меню, вызывается 1 раз при первом показе меню

        * menu - :py:class:`android.view.Menu`


    .. py:method:: onDestroy()

        Вызывается, перед выходом из "полноценного" состояния

        .. code-block:: java

            @Override
            public void onDestroy(){
                super.onDestroy();
            }


    .. py:method:: onOptionsItemSelected(item)

        Обработчик выбора элемента в меню

        * item - :py:class:`android.view.MenuItem`


    .. py:method:: onPause()

        Вызывается, перед выходом из "активного" состояния

        .. code-block:: java

            public void onPause(){
                super.onPause();
            }


    .. py:method:: onPrepareOptionsMenu(menu)

        Обработчик создания меню, вызывается каждый раз показе меню.

        Можно менять меню при каждом показе

        * menu - :py:class:`android.view.Menu`


    .. py:method:: onRestart()

        Вызывается, перед тем, как активность становится "видимой"

        .. code-block:: java

            @Override
            public void onRestart(){
                super.onRestart();
            }

    
    .. py:method:: onRestoreInstanceState(savedInstanceState)

        Вызывается, когда метод onCreate завершил свою работу,
        и используется для восстановления состояния пользовательского интерфейса

        * savedInstanceState - :py:class:`android.os.Bundle`

        .. code-block:: java

            @Override
            public void onRestoreInstanceState(Bundle savedInstanceState) {
                super.onRestoreInstanceState(savedInstanceState);
            }


    .. py:method:: onResume()

        Вызывается при восстановлении из неактивного состояния

        .. code-block:: java

            @Override
            public void onResume(){
                super.onResume();
            }

    
    .. py:method:: onSaveInstanceState(savedInstanceState)

        Вызывается для того,
        чтобы сохранить пользовательский интерфейс перед выходом из "активного" состояния.

        * savedInstanceState - :py:class:`android.os.Bundle`

        .. code-block:: java

            @Override
            public void onSaveInstanceState(Bundle savedInstanceState) {
                super.onSaveInstanceState(savedInstanceState);
                savedInstanceState.putInt(KEY_INDEX, mCurrentIndex);
            }

    
    .. py:method:: onStart()

        Вызывается когда активити стала видимой

        .. code-block:: java

            @Override
            public void onStart(){
                super.onStart();
            }

    
    .. py:method:: onStop()

        Вызывается перед тем, как Активность перестает быть "видимой"

        .. code-block:: java

            @Override
            public void onStop(){
                super.onStop();
            }


    .. py:method:: registerForContextMenu(view)

        Добавляет для вью обработчик контекста

        * view - :py:class:`android.view.View`


    .. py:method:: setContentView(view)

        Устанавливает содержимое активити

        .. code-block:: java

            @Override
            public void onCreate(Bundle savedInstanceState) {
                super.onCreate(savedInstanceState);

                setContentView(R.layout.main);
            }

        .. code-block:: java

            @Override
            public void onCreate(Bundle savedInstanceState) {
                super.onCreate(savedInstanceState);

                TextView textView = new TextView(this);
                setContentView(textView);
            }


    .. py:method:: startActivity(Intent intent)

        Запускает активность по интенту

        .. code-block:: java

            Intent intent = new Intent(this, SomeClass.class);
            startActivity(intent);
