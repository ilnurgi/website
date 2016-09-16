FAQ
===

Треуголник
----------

.. code-block:: css

    blockquote {
        background-color: green;
        position: relative;
        color: white;
        padding: 15px 25px;
        margin: 10px 10px 0;
    }

    blockquote:after {
        border: 15px solid;
        border-color: green transparent transparent;
        top: 100%; left: 10px;
        width: 0; height: 0;
        position: absolute;
        content: '';
    }