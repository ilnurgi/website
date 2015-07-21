Операторы
=========

Условия
-------

>>> if a == 5:
        print 5
    elif a == 6:
        print 6
    else:
        print 7
>>> 

Цикл
----

>>> for index in iter:
        if i == 0:
            break # прерывание цикла
        elif i == 1:
            continue # переход на следующую итерацию цикла
        print i
    else:
        print u'Данный блок выполняется если цикл закончился без break'

>>> while a < 5:
        if a == 1:
            break # прерывание цикла
        elif a == 2:
            continue # переход на следующую итерацию цикла
        print a
    else:
        print u'Данный блок выполняется если цикл закончился без break'

Перехват ошибок
---------------

>>> try:
        a = 5/0
    except ValueError:
        print 'valueError'
    except Exception as err:
        print 'error'
    else:
        print u'Данный блок выполняется если исключений не возникло'
    finaly:
        print u'Данный блок выполняется выполняется в любом случае'

Другие
------

::
    
    #!/usr/bin/python
    # установили интерпретатор, который исполнит данный скрипт
    # coding: utf-8
    # установили кодировку файла

    # выводим в поток вывода строку
    print 'x'

    # в третьей редакции
    print('x')
    
    # оператор пустышка, ничего не деалет
    pass