.. py:module:: java.lang

ClassLoader - отвечает за загрузку классов
==========================================

Содержит методы, необходимые для динамической загрузки новых классов

Это абстрактный класс, ответственный за загрузку классов. По имени класса он находит либо генерирует данные, которые составляют определение класса. Обычно для этого используется следующая стратегия: название класса преобразуется в название файла - "class file", из которого и считывается вся необходимая информация.

Каждый объект Class содержит ссылку на объект ClassLoader, посредством которого он был загружен.

Для изменения способа загрузки классов, можно реализовать свой загрузчик классов, унаследовав его от ClassLoader. Так, хотя обычно классы загружаются из файлов, однако бывают и другие ситуации. Например, классы могут загружаться через сетевое соединение.


.. py:class:: ClassLoader()

    .. py:method:: defineClass() 

        преобразует массив байт в экземпляр класса Class. Экземпляры полученного таким образом класса могут быть получены, используя метод newInstance() у объекта Class. Методы объектов, полученных с помощью загрузчика классов, могут ссылаться на другие, доступные в запущенном приложении классы. Для получения классов, на которые можно ссылаться, вызывается метод loadClass у загрузчика классов.

::
    
    class NetworkClassLoader extends ClassLoader {
        String host;
        int port;
    
        public NetworkClassLoader(String host, int port) {
            this.host = host;
            this.port = port;
        }
    
        public Class findClass(String className) {
            byte[] bytes = loadClassData(className);
            return defineClass(className, bytes, 0, bytes.length)
        }
        
        private byte[] loadClassData(String className) {
            byte[] result = null;
            // open connection, load the class data
            return result;
        }
    }