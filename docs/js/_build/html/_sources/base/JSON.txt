JSON
====

.. js:class:: JSON()


    .. js:function:: parse(text[, reviver])

        Из строки в JSON


    .. js:function:: stringify(obj[, filter[, indent]])

        Се­риа­ли­зу­ет объ­ект, мас­сив или эле­мен­тар­ное зна­че­ние

        .. code-block:: js

            // Про­стая се­риа­ли­за­ция
            var text = JSON.stringify(data);
            
            // Ука­зать точ­но, ка­кие по­ля под­ле­жат се­риа­ли­за­ции
            var text = JSON.stringify(address, ["city","state","country"]);

            // Ука­зать функ­цию за­ме­ны, что­бы мож­но бы­ло се­риа­ли­зо­вать объ­ек­ты RegExp
            var text = JSON.stringify(patterns, function(key, value) {
                if (value.constructor === RegExp) return value.toString();
                return value;
            });
            
            // То­го же эф­фек­та мож­но до­бить­ся ина­че:
            RegExp.prototype.toJSON = function() { return this.toString(); }