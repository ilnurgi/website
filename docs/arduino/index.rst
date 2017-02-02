Мои конспекты по Arduino
========================

.. code-block:: c

    int ledPin = 13;

    void setup(){
        pinMode(ledPin, OUTPUT);
    }

    void loop(){
        digitalWrite(ledPin, HIGHT);
        delay(1000);
        digitalWrite(ledPin, LOW);
        delay(1000);
    }


bh1750 - датчик освещенности

.. toctree::
    :maxdepth: 1

