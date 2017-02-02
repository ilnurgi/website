XMLHttpRequestUpload
====================


.. py:class:: XMLHttpRequestUpload()

    Наследник :py:class:`EventTarget`

    .. py:attribute:: onabort

        Вы­зы­ва­ет­ся при пре­ры­ва­нии вы­груз­ки.


    .. py:attribute:: onerror

        Вы­зы­ва­ет­ся, ко­гда в про­цес­се вы­груз­ки воз­ни­ка­ет се­те­вая ошиб­ка.


    .. py:attribute:: onload

        Вы­зы­ва­ет­ся в слу­чае ус­пеш­но­го за­вер­ше­ния вы­груз­ки


    .. py:attribute:: onloadend

        Вы­зы­ва­ет­ся в слу­чае ус­пеш­но­го или не­удач­но­го за­вер­ше­ния вы­груз­ки.

        Со­бы­тие «loadend» все­гда сле­ду­ет за со­бы­тия­ми «load»,
        «abort», «error» и «timeout».


    .. py:attribute:: onloadstart

        Вы­зы­ва­ет­ся с на­ча­лом вы­груз­ки.


    .. py:attribute:: onprogress

        Вы­зы­ва­ет­ся пе­рио­ди­че­ски (при­мер­но раз в 50 мил­ли­се­кунд) в хо­де вы­груз­ки.


    .. py:attribute:: ontimeout

        Вы­зы­ва­ет­ся, ес­ли ис­тек­ло вре­мя ожи­да­ния,
        оп­ре­де­ляе­мое свой­ст­вом timeout объ­ек­та XMLHttpRequest.