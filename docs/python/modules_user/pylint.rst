.. py:module:: pylint

pylint
======

.. code-block:: sh

    pip install pylint
    pylint script.py
    pylint --generate-rcfile > .pylintrc

.. code-block:: ini

    # .pylintrc

    init-hook='import sys; sys.path.append("/path/to/module/")'