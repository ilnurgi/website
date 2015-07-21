XMLHttpRequestUpload
====================


.. js:class:: XMLHttpRequestUpload()

    Наследник :js:class:`EventTarget`

    .. js:attribute:: onabort

        Вы­зы­ва­ет­ся при пре­ры­ва­нии вы­груз­ки.


    .. js:attribute:: onerror

        Вы­зы­ва­ет­ся, ко­гда в про­цес­се вы­груз­ки воз­ни­ка­ет се­те­вая ошиб­ка.


    .. js:attribute:: onload

        Вы­зы­ва­ет­ся в слу­чае ус­пеш­но­го за­вер­ше­ния вы­груз­ки


    .. js:attribute:: onloadend

        Вы­зы­ва­ет­ся в слу­чае ус­пеш­но­го или не­удач­но­го за­вер­ше­ния вы­груз­ки. Со­бы­тие «loadend» все­гда сле­ду­ет за со­бы­тия­ми «load», «abort», «error» и «timeout».


    .. js:attribute:: onloadstart

        Вы­зы­ва­ет­ся с на­ча­лом вы­груз­ки.


    .. js:attribute:: onprogress

        Вы­зы­ва­ет­ся пе­рио­ди­че­ски (при­мер­но раз в 50 мил­ли­се­кунд) в хо­де вы­груз­ки.


    .. js:attribute:: ontimeout

        Вы­зы­ва­ет­ся, ес­ли ис­тек­ло вре­мя ожи­да­ния, оп­ре­де­ляе­мое свой­ст­вом timeout объ­ек­та XMLHttpRequest.