Фабрики
=======


.. code-block:: js

    
    angular
    .module('app', [])
    .factory(
        'some_factory',
        function(){
            return {
                some_var: 'some_var_description'
            }
        }); 