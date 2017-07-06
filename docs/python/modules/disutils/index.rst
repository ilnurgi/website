.. py:module:: disutils

disutils
========

.. toctree::
    :maxdepth: 1

    core


В папке должен быть файл LICENSE.txt, MANIFEST.in

Консольные команды
------------------

* sdist - создает утсановончый пакет с исходными кодами

    .. code-block:: sh

        python setup.py sdist

* bdist - создает утсановончый пакет с исходными кодами

    .. code-block:: sh

        python setup.py bdist

Дистрибуция на pypi
-------------------

1. создать аккаунт на https://testpypi.python.org/pypi?:action=register_form
2. создать файл .pypic.rc и положить в домашнюю директорию ~/.pypirc.

    .. code-block:: ini

        [disutils]
        index-servers=
        pypitest
        pypimain

        [pypitest]
        repository=https://testpypi.python.org/pypi
        username=username
        password=password

        [pypimain]
        repository = https://pypi.python.org/pypi
        username=username
        password=password

3. регистрируем

    .. code-block:: sh

        python setup.py register -r pypitest
        # or
        python setup.py register -r https://testpypi.python.org/pypi

4. загрузка пакета

    .. code-block:: sh

        python setup.py sdist upload -r pypitest


Все пункты одной командой

.. code-block:: sh

    python setup.py register -r pypitest sdist upload -r pypitest

Можно создать локальный pypi server

    .. code-block:: sh

        pip install pypiserver
        pypi-server -p 8081 ./dist
        pip install -i http://localhost:8081 some_package_name