.. py:module:: logs

logs
====

Данный модуль предоставляет доступ к журналу смартфона, где аккумулируется все информация о принятых или отправленных SMS, совершенных звонках и т.д. 

.. py:method:: raw_log_data() 

    Возвращает все содержимое журнала в виде списка словарей, каждый элемент которого несет определенную информацию о событии:

        * 'number' - номер (строка Unicode);
        * 'name' - имя (строка Unicode);
        * 'description' - тип
            * 'Short message' - короткое сообщение
            * 'Voice call' - голосовой вызов);
        * 'direction' - направление
            * 'Incoming' - входящий
            * 'Outgoing' - исходящий);
        * 'status' - статус
        * 'Sent' - отправлено
        * 'subject' - содержимое;
        * 'id' - уникальный номер;
        * 'contact';
        * 'duration';
        * 'duration type';
        * 'flags';
        * 'link';
        * 'data';
        * 'time' - время события.

    >>> logs.raw_log_data()
    [
     {'status': u'Delivered',
      'direction': u'Incoming',
      ...}
    ]

.. py:method:: log_data(type, [start_log=0, num_of_logs=_all_logs, mode='in']) 

    :param type: тип лога ('call', 'sms', 'data', 'fax', 'email', 'scheduler')
    :param mode: тип ('in', 'out', 'fetched', 'missed', 'in_alt', 'out_alt')
    :param start_log: начальная позиция
    :param num_of_logs: количество записей
    
    Возвращает список событий

.. py:method:: log_data_by_time(type, start_time, end_time, [mode='in']) 
    
    :param type: тип лога ('call', 'sms', 'data', 'fax', 'email', 'scheduler')
    :param mode: тип ('in', 'out', 'fetched', 'missed', 'in_alt', 'out_alt')
    :param start_time: начало промежутка, сек
    :param end_time: конец промежутка, сек

    Возвращает список событий во временном периоде

.. py:method:: calls([start_log=0, num_of_logs=_all_logs, mode='in']) 
        
    :param mode: тип ('in', 'out', 'fetched', 'missed', 'in_alt', 'out_alt')
    :param start_log: начальная позиция
    :param num_of_logs: количество записей
    
    Возвращает список вызовов

.. py:method:: faxes([start_log=0, num_of_logs=_all_logs, mode='in'])

    :param mode: тип ('in', 'out', 'fetched', 'missed', 'in_alt', 'out_alt')
    :param start_log: начальная позиция
    :param num_of_logs: количество записей 
    
    Возвращает список факсов

.. py:method:: emails([start_log=0, num_of_logs=_all_logs, mode='in']) 
    
    :param mode: тип ('in', 'out', 'fetched', 'missed', 'in_alt', 'out_alt')
    :param start_log: начальная позиция
    :param num_of_logs: количество записей

    Возвращает список электронных писем

.. py:method:: sms([start_log=0, num_of_logs=_all_logs, mode='in']) 
    
    :param mode: тип ('in', 'out', 'fetched', 'missed', 'in_alt', 'out_alt')
    :param start_log: начальная позиция
    :param num_of_logs: количество записей

    Возвращает список сообщений

.. py:method:: scheduler_logs([start_log=0, num_of_logs=_all_logs, mode='in']) 

    :param mode: тип ('in', 'out', 'fetched', 'missed', 'in_alt', 'out_alt')
    :param start_log: начальная позиция
    :param num_of_logs: количество записей

    Возвращает список выполненных событий по расписанию

.. py:method:: data_logs([start_log=0, num_of_logs=_all_logs, mode='in']) 
    
    :param mode: тип ('in', 'out', 'fetched', 'missed', 'in_alt', 'out_alt')
    :param start_log: начальная позиция
    :param num_of_logs: количество записей

    Возвращает список событий по передаче данных