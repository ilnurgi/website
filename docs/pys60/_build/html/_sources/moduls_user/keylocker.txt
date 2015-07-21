.. py:module:: keylocker

keylocker
=========

Модуль для блокирвки/разблокировки клавиатуры 

.. py:method:: Lock() 
    
    Блокирует без уведомлений
    
    >>> keylocker.Lock()
    True

.. py:method:: Lock_WithNote() 
    
    Блокирует c уведомлением
    
    >>> keylocker.Lock_WithNote()
    True

.. py:method:: Unlock() 
    
    Разблокирует без уведомлений

    >>> keylocker.Unlock()
    True

.. py:method:: Unlock_WithNote() 
    
    Разблокирует c уведомлением
    
    >>> keylocker.Unlock_WithNote()
    True