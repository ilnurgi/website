os
==

.. code-block:: js

    const os = require('os');


cpus
----

.. js:function:: cpus()

    Возвращает массив с данными о количестве ядер системы

    .. code-block:: js

        os.cpus()
        /*
            [
                {
                    model: 'Intel(R) Core(TM) i3-4000M CPU @ 2.40GHz',
                    speed: 2394,
                    times: {
                        user: 35267224,
                        nice: 0,
                        sys: 18222024,
                        idle: 212249843,
                        irq: 948423
                    }
                },
                ...
            ]
        */