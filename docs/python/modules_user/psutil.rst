.. py:module:: psutil

=======================================
psutil - получение системной информации
=======================================

Версия `psutil <http://pythonhosted.org/psutil/>`_ на момент написания была 3.2.2

Введение
========

psutil (python system and process utilities) - является кросс-платформенной библиотекой
для получения информации о запущенных процессах и
использования системы (процессор, память, диски, сеть) в Python.

Модуль реализует многие команды командной строки, такие как:
ps, top, lsof, netstat, ifconfig, who, df, kill, free, nice, ionice, iostat,
iotop, uptime, pidof, tty, taskset, pmap.

Поддерживает Linux, Windows, OSX, FreeBSD и Sun Solaris,
как 32-битные, так и 64-битные архитектуры,
с версиями Python от 2.6 до 3.4
(пользователи Python 2.4 и 2.5 могут использовать 2.1.3 версию модуля).

Также поддерживается PyPy.

Системная информация
====================

Процессор, CPU
--------------

.. py:method:: cpu_times(percpu=False)
    
    Возвращает именованный кортеж из CPU times. Каждый атрибут кортежа представляет собой время потраченное процессором в данном режиме. Ключи кортежа зависит от операционной системы компьютeра:

    * user
    * system
    * idle
    * nice (UNIX)
    * iowait (Linux)
    * irq (Linux, FreeBSD)
    * softirq (Linux)
    * steal (Linux 2.6.11+)
    * guest (Linux 2.6.24+)
    * guest_nice (Linux 3.2.0+)

    Если `percpu=True` то вернет список именнованных кортежей для каждого логического CPU системы. 

        >>> psutil.cpu_times()
        scputimes(user=17411.7, nice=77.99, system=3797.02, idle=51266.57, iowait=732.58, irq=0.01, softirq=142.43, steal=0.0, guest=0.0, guest_nice=0.0)
        >>> psutil.cpu_times(True)
        [scputimes(user=28786.64, nice=267.74, system=11344.25, idle=651167.6, iowait=2431.1, irq=0.23, softirq=232.56, steal=0.0, guest=0.0, guest_nice=0.0),
          scputimes(user=28782.91, nice=267.89, system=11301.36, idle=650911.02, iowait=3170.37, irq=0.06, softirq=115.83, steal=0.0, guest=0.0, guest_nice=0.0),
          scputimes(user=21859.61, nice=261.58, system=7614.26, idle=662835.49, iowait=3485.7, irq=0.0, softirq=39.64, steal=0.0, guest=0.0, guest_nice=0.0),
          scputimes(user=22585.24, nice=259.34, system=7948.79, idle=657654.77, iowait=7588.63, irq=0.0, softirq=43.38, steal=0.0, guest=0.0, guest_nice=0.0)]


.. py:method:: cpu_percent(interval=None, percpu=False)
    
    Возвращает число с точкой, представляющий общее использование процессора. 

    * `interval` - если больше 0.0, то возвращает загрузку именно за указанный интервал, иначе за промежуток с импорта модуля или последнего вызова метода
    * `percpu` - если True, вернет список из данных для кажлого CPU

        >>> # тут будет блокировка потока
        >>> psutil.cpu_percent(interval=1)
        2.0
        >>> # блокировки нет, цифра с момента последнего вызова
        >>> psutil.cpu_percent(interval=None)
        2.9
        >>> # блокировка потока
        >>> psutil.cpu_percent(interval=1, percpu=True)
        [2.0, 1.0]

    .. warning:: 

        Первый вызов функции будет вызван с параметром `interval=0.0` или `interval=None` и вернет значение 0.0, которое нужно проигнорировать


.. py:method:: cpu_times_percent(interval=None, percpu=False)
    
    Аналог :py:meth:`cpu_percent`, но предоставляет информацию для каждого CPU в виде именованных кортедей как и :py:meth:`cpu_times(percpu=True)`

    >>> psutil.cpu_times_percent(interval=1, percpu=True)
    [scputimes(user=6.1, nice=0.0, system=2.0, idle=91.9, iowait=0.0, irq=0.0, softirq=0.0, steal=0.0, guest=0.0, guest_nice=0.0),
      scputimes(user=6.1, nice=0.0, system=2.0, idle=91.8, iowait=0.0, irq=0.0, softirq=0.0, steal=0.0, guest=0.0, guest_nice=0.0),
      scputimes(user=13.0, nice=0.0, system=3.0, idle=84.0, iowait=0.0, irq=0.0, softirq=0.0, steal=0.0, guest=0.0, guest_nice=0.0),
      scputimes(user=6.0, nice=0.0, system=3.0, idle=81.0, iowait=10.0, irq=0.0, softirq=0.0, steal=0.0, guest=0.0, guest_nice=0.0)]

    .. warning:: 

        Первый вызов функции будет вызван с параметром `interval=0.0` или `interval=None` и вернет значение 0.0, которое нужно проигнорировать


.. py:method:: cpu_count(logical=True)
        
    Возвращает количество логических/физических процессоров в системе.

    >>> psutil.cpu_count()
    4
    >>> psutil.cpu_count(logical=False)
    2


Память, Memory
--------------

.. py:method:: virtual_memory()

    Возвращает именованный кортеж, статистика об использовании системной памяти.
    
    * `total` - общее количество физической памяти
    * `available` - доступная память для процессов
    * `percent` - процент использования памяти, (total - available) / total * 100.
    * `used` - используемая память
    * `free` - свободная память
    * `active` - (UNIX), используемая память
    * `inactive` - (UNIX), неиспользуемая память
    * `buffers` - (Linux, BSD), кеш, метаданные файловой системы
    * `cached` - (Linux, BSD): кеш для различных вещей
    * `wired` - (BSD, OSX): память, не перемещаемая на диск
    * `shared` - (BSD): память доступная одновременно для нескольких процессов

    Сумма доступной и используемой может быть не равна общей памяти, в зависимости от платформы.

    >>> mem = psutil.virtual_memory()
    >>> mem
    svmem(total=8374149120L, available=1247768576L, percent=85.1, used=8246628352L, free=127520768L, active=3208777728, inactive=1133408256, buffers=342413312L, cached=777834496)
    >>>
    >>> THRESHOLD = 100 * 1024 * 1024  # 100MB
    >>> if mem.available <= THRESHOLD:
    ...     print("warning")
    ...
    >>>


.. py:method:: swap_memory()

    Возвращает именованный кортеж, статиска по файлу подкачки системы

    * `total` - общий размер файла подкачки
    * `used` - используемый размер файла подкачки
    * `free` - свободный размер
    * `percent` - процент заполнения, (total - available) / total * 100
    * `sin` - количество байт записанных на диск
    * `sout` - количество байт, считанных с диска
    
    sin и sout на Windows бессмысленны и всегда вернут 0

    >>> psutil.swap_memory()
    sswap(total=2097147904L, used=886620160L, free=1210527744L, percent=42.3, sin=1050411008, sout=1906720768)


Диски, Disks
------------

.. py:method:: disk_partitions(all=False)
    
    Возвращает список именованных кортежей, информация по смонтированным разделам диска - устройство, точку монтирования, тип. 

    * `all` - информация только по физическим дискам

    `fstype` - зависит от платформы: linux - 'ext3', 'iso9660', windows - "removable", "fixed", "remote", "cdrom", "unmounted" or "ramdisk", OSX и FreeBSD - getfsstat(2)

    >>> psutil.disk_partitions()
    [sdiskpart(device='/dev/sda3', mountpoint='/', fstype='ext4', opts='rw,errors=remount-ro'),
     sdiskpart(device='/dev/sda7', mountpoint='/home', fstype='ext4', opts='rw')]


.. py:method:: disk_usage(path)

    Возвращает именованный кортеж, информация по использованию диска

    >>> psutil.disk_usage('/')
    sdiskusage(total=21378641920, used=4809781248, free=15482871808, percent=22.5)


.. py:method:: disk_io_counters(perdisk=False)
    
    Возвращает именованный котреж, статистика по вводу/выводу раздела

    Если `perdisk=True`, то вернет список для всех физических устройств

    * read_count - количество чтении
    * write_count - количество записей
    * read_bytes - количество прочитанных байт
    * write_bytes - количество записанных байт
    * read_time - время чтения с диска, миллисекунды
    * write_time - время записи на диск, миллисекунды

    >>> psutil.disk_io_counters()
    sdiskio(read_count=8141, write_count=2431, read_bytes=290203, write_bytes=537676, read_time=5868, write_time=94922)
    >>> psutil.disk_io_counters(perdisk=True)
    {'sda1': sdiskio(read_count=920, write_count=1, read_bytes=2933248, write_bytes=512, read_time=6016, write_time=4),
      'sda2': sdiskio(read_count=18707, write_count=8830, read_bytes=6060, write_bytes=3443, read_time=24585, write_time=1572),
      'sdb1': sdiskio(read_count=161, write_count=0, read_bytes=786432, write_bytes=0, read_time=44, write_time=0)}


Сеть, Network
-------------

.. py:method:: net_io_counters(pernic=False)    

    Возвращает именованный кортеж, статистика по вводу/выводу сети

    * `bytes_sent` - количество отправленных байтов
    * `bytes_recv` - количество принятых байтов
    * `packets_sent` - количество отправленных байтов
    * `packets_recv` - количество принятых байтов
    * `errin` - количество ошибок при приемке
    * `errout` - количество ошибок при отправке
    * `dropin` - количесвто пришедших пакетов, которые были отброшены
    * `dropout` - количество отправленных пакетов, которые были отброшены (0 на OSX и BSD)

    Если `pernic=True` вернет словарь, по всем интерфейсам системы

    >>> psutil.net_io_counters()
    snetio(bytes_sent=14508483, bytes_recv=62749361, packets_sent=84311, packets_recv=94888, errin=0, errout=0, dropin=0, dropout=0)
    >>> psutil.net_io_counters(pernic=True)
    {'lo': snetio(bytes_sent=547971, bytes_recv=547971, packets_sent=5075, packets_recv=5075, errin=0, errout=0, dropin=0, dropout=0),
     'wlan0': snetio(bytes_sent=13921765, bytes_recv=62162574, packets_sent=79097, packets_recv=89648, errin=0, errout=0, dropin=0, dropout=0)}


.. py:method:: net_connections(kind='inet')
    
    Возвращает список именновых кортежей, статистику по сокетным соединениям.

    * `fd` - десриптор сокета
    * `family` - адрес родителя AF_INET, AF_INET6 или AF_UNIX.
    * `type` - тип адреса SOCK_STREAM или SOCK_DGRAM.
    * `laddr` - локальный адрес
    * `raddr` - удаленный адрес
    * `status` - статус TCP соединения. Возвращает одно из значений psutil.CONN_*. Для UDP и UNIX сокета возвращает psutil.CONN_NONE.
    * `pid` - пид процесса, который открыл сокет. 

    ==========  =================
    Kind value    Connections using
    ==========  =================
    “inet”      IPv4 and IPv6
    “inet4”     IPv4
    “inet6”     IPv6
    “tcp”       TCP
    “tcp4”      TCP over IPv4
    “tcp6”      TCP over IPv6
    “udp”       UDP
    “udp4”      UDP over IPv4
    “udp6”      UDP over IPv6
    “unix”      UNIX socket (both UDP and TCP protocols)
    “all”       the sum of all the possible families and protocols
    ==========  =================

    >>> psutil.net_connections()
    [pconn(fd=115, family=<AddressFamily.AF_INET: 2>, type=<SocketType.SOCK_STREAM: 1>, laddr=('10.0.0.1', 48776), raddr=('93.186.135.91', 80), status='ESTABLISHED', pid=1254),
     pconn(fd=117, family=<AddressFamily.AF_INET: 2>, type=<SocketType.SOCK_STREAM: 1>, laddr=('10.0.0.1', 43761), raddr=('72.14.234.100', 80), status='CLOSING', pid=2987),
     pconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=<SocketType.SOCK_STREAM: 1>, laddr=('10.0.0.1', 60759), raddr=('72.14.234.104', 80), status='ESTABLISHED', pid=None),
     pconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=<SocketType.SOCK_STREAM: 1>, laddr=('10.0.0.1', 51314), raddr=('72.14.234.83', 443), status='SYN_SENT', pid=None)
     ...]

    .. note::

        (OSX) psutil.AccessDenied is always raised unless running as root (lsof does the same).

    .. note::

        (Solaris) UNIX sockets are not supported.


.. py:method:: net_if_addrs()
    
    Возвращает словарь, где ключ - сетевой интерфес, а значение список именованных кортежей, информацию по NIC (network interface card).

    * `family`
    * `address`
    * `netmask`
    * `broadcast`
    * `ptp`

    >>> psutil.net_if_addrs()
    {'lo': [snic(family=<AddressFamily.AF_INET: 2>, address='127.0.0.1', netmask='255.0.0.0', broadcast='127.0.0.1', ptp=None),
            snic(family=<AddressFamily.AF_INET6: 10>, address='::1', netmask='ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff', broadcast=None, ptp=None),
            snic(family=<AddressFamily.AF_LINK: 17>, address='00:00:00:00:00:00', netmask=None, broadcast='00:00:00:00:00:00', ptp=None)],
     'wlan0': [snic(family=<AddressFamily.AF_INET: 2>, address='192.168.1.3', netmask='255.255.255.0', broadcast='192.168.1.255', ptp=None),
               snic(family=<AddressFamily.AF_INET6: 10>, address='fe80::c685:8ff:fe45:641%wlan0', netmask='ffff:ffff:ffff:ffff::', broadcast=None, ptp=None),
               snic(family=<AddressFamily.AF_LINK: 17>, address='c4:85:08:45:06:41', netmask=None, broadcast='ff:ff:ff:ff:ff:ff', ptp=None)]}


.. py:method:: psutil.net_if_stats()
    
    Возвращает словарь, ключ - интерфейс, значение - именованный кортеж, информация об интерфейсе

    * `isup` - интерфейс поднят
    * `duplex` - NIC_DUPLEX_FULL, NIC_DUPLEX_HALF or NIC_DUPLEX_UNKNOWN
    * `speed` - скорость инетерфейса в MB
    * `mtu`

    >>> psutil.net_if_stats()
    {'eth0': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=100, mtu=1500),
     'lo': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>, speed=0, mtu=65536)}


Другая информация
-----------------

.. py:method:: psutil.users()
    
    Возвращает список именованных кортежей, информация о подключенных пользователях

    * `user` - имя пользователя
    * `terminal` - tty или pseudo-tty терминал к которому подключен пользователь
    * `host` - имя хоста с которого подключен пользователь
    * `started` - дата подключения

    >>> psutil.users()
    [suser(name='giampaolo', terminal='pts/2', host='localhost', started=1340737536.0),
     suser(name='giampaolo', terminal='pts/3', host='localhost', started=1340737792.0)]


.. py:method:: boot_time()
    
    Возвращает таймстамп, время закгрузки системы

    >>> psutil.boot_time()
    1389563460.0


Процессы
========

Методы
------

.. py:method:: pids()
    
    Возвращает список PID запущенных процессов. 

    Для итерации по списку процессов лучше использовать :py:meth:`process_iter()`

    Для проверки запущенности процесса по PID лучше использовать :py:meth:`pid_exists(`


.. py:method:: pid_exists(pid)
    
    Проверяет, что указанный PID процесса запущен. 


.. py:method:: process_iter()
    
    Возвращает итератор, возвращающий :py:class:`Process`, запущенных процессов в системе. Каждый экземпляр будет создан только 1 раз и будет храниться в кеше. 

    .. code-block:: py
        
        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['pid', 'name'])
            except psutil.NoSuchProcess:
                pass
            else:
                print(pinfo)


.. py:method:: wait_procs(procs, timeout=None, callback=None)    
    
    Convenience function which waits for a list of Process instances to terminate. Return a (gone, alive) tuple indicating which processes are gone and which ones are still alive. The gone ones will have a new returncode attribute indicating process exit status (it may be None). callback is a function which gets called every time a process terminates (a Process instance is passed as callback argument). Function will return as soon as all processes terminate or when timeout occurs. Tipical use case is:

    * send SIGTERM to a list of processes
    * give them some time to terminate
    * send SIGKILL to those ones which are still alive

    .. code-block:: py
        
        def on_terminate(proc):
            print("process {} terminated with exit code {}".format(proc, proc.returncode))

        procs = [...]  # a list of Process instances
        for p in procs:
            p.terminate()
        gone, alive = wait_procs(procs, timeout=3, callback=on_terminate)
        for p in alive:
            p.kill()


Исключения
----------

.. py:class:: Error()
    
    Базовый класс для всех исключений модуля


.. py:class:: NoSuchProcess(pid, name=None, msg=None)
    
    Процесс не найден


.. py:class:: ZombieProcess(pid, name=None, ppid=None, msg=None)    
    
    Зомби процесс.

    Наследник :py:class:`NoSuchProcess`
    

.. py:class:: AccessDenied(pid=None, name=None, msg=None)    
    
    Не хватает прав для доступа к объекту
    

.. py:class:: TimeoutExpired(seconds, pid=None, name=None, msg=None)    
    
    Вышло время ожидания


Process
-------

.. py:class:: Process(pid=None)
    
    Процесс системы. 

    Возбуждает :py:class:`NoSuchProcess` если PID не найден.
    
    Возбуждает :py:class:`AccessDenied` в методах, если не будет хватать прав.

    .. warning::

        the way this class is bound to a process is uniquely via its PID. That means that if the Process instance is old enough and the PID has been reused by another process in the meantime you might end up interacting with another process. The only exceptions for which process identity is pre-emptively checked (via PID + creation time) and guaranteed are for nice() (set), ionice() (set), cpu_affinity() (set), rlimit() (set), children(), parent(), suspend() resume(), send_signal(), terminate(), and kill() methods. To prevent this problem for all other methods you can use is_running() before querying the process or use process_iter() in case you’re iterating over all processes.


    .. py:attribute:: pid
        
        PID процесса

    
    .. py:method:: ppid()
        
        Родительский PID процесса. На Windows результат будет закеширирован при первом вызове


    .. py:method:: name()
    
        Возвращает имя процесса. Результат будет закеширован при после первого вызова.


    .. py:method:: exe()
        
        Возвращает путь к исполняемому файлу, может быть пустой строкой. Результат будет закеширован при после первого вызова.


    .. py:method:: cmdline()
        
        Возвращает булево, команда вызвана в командной строке.


    .. py:method:: create_time()
    
        Возвращает таймстамп, время создания процесса. Результат будет закеширован при после первого вызова..

        >>> p = psutil.Process()
        >>> p.create_time()
        1307289803.47

    
    .. py:method:: as_dict(attrs=None, ad_value=None)
        
        Возвращает словарь, информацию о процессе. 

        * `attrs` - вернуть только указанные поля
        * `ad_value` - занчение по умолчанию, для ключей, которых могут вызвать ошибки :py:class:`AccessDenied` или :py:class:`ZombieProcess`
        
        >>> p = psutil.Process()
        >>> p.as_dict(attrs=['pid', 'name', 'username'])
        {'username': 'giampaolo', 'pid': 12366, 'name': 'python'}


    .. py:method:: parent()
        
        Возвращает :py:class:`Process`, родительский процесс для текущего процесса. 


    .. py:method:: status()
        
        Возвращает строку, статус процесса, psutil.STATUS_*


    .. py:method:: cwd()
        
        Возвращает строку, абсолютный путь рабочей директории процесса


    .. py:method:: username()
        
        Возвращает строку, имя пользователя обладаетля процесса.

    
    .. py:method:: uids()
        
        The real, effective and saved user ids of this process as a namedtuple. 

        Поддержка: UNIX


    .. py:method:: gids()
    
        The real, effective and saved group ids of this process as a namedtuple. 

        Поддержка: UNIX


    .. py:method:: terminal()
        
        Возвращает терминал, связанный с этим процессом

        Поддержка: UNIX


    .. py:method:: nice(value=None)
        
        Получить или установить приоритет процесса. В UNIX это число от -20 до 20. 

        >>> p = psutil.Process()
        >>> p.nice(10)  # set
        >>> p.nice()  # get
        10

        На Windows необходимо использовать константы psutil.*_PRIORITY_CLASS

        >>> p.nice(psutil.HIGH_PRIORITY_CLASS)


    .. py:method:: ionice(ioclass=None, value=None)    
        
        Получить или установить приоритет ввода/вывода для процесса. 

        * `ioclass` - Linux - psutil.IOPRIO_CLASS_*, windows - 2,1,0
        * `value` - linux - от 0 до 7, windows - не поддерживается

        >>> p = psutil.Process()
        >>> p.ionice(psutil.IOPRIO_CLASS_IDLE)  # set
        >>> p.ionice()  # get
        pionice(ioclass=<IOPriority.IOPRIO_CLASS_IDLE: 3>, value=0)

        Поддержка: Linux, Windows > Vista


    .. py:method:: rlimit(resource, limits=None)
        
        Get or set process resource limits (see man prlimit). resource is one of the psutil.RLIMIT_* constants. limits is a (soft, hard) tuple. This is the same as resource.getrlimit() and resource.setrlimit() but can be used for every process PID and only on Linux. Example:

        >>> p = psutil.Process()
        >>> # process may open no more than 128 file descriptors
        >>> p.rlimit(psutil.RLIMIT_NOFILE, (128, 128))
        >>> # process may create files no bigger than 1024 bytes
        >>> p.rlimit(psutil.RLIMIT_FSIZE, (1024, 1024))
        >>> # get
        >>> p.rlimit(psutil.RLIMIT_FSIZE)
        (1024, 1024)
        >>>
        
        Поддержка: Linux


    .. py:method:: io_counters()
        
        Return process I/O statistics as a namedtuple including the number of read and write operations performed by the process and the amount of bytes read and written. For Linux refer to /proc filesysem documentation. On BSD there’s apparently no way to retrieve bytes counters, hence -1 is returned for read_bytes and write_bytes fields. OSX is not supported.

        >>> p = psutil.Process()
        >>> p.io_counters()
        pio(read_count=454556, write_count=3456, read_bytes=110592, write_bytes=0)
        
        Поддержка: all platforms except OSX and Solaris


    .. py:method:: num_ctx_switches()    

        The number voluntary and involuntary context switches performed by this process.


    .. py:method:: num_fds()    

        The number of file descriptors used by this process.

        Availability: UNIX


    .. py:method:: num_handles()

        The number of handles used by this process.

        Availability: Windows


    .. py:method:: num_threads()    

        The number of threads currently used by this process.


    .. py:method:: threads()    

        Return threads opened by process as a list of namedtuples including thread id and thread CPU times (user/system).


    .. py:method:: cpu_times()    

        Return a tuple whose values are process CPU user and system times which means the amount of time expressed in seconds that a process has spent in user / system mode. This is similar to os.times() but can be used for every process PID.


    .. py:method:: cpu_percent(interval=None)    

        Return a float representing the process CPU utilization as a percentage. When interval is > 0.0 compares process times to system CPU times elapsed before and after the interval (blocking). When interval is 0.0 or None compares process times to system CPU times elapsed since last call, returning immediately. That means the first time this is called it will return a meaningless 0.0 value which you are supposed to ignore. In this case is recommended for accuracy that this function be called a second time with at least 0.1 seconds between calls. Example:

        >>> p = psutil.Process()
        >>> # blocking
        >>> p.cpu_percent(interval=1)
        2.0
        >>> # non-blocking (percentage since last call)
        >>> p.cpu_percent(interval=None)
        2.9
        >>>

        Note a percentage > 100 is legitimate as it can result from a process with multiple threads running on different CPU cores.
        Warning the first time this method is called with interval = 0.0 or None it will return a meaningless 0.0 value which you are supposed to ignore.
        cpu_affinity(cpus=None)    
        Get or set process current CPU affinity. CPU affinity consists in telling the OS to run a certain process on a limited set of CPUs only. The number of eligible CPUs can be obtained with list(range(psutil.cpu_count())). On set raises ValueError in case an invalid CPU number is specified.

        >>> psutil.cpu_count()
        4
        >>> p = psutil.Process()
        >>> p.cpu_affinity()  # get
        [0, 1, 2, 3]
        >>> p.cpu_affinity([0])  # set; from now on, process will run on CPU #0 only
        >>> p.cpu_affinity()
        [0]
        >>>
        >>> # reset affinity against all CPUs
        >>> all_cpus = list(range(psutil.cpu_count()))
        >>> p.cpu_affinity(all_cpus)


        Availability: Linux, Windows, BSD


    .. py:method:: memory_info()    

        Return a tuple representing RSS (Resident Set Size) and VMS (Virtual Memory Size) in bytes. On UNIX rss and vms are the same values shown by ps. On Windows rss and vms refer to “Mem Usage” and “VM Size” columns of taskmgr.exe. For more detailed memory stats use memory_info_ex().


    .. py:method:: memory_info_ex()    

        Return a namedtuple with variable fields depending on the platform representing extended memory information about the process. All numbers are expressed in bytes.

        ======= ======= === ======= =======
        Linux   OSX     BSD SunOS   Windows
        ======= ======= === ======= =======
        rss     rss     rss rss     num_page_faults
        vms     vms     vms vms     peak_wset
        shared  pfaults text        wset
        text    pageins data        peak_paged_pool
        lib             stack       paged_pool
        data                        peak_nonpaged_pool
        dirty                       nonpaged_pool
                                    pagefile
                                    peak_pagefile
                                    private
        ======= ======= === ======= =======

        Windows metrics are extracted from PROCESS_MEMORY_COUNTERS_EX structure. Example on Linux:

        >>> p = psutil.Process()
        >>> p.memory_info_ex()
        pextmem(rss=15491072, vms=84025344, shared=5206016, text=2555904, lib=0, data=9891840, dirty=0)


    .. py:method:: memory_percent()    

        Compare physical system memory to process resident memory (RSS) and calculate process memory utilization as a percentage.


    .. py:method:: memory_maps(grouped=True)    

        Return process’s mapped memory regions as a list of namedtuples whose fields are variable depending on the platform. As such, portable applications should rely on namedtuple’s path and rss fields only. This method is useful to obtain a detailed representation of process memory usage as explained here. If grouped is True the mapped regions with the same path are grouped together and the different memory fields are summed. If grouped is False every mapped region is shown as a single entity and the namedtuple will also include the mapped region’s address space (addr) and permission set (perms). See examples/pmap.py for an example application.

        >>> p = psutil.Process()
        >>> p.memory_maps()
        [pmmap_grouped(path='/lib/x8664-linux-gnu/libutil-2.15.so', rss=16384, anonymous=8192, swap=0),
         pmmap_grouped(path='/lib/x8664-linux-gnu/libc-2.15.so', rss=6384, anonymous=15, swap=0),
         pmmap_grouped(path='/lib/x8664-linux-gnu/libcrypto.so.0.1', rss=34124, anonymous=1245, swap=0),
         pmmap_grouped(path='[heap]', rss=54653, anonymous=8192, swap=0),
         pmmap_grouped(path='[stack]', rss=1542, anonymous=166, swap=0),
         ...]
        >>>


    .. py:method:: children(recursive=False)    

        Return the children of this process as a list of Process objects, pre-emptively checking whether PID has been reused. If recursive is True return all the parent descendants. Example assuming A == this process:

        A ─┐
           │
           ├─ B (child) ─┐
           │             └─ X (grandchild) ─┐
           │                                └─ Y (great grandchild)
           ├─ C (child)
           └─ D (child)

        >>> p.children()
        B, C, D
        >>> p.children(recursive=True)
        B, X, Y, C, D

        Note that in the example above if process X disappears process Y won’t be returned either as the reference to process A is lost.


    .. py:method:: open_files()    
        
        Return regular files opened by process as a list of namedtuples including the absolute file name and the file descriptor number (on Windows this is always -1). Example:

        >>> f = open('file.ext', 'w')
        >>> p = psutil.Process()
        >>> p.open_files()
        [popenfile(path='/home/giampaolo/svn/psutil/file.ext', fd=3)]

        Warning on Windows this is not fully reliable as due to some limitations of the Windows API the underlying implementation may hang when retrieving certain file handles. In order to work around that psutil on Windows Vista (and higher) spawns a thread and kills it if it’s not responding after 100ms. That implies that on Windows this method is not guaranteed to enumerate all regular file handles (see full discusion here).
        Warning on FreeBSD this method can return files with a ‘null’ path (see issue 595).
        Changed in version 3.1.0: no longer hangs on Windows.


    .. py:method:: connections(kind="inet")    
        
        Return socket connections opened by process as a list of namedtuples. To get system-wide connections use psutil.net_connections(). Every namedtuple provides 6 attributes:

        * `fd` - the socket file descriptor. This can be passed to socket.fromfd() to obtain a usable socket object. This is only available on UNIX; on Windows -1 is always returned.
        * `family` - the address family, either AF_INET, AF_INET6 or AF_UNIX.
        * `type` - the address type, either SOCK_STREAM or SOCK_DGRAM.
        * `laddr` - the local address as a (ip, port) tuple or a path in case of AF_UNIX sockets.
        * `raddr` - the remote address as a (ip, port) tuple or an absolute path in case of UNIX sockets. When the remote endpoint is not connected you’ll get an empty tuple (AF_INET) or None (AF_UNIX). On Linux AF_UNIX sockets will always have this set to None.
        * `status` - represents the status of a TCP connection. The return value is one of the psutil.CONN_* constants. For UDP and UNIX sockets this is always going to be psutil.CONN_NONE.
        
        The kind parameter is a string which filters for connections that fit the following criteria:

        =========== =================
        Kind value  Connections using
        =========== =================
        inet        IPv4 and IPv6
        inet4       IPv4
        inet6       IPv6
        tcp         TCP
        tcp4        TCP over IPv4
        tcp6        TCP over IPv6
        udp         UDP
        udp4        UDP over IPv4
        udp6        UDP over IPv6
        unix        UNIX socket (both UDP and TCP protocols)
        all         the sum of all the possible families and protocols
        =========== =================

        >>> p = psutil.Process(1694)
        >>> p.name()
        'firefox'
        >>> p.connections()
        [pconn(fd=115, family=<AddressFamily.AF_INET: 2>, type=<SocketType.SOCK_STREAM: 1>, laddr=('10.0.0.1', 48776), raddr=('93.186.135.91', 80), status='ESTABLISHED'),
         pconn(fd=117, family=<AddressFamily.AF_INET: 2>, type=<SocketType.SOCK_STREAM: 1>, laddr=('10.0.0.1', 43761), raddr=('72.14.234.100', 80), status='CLOSING'),
         pconn(fd=119, family=<AddressFamily.AF_INET: 2>, type=<SocketType.SOCK_STREAM: 1>, laddr=('10.0.0.1', 60759), raddr=('72.14.234.104', 80), status='ESTABLISHED'),
         pconn(fd=123, family=<AddressFamily.AF_INET: 2>, type=<SocketType.SOCK_STREAM: 1>, laddr=('10.0.0.1', 51314), raddr=('72.14.234.83', 443), status='SYN_SENT')]
    

    .. py:method:: is_running()    

        Return whether the current process is running in the current process list. This is reliable also in case the process is gone and its PID reused by another process, therefore it must be preferred over doing psutil.pid_exists(p.pid).

        Note this will return True also if the process is a zombie (p.status() == psutil.STATUS_ZOMBIE).


    .. py:method:: send_signal(signal)    
        
        Send a signal to process (see signal module constants) pre-emptively checking whether PID has been reused. On UNIX this is the same as os.kill(pid, sig). On Windows only SIGTERM, CTRL_C_EVENT and CTRL_BREAK_EVENT signals are supported and SIGTERM is treated as an alias for kill().
        
    
    .. py:method:: suspend()    

        Suspend process execution with SIGSTOP signal pre-emptively checking whether PID has been reused. On UNIX this is the same as os.kill(pid, signal.SIGSTOP). On Windows this is done by suspending all process threads execution.

    
    .. py:method:: resume()    

        Resume process execution with SIGCONT signal pre-emptively checking whether PID has been reused. On UNIX this is the same as os.kill(pid, signal.SIGCONT). On Windows this is done by resuming all process threads execution.

    
    .. py:method:: terminate()    

        Terminate the process with SIGTERM signal pre-emptively checking whether PID has been reused. On UNIX this is the same as os.kill(pid, signal.SIGTERM). On Windows this is an alias for kill().

    
    .. py:method:: kill()    

        Kill the current process by using SIGKILL signal pre-emptively checking whether PID has been reused. On UNIX this is the same as os.kill(pid, signal.SIGKILL). On Windows this is done by using TerminateProcess.

    
    .. py:method:: wait(timeout=None)    

        Wait for process termination and if the process is a children of the current one also return the exit code, else None. On Windows there’s no such limitation (exit code is always returned). If the process is already terminated immediately return None instead of raising NoSuchProcess. If timeout is specified and process is still alive raise TimeoutExpired exception. It can also be used in a non-blocking fashion by specifying timeout=0 in which case it will either return immediately or raise TimeoutExpired. To wait for multiple processes use psutil.wait_procs().


Popen
-----

.. py:class:: Popen(*args, **kwargs)    
    
    A more convenient interface to stdlib subprocess.Popen. It starts a sub process and deals with it exactly as when using subprocess.Popen but in addition it also provides all the methods of psutil.Process class in a single interface. For method names common to both classes such as send_signal(), terminate() and kill() psutil.Process implementation takes precedence. For a complete documentation refer to subprocess module documentation.

    Note Unlike subprocess.Popen this class pre-emptively checks wheter PID has been reused on send_signal(), terminate() and kill() so that you can’t accidentally terminate another process, fixing http://bugs.python.org/issue6973.

    >>> import psutil
    >>> from subprocess import PIPE
    >>>
    >>> p = psutil.Popen(["/usr/bin/python", "-c", "print('hello')"], stdout=PIPE)
    >>> p.name()
    'python'
    >>> p.username()
    'giampaolo'
    >>> p.communicate()
    ('hello\n', None)
    >>> p.wait(timeout=2)
    0
    >>>


Constants
---------

.. py:attribute:: psutil.STATUS_RUNNING
.. py:attribute:: psutil.STATUS_SLEEPING
.. py:attribute:: psutil.STATUS_DISK_SLEEP
.. py:attribute:: psutil.STATUS_STOPPED
.. py:attribute:: psutil.STATUS_TRACING_STOP
.. py:attribute:: psutil.STATUS_ZOMBIE
.. py:attribute:: psutil.STATUS_DEAD
.. py:attribute:: psutil.STATUS_WAKE_KILL
.. py:attribute:: psutil.STATUS_WAKING
.. py:attribute:: psutil.STATUS_IDLE
.. py:attribute:: psutil.STATUS_LOCKED


.. py:attribute:: psutil.STATUS_WAITING
    
    A set of strings representing the status of a process. Returned by psutil.Process.status().

.. py:attribute:: psutil.CONN_ESTABLISHED
.. py:attribute:: psutil.CONN_SYN_SENT
.. py:attribute:: psutil.CONN_SYN_RECV
.. py:attribute:: psutil.CONN_FIN_WAIT1
.. py:attribute:: psutil.CONN_FIN_WAIT2
.. py:attribute:: psutil.CONN_TIME_WAIT
.. py:attribute:: psutil.CONN_CLOSE
.. py:attribute:: psutil.CONN_CLOSE_WAIT
.. py:attribute:: psutil.CONN_LAST_ACK
.. py:attribute:: psutil.CONN_LISTEN
.. py:attribute:: psutil.CONN_CLOSING
.. py:attribute:: psutil.CONN_NONE
.. py:attribute:: psutil.CONN_DELETE_TCB(Windows)
.. py:attribute:: psutil.CONN_IDLE(Solaris)


.. py:attribute:: psutil.CONN_BOUND(Solaris)
    
    A set of strings representing the status of a TCP connection. Returned by psutil.Process.connections() (status field).

.. py:attribute:: psutil.ABOVE_NORMAL_PRIORITY_CLASS
.. py:attribute:: psutil.BELOW_NORMAL_PRIORITY_CLASS
.. py:attribute:: psutil.HIGH_PRIORITY_CLASS
.. py:attribute:: psutil.IDLE_PRIORITY_CLASS
.. py:attribute:: psutil.NORMAL_PRIORITY_CLASS


.. py:attribute:: psutil.REALTIME_PRIORITY_CLASS
    
    A set of integers representing the priority of a process on Windows (see MSDN documentation). They can be used in conjunction with psutil.Process.nice() to get or set process priority.

    Availability: Windows


.. py:attribute:: psutil.IOPRIO_CLASS_NONE
.. py:attribute:: psutil.IOPRIO_CLASS_RT
.. py:attribute:: psutil.IOPRIO_CLASS_BE


.. py:attribute:: psutil.IOPRIO_CLASS_IDLE
    
    A set of integers representing the I/O priority of a process on Linux. They can be used in conjunction with psutil.Process.ionice() to get or set process I/O priority. IOPRIO_CLASS_NONE and IOPRIO_CLASS_BE (best effort) is the default for any process that hasn’t set a specific I/O priority. IOPRIO_CLASS_RT (real time) means the process is given first access to the disk, regardless of what else is going on in the system. IOPRIO_CLASS_IDLE means the process will get I/O time when no-one else needs the disk. For further information refer to manuals of ionice command line utility or ioprio_get system call.

    Availability: Linux

    Changed in version 3.0.0: on Python >= 3.4 thse constants are enums instead of a plain integer.


.. py:attribute:: psutil.RLIMIT_INFINITY
.. py:attribute:: psutil.RLIMIT_AS
.. py:attribute:: psutil.RLIMIT_CORE
.. py:attribute:: psutil.RLIMIT_CPU
.. py:attribute:: psutil.RLIMIT_DATA
.. py:attribute:: psutil.RLIMIT_FSIZE
.. py:attribute:: psutil.RLIMIT_LOCKS
.. py:attribute:: psutil.RLIMIT_MEMLOCK
.. py:attribute:: psutil.RLIMIT_MSGQUEUE
.. py:attribute:: psutil.RLIMIT_NICE
.. py:attribute:: psutil.RLIMIT_NOFILE
.. py:attribute:: psutil.RLIMIT_NPROC
.. py:attribute:: psutil.RLIMIT_RSS
.. py:attribute:: psutil.RLIMIT_RTPRIO
.. py:attribute:: psutil.RLIMIT_RTTIME
.. py:attribute:: psutil.RLIMIT_RTPRIO
.. py:attribute:: psutil.RLIMIT_SIGPENDING


.. py:attribute:: psutil.RLIMIT_STACK
    
    Constants used for getting and setting process resource limits to be used in conjunction with psutil.Process.rlimit(). See man prlimit for futher information.

    Availability: Linux


.. py:attribute:: psutil.AF_LINK
    
    Constant which identifies a MAC address associated with a network interface. To be used in conjunction with psutil.net_if_addrs().

    New in 3.0.0


.. py:attribute:: psutil.NIC_DUPLEX_FULL
.. py:attribute:: psutil.NIC_DUPLEX_HALF


.. py:attribute:: psutil.NIC_DUPLEX_UNKNOWN
    
    Constants which identifies whether a NIC (network interface card) has full or half mode speed. NIC_DUPLEX_FULL means the NIC is able to send and receive data (files) simultaneously, NIC_DUPLEX_FULL means the NIC can either send or receive data at a time. To be used in conjunction with psutil.net_if_stats().

    New in 3.0.0