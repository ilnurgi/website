.. py:module:: bottle

bottle
======


http://bottlepy.org/docs/dev

.. code-block:: shell

    pip install bottle

.. code-block:: py

    from bottle import route, run, static_file

    @route("/")
    def index():
        return "text"

    @route("/")
    def index2():
        return static_file("index.html", root=".")

    @route("/<idi>")
    def index3(idi):
        return "idi = {0}".format(idi)

    run(host="localhost", port=9999, debug=True, reloader=True)


.. code-block:: py

    # application.wsgi
    # для использования с веб-сервером (nginx, apache)

    import bottle

    application = bottle.default_app()

    @bottle.roue("/")
    def index():
        return "hello world"

.. code-block:: conf

    # пример конфига апача
    <VirtualHost *:80>
        DocumentRoot /var/www
        WSGIScriptAlias / /var/www/test/home.wsgi
        <Directory /var/www/test>
            Order allow,deny
            Allow from all
        </Directory>
    </VirtualHost>

