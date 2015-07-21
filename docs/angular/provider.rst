provider
========

.. code-block:: js

    customInterpolationApp.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('//');
        $interpolateProvider.endSymbol('//');
        // в хтмл можно писать //переменная//
    });