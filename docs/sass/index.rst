sass
====

.. code-block:: sh

    npm install gulp-sass


.. code-block:: sass

    // блоки выделяются отсутпами, а не фигурными скобками

    $color-green: #6cca4f;
    $padding: 20px;
    $width: 80%;

    // миксин
    =reset(){
        //
    }

    // вызов миксина
    +reset()
    .wrapper
        +wrapper()
    .parent
        .child
            +row-flex()
            +lg-block
                background-color: red;





scss
====

.. code-block:: css

    // переменные
    $key: "some-key";
    $val: 12px;
    $color-green: #6cca4f;
    $padding: 20px;
    $width: 80%;

    // миксин
    @mixin reset(){
        //
    }
    @mixin box-sizing{
        box-sizing: border-box;
    }
    @mixin border-radius($radius) {
        border-radius: $radius;
    }

    // вызов миксина
    @include wrapper;
    @include reset();
    @include debug(@key, @value);
    @include some-block{
        padding: 3px;
        margin-left: #{calc(#{$value} + #{value})};
    };
    .block {
        padding: $padding;
        border: 1px solid $color-green;
        width: $width/2 - 2%;

        color: darken(#4b6ef2, 40%);

        @include box-sizing;

        @include border-radius(10px);
    }
