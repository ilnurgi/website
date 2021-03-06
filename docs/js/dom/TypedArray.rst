TypedArray - массивы с двоичными элементами фиксированного размера
==================================================================

Ти­пи­зи­ро­ван­ные мас­си­вы яв­ля­ют­ся под­ти­па­ми ArrayBufferView, ко­то­рый ин­тер­пре­ти­ру­ет бай­ты в объ­ек­те ArrayBuffer, на ко­то­ром он ос­но­ван, как мас­сив чи­сел и по­зво­ля­ет чи­тать и из­ме­нять эле­мен­ты это­го мас­си­ва. Дан­ная спра­воч­ная ста­тья опи­сы­ва­ет не ка­кой-то кон­крет­ный тип ти­пи­зи­ро­ван­ных мас­си­вов, а ох­ва­ты­ва­ет во­семь раз­ных ви­дов ти­пи­зи­ро­ван­ных мас­си­вов. Все эти во­семь ти­пов яв­ля­ют­ся под­ти­па­ми ArrayBufferView и от­ли­ча­ют­ся друг от дру­га толь­ко ко­ли­че­ст­вом бай­тов, вы­де­лен­ных для од­но­го эле­мен­та мас­си­ва и спо­со­бом ин­тер­пре­та­ции этих эле­мен­тов.


.. py:class:: TypedArray(unsigned long length)
.. py:class:: TypedArray(TypedArray array)
.. py:class:: TypedArray(type[] array)
.. py:class:: TypedArray(ArrayBuffer buffer, [unsigned long byteOffset], [unsigned long length])

    Наследник :py:class:`ArrayBufferView`


    .. py:attribute:: length
        
        Ко­ли­че­ст­во эле­мен­тов в  мас­си­ве. Ти­пи­зи­ро­ван­ные мас­си­вы име­ют фик­си­ро­ван­ный раз­мер, по­это­му зна­че­ние это­го свой­ст­ва ни­ко­гда не из­ме­ня­ет­ся. Не пу­тай­те это свой­ст­во со свой­ст­вом byteLength, унас­ле­до­ван­ным от ArrayBufferView.


    .. py:function:: set(TypedArray array, [unsigned long offset])
        
        Ко­пи­ру­ет эле­мен­ты мас­си­ва array в  дан­ный ти­пи­зи­ро­ван­ный мас­сив, на­чи­ная с ин­дек­са offset.


    .. py:function:: set(number[] array, [unsigned long offset])
        
        Эта вер­сия ме­то­да set() по­доб­на пре­ды­ду­щей, но при­ни­ма­ет не ти­пи­зи­ро­ван­ный, а ис­тин­ный мас­сив.


    .. py:function:: subarray(long start, long end)
        
        Воз­вра­ща­ет но­вый ти­пи­зи­ро­ван­ный мас­сив, опи­раю­щий­ся на тот же объ­ект Array­Buffer, что и дан­ный мас­сив. Пер­вым эле­мен­том воз­вра­щае­мо­го мас­си­ва яв­ля­ет­ся эле­мент дан­но­го мас­си­ва с ин­дек­сом start. А по­след­ним – эле­мент дан­но­го мас­си­ва с ин­дек­сом end–1. От­ри­ца­тель­ные зна­че­ния в ар­гу­мен­тах start и end ин­тер­пре­ти­ру­ют­ся как сме­ще­ния от­но­си­тель­но кон­ца дан­но­го мас­си­ва.