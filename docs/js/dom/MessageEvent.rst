MessageEvent - сообщение из другого контекста выполнения
========================================================

.. py:class:: MessageEvent()

    Наследник :py:class:`Event`

    .. py:attribute:: data
        
        Это свой­ст­во хра­нит дос­тав­лен­ное со­об­ще­ние. Свой­ст­во data мо­жет иметь зна­че­ние лю­бо­го ти­па, ко­то­рое мож­но ско­пи­ро­вать с при­ме­не­ни­ем ал­го­рит­ма струк­ту­ри­ро­ван­но­го ко­пи­ро­ва­ния. К ним от­ но­сят­ся зна­че­ния ба­зо­во­го Ja­va­Script, вклю­чая объ­ек­ты и мас­си­вы, но не функ­ции. Не­ко­то­рые зна­че­ния кли­ент­ско­го Ja­va­Script, та­кие как уз­лы Document и Element, не мо­гут пе­ре­да­вать­ся, но мо­гут пе­ре­да­вать­ся объ­ек­ты Blob и ArrayBuffer.


    .. py:attribute:: lastEventId
        
        Для со­бы­тий «message» в ин­тер­фей­се EventSource это по­ле со­дер­жит стро­ку lastEventId, ес­ли име­ет­ся, от­прав­лен­ную сер­ве­ром.


    .. py:attribute:: origin
        
        Для со­бы­тий «message» в ин­тер­фей­сах EventSource или Window это свой­ст­во со­дер­жит URL-ад­рес от­пра­ви­те­ля со­об­ще­ния.


    .. py:attribute:: ports
        
        Для со­бы­тий «message» в  ин­тер­фей­сах Window, Worker и MessagePort это свой­ст­во со­дер­жит мас­сив объ­ек­тов MessagePort, ес­ли он был пе­ре­дан со­от­вет­ст­вую­ще­му вы­зо­ву postMessage().


    .. py:attribute:: source
        
        Для со­бы­тий «message» в ин­тер­фей­се Window это свой­ст­во ссы­ла­ет­ся на объ­ект Window, от­пра­вив­ший со­об­ще­ние.