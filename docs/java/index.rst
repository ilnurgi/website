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



описание флагов жавы
-XX:-OmitStackTraceInFastThrow - выключает оптимизацию вывода стрек стрейса

-XX:+PrintConcurentLocks - выводит информацию о том какой поток находится в блоке синхронайз

/*
получение названия файла и номера строчки текущегй работы
дорогая операция
*/
public static String getLocation(){
    StackTraceElement s = new Exception().getStackTrace()[2];

    // Thread.current().getStackTrace(); аналог

    return s.getFileName() + ':' + s.getLineNumber();
}



подключение модуля для статитсики запросов

.. code-block:: ini
    
    # postgresql.conf
    shared_preload_libraries = 'pg_stat_statements'

    # сколько запросов держать в памяти
    pg_stat_staetements.max = 10000

    # какие запросы обрабатывать
    pg_stat_staetements.track = all

.. code-block:: sql
    
    -- регистраци
    create extension if not exists pg_stat_staetements;

    -- сброс статистики
    select pg_stat_staetements_reset();
    ....
    select * from pg_stat_staetements;



протоколирования запросов

.. code-block:: ini
    
    # включение
    log_duration = on
    # время в мс, больше которой запросы логируются
    log_min_duration_statement = 50

    # логгирование в csv файл, пригодный для анализа утилитой pgbadger
    # sudo apt-get install libtext-csv-xs-perl pgbadger
    # pgbadger /var/log/*.csv
    log_lock_waits = on
    log_filename = 'postgresql-%Y-%m-%d_%H%M%S'
    log_directory = '/var/log/postgresql'
    log_destination = 'csvlog'
    logging_collector = on

.. code-block:: sql

    -- включение логирования для конкретного запроса
    set log_min_duration_statement = 50;
    select * from table;