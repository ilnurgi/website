.. py:module:: pyaudio

pyaudio - инструмент для работы со звуком
=========================================

Модуль позволяет работать с кросплатформенной библиотекой PortAudio, проигрывать и записывать звуки.


Атрибуты модуля
---------------


Методы модуля
-------------

.. py:method:: get_format_from_width(width, unsigned-True)

    возвращает :ref:`sample_formats` формата PortAudio для указанной ширины

    :param int width: ширина образца в байтах
    :param bool unsigned: для ширины 1 байт, знаковый или беззнаковый
    :raises ValueError: если ширина не корректна

.. py:method:: get_portaudio_version()

    возвращает версию PortAudio

    >>> pyaudio.get_portaudio_version()
    1899L


.. py:method:: get_portaudio_version_text()
    
    возврашает полную информацию о версии модуля

    >>> pyaudio.get_portaudio_version_text()
    u'PortAudio V19-devel (built Feb 25 2014 21:09:53)'


.. py:method:: get_sample_size(format)

    возвращает размер (в байтах) для заданного формата образца

    :param format: :ref:`sample_formats`
    :raises ValueError: при неверном типе формата



Объекты модуля
--------------

.. py:class:: PyAudio()

    основной объект модуля, который предоставляет возможность работы со звуком.


    .. py:method:: close(stream)

        закрывает поток

        :param pyaudio.Stream stream: поток
        :raises ValueError: если потока не существует


    .. py:method:: get_default_host_api_info()

        возвращает словарь, содержащий устройства для работы со звуком в системе

        :raises IOError: если нет устройств в системе

        >>> p.get_default_host_api_info()
        {'defaultInputDevice': 5L,
         'defaultOutputDevice': 5L,
         'deviceCount': 6L,
         'index': 0L,
         'name': u'ALSA',
         'structVersion': 1L,
         'type': 8L}


    .. py:method:: get_default_input_device_info()

        возвращает словарь, содержащий устройства ввода в системе

        >>> p.get_default_input_device_info()
        {'defaultHighInputLatency': 0.034829931972789115,
         'defaultHighOutputLatency': 0.034829931972789115,
         'defaultLowInputLatency': 0.008707482993197279,
         'defaultLowOutputLatency': 0.008707482993197279,
         'defaultSampleRate': 44100.0,
         'hostApi': 0L,
         'index': 5L,
         'maxInputChannels': 32L,
         'maxOutputChannels': 32L,
         'name': u'default',
         'structVersion': 2L}


    .. py:method:: get_default_output_device_info()

        возвращает словарь, содержащий устройства вывода в системе

        >>> p.get_default_output_device_info()
        {'defaultHighInputLatency': 0.034829931972789115,
         'defaultHighOutputLatency': 0.034829931972789115,
         'defaultLowInputLatency': 0.008707482993197279,
         'defaultLowOutputLatency': 0.008707482993197279,
         'defaultSampleRate': 44100.0,
         'hostApi': 0L,
         'index': 7L,
         'maxInputChannels': 32L,
         'maxOutputChannels': 32L,
         'name': u'default',
         'structVersion': 2L}


    .. py:method:: get_device_count()

        возвращает количесвто устройств

        >>> p.get_device_count()
        8L


    .. py:method:: get_device_info_by_host_api_device_index(host_api_index, host_api_device_index) 

        возвращает словарь, содержащий параметры для указанного устройства.

        :raiseы IOError: для неподдерживаемых устройств


    .. py:method:: get_device_info_by_index(device_index)

        возвращает словарь, информацию об устройстве

        :raises IOError: для неподдерживаемых устройств


    .. py:method:: get_format_from_width(width, unsigned-True)

        возвращает :ref:`sample_formats` для указанной ширины. аналог :py:meth:`get_format_from_width`

        :param int width: ширина образца в байтах (от 1 до 4)
        :param bool unsigned: для ширины 1 байт, знаковый или беззнаковый
        :raiseы ValueError: если ширина не корректна


    .. py:method:: get_host_api_count()

        возвращает количество доступных интерфейсов PortAudio.

        >>> p.get_host_api_count()
        2L


    .. py:method:: get_host_api_info_by_index(host_api_index)

        возвращает словарь, информацию об устройстве

        :raises IOError: для неподдерживаемых устройств


    .. py:method:: get_host_api_info_by_type(host_api_type)

        возвращает словарь, информацию об устройстве

        :raises IOError: для неподдерживаемых устройств


    .. py:method:: get_sample_size(format)

        возвращает размер (в байтах) для заданного формата образца, аналог :py:meth:`get_sample_size`

        :param format: :ref:`sample_formats`
        :raises ValueError: при неверном типе формата


    .. py:method:: is_format_supported(rate, input_device=None, input_channels=None, input_format=None, output_device=None, output_channels=None, output_format=None)

        возвращает True, если указанная конфигурация поддерживается устройством, иначе возбуждает исключение

        :param rate: скорость потока (в Hz)
        :param input_device: индекс входного устройств. None для полудуплексных выходных потоков
        :param input_channels: количество входных каналов. Игнорируется если input_device не задан
        :param input_format: входной формат PortAudio
        :param output_device: индекс выходного устройства. None для полудуплексных входных потоков
        :param output_channels: количество выходных каналов. Игнорируется если output_device не задан
        :param output_format: выходной формат PortAudio
        :raises ValueError: если конфигурация не поддерживается. Исключение в виде кортежа (error string, PortAudio Error Code).


    .. py:method:: open(*args, **kwargs)

        возвращает объект :py:class:`Stream`, открывает поток на воспроизведение или чтение звука. принимает те же параметр что и конструктор :py:class:`Stream`


    .. py:method:: terminate()

        закрывает объект


.. py:class:: Stream(**kwargs)

    звуковой поток. используйте :py:meth:`PyAudio.open()` для получения данного объекта

    :param PA_manger: ссылка на экземпляр PyAudio
    :param rate: скорость потока
    :param channels: количество каналов
    :param format: :ref:`sample_formats`
    :param input: указывает, что это входной поток, по умолчанию `False`
    :param output: указывает, что это выходной поток, по умолчанию `False`
    :param input_device_index: индекс входного устройства, игнорируется, если `input` = `False`. По умолчанию `None`, дефолтное устройство
    :param output_device_index: индекс выходного устройства, игнорируется, если `output` = `False`. По умолчанию `None`, дефолтное устройство
    :param frames_per_buffer: количество фреймов в буфере
    :param start: стартует поток после инициализации сразу, по умолчанию `True`
    :param input_host_api_specific_stream_info: указывает на специфичное хост входное устройтсво (:py:class:`pyaudio.PaMacCoreStreamInfo`)
    :param output_host_api_specific_stream_info: указывает на специфичное хост выходное устройтсво (:py:class:`pyaudio.PaMacCoreStreamInfo`)
    :param stream_callback: обработчик потока, вызывается каждый раз, когда в поток попадают данные. сигнатура обработчика `callback(input_data, frame_count, time_info, status_flag)`, должен возвраващть кортеж (frame_count, flag)


    .. py:method:: close()

        закрывает поток


    .. py:method:: get_cpu_load()

        возвращает вещественное число, загрузку процессора


    .. py:method:: get_input_latency()

        возвращает задержку ввода


    .. py:method:: get_output_latency()

        возвращает задержку вывода


    .. py:method:: get_time()

        возвращает количество фреймов, которые могут быть записаны без ожидания


    .. py:method:: get_write_available()

        возвращает время потока


    .. py:method:: is_active()

        возвращает статус состояния потока


    .. py:method:: is_stopped()

        возвращает статус состояния потока


    .. py:method:: read(num_frames)

        читает данные из потока, при записи звука


    .. py:method:: start_stream()

        запускает поток


    .. py:method:: stop_stream()

        завершает поток


    .. py:method:: write(frames, num_frames=None, exception_on_underflow=False)

        записывает в поток данные, например при воспроизведении звука

        :param frames: данные
        :param num_frames: количество данных для записи в поток
        :param exception_on_underflow: обработка ошибки переполнения потока


.. py:class:: PaMacCoreStreamInfo(flags=None, channel_map=None)
    
    утсройство доступное только на MacOS
    
    :param flags: :ref:`macos_flags`
    :param channel_map: массив, описывающий отображанеие канала


    .. py:method:: get_channel_map()

        возвращает карту канала


    .. py:method:: get_flags()

        возвращает флаги


.. _sample_formats: 

Типы образцов
-------------

.. py:attribute:: paFloat32 - 1

    32-х битный long


.. py:attribute:: paInt32 - 2

    32-х битный int


.. py:attribute:: paInt24 - 4

    24-х битный int


.. py:attribute:: paInt16 - 8

    16 битный int


.. py:attribute:: paInt8 - 16

    8 битный int


.. py:attribute:: paUint8 - 32

    8 битный беззнаковый int


.. py:attribute:: paCustomFormat - 65536

    специальный формат


Типы рузльтатов обработчика записи
----------------------------------

.. py:attribute:: paContinue - 0

    следующитй блок потока


.. py:attribute:: paComplete - 1

    последний блок потока


.. py:attribute:: paAbort - 2

    обнаружена ошибка, остановить проигрывание или запись


Типы флагов обработчика
-----------------------

.. py:attribute:: paInputUnderflow - 1

    входной буфер не заполнен


.. py:attribute:: paInputOverflow - 2

    входной буфер переполнен


.. py:attribute:: paOutputUnderflow - 4

    выходной поток не заполнен


.. py:attribute:: paOutputOverflow - 8

    выходной поток переполнен


.. py:attribute:: paPrimingOutput - 16

    подготовка, но ещё не воспроизведение


Типы устройств
--------------

.. py:attribute:: paInDevelopment - 0

    Still in development


.. py:attribute:: paDirectSound - 1

    DirectSound (Windows only)

    
.. py:attribute:: paMME - 2

    Multimedia Extension (Windows only)


.. py:attribute:: paASIO - 3

    Steinberg Audio Stream Input/Output


.. py:attribute:: paSoundManager - 4

    SoundManager (OSX only)


.. py:attribute:: paCoreAudio - 5

    CoreAudio (OSX only)


.. py:attribute:: paOSS - 7
    
    Open Sound System (Linux only)


.. py:attribute:: paALSA - 8

    Advanced Linux Sound Architecture (Linux only)


.. py:attribute:: paAL - 9 

    Open Audio Library


.. py:attribute:: paBeOS - 10

    BeOS Sound System


.. py:attribute:: paWDMKS - 11

    Windows Driver Model (Windows only)


.. py:attribute:: paJACK - 12
    
    JACK Audio Connection Kit


.. py:attribute:: paWASAPI - 13

    Windows Vista Audio stack architecture


.. py:attribute:: paNoDevice - -1
    
    нет актуалного устройства


Типы ошибок
-----------

.. py:class:: paNoError
.. py:class:: paNotInitialized
.. py:class:: paUnanticipatedHostError
.. py:class:: paInvalidChannelCount
.. py:class:: paInvalidSampleRate
.. py:class:: paInvalidDevice
.. py:class:: paInvalidFlag
.. py:class:: paSampleFormatNotSupported
.. py:class:: paBadIODeviceCombination
.. py:class:: paInsufficientMemory
.. py:class:: paBufferTooBig
.. py:class:: paBufferTooSmall
.. py:class:: paNullCallback
.. py:class:: paBadStreamPtr
.. py:class:: paTimedOut
.. py:class:: paInternalError
.. py:class:: paDeviceUnavailable
.. py:class:: paIncompatibleHostApiSpecificStreamInfo
.. py:class:: paStreamIsStopped
.. py:class:: paStreamIsNotStopped
.. py:class:: paInputOverflow
.. py:class:: paOutputUnderflowed
.. py:class:: paHostApiNotFound
.. py:class:: paInvalidHostApi
.. py:class:: paCanNotReadFromACallbackStream
.. py:class:: paCanNotWriteToACallbackStream
.. py:class:: paCanNotReadFromAnOutputOnlyStream
.. py:class:: paCanNotWriteToAnInputOnlyStream
.. py:class:: paIncompatibleStreamHostApi

.. _macos_flags:

Специфичные типы для MacOS
--------------------------

.. py:attribute:: paMacCoreChangeDeviceParameters
.. py:attribute:: paMacCoreFailIfConversionRequired
.. py:attribute:: paMacCoreConversionQualityMin
.. py:attribute:: paMacCoreConversionQualityMedium
.. py:attribute:: paMacCoreConversionQualityLow
.. py:attribute:: paMacCoreConversionQualityHigh
.. py:attribute:: paMacCoreConversionQualityMax
.. py:attribute:: paMacCorePlayNice
.. py:attribute:: paMacCorePro
.. py:attribute:: paMacCoreMinimizeCPUButPlayNice
.. py:attribute:: paMacCoreMinimizeCPU

Примеры
-------

::

    """проигрывание wav файла, блокирующий поток выполнения"""

    import pyaudio
    import wave
    import sys

    CHUNK - 1024

    if len(sys.argv) < 2:
        print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
        sys.exit(-1)

    wf - wave.open(sys.argv[1], 'rb')

    # instantiate PyAudio (1)
    p - pyaudio.PyAudio()

    # open stream (2)
    stream - p.open(format-p.get_format_from_width(wf.getsampwidth()),
                    channels-wf.getnchannels(),
                    rate-wf.getframerate(),
                    output-True)

    # read data
    data - wf.readframes(CHUNK)

    # play stream (3)
    while data !- '':
        stream.write(data)
        data - wf.readframes(CHUNK)

    # stop stream (4)
    stream.stop_stream()
    stream.close()

    # close PyAudio (5)
    p.terminate()


::

    """проигрывание wav файла, не блокирующий поток"""

    import pyaudio
    import wave
    import time
    import sys

    if len(sys.argv) < 2:
        print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
        sys.exit(-1)

    wf - wave.open(sys.argv[1], 'rb')

    # instantiate PyAudio (1)
    p - pyaudio.PyAudio()

    # define callback (2)
    def callback(in_data, frame_count, time_info, status):
        data - wf.readframes(frame_count)
        return (data, pyaudio.paContinue)

    # open stream using callback (3)
    stream - p.open(format-p.get_format_from_width(wf.getsampwidth()),
                    channels-wf.getnchannels(),
                    rate-wf.getframerate(),
                    output-True,
                    stream_callback-callback)

    # start the stream (4)
    stream.start_stream()

    # wait for stream to finish (5)
    while stream.is_active():
        time.sleep(0.1)

    # stop stream (6)
    stream.stop_stream()
    stream.close()
    wf.close()

    # close PyAudio (7)
    p.terminate()
