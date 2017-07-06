.. py:module:: sphinx

sphinx
======

.. code-block:: sh

    pip install sphinx
    pip install pygments
    sphinx-quickstart


.. code-block:: py

    # conf.py

    extensions = [

        # для автогенерации доков из исходников
        'sphinx.ext.autodoc',

        # для использования .. todo::
        'sphinx.ext.todo'
    ]

    sys.path.insert(0, os.path.abspath(src_path))


.. code-block:: sh

    sphinx-apidoc -o source/ ../
    sphinx-build source build
    make html