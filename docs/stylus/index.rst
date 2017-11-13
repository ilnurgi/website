stylus
======

.. code-block:: sh

    npm install gulp-stylus


.. code-block:: css

    // блоки выделяются отступами, а не фигурными скобками
    $color-green: #6cca4f;
    $padding: 20px;
    $width: 80%;

    // миксин
    row-flex()
        display flex
        width "calc(%s - %s)" % ($value $offset)

    // вызов миксина
    reset()
    debug(@key, @value)

    .row
        .column
            row-flex()
            md-block(@block{
                background: red
            })