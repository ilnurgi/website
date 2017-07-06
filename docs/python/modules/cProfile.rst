.. py:module:: cProfile

cProfile
========

.. code-block:: sh

    python -m cProfile some.py

    # сортировка
    python -m cProfile -s tottime some.py

    # генерирует отчет для pstats
    python -m cProfile -o profile_output some.py


.. code-block:: py

    import cProfile
    import pstats

    def view_stats(fil, text):
        """
        просмотр pstats для файла
        """
        stats = pstats.Stats(fil)
        # удаляем длинные папки
        stats.strip.dirs()
        sorted_stats = stats.sort_stats('tottime')
        sorted_stats.print_stats('text')

    def some_method():
        pass

    cProfile.run('some_method()', 'profile_output_new')
    view_stats('profile_output_new', 'some')