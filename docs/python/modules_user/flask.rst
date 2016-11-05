.. py:module:: flask

flask
=====

.. code-block:: shell

    pip install flask

.. code-block:: py

    from flask import Flask, render_template, request
    app = Flask(__name__, static_folder='.', static_url_path='')

    @app.route('/')
    def home():
        return app.send_static_file('index.html')

    @app.route('/')
    def home2():
        return render_template('index.html', **{})

    @app.route('/<idi>')
    def echo(idi):
        return "id = {0}".format(idi)

    @app.route('/')
    def echo2():
        return "id = {0}".format(request.args.get("idi"))

    app.run(port=9999, debug=True)