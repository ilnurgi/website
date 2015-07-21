.. py:module:: java.lang

Class - экземпляры этого класса представляют классы и интерфейсы в запущенной Java-программе
=============================================================================

.. py:class:: Class()

    
    .. py:method:: public static Class forName(String name, boolean initialize, ClassLoader loader)

        Возвращает объект Class, соответствующий классу или интерфейсу с названием, указанным в name (необходимо указывать полное название класса или интерфейса), используя переданный загрузчик классов. Если в качестве загрузчика классов loader передано значение null, будет взят таковой, который использовался для загрузки вызывающего класса. При этом класс будет инициализирован, только если значение initialize равно true и класс не был инициализирован ранее.


    .. py:method:: public Object newInstance()

        Создает и возвращает объект класса, который представляется данным экземпляром Class. Создание будет проходить, используя конструктор без параметров. Если такового в классе нет, будет брошено исключение InstantiationException. Это же исключение будет брошено, если объект Class соответствует абстрактному классу, интерфейсу или же по какой-либо другой причине.

        .. py:method:: getClass()

        возвращает класс объекта


    .. py:staticmethod:: forName(String className)

        возвращает экземпляр класса

        ::

            Class c1 = Class.forName("java.lang.String");


    .. py:method:: isAnnotation()
    .. py:method:: isArray()
    .. py:method:: isInterface()
    .. py:method:: isEnum()
    .. py:method:: isPrimitive()
    .. py:method:: getDeclaredClasses()
    .. py:method:: getDeclaredConstructors()
    .. py:method:: getDeclaredMethods()
    .. py:method:: getDeclaredFields()
    .. py:method:: getSuperclass()
    .. py:method:: getPackage()
    .. py:method:: getModifiers()