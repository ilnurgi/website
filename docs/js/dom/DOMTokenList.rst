DOMTokenList - множество лексем, разделенных пробелами
======================================================


.. py:class:: DOMTokenList()
    
    Наследние :py:class:`DOMTokenList`


    .. py:attribute:: length
    
        Ко­ли­че­ст­во уни­каль­ных лек­сем, со­дер­жа­щих­ся в нем.


    .. py:function:: add(string token)

        Если :py:class:`DOMTokenList` еще не содержит лексему token,
        она будет добавлена в конец списка.
    

    .. py:function:: contains(string token)
        
        Возвращает true, если объект :py:class:`DOMTokenList` содержит лексему token,
        или false – в противном случае.


    .. py:function:: item(unsigned long index)
    
        Воз­вра­ща­ет лек­се­му по ука­зан­но­му ин­дек­су или null, ес­ли ин­декс index вы­хо­дит за гра­ни­цы мас­си­ва. Объ­ект DOMTokenList мож­но так­же ин­дек­си­ро­вать не­по­сред­ст­ вен­но, не при­бе­гая к это­му ме­то­ду.


    .. py:function:: remove(string token)
    
        Удаляет указанную лексему.


    .. py:function:: toggle(string token)
    
        Если :py:class:`DOMTokenList` содержит лексему token,
        этот метод удалит ее. Иначе – добавит.