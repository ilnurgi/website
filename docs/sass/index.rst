sass
====

.. code-block:: shell

    sudo apt-get install ruby
    sudo gem install sass
    mkdir project
    cd project
    touch style.css
    touch.scss
    sass --watch style.css:style.css

.. code-block:: sass

    $color-green: #6cca4f;
    $padding: 20px;
    $width: 80%;

    @mixin box-sizing{
        box-sizing: border-box;
    }

    @mixin border-radius($radius) {
        border-radius: $radius;
    }

    .block {
        padding: $padding;
        border: 1px solid $color-green;
        width: $width/2 - 2%;

        color: darken(#4b6ef2, 40%);

        @include box-sizing;

        @include border-radius(10px);
    }