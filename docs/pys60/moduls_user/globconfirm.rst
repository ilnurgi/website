.. py:module:: globconfirm

globconfirm
===========

.. py:method:: show(title, type) 
    
    :param title: сообщение
    :param type: тип окна

        * note
        * warning
        * confirm
        * error
        * charging
        * wait
        * permanent
        * not_charging
        * battery_full
        * battery_low
        * recharge_battery
        * text        

    Отображает информационное окно 

    >>> globconfirm.show(u'hello world', 'note')

.. image:: globconfirm.png