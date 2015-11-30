BarcodeReader
=============

.. js:class:: BarcodeReader

    .. code-block:: js
        
        brc = app.CreateObject('BarcodeReader');

        cam = app.CreateCameraView( 0.8, 1, "VGA, UseYUV" );


    .. js:function:: Decode(cameraView)

        result contains

        * `barcodeType` - The type of the barcode, e.g. QR Code, Data Matrix, EAN 13, etc. See Supported Barcodes for the complete list.
        * `contentType` - The type of the barcode contents. The content can represent product codes, address book contacts, telephone numbers, etc. See Content Types for the complete list.

            * `ADDRESSBOOK` -  Contact Information
            * `CALENDAR` -     Calendar Event
            * `EMAIL` -  ADDRESS   Email Address
            * `GEO` -  Geo Location
            * `ISBN` -     International Standard Book Number
            * `PRODUCT` -  Product Code
            * `SMS` -  SMS Message
            * `TEL` -  Telephone Number
            * `TEXT` -     Plain Text
            * `URI` -  URI
            * `VIN` -  Vehicle Identification Number
            * `WIFI` -     Wifi Network Information
        * `content` - The human readable representation of the barcode contents.
        * `raw` -  Contains the barcode content in it's original form. In some cases this will be the same as the content property, but if the contentType is ADDRESSBOOK for example, the raw property will contain the vCard or meCard contact data.


    .. js:function:: SetBarcodeTypes(types)

        CODABAR, CODE 128, CODE 39, CODE 93, DATA MATRIX, EAN 13, EAN 8, ITF, QR CODE, RSS , UPC 




