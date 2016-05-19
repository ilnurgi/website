Мои конспекты по AngularJS
==========================

.. toctree::
    :maxdepth: 1

    methods
    directive
    services
    filters
    methods_module
    helpers

.. toctree::
    :maxdepth: 2

    modules/index


.. code-block:: html

    <div>
        1 + 2 = {{ 1 + 2 }}
    </div>


.. code-block:: html

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


