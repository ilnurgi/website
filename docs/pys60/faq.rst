FAQ
===========

.. glossary:: 
    
    Использование кириллицы в pys60 1.x
    
        >>> def ru(text):  
                return text.decode('кодировка файла скрипта')
        >>> text = ru('привет')

    Чтобы скрипт не вылетал после того как он исполнится

        >>> # в начале скрипта создаем замок
        >>> lock = e32.Ao_lock()
        >>> ...
        >>> def exit():
                """функция, выхода из скрипта"""
                lock.signal()        
        >>> ...
        >>> # в конце скрипта
        >>> lock.wat()

    Импорт pyd модулей

        >>> try:
                import im
                mymodule = imp.load_dynamic('mymodule', 'c:\\sys\\bin\\mymodule.pyd')
            except:
                import mymodule
        >>>