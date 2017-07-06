.. py:module:: beautifulsoup

beautifulsoup
=============

.. code-block:: shell

    pip install beautifulsoup4


>>> from bs4 import BeautifulSoup

BeautifulSoup()
---------------

.. py:class:: BeautifulSoup(html_string)

    Парсер html

    .. code-block:: py

        bs_obj = BeautifulSoup(some_html_string)


    .. py:method:: find(name=None, attributes={}, recursive=True, text=None, *kwargs)

        Возвращает первый найденный элемент


    .. py:method:: findAll(name=None, attributes={}, recursive=True, text=None, limit=None, *kwargs)

        Возвращает список элементов :py:class:`Tag`, по указанному тегу и фильтру

        .. code-block:: py

            span_list = bs_obj.findAll('span', {'class': 'green'})
            for span in span_list:
                print(span.get_text())

            hs = bs_obj.findAll({'h1', 'h2', 'h3', 'h4', 'h5', 'h6'})

            id_text_elem = bs_obj.findAll(id='text')

            imgs = bs_obj.findAll('img', {'src': re.compile('\.\.\/img\/*\.jpg')})

            imgs = bs_obj.findAll(lambda tag: len(tag.attrs) == 2)


Tag()
-----

.. py:class:: Tag()

    Тег элемент


    .. py:attribute:: attrs

        Словарь атрибутов элемента

        .. code-block:: py

            table_elem.attrs
            # {'class': 'table'}

            image_elem.attrs['src']


    .. py:attribute:: children

        Список дочерних элементов :py:class:`Tag`

        .. code-block:: py

            for child in span_elem.children:
                print(child.get_text())


    .. py:attribute:: descendants

        Список всех вложенных элементов :py:class:`Tag`

        .. code-block:: py

            for child in span_elem.descendants:
                print(child)


    .. py:attribute:: next_sibling

        Список всех элементов на уровне

        .. code-block:: py

            for sibling in table_elem.tr.next_sibling:
                print(sibling)


    .. py:attribute:: parent

        Родительский элемент :py:class:`Tag`

        .. code-block:: py

            table_elem.parent


    .. py:attribute:: previous_siblings

        Список всех элементов на уровне

        .. code-block:: py

            for sibling in table_elem.tr.previous_siblings:
                print(sibling)


    .. py:method:: get_text()

        Удаляем все теги из элемента и возвращает только текст содержимого

        .. code-block:: py

            span_elem.get_text()
            # some text


NavigableString()
-----------------

.. py:class:: NavigableString()

    Текст внутри тегов


Comment()
---------

.. py:class:: Comment()

    Коментарии