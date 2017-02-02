jqueryvalidation
================

https://jqueryvalidation.org/

.. code-block:: js

    $("#form_id").validate({

        // правила валидации полей
        rules: {
            form_field_name: {
                required: true,
                email: true,
                equalTo: "form_field_id",
                minlength: 6,
                digits: true
            }
        },

        // сообщения ошибок при валидации полей
        messages: {
            form_field_name: {
                required: "message"
            }
        },

        // убирать ошибку при фокусе элемента
        focusCleanUp: true,

        // убрать фокус после валидации
        focusInvalid: false,

        // обработчик ошибки валидации
        invalidHandler: function(event, validator){
            $(".js-form-message").text("Ошибка");
        },

        // обработчик ввода
        onkeyup: function(element){
            $(".js-form-message").text("");
        },

        // обработчик ошибок
        errorPlacement: function(error, element){
            return true;
        }
    });