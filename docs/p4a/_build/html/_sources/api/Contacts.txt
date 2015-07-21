Contacts
========

Результат работы всех методов :py:class:`Result`

.. py:method:: contactsGet([list attributes])
 
    возвращает список контактов


.. py:method:: contactsGetAttributes()

    возвращает список доступных атрибутов контаков


.. py:method:: contactsGetById(int id[ , list attributes])

    возвращает контакт по иди


.. py:method:: contactsGetCount()

    возвращает общее количество контактов


.. py:method:: contactsGetIds()

    возвращает список иди, контактов


.. py:method:: pickContact()

    отображает окно со списком контаков, с возможностью поиска, возвращает выбранный контакт

    >>> droid.pickContact().result
    {
        u'flags': 1, 
        u'extras': None, 
        u'data': u'content://contacts/people/1', 
        u'categories': None
    }


.. py:method:: pickPhone()

    отображает окно со списком контаков и с номерами телефонов, с возможностью поиска, возвращает номер телефона выбранного контакта

    >>> droid.pickPhone()
    123


.. py:method:: queryAttributes(str uri)
 
    :param str uri: The URI, using the content:// scheme, for the content to retrieve

    Content Resolver Query Attributes


.. py:method:: queryContent(**kwargs)
 
    :param str uri: The URI, using the content:// scheme, for the content to retrieve.,
    :param list attributes: не обязательный, A list of which columns to return. Passing null will return all columns,
    :param str selection: не обязательный, A filter declaring which rows to return,
    :param list selectionArgs: не обязательный, You may include ?s in selection, which will be replaced by the values from selectionArgs,
    :param str order: не обязательный,  How to order the rows

    Content Resolver Query