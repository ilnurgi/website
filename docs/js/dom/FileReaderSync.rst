FileReaderSync - синхронный интерфейс чтения объекта File или Blob
===============================================================


.. js:class:: FileReader()

    .. js:function:: readAsArrayBuffer(Blob blob)
    
        Чи­та­ет бай­ты из объ­ек­та blob и воз­вра­ща­ет их в ви­де объ­ек­та ArrayBuffer.


    .. js:function:: readAsBinaryString(Blob blob)
    
        Чи­та­ет бай­ты из объ­ек­та blob, пре­об­ра­зу­ет их в дво­ич­ную стро­ку (String.fromChar­Code()) и воз­вра­ща­ет ее.


    .. js:function:: readAsDataURL(Blob blob)
    
        Чи­та­ет бай­ты из объ­ек­та blob, пре­об­ра­зу­ет их с уче­том свой­ст­ва type объ­ек­та blob в URL-ад­рес data:// и воз­вра­ща­ет его.


    .. js:function:: readAsText(Blob blob, [string encoding])
    
        Чи­та­ет бай­ты дан­ных из объ­ек­та blob, де­ко­ди­ру­ет их с ис­поль­зо­ва­ни­ем ко­ди­ров­ки enco­ding (или с ис­поль­зо­ва­ни­ем ко­ди­ров­ки UTF-8 или UTF-16, ес­ли ар­гу­мент enco­ding не ука­зан) и воз­вра­ща­ет по­лу­чен­ную стро­ку.