Синтаксис шаблонов
==================

В шаблонах могут использоваться и выражения

.. code-block:: js

    <div>
        1 + 2 = {{ 1 + 2 }}
    </div>


.. code-block:: js

    <pre>form = {{user}}</pre>

    <div ng-controller="ngAppDemoController">
        I can add: {{a}} + {{b}} =  {{ a+b }}
    </div>

    <body ng-app="">
        <script type="text/ng-template" id="/tpl.html">
            Content of the template.
        </script>
        <a ng-click="currentTpl='/tpl.html'" id="tpl-link">Load inlined template</a>
        <div id="tpl-content" ng-include src="currentTpl"></div>
    </body>