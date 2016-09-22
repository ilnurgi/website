.. py:module:: redis

redis
=====

Клиент для подключения к серверу redis, сервер структуры данных

.. code-block:: shell

    pip install redis


.. code-block:: py

    import redis

    conn = redis.Redis()

.. code-block:: py

    conn.set("key1", "value1")
    # True

    conn.get("key1")
    # "value1"

    conn.setnx("key1", "value1")
    # False
    # ключ уже существует

    conn.getset("key1", "new_value1")
    # value1
    # возвращает старое и сохраняет новое

    conn.getrange("key1", -6, -1)
    # "value1"

    conn.setrange("key1", 0, "NEW")

    conn.get("key1")
    # "NEW_value1"

    conn.mset({"key2": "value2"})
    # True

    conn.mget(("key1", "key2"))
    # ["NEW_value1", "value2"]

    conn.delete("fever")
    # True

.. code-block:: py

    conn.set('key3', 0)

    conn.incr('key3')
    # 1

    conn.incr('key3', 10)
    # 11

    conn.decr('key3')
    # 10

    conn.decr('key3', 7)
    # 3

    conn.set('key4', '101.5')
    # True

    conn.incrbyfloat('key4')
    # 102.5

    conn.incrbyfloat('key4', 0.5)
    # 103.0

    conn.incrbyfloat('key4', -0.5)
    # 102.5

.. code-block:: py

    # списки могут содержать только строки

    conn.lpush('key5', 'value1')
    # 1

    conn.lpush('key5', 'value2', 'value3')
    # 3

    conn.linsert('key5', 'before', 'value2', 'value4')
    # 4

    conn.linsert('key5', 'after', 'value2', 'value5')
    # 5

    conn.lset('key5', 2, 'value6')
    # True

    conn.rpush('key5', 'value7')
    # 7

    conn.lindex('key5', 3)
    # 'value3'

    conn.lrange('key5', 0, 2)
    # 'value1', 'value2', 'value3'

    conn.ltrim('key5', 1, 4)
    # True

.. code-block:: py

    # хеши могут содержать только строки

    conn.hmset("key6", {"k1": "v1"})
    # True

    conn.hset("key6", "k1", "n_v1")
    # 1

    conn.hsetnx("key6", "k2", "v2")
    # 1

    conn.hget("key6", "k1")
    # "n_v1"

    conn.hmget("key6", "k1", "k2")
    # ["n_v1", "v2"]

    conn.hkeys("key6")
    # ["k1", "k2"]

    conn.hvals("key6")
    # ["n_v1", "v2"]

    conn.hlen("key6")
    # 2

    conn.hgetall("key6")
    # {"k1": "n_v1", "k2": "v2"}