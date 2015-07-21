socket
======

работа с синезубом


::

    import socket

    address, services = socket.bt_obex_discover()

    print "Chosen device:", address, services
    # Chosen device: 00:12:d2:41:35:e4 {u"OBEX Object Push":9}

    MY_PC = "00:12:d2:41:35:e4"
    address, services = socket.bt_obex_discover(MY_PC)


    Example 56: Send photos to another phone using Bluetooth

    import camera, e32, socket, appuifw

    PHOTO = u"e:\\Images\\bt_photo_send.jpg"

    def send_photo():
        try:
            address, services = socket.bt_obex_discover()
        except:
            appuifw.note(u"OBEX Push not available", "error")
        return

        if u'OBEX Object Push' in services:
            channel = services[u'OBEX Object Push']
            socket.bt_obex_send_file(address, channel, PHOTO)
            appuifw.note(u"photo sent", "info")
        else:
        appuifw.note(u"OBEX Push not available", "error")

    def take_photo():
        photo = camera.take_photo()
        canvas.blit(photo, scale = 1)
        photo.save(PHOTO)

    def quit():
        app_lock.signal()
        
    canvas = appuifw.Canvas()
    appuifw.app.body = canvas
    appuifw.app.exit_key_handler = quit
    appuifw.app.title = u"BT photo send"
    appuifw.app.menu = [(u"Take photo", take_photo),\
    (u"Send photo", send_photo)]
    app_lock = e32.Ao_lock()
    app_lock.wait()


    # BT Chat

    import socket, appuifw

    def chat_server():
        server = socket.socket(socket.AF_BT, socket.SOCK_STREAM)
        channel = socket.bt_rfcomm_get_available_server_channel(server)
        server.bind(("", channel))
        server.listen(1)
        socket.bt_advertise_service(u"btchat", server, True, socket.RFCOMM)
        socket.set_security(server, socket.AUTH | socket.AUTHOR)
        print "Waiting for clients..."
        conn, client_addr = server.accept()
        print "Client connected!"
        talk(conn, None)
    def chat_client():
        conn = socket.socket(socket.AF_BT, socket.SOCK_STREAM)PHONE-TO-PHONE COMMUNICATION
        139
        address, services = socket.bt_discover()
        if 'btchat' in services:
            channel = services[u'btchat']
            conn.connect((address, channel))
            print "Connected to server!"
            talk(None, conn)
        else:
            appuifw.note(u"Target is not running a btchat server", "error")

    def receive_msg(fd):
        print "Waiting for message.."
        reply = fd.readline()
        print "Received: " + reply
        appuifw.note(unicode(reply), "info")

    def send_msg(fd):
        msg = appuifw.query(u"Send a message:", "text")
        print "Sending: " + msg
        print >> fd, msg

    def talk(client, server):
        try:
            if server:
                fd = server.makefile("rw", 0)
                receive_msg(fd)
            if client:
                fd = client.makefile("rw", 0)
            while True:
                send_msg(fd)
                receive_msg(fd)
        except:
            appuifw.note(u"Connection lost", "info")
            if client:
                client.close()
            if server:
                server.close()
            print "Bye!"

    index = appuifw.popup_menu([u"New server", u"Connect to server"], u"BTChat mode")
    if index != None:
        if index:
            chat_client()
        else:
            chat_server()


    Example 59: Bluetooth client

    import appuifw, socket, e32

    ECHO = True

    def choose_service(services):
        names = []
        channels = []
        for name, channel in services.items():
            names.append(name)
            channels.append(channel)
        index = appuifw.popup_menu(names, u"Choose service")
        return channels[index]

    def read_and_echo(fd):
        buf = r = ""
        while r != "\n" and r != "\r":
            r = fd.read(1)
            if ECHO: fd.write(r)
            buf += r
        if ECHO: fd.write("\n")
        return buf

    address, services = socket.bt_discover()
    channel = choose_service(services)
    conn = socket.socket(socket.AF_BT, socket.SOCK_STREAM)
    conn.connect((address, channel))
    to_peer = conn.makefile("rw", 0)

    while True:
        msg = appuifw.query(u"Send a message", "text")
        if msg:
            print >> to_peer, msg + "\r"
            print "Sending: " + msg
            print "Waiting for reply..."
            reply = read_and_echo(to_peer).strip()
            appuifw.note(unicode(reply), "info")
        if reply.find("bye!") != -1:
            break
        else:
            break
    to_peer.close()
    conn.close()
    print "bye!"


гпс через бт
------------

::

    import socket

    # Findabluetooth GPS
    address , services = socket .btdiscover( )
    print ”Discovered : %s , %s ” % (address, services )

    target = (address , services.values( )[0] )

    # Connect
    conn = socket.socket(socket.AF BT , socket.SOCK STREAM)
    conn.connect(target)
    gps = conn.makefile( ”r” , 0 )
    while True :
        # Get sentence , strip of CR/NL or other whitespace
        sentence = gps.readline().strip()
        if sentence[0:3 ] == ’$GP ’ and sentence[ −3] == ’ ∗ ’ :
            print sentence [3:6]

    возвращаемый ответ
    RMC -> Recommended Minimum sentence C
    123519 -> Fix taken at 12:35:19 UTC
    A -> Status A=activeo V=Void
    4807.038,N -> Latitude 48 deg 07.038’N
    01131.000,E -> Longitude 11 deg 31.000’E
    022.4 -> Speed over the ground in knots
    084.4 -> Track angle in degrees True
    230394 -> Date − 23 rd of March 1994
    003.1,W -> Magnetic Variation
    ∗6A -> The checksum data, always begins with ∗



    А ТУТ МЫ СЧИТАЕМ РАССТОЯНИЕ

    import math

    # radians and degrees are omitted from the pys60 math distribution
    def radians(degrees) :
        return(math.pi ∗ degrees)/180.0

    def distance(lat1, lon1, lat2, lon2) :
        ”””Computes the geodesic distance, in meters ,
        between two locations expressed in geographic coordinates
        Ref : http://en.wikipedia.org/wiki/Haversineformula”””
        
        R = 6371000 # Earth radius in meters (approximately)
        
        dLat = radians(float(lat2) − float(lat1))
        dLon = radians(float(lon2) − float(lon1))
        a = math.sin(dLat/2.0) ∗ math.sin(dLat/2.0)\
        + math.cos(radians(float(lat1))) ∗ math.cos(radians(float(lat2)))\
        ∗ math.sin(dLon/2.0) ∗ math.sin(dLon/2.0) ;
        c = 2.0 ∗ math.atan2(math.sqrt(a), math.sqrt(1.0 − a))
        return R ∗ c
