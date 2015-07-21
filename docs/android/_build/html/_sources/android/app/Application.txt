.. _android_app_Application:

android.app.Application
=======================


.. py:class:: android.app.Application()

    объект, приложение


    .. py:method:: onCreate()

        вызывается при создании приложения


    .. py:method:: onTerminate()

        вызывается при преждевременном завершении работы


    .. py:method:: onLowMemory()

        вызывается при нехватке памяти передним приложениям


    .. py:method:: onConfigurationChanged()

        вызывается при изменении конфигурации


    .. py:method:: getGlobalStateValue()
    .. py:method:: setGlobalStateValue(value)


::

    import android.app.Application;
    import android.content.res.Configuration;
    
    public class MyApplication extends Application {
        
        private static MyApplication singleton;
        
        // Возвращает экземпляр данного класса
        public static MyApplication getInstance() {
            return singleton;
        }

        @Override
        public final void onCreate() {
            super.onCreate();
            singleton = this;
        }
    }
    

        