.. _android_app_Activity:

android.app.Activity
====================


.. py:class:: android.app.Activity

    базовый класс для визуальных и интерактивных компонентов приложения.

    
    .. py:method:: onCreate(savedInstanceState)

        обработчик создания

        :param savedInstanceState: :ref:`Bundle`

    
    .. py:method:: onRestoreInstanceState(savedInstanceState)

        Вызывается, когда метод onCreate завершил свою работу, и используется для восстановления состояния пользовательского интерфейса 

        :param savedInstanceState: :ref:`Bundle`

    
    .. py:method:: onSaveInstanceState(savedInstanceState)

        Вызывается для того, чтобы сохранить пользовательский интерфейс перед выходом из "активного" состояния.

        :param savedInstanceState: :ref:`Bundle`

    
    .. py:method:: onRestart()

        Вызывается, перед тем, как активность становится "видимой"

    
    .. py:method:: onStart()

        Вызывается, вначале "видимого" состояния

    
    .. py:method:: onStop()

        Вызывается перед тем, как Активность перестает быть "видимой"

    
    .. py:method:: onResume()

        Вызывается, вначале "активного" состояния

    
    .. py:method:: onPause()

        Вызывается, перед выходом из "активного" состояния

    
    .. py:method:: onDestroy()

        Вызывается, перед выходом из "полноценного" состояния


    .. py:method:: onCreateOptionsMenu(menu)

        обработчик создания меню, вызывается 1 раз при первом показе меню

        :param menu: :ref:`android_view_Menu`


    .. py:method:: onPrepareOptionsMenu(menu)

        обработчик создания меню, вызывается каждый раз показе меню. Можно менять меню при каждом показе

        :param menu: :ref:`android_view_Menu`


    .. py:method:: onOptionsItemSelected(item)

        обработчик выбора элемента в меню

        :param item: :ref:`android_view_MenuItem`


    .. py:method:: onCreateContextMenu(menu, view, menuInfo)

        обработчик контекстного меню, вызывается каждый раз перед показом

        :param menu: :ref:`android_view_ContextMenu`
        :param view: :ref:`android_view_View`
        :param menuInfo: :ref:`android_view_ContextMenu_ContextMenuInfo`


    .. py:method:: onContextItemSelected(item)

        обработчик выбора элемента в контекстном меню

        :param item: :ref:`android_view_MenuItem` 


    .. py:method:: onConfigurationChanged(config)

        обработчик изменения конфигурации

        :param item: :ref:`_android_content_res_Configuration` 


    .. py:method:: registerForContextMenu(view)

        добавляет для вью обработчик контекста

        :param view: :ref:`android_view_View`


    .. py:method:: setContentView()

        устанавливает содержимое активити из лэйаута

        >>> setContentView(R.layout.main);

    .. py:method:: findViewById(id)

        возвращает объект по иди

        >>> findViewById(R.id.textView);




    .. py:method:: getResources()

        возвращает объект :ref:`android_content_res_Resources`

    .. py:method:: getMenuInflater().inflate(R.menu.mymenu, menu)

        getMenuInflater возвращает объект MenuInflater



Примеры
-------

::
    
    publick class MainActivity extends Activity impements OnClickListener {

        @Override
        publick void onCreate(Bundle savedInstanceState) {
            // обработчик создания активити
            super.onCreate(savedInstanceState);
            ...
        };

        @Override
        publick void onClick(View) {
            // обработчик клика по вью
            ...
        };

        @Override
        publick boolean onCreateOptionsMenu(Menu menu) {
            // обработчик создания меню, вызывается 1 раз при первом показе меню
            ...
            return super.onCreateOptionsMenu(menu);
        };

        @Override
        publick boolean onPrepareOptionsMenu(Menu menu) {
            // обработчик создания меню, вызывается каждый раз показе меню
            ...
            return super.onCreateOptionsMenu(menu);
        };

        @Override
        publick boolean onOptionsItemSelected(MenuItem item) {
            // обработчик выбора элемента в меню
            ...
            return super.onOptionsItemSelected(item);
        };

        @Override
        publick boolean onOptionsItemSelected(MenuItem item) {
            // обработчик контекстного меню, вызывается каждый раз перед показом
            ...
            return super.onOptionsItemSelected(item);
        };

        @Override
        publick boolean onOptionsItemSelected(MenuItem item) {
            // обработчик выбора элемента в контекстном меню
            ...
            return super.onOptionsItemSelected(item);
        };

        @Override
        public void onConfigurationChanged(Configuration conf) {
            super.onConfigurationChanged(conf);
            // обработчик изменения конфигурации
            ...


    };