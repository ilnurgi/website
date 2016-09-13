DOMException - исключение, возбуждаемое web api
===============================================


.. py:class:: DOMException()

    Наследник :py:class:`Node`


    .. py:attribute:: code
    
        Зна­че­ние од­ной из кон­стант, пе­ре­чис­лен­ных вы­ше, оп­ре­де­ляю­щих тип ис­клю­че­ния.

        * `DOMException.INDEX_SIZE_ERR` = 1

        * `DOMException.HIERARCHY_REQUEST_ERR` = 3

        * `DOMException.WRONG_DOCUMENT_ERR` = 4

        * `DOMException.INVALID_CHARACTER_ERR` = 5

        * `DOMException.NO_MODIFICATION_ALLOWED_ERR` = 7

        * `DOMException.NOT_FOUND_ERR` = 8

        * `DOMException.NOT_SUPPORTED_ERR` = 9

        * `DOMException.INVALID_STATE_ERR` = 11

        * `DOMException.SYNTAX_ERR` = 12

        * `DOMException.INVALID_MODIFICATION_ERR` = 13

        * `DOMException.NAMESPACE_ERR` = 14

        * `DOMException.INVALID_ACCESS_ERR` = 15

        * `DOMException.TYPE_MISMATCH_ERR` = 17

        * `DOMException.SECURITY_ERR` = 18

        * `DOMException.NETWORK_ERR` = 19

        * `DOMException.ABORT_ERR` = 20

        * `DOMException.URL_MISMATCH_ERR` = 21

        * `DOMException.QUOTA_EXCEEDED_ERR` = 22

        * `DOMException.TIMEOUT_ERR` = 23

        * `DOMException.DATA_CLONE_ERR` = 25

    .. py:attribute:: name
    
        Имя ти­па ис­клю­че­ния. Это бу­дет имя од­ной из кон­стант, пе­ре­чис­лен­ных вы­ше, в ви­де стро­ки.