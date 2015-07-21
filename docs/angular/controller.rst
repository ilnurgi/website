ng-controller - контроллеры
===========================


.. code-block:: js

    function Controller($scope){
        // определение конеткста контроллера
    }

    // или

    angular.module('moduleName', []).
        controller('controllerName', function($scope){
            ...
        }
    )

    <div id="ctrl-as-exmpl" ng-controller="SettingsController1 as settings">