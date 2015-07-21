Фильтры
=======

Фильтры это вспомогательные функции


.. js:attribute:: date

    Форматирует дату по укзанному шаблону

    .. code-block: js

        {{ today | date:'dd/MM/yyyy' }}
        // 23.05.1970



.. js:attribute:: curency

    Форматирует строку двумя знаками после запятой и символом доллар

    .. code-block: js

        {{ 234 | curency}}
        // $234.00


.. js:attribute:: filter

    Фильтрует массив

    .. code-block:: js

        Search: <input ng-model="query">
        // промежуточное сохранение выборки
        <li ng-repeat="friend in data = (friends | filter:query)"></li>

        <li ng-repeat="friend in friends | filter:query"></li>
        <li ng-repeat="friend in friends | filter:{query:name, status:true}"></li>        
        <li ng-repeat="friend in friends | filter:{$:name, status:true}"></li>

        // функция сортировки
        <li ng-repeat="friend in friends | filter:functionFromScope"></li>

        function functionFromScope(item){}


.. js:attribute:: json

    Форматирует объект, в удобно читаемый вид

    .. code-block: js

        {{ {'key': 'value'} | json }}


.. js:attribute:: limitTo

    Ограничивает стрку указанным размером

    .. code-block: js

        {{ 'VeryLongString' | limitTo:10 }}


.. js:attribute:: lowercase

    Приводит строку к нижнему регистру

    .. code-block: js

        {{ 'VeryLongString' | lowercase }}
        // verylongstring


.. js:attribute:: number

    Форматирует число

    .. code-block: js

        {{ 12345.1 | number }}
        // 1,2345.100


.. js:attribute:: orderby

    Сортирует массив    

    .. code-block: js

        <li ng-repeat="friend in friends | orderBy:predicate:reverse"></li>
        <li ng-repeat="friend in friends | orderBy:sortField"></li>
        <li ng-repeat="friend in friends | orderBy:!sortField"></li>
        <li ng-repeat="friend in friends | orderBy:!sortField"></li>


.. js:attribute:: upercase

    Приводит строку к верхнему регистру

    .. code-block: js

        {{ 'VeryLongString' | upercase }}
        // VERYLONGSTRING



