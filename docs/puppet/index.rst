Конспекты по puppet
===================

.. toctree::
   :maxdepth: 2

   modules
   class   
   resources/index


Встроенные переменные
---------------------

* `$operatingsystem` — операционная система.

* `$fqdn` — полное доменное имя.

* `$hostname` — имя хоста.

* `$ipaddress` — IP адрес.

* `$osfamily` — семейство операционных систем.

* `$is_virtual` — запущена ли ОС в виртуальной машине.

Встроенные переменные становятся доступными благодаря утилите facter, устанавливаемой вместе с puppet, которая берёт информацию из системы. 


.. code-block:: puppet

   # просмотр всех переменных окружения клиента
   file { 
      '/tmp/facts.yaml':
         content => inline_template('<%= scope.to_hash.reject { |k,v| !( k.is_a?(String) && v.is_a?(String) ) }.to_yaml %>'),
   }

Операторы
---------

.. code-block:: puppet

   if condition {
      ...
   } elsif condition {
      ...
   } else {
      ...
   }


.. code-block:: puppet

   case $operatingsystem {
         centos, redhat: { $apache = "httpd" }
         debian, ubuntu: { $apache = "apache2" }
         default: { fail("Unrecognized operating system for webserver") }
   }


.. code-block:: puppet

   $apache = $operatingsystem ? {
      centos                => 'httpd',
      redhat                => 'httpd',
      /(?i)(ubuntu|debian)/ => "apache2",
      default               => undef,
   }
