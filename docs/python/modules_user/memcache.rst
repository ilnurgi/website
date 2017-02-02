.. py:module:: memcached

memcached
=========

Клиент для сервера memcached

.. code-block:: bash

    pip install python-memcached

.. code-block:: py

    import memcache
    db = memcache.Client(["127.0.0.1:11211"])

    db.set("key1", "value1")
    # True

    db.get("key1")
    # "value1"

    db.set("key2", 0)
    # True

    db.incr("key2", 3)
    # 3

    db.get("key2")
    # 3