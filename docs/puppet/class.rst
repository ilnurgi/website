class - классы
==============


.. code-block:: puppet

    class helloworld {
        notify {
            'hello, world!':}
    }


.. code-block:: puppet
    
    class hello($name) {
        notify {
            'hello, $name!':}
    }

    class { 'hello': name => 'ilnurgi'}


.. code-block:: puppet
    
    # вызов класса
    class {'helloworld':}


.. code-block:: puppet
    
    # наследованеи классов
    class unix {
        file { 
            '/etc/passwd':
                owner => 'root',
                group => 'root',
                mode  => '0644',
        }
        
        file { 
            '/etc/shadow':
                owner => 'root',
                group => 'root',
                mode  => '0440',
        }
    }

    class freebsd inherits unix {
        File['/etc/passwd', '/etc/shadow'] { 
            group => 'wheel', owner => undef 
        }
    }
