.. py:module:: multiprocessing

multiprocessing
===============


Pool
----

.. py:class:: Pool(worker_count)

    .. code-block:: py

        pool = Pool(2)


    .. py:class:: ApplyResult()

        .. py:method:: get()

            возвращает значение результата


    .. py:method:: apply(func, args)

        .. code-block:: py

            result = [pool.apply(some_func, args=(num, )) for num in [1, 2, 3]]


    .. py:method:: apply_async(func, args)

        Возвращает :py:class:`ApplyResult`

        .. code-block:: py

            result = [pool.apply_async(some_func, args=(num, )) for num in [1, 2, 3]]


    .. py:method:: close()

        .. code-block:: py

            pool.close()


    .. py:method:: join()

        .. code-block:: py

            pool.join()


    .. py:method:: map(func, iterable)

        .. code-block:: py

            pool.map(some_func, [1,2,3])


    .. py:method:: starmap_async()




current_process
---------------

.. py:method:: current_process()

    Возвращает текущий процесс


