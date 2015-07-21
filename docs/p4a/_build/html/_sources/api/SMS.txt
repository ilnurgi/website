SMS
===


.. py:method:: smsDeleteMessage(int message_id)

    удаляет сообщение


.. py:method:: smsGetAttributes()

    возвращает список всех атрибутов сообщений 


.. py:method:: smsGetMessageById(int message_id[, list attributes])

    возвращает список атрибутов сообщения


.. py:method:: smsGetMessageCount(bool unreadOnly[ , str folder='inbox'])

    возвращает количесвто сообщений


.. py:method:: smsGetMessageIds(bool unreadOnly[, str folder='inbox'])

    возвращает список всех сообщений


.. py:method:: smsGetMessages(bool unreadOnly[, str folder='inbox', list attributes])

    возвращает сообщения с атрибутоами


.. py:method:: smsMarkMessageRead(list message_ids, bool read)

    отмечает сообщение как прочитанное


.. py:method:: smsSend(str destinationAddress, str text)

    отправялет сообщение