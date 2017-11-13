.. code-block:: sh

    npm install gulp-less


.. code-block:: css

    // переменные
    @red: #0ff;

    // миксин
    .mixin(){
        display: flex;
    }
    .mixin(@name, @value){
        @{name}: @value;
    }
    .mixin-block(@content) {
        @media {
            @content;
        }
    }

    //  вложенность и вызов миксина
    .row {
        @media {
            display: flex;
        }

        .column {
            color: @red;
            width: ~"calc(100% - @{size})";
        }

        &:hover {
            color: black;
        }

        &-column {
            color: red;
        }

        .mixin();
        .mixin(order, 0);
        .mixin-block({
            order: 0
        });
    }