.. py:module:: elocation

elocation
=========

.. py:method:: extended_gsm_location()

    Некоторая информация о возвращаеммых данных

    * NetworkId - Идентификационный номер оператора. (Identification number of the network operator (The network identity, NID in CDMA and MNC in GSM)
    * DisplayTag - The alpha-tag of the network operator
    * Network Mode
        * Unregistered - мобильник не зарегистрироан (Mobile device is not registered)
        * GSM/GPRS - GSM/GPRS or DCS1800 network
        * AMPS - AMPS network
        * IS-95 - CDMA (IS-95) network
        * CDMA2000 - CDMA (cdma2000) network
        * WCDMA - WCDMA (UTRA Frequency Division Duplex (FDD)) network
        * TD-CDMA - TD-CDMA (UTRA Time Division Duplex (TDD)) network
        * Unknown - Network mode is unknown
    * NetworkStatus - Indicative (you cannot acces other networks seen by the phone currently, the network seen is the onne you are locked on)
        * Unknown - Status is unknown
        * Available - A network that the mobile device is allowed to register to
        * Current - Currently registered network
        * Forbidden - A network that the ME is not allowed to register to
    * CountryCode - Identification number of the country (network MCC)
    * AreaCode - Location area code, (can be different for each operator in the same area)
    
    For GSM/WCDMA Networks:

    * Network Access Technology
        * GSM - The access technology is GSM
        * GSM COMPACT - The access technology is GSM COMPACT. However GSM COMPACT systems which use GSM frequency bands but with the CBPCCH broadcast channel are considered as a separate access technology from GSM
        * UMTS - The access technology is UTRAN (UMTS Network)
        * Unknown - This is used when there is no network activity and therefore no RAT active
    * CellId - The cell identity code
    * ShortName - The short name (up to 8 characters) of the network operator
    * LongName - The long name (up to 16 characters) of the network operator
    
    For (Td)CDMA Networks:
        
    * BandInfo: Mobile phone network band information. Example: 800MHz Band C
    
    For AMPS and (Td)CDMA Networks:
    
    * CdmaSID: On CDMA networks, the system identity (SID) of the CDMA or AMPS network

    >>> elocation.extended_gsm_location()
    {{'NetworkId': u'02', 'DisplayTag': u'MegaFon', 'NetworkMode': 'GSM/GPRS', 'NetworkStatus': 'Current', 'CountryCode': u'250', 'AreaKnown': 1, 'AreaCode': 1651, 'NetworkAccessTechnology': 'GSM', 'LongName': u'MegaFon', 'ShortName': u'', 'CellId': 48281}


.. py:method:: get_imsi() 
    
    Возвращает imsi смартфона 

.. py:method:: get_registration_status() 

    Return a string indicating the status of the phone registration on the cellular network. See Symbian documentation CTelephony::TRegistrationStatus.
        
    * ERegistrationUnknown - Registration status is unknown.
    * ENotRegisteredNoService - Not registered. The ME can not detect any other networks and is not currently searching a new operator to register to.
    * ENotRegisteredEmergencyOnly - Not registered. The ME can detect other networks on which it is possible to make emergency calls only.
    * ENotRegisteredSearching - Not registered, but the ME is currently searching a new operator to register to.
    * ERegisteredBusy - Registered, network busy.
    * ERegisteredOnHomeNetwork - Registered on home network.
    * ERegistrationDenied - Registration denied.
    * ERegisteredRoaming - Registered, roaming.

    >>> elocation.get_registration_status()
    RegistrationUnknown

.. py:method:: gsm_location()
    
    >>> elocation.gsm_location()
    (u'250', u'02', 1651, 5, 1)

.. py:method:: version() 
    
    Возвращает версию установленного модуля

    >>>elocation.version()
    elocation v.0.2.7_d