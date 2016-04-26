моки
====

.. code-block:: js

    angular
    .module('app', ['ngMockE2E'])
    .run(function($httpBackebd){
        $httpBackend.whenGET('url').respond(200, books)
        $httpBackend.whenPOST('url').respond(function(method, url, data){
            var result = {};
            return [200, result]
        })
    })