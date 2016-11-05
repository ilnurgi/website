.. py:module:: beautifulsoup

beautifulsoup
=============

.. code-block:: shell

    pip istall beautifulsoup4


.. code-block:: py

    from bs4 import BeautifulSoup as soup

    # some_code

    doc = soup(page)
    links = [element.get('href') for element in doc.find_all('a')]

