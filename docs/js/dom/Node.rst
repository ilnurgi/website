Node - узел дом дерева документа
================================

.. js:class:: Node()

    .. js:attribute:: ELEMENT_NODE

    .. js:attribute:: ATTRIBUTE_NODE

    .. js:attribute:: TEXT_NODE

    .. js:attribute:: CDATA_SECTION_NODE

    .. js:attribute:: ENTITY_REFERENCE_NODE

    .. js:attribute:: ENTITY_NODE

    .. js:attribute:: PROCESSING_INSTRUCTION_NODE

    .. js:attribute:: COMMENT_NODE

    .. js:attribute:: DOCUMENT_NODE

        Узел - документ

    .. js:attribute:: DOCUMENT_TYPE_NODE

    .. js:attribute:: DOCUMENT_FRAGMENT_NODE

    .. js:attribute:: NOTATION_NODE

    .. js:attribute:: attributes

        список атрибутов данного узла


    .. js:attribute:: baseURI
        
        Определяет базовый URL-адрес для данного объекта,
        который будет использоваться при разрешении относительных URL-адре­сов.

        Для всех узлов в HTML-документах этот URL-адрес определяется элементом <base>
        или свойством Document.URL,
        из значения которого исключается идентификатор фрагмента.


    .. js:attribute:: children

        Коллекция, дочерних элементов узла, без текстовых


    .. js:attribute:: childNodes

        Коллекция, :js:class:`NodeList`, дочерних узлов узла,
        включая текстовые.


    .. js:attribute:: firstChild

        Первый дочерний элемент :js:class:`Node` данного узла


    .. js:attribute:: lastChild

        Последний дочерний элемент :js:class:`Node` данного узла


    .. js:attribute:: nextSibling

        Возвращает соседний узел справа, :js:class:`Node`


    .. js:attribute:: nodeName

        имя узла


    .. js:attribute:: nodeType

        Тип узла в виде числа


    .. js:attribute:: nodeValue

        значение узла


    .. js:attribute:: ownerDocument

        Ссылка на корневой узел :js:class:`Document`

        
    .. js:attribute:: parentElement

        Возвращает родительский элемент, :js:class:`Element`


    .. js:attribute:: parentNode

        Возвращает родительский узел, :js:class:`Node`


    .. js:attribute:: previousSibling

        Возвращает соседний узел слева, :js:class:`Node`


    .. js:attribute:: textContent

        текстовое содержимое узла и его наследников
        

    .. js:function:: appendChild(node)

        Добавляет узел :js:class:`Node` узлу.

        Привязывает новый узел к дереву,
        ставя его последним в списке дочерних узлов данного узла


    .. js:function:: cloneNode(deep)

        Создает и возвращает копию узла :js:class:`Node`, для которого он вызван.


    .. js:function:: compareDocumentPosition(Node other)
        
        Срав­ни­ва­ет по­зи­цию дан­но­го уз­ла в до­ку­мен­те с по­зи­ци­ей уз­ла other и воз­вра­ща­ет чис­ло, би­ты ко­то­ро­го опи­сы­ва­ют от­но­ше­ния ме­ж­ду уз­ла­ми. Ес­ли срав­ни­вае­мые уз­лы яв­ля­ют­ся од­ним и тем же уз­лом, все би­ты в ре­зуль­та­те бу­дут сбро­ше­ны, т. е. ме­тод вер­нет 0. Ина­че в воз­вра­щае­мом зна­че­нии бу­дет ус­та­нов­лен один или бо­лее би­тов. 

        * `Node.DISCONNECTED` = 0x01, Два уз­ла при­над­ле­жат раз­ным до­ку­мен­том, по­это­му их по­зи­ции не мо­гут срав­ни­вать­ся.

        * `Node.PRECEDING` = 0x02, Узел other рас­по­ла­га­ет­ся пе­ред дан­ным уз­лом.

        * `Node.FOLLOWING` = 0x04, Узел other рас­по­ла­га­ет­ся по­сле дан­но­го уз­ла.
        
        * `Node.CONTAINS` = 0x08, Узел other со­дер­жит дан­ный узел. Ко­гда ус­та­нов­лен этот бит, все­гда бу­дет ус­та­нов­лен бит PRECEDING.
        
        * `Node.CONTAINED_BY` = 0x10, Узел other со­дер­жит­ся внут­ри дан­но­го уз­ла. Ко­гда ус­та­нов­лен этот бит, все­гда бу­дет ус­та­нов­лен бит FOLLOWING.


    .. js:function:: hasChildNodes()

        возвращает значение true , если узел имеет хотя бы один дочерний узел


    .. js:function:: insertBefore(newNode, refNode)

        Вставляет новый узел `newNode`, :js:class:`Node`,
        перед существующим узлом `refNode` :js:class:`Node`


    .. js:function:: isDefaultNamespace(string namespace)
        
        Воз­вра­ща­ет true, ес­ли URL-ад­рес про­стран­ст­ва имен namespace сов­па­да­ет с URL-ад­ре­сом про­стран­ст­ва имен по умол­ча­нию, ко­то­рый воз­вра­ща­ет вы­зов lookupName­spaceURI(null), и false – в про­тив­ном слу­чае.


    .. js:function:: isEqualNode(Node other)
        
        Воз­вра­ща­ет true, ес­ли дан­ный узел и узел other яв­ля­ют­ся иден­тич­ны­ми, т. е. име­ют один и тот же тип, имя те­га, ат­ри­бу­ты и (ре­кур­сив­но) до­чер­ние уз­лы. Воз­вра­ща­ет false, ес­ли два уз­ла не яв­ля­ют­ся эк­ви­ва­лент­ны­ми.


    .. js:function:: isSameNode(Node other)
        
        Воз­вра­ща­ет true, ес­ли дан­ный узел и узел other яв­ля­ют­ся од­ним и тем же уз­лом, и false – в про­тив­ном слу­чае. Вме­сто это­го ме­то­да мож­но так­же про­сто ис­поль­зо­вать опе­ра­тор ==.


    .. js:function:: lookupNamespaceURI(string prefix)
        
        Воз­вра­ща­ет URL-ад­рес про­стран­ст­ва имен, свя­зан­но­го с  ука­зан­ным пре­фик­сом про­стран­ст­ва имен prefix, или null, ес­ли та­кой пре­фикс не оп­ре­де­лен. Ес­ли ар­гу­мент prefix име­ет зна­че­ние null, воз­вра­ща­ет URL-ад­рес про­стран­ст­ва имен по умол­ча­нию.
    

    .. js:function:: lookupPrefix(string namespace)
        
        Воз­вра­ща­ет пре­фикс про­стран­ст­ва имен, свя­зан­но­го с  ука­зан­ным URL-ад­ре­сом про­стран­ст­ва имен, или null, ес­ли та­кое про­стран­ст­во имен не оп­ре­де­ле­но.


    .. js:function:: normalize()
        
        Нор­ма­ли­зу­ет все уз­лы, яв­ляю­щие­ся по­том­ка­ми дан­но­го, объ­еди­няя смеж­ные уз­лы и уда­ляя пус­тые. Обыч­но до­ку­мен­ты не име­ют пус­тых или смеж­ных тек­сто­вых уз­лов, но они мо­гут по­явить­ся в ре­зуль­та­те до­бав­ле­ния и уда­ле­ния уз­лов сце­на­ри­ем.


    .. js:function:: querySelector(selector:string)

        Возвращает первый элемент :js:class:`Element`,
        соответствующий CSS-селекторам selectors
        (это может быть единственный CSS-селектор или группа селекторов,
        разделенных запятыми).

        .. code-block:: js

            var logo = document.body.querySelector('.logo');
            logo;
            // <img ...>



    .. js:function:: querySelectorAll(string selectors)

        Возвращает массив :js:class:`NodeList`,
        содержащий все элементы Element в  данном документе,
        соответствующие селекторам selectors
        (это может быть единственный CSS-селектор или группа селекторов,
        разделенных запятыми).

        .. warning::

            В отличие от объектов NodeList,
            возвращаемых методом getElementsByTagName() и аналогичными ему,
            объект NodeList, возвращаемый этим методом,
            является статическим и содержит элементы,
            соответствующие селекторам, существовавшие на момент вызова метода.


    .. js:function:: removeChild(node)

        Удаляет указанный узел :js:class:`Node` из узла


    .. js:function:: replaceChild(newNode, oldNode)

        Заменяет старый узел `oldNode` :js:class:`Node`,
        новым узлом `newNode` :js:class:`Node`
