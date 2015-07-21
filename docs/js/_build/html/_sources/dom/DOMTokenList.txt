DOMTokenList - множество лексем, разделенных пробелами
======================================================


.. js:class:: DOMTokenList()
    
    Наследние :js:class:`DOMTokenList`


    .. js:attribute:: length
    
        Ко­ли­че­ст­во уни­каль­ных лек­сем, со­дер­жа­щих­ся в нем.


    .. js:function:: add(string token)

        Ес­ли DOMTokenList еще не со­дер­жит лек­се­му token, она бу­дет до­бав­ле­на в ко­нец спи­ска.
    

    .. js:function:: contains(string token)
        
        Воз­вра­ща­ет true, ес­ли объ­ект DOMTokenList со­дер­жит лек­се­му token, или false – в про­тив­ном слу­чае.


    .. js:function:: item(unsigned long index)
    
        Воз­вра­ща­ет лек­се­му по ука­зан­но­му ин­дек­су или null, ес­ли ин­декс index вы­хо­дит за гра­ни­цы мас­си­ва. Объ­ект DOMTokenList мож­но так­же ин­дек­си­ро­вать не­по­сред­ст­ вен­но, не при­бе­гая к это­му ме­то­ду.


    .. js:function:: remove(string token)
    
        Ес­ли DOMTokenList со­дер­жит лек­се­му token, этот ме­тод уда­лит ее. Ина­че он ни­че­го де­лать не бу­дет.


    .. js:function:: toggle(string token)
    
        Ес­ли DOMTokenList со­дер­жит лек­се­му token, этот ме­тод уда­лит ее. Ина­че – до­ба­вит.