Конспекты по Java
=================

Содержание

.. toctree::
    :maxdepth: 2

    base/index
    java/index





::

    /** коментарии */
    // коментарии

    @Override - признак переопределнности

    switch (){
        
        case :
            ...
            break
        case :
            ...
            break
        default:

    }

    loops циклы   
    package com.android;
    import ....


    char[] array = new char[3]
    char[][] array = new char[3][3]

    public Field() {
      this(DEFAULT_SIZE)
    }

    public Field(int size) {
      
    }

    public class Student extends Human {}

    abstract
    implements

    ArrayList, Inteher(), Float(), String()

    Double.parseDouble(String str)

    final методы не могут быть перекрыты
    final классы не могут быть унаследованы
    final атрибуты не могут быть перезаписаны

    try {
      
    } catch (final IOException e){
      final - оптимизирует код лучше для продакшена
    } catch (IOException | Error2 | Error3 e){
      final - оптимизирует код лучше для продакшена
    } finaly {
      
    }

    try (myFileInputStream=new FileInputStream('1.txt')){
      throw new Exception()
    } catch (Exception e){
      e.printStackTrace()
    }

    implements Item1, item2 ....

    instanceof

    java.util
    java.util.concurrent

    <?>
    <? extends Model>
    <? super Model>

    serialazation traNSIENT

    все объекты имеюют метод ToSting()

    System.arraycopy(arr0, 1, arr1, 2, 3) копирование массива


    Character.isDigit(str)
    Integer.valueOf(str)

    "".substring()