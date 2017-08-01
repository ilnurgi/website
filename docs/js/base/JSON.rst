JSON
====

.. py:class:: JSON()


    .. py:function:: parse(text[, reviver])

        Из строки в JSON

        .. code-block:: js

            JSON.parse('{"name": "ilnur"}');
            /*
            {
                "name": "ilnur"
            }
            */


    .. py:function:: stringify(obj[, filter[, indent]])

        Сериализует объект, массив или элементарное значение

        .. code-block:: js

            data = {
                'name': 'ilnur',
                age: 25
            }

            // Простая сериализация
            JSON.stringify(data);
            // "{"name":"ilnur","age":25}"
            
            // Указать точно, какие поля подлежат сериализации
            JSON.stringify(address, ["name"]);
            // {"name":"ilnur"}

            // Указать функцию замены, чтобы можно было сериализовать объекты RegExp
            JSON.stringify(patterns, function(key, value) {
                if (value.constructor === RegExp) return value.toString();
                return value;
            });
            
            // Того же эффекта можно добиться иначе:
            RegExp.prototype.toJSON = function() {
                return this.toString();
            }