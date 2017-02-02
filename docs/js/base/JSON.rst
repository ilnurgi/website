JSON
====

.. py:class:: JSON()


    .. py:function:: parse(text[, reviver])

        Из строки в JSON


    .. py:function:: stringify(obj[, filter[, indent]])

        Сериализует объект, массив или элементарное значение

        .. code-block:: js

            // Простая сериализация
            var text = JSON.stringify(data);
            
            // Указать точно, какие поля подлежат сериализации
            var text = JSON.stringify(address, ["city","state","country"]);

            // Указать функцию замены, чтобы можно было сериализовать объекты RegExp
            var text = JSON.stringify(patterns, function(key, value) {
                if (value.constructor === RegExp) return value.toString();
                return value;
            });
            
            // Того же эффекта можно добиться иначе:
            RegExp.prototype.toJSON = function() { return this.toString(); }