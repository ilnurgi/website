Стандартные фильтры
===================


currency
--------

Форматирует число в денежном формате

.. code-block:: html

    <span>{{ expression | currence[:symbol] }}</span>

.. code-block:: js

    $filter('currency')(amount[, symbol])

.. code-block:: html

    <span>{{amount | currency}}</span>
    <span>{{amount | currency:"USD$"}}</span>


date
----

Форматирует дату по укзанному шаблону

* 'yyyy' - 4 цифры для вывода года (например, 1 => 0001, 2010 => 2010)

* 'yy' - 2 последние цифры года (00-99). (пример, 2001 => 01, 2010 => 10)

* 'y' - 1 число для вывода года (например, 1 => 1, 199 => 199)

* 'MMMM' - месяц в длинном формате (January-December)

* 'MMM' - месяц в трехбуквенном формате (Jan-Dec)

* 'MM' - месяц цифрами, с ведущим нулем (01-12)

* 'M' - месяц цифрами, без ведущего нуля (1-12)

* 'dd' - день в месяце, с ведущим нулем (01-31)

* 'd' - день в месяце, без ведущего нуля (1-31)

* 'EEEE' - День недели в длинном формате,(Sunday-Saturday)

* 'EEE' - День недели в коротком формате, (Sun-Sat)

* 'HH' - Час, с ведущим нулем (00-23)

* 'H' - Час без ведущего нуля (0-23)

* 'hh' - Час, с ведущим нулем в 12-ти часовом формате (01-12)

* 'h' - Час без ведущего нуля в 12-ти часовом формате (1-12)

* 'mm' - Минуты с ведущим нулем (00-59)

* 'm' - Минуты без ведущего нуля(0-59)

* 'ss' - Секунды с ведущим нулем (00-59)

* 's' - Секунды без ведущего нуля (0-59)

* 'a' - Указатель am/pm для 12-ти часового формата.

* 'Z' - 4 цифры (плюс знак), представляющие сдвиг временной зоны (часовой пояс) (-1200-
+1200)


* 'medium' - эквивалент 'MMM d, y h:mm:ss a' для локализации en_US (пример, Sep 3, 2010
12:05:08 pm)

* 'short' - эквивалент 'M/d/yy h:mm a' для локализации en_US (пример, 9/3/10 12:05 pm)

* 'fullDate' - эквивалент 'EEEE, MMMM d,y' для локализации en_US (пример, Friday,
September 3, 2010)

* 'longDate' - эквивалент 'MMMM d, y' для локализации en_US (пример, September 3, 2010)

* 'mediumDate' - эквивалент 'MMM d, y' для локализации en_US (пример, Sep 3, 2010)

* 'shortDate' - эквивалент 'M/d/yy' для локализации en_US (пример, 9/3/10)

* 'mediumTime' - эквивалент 'h:mm:ss a' для локализации en_US (пример, 12:05:08 pm)

* 'shortTime' - эквивалент 'h:mm a' для локализации en_US (пример 12:05 pm)

.. code-block:: html

    <span>{{ date_expression | date[:format] }}</span>

.. code-block:: js

    $filter('date')(date[, format])

.. code-block:: html

    <span>{{1288323623006 | date:'medium'}}</span>
    <span>{{1288323623006 | date:'yyyy-MM-dd HH:mm:ss Z'}}</span>
    <span>{{1288323623006 | date:'MM/dd/yyyy @ h:mma'}}</span>


filter
------

Фильтрует массив

.. code-block:: html

    <span>{{ filter_expression | filter:expression }}</span>

.. code-block:: js

    $filter('filter')(array, expression)

.. code-block:: html

    <script type="text/javascript">
        function functionFromScope(item){}
    </script>

    Search: <input ng-model="query">

    <!-- промежуточное сохранение выборки -->
    <li ng-repeat="friend in data = (friends | filter:query)"></li>

    <li ng-repeat="friend in friends | filter:query"></li>
    <li ng-repeat="friend in friends | filter:{query:name, status:true}"></li>
    <li ng-repeat="friend in friends | filter:{$:name, status:true}"></li>

    // функция сортировки
    <li ng-repeat="friend in friends | filter:functionFromScope"></li>


json
----

Форматирует объект, в удобно читаемый вид

.. code-block:: html

    <span>{{ json_expression | json }}</span>

.. code-block:: js

    $filter('json')(object)

.. code-block:: js

    {{ {'key': 'value'} | json }}


limitTo
-------

Ограничивает строку указанным размером

.. code-block:: html

    <span>{{ limit_expression | limitTo:limit }}</span>

.. code-block:: js

    $filter('limitTo')(expression[, limit])

.. code-block:: js

    {{ 'VeryLongString' | limitTo:10 }}


lowercase
---------

Приводит строку к нижнему регистру

.. code-block:: html

    <span>{{ lowercase_expression | lowercase }}</span>

.. code-block:: js

    $filter('lowercase')(lowercase_expression)

.. code-block:: html

    <span>{{ 'VeryLongString' | lowercase }}</span>


number
------

Форматирует число

.. code-block:: html

    <span>{{ number_expression | number[:fractionSize] }}</span>

.. code-block:: js

    $filter('number')(number[, fractionSize])

.. code-block:: html

    <span>{{ 12345.1 | number }}</span>


orderby
-------

Сортирует массив

.. code-block:: html

    <span>{{ orderby_expression | orderby:expression[:reverse]] }}</span>

.. code-block:: js

    $filter('orderby')(orderby_expression, expression[, reverse])

.. code-block:: html

    <li ng-repeat="friend in friends | orderBy:predicate:reverse"></li>
    <li ng-repeat="friend in friends | orderBy:sortField"></li>
    <li ng-repeat="friend in friends | orderBy:!sortField"></li>
    <li ng-repeat="friend in friends | orderBy:!sortField"></li>


uppercase
---------

Приводит строку к верхнему регистру

.. code-block:: html

    <span>{{ uppercase_expression | uppercase }}</span>

.. code-block:: js

    $filter('uppercase')(uppercase_expression)

.. code-block:: html

    <span>{{ 'VeryLongString' | upercase }}</span>