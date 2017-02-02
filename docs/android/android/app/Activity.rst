android.app.Activity
====================


.. py:class:: android.app.Activity

    Активность, экран который отображается пользователю

    .. code-block:: java

        import android.app.Activity;
        import android.os.Bundle;

        public class MyActivity extends Activity {
            ...
        }


    .. py:method:: findViewById(id)

        Возвращает объект по идентификатору

        .. code-block:: java

            Button btn = (Button)findViewById(R.id.btn);


    .. py:method:: getIntent()

        Возвращает интент, :py:class:`android.content.Intent`, который вызвал это активити

        .. code-block:: java

            Intent intent = getIntent()


    .. py:method:: getLayoutInflater()

        Возвращает конструктор вью объектов :py:class:`android.view.LayoutInflater`

        .. code-block:: java

            LayoutInflater layoutInflater = getLayoutInflater();


    .. py:method:: getPreferences(int mode)

        Возвращает объект настроек :py:class:`android.content.SharedPreferences` приложения

        Аналогичен :py:meth:`android.app.Activity.getSharedPreferences`,
        но название файла настроек использует как название активити

        * mode

            * :py:attr:`android.content.Context.MODE_PRIVATE`

        .. code-block:: java

            SharedPreferences sharedPreference = getPreferences(MODE_PRIVATE);


    .. py:method:: getResources()

        Возвращает объект ресурсов, :py:class:`android.content.res.Resources`


    .. py:method:: getSharedPreferences(String name, int mode)

        Возвращает объект настроек :py:class:`android.content.SharedPreferences` приложения

        Аналогичен :py:meth:`android.app.Activity.getPreferences`,
        но позволяет задать название файла настроек

        * mode

            * :py:attr:`android.content.Context.MODE_PRIVATE`

        .. code-block:: java

            SharedPreferences sharedPreference = getSharedPreferences(
                "MainSettings", MODE_PRIVATE);


    .. py:method:: onActivityResult(int requestCode, int resultCode, Intent data)


    .. py:method:: onBackPressed()

        Обработчик нажатия кнопки назад


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

        Обработчик контекстного меню, вызывается каждый раз перед показом

        * menu - :py:class:`android.view.ContextMenu`

        * view - :py:class:`android.view.View`

        * menuInfo - :py:class:`android.view.ContextMenu.ContextMenuInfo`


    .. py:method:: onCreateDialog(int id)

        Создает и возвращает :py:class:`android.app.Dialog`

        Все созданные диалоги сохраняются и не создаются повторно в дальнейшем

        Для изменения диалога необходимо использовать
        :py:meth:`android.app.Activity.onPrepareDialog`


    .. py:method:: onCreateOptionsMenu(menu)

        Обработчик создания меню, вызывается 1 раз при первом показе меню

        * menu - :py:class:`android.view.Menu`

        .. code-block:: java

            public boolean onCreateOptionsMenu(Menu menu) {

                menu.add("Item1");

                return super.onCreateOptionsMenu(menu);
            }

        .. code-block:: java

            public boolean onCreateOptionsMenu(Menu menu) {

                getMenuInflater().inflate(R.menu.myMenu, menu);

                return super.onCreateOptionsMenu(menu);
            }


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

        .. code-block:: java

            public boolean onOptionsItemSelected(MenuItem item) {

                return super.onOptionsItemSelected(item);
            }


    .. py:method:: onPause()

        Вызывается, перед тем как будет показано другое активити

        .. code-block:: java

            public void onPause(){
                super.onPause();
            }


    .. py:method:: onPrepareDialog(int dialogId, Dialog dialog)

        Изменяет диалог перед каждым показом


    .. py:method:: onPrepareOptionsMenu(menu)

        Обработчик создания меню, вызывается каждый раз при показе меню

        Можно менять меню при каждом показе

        * menu - :py:class:`android.view.Menu`

        .. code-block:: java

            public boolean onPrepareOptionsMenu(Menu menu) {

                menu.setGroupVisible(1, chb.isChecked());

                return super.onPrepareOptionsMenu(menu);
            }


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


    .. py:method:: setContentView(R.layout.id)

        Устанавливает содержимое активити

        .. code-block:: java

            setContentView(R.layout.main);

        .. code-block:: java

            setContentView(linearLayout, linearLayoutParams);


    .. py:method:: setResult(resultCode, Intent intent)

        Устанавлиает результат работы активити, для передачи его родительскому активити.

        .. code-block:: java

            Intent intent = new Intent();
            intent.putExtra(EXTRA_KEY, "some result");

            setResult(RESULT_OK, intent);


    .. py:method:: showDialog(int id)

        Создает дилог и показывает его

        Вызывает метод :py:meth:`android.app.Activity.onCreateDialog`


    .. py:method:: startActivity(Intent intent)

        Запускает активность по интенту

        * intent - :py:class:`android.content.Intent`

        .. code-block:: java

            Intent intent = new Intent(this, SomeClass.class);
            startActivity(intent);


    .. py:method:: startActivityForResult(Intent intent, int requestCode)

        Запускает активность по интенту для получения результатов от него.

        Текущий активити становится как бы родителем,
        и при закрытии запускаемого интента будет вызван метод
        :py:meth:`android.app.Activity.onActivityResult`

        * intent - :py:class:`android.content.Intent`

        .. code-block:: java

            Intent intent = new Intent(this, SomeClass.class);
            startActivityForResult(intent, 1);
