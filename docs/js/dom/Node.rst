Node - узел дом дерева документа
================================

.. py:class:: Node()

    .. py:attribute:: ELEMENT_NODE

    .. py:attribute:: ATTRIBUTE_NODE

    .. py:attribute:: TEXT_NODE

    .. py:attribute:: CDATA_SECTION_NODE

    .. py:attribute:: ENTITY_REFERENCE_NODE

    .. py:attribute:: ENTITY_NODE

    .. py:attribute:: PROCESSING_INSTRUCTION_NODE

    .. py:attribute:: COMMENT_NODE

    .. py:attribute:: DOCUMENT_NODE

        Узел - документ

    .. py:attribute:: DOCUMENT_TYPE_NODE

    .. py:attribute:: DOCUMENT_FRAGMENT_NODE

    .. py:attribute:: NOTATION_NODE

    .. py:attribute:: attributes

        список атрибутов данного узла


    .. py:attribute:: baseURI
        
        Определяет базовый URL-адрес для данного объекта,
        который будет использоваться при разрешении относительных URL-адре­сов.

        Для всех узлов в HTML-документах этот URL-адрес определяется элементом <base>
        или свойством Document.URL,
        из значения которого исключается идентификатор фрагмента.


    .. py:attribute:: children

        Коллекция, дочерних элементов узла, без текстовых


    .. py:attribute:: childNodes

        Коллекция, :py:class:`NodeList`, дочерних узлов узла,
        включая текстовые.


    .. py:attribute:: firstChild

        Первый дочерний элемент :py:class:`Node` данного узла


    .. py:attribute:: lastChild

        Последний дочерний элемент :py:class:`Node` данного узла


    .. py:attribute:: nextSibling

        Возвращает соседний узел справа, :py:class:`Node`


    .. py:attribute:: nodeName

        имя узла


    .. py:attribute:: nodeType

        Тип узла в виде числа


    .. py:attribute:: nodeValue

        значение узла


    .. py:attribute:: ownerDocument

        Ссылка на корневой узел :py:class:`Document`

        
    .. py:attribute:: parentElement

        Возвращает родительский элемент, :py:class:`Element`


    .. py:attribute:: parentNode

        Возвращает родительский узел, :py:class:`Node`


    .. py:attribute:: previousSibling

        Возвращает соседний узел слева, :py:class:`Node`


    .. py:attribute:: textContent

        текстовое содержимое узла и его наследников
        

    .. py:method:: appendChild(node)

        Добавляет узел :py:class:`Node` узлу.

        Привязывает новый узел к дереву,
        ставя его последним в списке дочерних узлов данного узла


    .. py:method:: cloneNode(deep)

        Создает и возвращает копию узла :py:class:`Node`, для которого он вызван.


    .. py:method:: compareDocumentPosition(Node other)
        
        Срав­ни­ва­ет по­зи­цию дан­но­го уз­ла в до­ку­мен­те с по­зи­ци­ей уз­ла other и воз­вра­ща­ет чис­ло, би­ты ко­то­ро­го опи­сы­ва­ют от­но­ше­ния ме­ж­ду уз­ла­ми. Ес­ли срав­ни­вае­мые уз­лы яв­ля­ют­ся од­ним и тем же уз­лом, все би­ты в ре­зуль­та­те бу­дут сбро­ше­ны, т. е. ме­тод вер­нет 0. Ина­че в воз­вра­щае­мом зна­че­нии бу­дет ус­та­нов­лен один или бо­лее би­тов. 

        * `Node.DISCONNECTED` = 0x01, Два уз­ла при­над­ле­жат раз­ным до­ку­мен­том, по­это­му их по­зи­ции не мо­гут срав­ни­вать­ся.

        * `Node.PRECEDING` = 0x02, Узел other рас­по­ла­га­ет­ся пе­ред дан­ным уз­лом.

        * `Node.FOLLOWING` = 0x04, Узел other рас­по­ла­га­ет­ся по­сле дан­но­го уз­ла.
        
        * `Node.CONTAINS` = 0x08, Узел other со­дер­жит дан­ный узел. Ко­гда ус­та­нов­лен этот бит, все­гда бу­дет ус­та­нов­лен бит PRECEDING.
        
        * `Node.CONTAINED_BY` = 0x10, Узел other со­дер­жит­ся внут­ри дан­но­го уз­ла. Ко­гда ус­та­нов­лен этот бит, все­гда бу­дет ус­та­нов­лен бит FOLLOWING.


    .. py:method:: hasChildNodes()

        возвращает значение true , если узел имеет хотя бы один дочерний узел


    .. py:method:: insertBefore(newNode, refNode)

        Вставляет новый узел `newNode`, :py:class:`Node`,
        перед существующим узлом `refNode` :py:class:`Node`


    .. py:method:: isDefaultNamespace(string namespace)
        
        Воз­вра­ща­ет true, ес­ли URL-ад­рес про­стран­ст­ва имен namespace сов­па­да­ет с URL-ад­ре­сом про­стран­ст­ва имен по умол­ча­нию, ко­то­рый воз­вра­ща­ет вы­зов lookupName­spaceURI(null), и false – в про­тив­ном слу­чае.


    .. py:method:: isEqualNode(Node other)
        
        Воз­вра­ща­ет true, ес­ли дан­ный узел и узел other яв­ля­ют­ся иден­тич­ны­ми, т. е. име­ют один и тот же тип, имя те­га, ат­ри­бу­ты и (ре­кур­сив­но) до­чер­ние уз­лы. Воз­вра­ща­ет false, ес­ли два уз­ла не яв­ля­ют­ся эк­ви­ва­лент­ны­ми.


    .. py:method:: isSameNode(Node other)
        
        Воз­вра­ща­ет true, ес­ли дан­ный узел и узел other яв­ля­ют­ся од­ним и тем же уз­лом, и false – в про­тив­ном слу­чае. Вме­сто это­го ме­то­да мож­но так­же про­сто ис­поль­зо­вать опе­ра­тор ==.


    .. py:method:: lookupNamespaceURI(string prefix)
        
        Воз­вра­ща­ет URL-ад­рес про­стран­ст­ва имен, свя­зан­но­го с  ука­зан­ным пре­фик­сом про­стран­ст­ва имен prefix, или null, ес­ли та­кой пре­фикс не оп­ре­де­лен. Ес­ли ар­гу­мент prefix име­ет зна­че­ние null, воз­вра­ща­ет URL-ад­рес про­стран­ст­ва имен по умол­ча­нию.
    

    .. py:method:: lookupPrefix(string namespace)
        
        Воз­вра­ща­ет пре­фикс про­стран­ст­ва имен, свя­зан­но­го с  ука­зан­ным URL-ад­ре­сом про­стран­ст­ва имен, или null, ес­ли та­кое про­стран­ст­во имен не оп­ре­де­ле­но.


    .. py:method:: normalize()
        
        Нор­ма­ли­зу­ет все уз­лы, яв­ляю­щие­ся по­том­ка­ми дан­но­го, объ­еди­няя смеж­ные уз­лы и уда­ляя пус­тые. Обыч­но до­ку­мен­ты не име­ют пус­тых или смеж­ных тек­сто­вых уз­лов, но они мо­гут по­явить­ся в ре­зуль­та­те до­бав­ле­ния и уда­ле­ния уз­лов сце­на­ри­ем.


    .. py:method:: querySelector(selector:string)

        Возвращает первый элемент :py:class:`Element`,
        соответствующий CSS-селекторам selectors
        (это может быть единственный CSS-селектор или группа селекторов,
        разделенных запятыми).

        .. code-block:: js

            var logo = document.body.querySelector('.logo');
            logo;
            // <img ...>



    .. py:method:: querySelectorAll(string selectors)

        Возвращает массив :py:class:`NodeList`,
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


    .. py:method:: removeChild(node)

        Удаляет указанный узел :py:class:`Node` из узла


    .. py:method:: replaceChild(newNode, oldNode)

        Заменяет старый узел `oldNode` :py:class:`Node`,
        новым узлом `newNode` :py:class:`Node`




    .. py:attribute:: action

        `form`


    .. py:attribute:: checked

        `input`


    .. py:attribute:: cols

        `textarea`


    .. py:attribute:: currentStyle

        Текущие CSS стили для IE


    .. py:attribute:: data

        Текст узла


    .. py:attribute:: dataset

        Датасет

        .. code-block:: js

            <input ... data-val="1" data-val-msg="123" />

            var value = elem.dataset.val,
                message = elem.dataset.valMsg;


    .. py:attribute:: defaultChecked

        `input`


    .. py:attribute:: defaultselected

        `option`


    .. py:attribute:: defaultValue

        `input, textarea`


    .. py:attribute:: disabled

        `textarea, select, option`


    .. py:attribute:: elements

        `form`


    .. py:attribute:: enctype

        `form`


    .. py:attribute:: form

        ссылка на форму, в которой находится элемент

        `input, textarea, select, option`


    .. py:attribute:: index

        `option`


    .. py:attribute:: innerHTML

        HTML Содержание узла


    .. py:attribute:: label

        `option`


    .. py:attribute:: length

        `form, select`


    .. py:attribute:: maxLength

        `input`


    .. py:attribute:: method

        `form`


    .. py:attribute:: multiple

        `select`


    .. py:attribute:: name

        имя элемента управления

        `form, name, select`


    .. py:attribute:: onabort

        Обработчик, прерывание загрузки изображения

        `img`


    .. py:attribute:: onblur

        Обработчик, элемент теряет фокус

        `button, input, label, select, textarea, body`


    .. py:attribute:: onchange

        Обработчик, элемент потерял фокус и его значение с момента получения фокуса изменилось

        `input, select, textarea`


    .. py:attribute:: onclick

        Обработчик, нажата или отпущена клавиша мыши


    .. py:attribute:: oncontextmenu

        Отображается контекстоное меню


    .. py:attribute:: ondblclick

        Обработчик, двойной щелчок


    .. py:attribute:: ondrag

        бук­си­ров­ка про­дол­жа­ет­ся (воз­бу­ж­да­ет­ся в эле­мен­те-ис­точ­ни­ке)


    .. py:attribute:: ondragend

        бук­си­ров­ка за­вер­ше­на (воз­бу­ж­да­ет­ся в эле­мен­те-ис­точ­ни­ке)


    .. py:attribute:: ondragenter

        бук­си­руе­мые дан­ные ока­за­лись над эле­мен­том (воз­бу­ж­да­ет­ся в эле­мен­те-при­ем­ни­ке)


    .. py:attribute:: ondragleave

        бук­си­руе­мые дан­ные вы­шли за гра­ни­цы эле­мен­та (воз­бу­ж­да­ет­ся в эле­мен­те-при­ем­ни­ке)


    .. py:attribute:: ondragover

        бук­си­ров­ка про­дол­жа­ет­ся (воз­бу­ж­да­ет­ся в эле­мен­те-при­ем­ни­ке)


    .. py:attribute:: ondragstart

        поль­зо­ва­тель на­чал опе­ра­цию бук­си­ров­ки (воз­бу­ж­да­ет­ся в эле­мен­те-ис­точ­ни­ке)


    .. py:attribute:: ondrop

        поль­зо­ва­тель за­вер­шил бук­си­ров­ку (воз­бу­ж­да­ет­ся в эле­мен­те-при­ем­ни­ке)


    .. py:attribute:: onerror

        Обработчик, ошибка загрузки изображения

        `img`


    .. py:attribute:: onfocus

        Обработчик, элемент получил фокус

        `button, input, label, select, textarea, body`


    .. py:attribute:: oninput

        вы­пол­нен ввод в эле­мент фор­мы (воз­бу­ж ­да­ет­ся зна­чи­тель­но ча­ще, чем onchange)


    .. py:attribute:: onkeydown

        Обработчик, клавиши нажата

        `body, form etc`


    .. py:attribute:: onkeypress

        Обработчик, клавиши нажата или отпущена

        `body, form etc`


    .. py:attribute:: onkeyup

        Обработчик, клавиши отпущена

        `body, form etc`


    .. py:attribute:: onload

        Обработчик, загрузка завершена

        `body, frameset, img`


    .. py:attribute:: onmousedown

        Обработчик, нажата кнопка мыши


    .. py:attribute:: onmousemove

        Обработчик, перемещение указателя мыши


    .. py:attribute:: onmouseout

        Обработчик, указатель мыши выходит за границы элемента


    .. py:attribute:: onmouseover

        Обработчик, указаетль мыши входит в границы элемента


    .. py:attribute:: onmouseup

        Обработчик, отпущена кнопка мыши

    .. py:attribute:: onmousewheel

        поль­зо­ва­тель по­вер­нул ко­ле­си­ко мы­ши


    .. py:attribute:: onreset

        Обработчик, запрос на очистку полей формы

        `form`


    .. py:attribute:: onresize

        Обработчик, изменени размеры окна

        `body, frameset`


    .. py:attribute:: onscroll

        Прокрутка элемента


    .. py:attribute:: onselect

        Обработчик, выбор текста

        `input, textarea`


    .. py:attribute:: onsubmit

        Обработчик, запрос на передачу данных формы

        `form`


    .. py:attribute:: onunload

        Документ выгружен

        `body, frameset`


    .. py:attribute:: ownerDocument


    .. py:attribute:: options

        `select`


    .. py:attribute:: readOnly

        `textarea`


    .. py:attribute:: rows

        `textarea`


    .. py:attribute:: selected

        `option`


    .. py:attribute:: selectedIndex

        `select`


    .. py:attribute:: size

        `input, select`


    .. py:attribute:: style

        CSS стили узла


    .. py:attribute:: tabIndex

        `textarea, select`


    .. py:attribute:: target

        `form`


    .. py:attribute:: text

        `option`


    .. py:attribute:: type

        тип элемента управления

        `input, textarea, select`


    .. py:attribute:: value

        Значение элемента

        `input, textarea, select, option`


    .. py:attribute:: ELEMENT (1)

        Элемент


    .. py:attribute:: ATTRIBUTE (2)

        Атрибут элемента


    .. py:attribute:: TEXT (3)

        Текстовый узел


    .. py:attribute:: CDATASECTION (4)

        Раздел CDATA (его содержимое не будет обрабатываться парсером)


    .. py:attribute:: entityreference (5)

        Имя ссылки на сущность


    .. py:attribute:: entity (6)

        Сущность


    .. py:attribute:: processinginstruction (7)

        Процессуальная инструкция


    .. py:attribute:: COMMENT (8)

        Комментарии


    .. py:attribute:: DOCUMENT (9)

        Весь документ


    .. py:attribute:: DocumentType (10)

        Декларация типа документа


    .. py:attribute:: DocumentFragment (11)

        Часть документа


    .. py:attribute:: Notation (12)

        Имя нотации


    .. py:method:: add()

        `select`


    .. py:method:: addEventListener(event, handler, capture)

        Добавляем свой обработчик элементу.

        * event - имя события, строка

        * handler - функция обраотчик

        * capture - true-обработчик срабатывает на этапе перехвата, false-обработчик срабатывает на этапе всплывания

        Доступно на DOM lvl.2


    .. py:method:: attachEvent(event, handler)

        Аналог :js:func:`addEventListener`, для IE


    .. py:method:: blur()

        `input, textarea, select`


    .. py:method:: click()

        `input`


    .. py:method:: cloneNode(bool)

        Создать копию узла, аргумент - в доме или нет.


    .. py:method:: detachEvent(event, handler)

        Аналог :js:func:`removeEventListener`, для IE


    .. py:method:: focus()

        `input, textarea, select`


    .. py:method:: getComputedStyle(element, null)

        Возвращает вычисляемые CSS стили


    .. py:method:: remove()

        `select`


    .. py:method:: removeAttribute(attr)

        Удаляет атрибут из узла


    .. py:method:: removeEventListener(event, handler, capture)

        Удаляет обработчик из элемента, :js:func:`addEventListener`

        Доступно на DOM lvl.2


    .. py:method:: reset()

        `form`


    .. py:method:: select()

        `input, textarea`


    .. py:method:: setAttribute(attr, value)

        Устанавливает атрибут для узла



    .. py:method:: submit()

        `form`
