http
====

.. code-block:: js

    $http({method: $scope.method, url: $scope.url, cache: $templateCache}).
        success(function(data, status) {
            $scope.status = status;
            $scope.data = data;
        }).
        error(function(data, status) {
            $scope.data = data || "Request failed";
            $scope.status = status;
    });