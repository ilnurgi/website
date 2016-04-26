route
=====

.. code-block:: js

    angular
    .module('app', ['ngRoute'])
    .config(function($routeProvider){
        $routeProvider
        .when('/', {
            temlate: 'html code',
            controller: 'myCtrl'
            // templateUrl: 'home.html'
        })
        .when('/posts/:postId', {
            temlate: 'html code',
            controller: 'myCtrl',
            controllerAs: 'vm'
            // templateUrl: 'home.html'
        })
        .otherwise({
            template: '404'
        })
    })
    .run(function($rootScope){
        // routeChangeStart, routeChangeSuccess
        $rootScope.$on('$routeChangeStart', function(event, current, previous, reject){
            ...
        })
    });

.. code-block:: html

    <ng-view></ng-view>

    