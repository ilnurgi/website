.. py:module:: contacts

contacts
========

Модуль позволяет работат с контактами
    
    >>> import contacts
    >>> db = contacts.open()  

.. py:method:: open([filename, mode])
    
    :param filename: путь к файлу справочника
    :param mode: режим открытия (c - создать, n - новый)

    Возвращает объект :py:class:`ContactDb()`. По дефолту открывает стандартный справочник смартфона.

ContactDb()
-----------

.. py:class:: ContactDb()

    Объект, база данных контактов

.. py:method:: ContactDb.add_contact() 
    
    Возвращает объект новый объект :py:class:`Contact`

.. py:method:: ContactDb.find(searchterm) 
    
    Поиск контаков которые содержат searcterm, возвращает список 

.. py:method:: ContactDb.import_vcards(vcards) 
    
    Импорт карточек 

.. py:method:: ContactDb.export_vcards(ids) 
    
    Експорт контакта с номером id в карточку, возвращает строку 

.. py:method:: ContactDb.keys() 
    
    Возвращает список ID контактов, объектов Contact. 

.. py:method:: ContactDb.compact_required() 
    
    Verifies whether compacting is recommended. Returns an integer value indicating either a true or false state. Returns True if more than 32K of space is unused and if this comprises more than 50 percent of the database file, or if more than 256K is wasted in the database file. 

.. py:method:: ContactDb.compact() 
    
    Compacts the database to its minimum size. 

.. py:method:: ContactDb.field_types() 
    
    Возвращает список словарей который содержит информацию обо всех филдах. 

.. py:method:: ContactDb.groups 
    
    Список объектов :py:class:`Groups` групп контактов

Contact()
---------

.. py:class:: Contact()

.. py:method:: Contact.begin() 
    
    Блокирует изменение контакта текущими приложениями. 

.. py:method:: Contact.commit() 
    
    Освобождвает блокировку и сохраняет изменения 

.. py:method:: Contact.rollback() 
    
    Освобождает блокировку и откатывает изменения

.. py:method:: Contact.as_vcard() 
    
    Возвращает строку контакта в формате карточки. 

.. py:method:: Contact.add_field(type [, value [, label=field label ][, location=location spec ]]) 
    
    :param type: 

        * city
        * company_name
        * country
        * date
        * dtmf_string
        * email_address
        * extended_address
        * fax_number
        * first_name
        * job_title
        * last_name
        * mobile_number
        * note
        * pager_number
        * phone_number
        * po_box
        * postal_address
        * postal_code
        * state
        * street_address
        * url
        * video_number
        * picture
        * second_name
        * voip
        * sip_id
        * personal_ringtone
        * share_view
        * prefix
        * suffix
        * push_to_talk
        * locationid_indication

        The following field types are recognized but cannot be created at present:

        * first_name_reading
        * last_name_reading
        * speed_dial
        * thumbnail_image
        * voice_tag
        * wvid

    Добавляет новый филд контакту.

.. py:method:: Contact.find([type=field type ][, location=field location ]) 
    
    Возвращает список фидов контакта. Если параметры не заданы, то возвращает все фиды.

    db[7].find()

.. py:attribute:: Contact.id 
    
    Возвращает уникальный номер контакта, id. Только для чтения 

.. py:attribute:: Contact.title 
    
    Возвращает имя абонента. Только для чтения 

.. py:attribute:: Contact.last_modified 
    
    Возвращает дату последнего измененения контакта. Только для чтения 

.. py:attribute:: Contact.is_group 
    
    Возвращает 1 если контакт состоит в группе. Только для чтения

ContactField()
--------------

.. py:class:: ContactField()

.. py:attribute:: ContactField.label 
    
    Отображаемый текст фида. 

.. py:attribute:: ContactField.value 
    
    Значение фида 

.. py:attribute:: ContactField.type 
    
    Тип фида 

.. py:attribute:: ContactField.location 
    
    Параметр соответствует типу номера - обычный (none), домашний ('home'), служебный ('work') 

.. py:attribute:: ContactField.schema 

    A dictionary that contains some properties of this field. The contents of this dictionary correspond to those returned by the ContactDb method field_types.

Groups()
--------

.. py:class:: Groups()

.. py:method:: Groups.add_group([name]) 
    
    Добавляет новую группу

Group()
-------

.. py:class:: Group()

.. py:attribute:: Group.id 
    
    Возвращает id группы 

.. py:attribute:: Group.name 
    
    Возвращает название группы

FAQ
---

.. glossary:: 
    
    Удаляем контакт

        .. code-block:: python 
        
            import contacts
            db = contacts.open()
            del db[contact.id]