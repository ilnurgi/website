Element
=======

Элемент узла дом дерева

.. py:class:: Element()
.. py:class:: HTMLElement()

    Наследник :py:class:`Node`, :py:class:`EventTarget`

    `<abbr>`, `<acronym>`, `<address>`, `<b>`, `<bdo>`, `<big>`, `<center>`,
    `<cite>`, `<code>`, `<dd>`, `<dfn>`, `<dt>`, `<em>`, `<i>`, `<kbd>`,
    `<noframes>`, `<noscript>`, `<s>`, `<samp>`, `<small>`, `<span>`,
    `<strike>`, `<strong>`, `<sub>`, `<sup>`, `<tt>`, `<u>`, `<var>`


    .. py:attribute:: Attributes

        Возвращает :py:class:`NamedNodeMap` список атрибутов элемента


    .. py:attribute:: attributes

        Возвращает массив атрибутов :py:class:`Attr` элемента


    .. py:attribute:: childElementCount
        
        Ко­ли­че­ст­во до­чер­них эле­мен­тов (не до­чер­них уз­лов), ко­то­рые име­ет дан­ный эле­мент.


    .. py:attribute:: children
        
        Объ­ект, по­доб­ный мас­си­ву, со­дер­жа­щий до­чер­ние эле­мен­ты (ис­клю­чая до­чер­ние уз­лы, не яв­ляю­щие­ся эле­мен­та­ми Element, та­кие как Text и Comment).


    .. py:attribute:: classList

        Ссылка на :py:class:`DOMTokenList`, объект для работы с классами объекта

        .. code-block:: js

            element.classList.add("show");
            element.classList.remove("show");
            element.classList.toggle("show");
            element.classList.contains("show");


    .. py:attribute:: className

        Это свой­ст­во пред­став­ля­ет ат­ри­бут class эле­мен­та.


    .. py:attribute:: clientHeight

        Внутренняя высота элемента


    .. py:attribute:: clientLeft

        Ширина левой границы элемента


    .. py:attribute:: clientTop

        Ширина верхней границы элемента


    .. py:attribute:: clientWidth

        Внутреннняя ширина элемента


    .. py:attribute:: currentStyle
    
        Это свой­ст­во :py:class:`CSSStyleDeclaration`,
        реа­ли­зо­ван­ное толь­ко в IE,
        яв­ля­ет­ся пред­став­ле­ни­ем кас­кад­но­го на­бо­ра всех CSS-свойств,
        при­ме­няе­мых к эле­мен­ту.

        В IE вер­сии 8 и ни­же его мож­но ис­поль­зо­вать как за­ме­ну стан­дарт­но­му
         ме­то­ду :py:meth:`Window.getComputedStyle`.


    .. py:attribute:: dataset
        
        С лю­бым HTML-эле­мен­том мож­но свя­зать лю­бые зна­че­ния,
        при­сваи­вая их ат­ри­бу­там, име­на ко­то­рых на­чи­на­ют­ся с  пре­фик­са «data-».

        Дан­ное свой­ст­во dataset пред­став­ля­ет мно­же­ст­во ат­ри­бу­тов с дан­ны­ми и
        уп­ро­ща­ет ра­бо­ту с ни­ми.

        Зна­че­ние это­го свой­ст­ва ве­дет се­бя как обыч­ный объ­ект.

        Ка­ж­дое свой­ст­во объ­ек­та со­от­вет­ст­ву­ет од­но­му ат­ри­бу­ту с дан­ны­ми.

        Ес­ли эле­мент име­ет ат­ри­бут с име­нем data-x,
        объ­ект dataset по­лу­чит свой­ст­во с име­нем x, и
        dataset.x бу­дет воз­вра­щать то же зна­че­ние,
        что и вы­зов getAttribute("data-x").

        Опе­ра­ции чте­ния и при­сваи­ва­ния зна­че­ний свой­ст­вам объ­ек­та dataset
        бу­дут чи­тать и при­сваи­вать зна­че­ния со­от­вет­ст­вую­щим ат­ри­бу­там с
        дан­ны­ми это­го эле­мен­та.

        Опе­ра­тор delete мож­но ис­поль­зо­вать для уда­ле­ния ат­ри­бу­тов с дан­ны­ми,
        а цикл for/in – для их пе­ре­чис­ле­ния.


    .. py:attribute:: firstElementChild
        
        Это свой­ст­во по­доб­но свой­ст­ву :py:attr:`Node.firstChild`,
        но оно иг­но­ри­ру­ет уз­лы Text и Comment и воз­вра­ща­ет толь­ко эле­мен­ты ти­па
        :py:class:`Element`.


    .. py:attribute:: id

        Идентификатор элемента


    .. py:attribute:: innerHTML

        Содержимое элемента

        .. code-block:: js

            Element.innerHTML = '<div>Потомок</div>'


    .. py:attribute:: isContentEditable
        
        Это свой­ст­во име­ет зна­че­ние true,
        ес­ли эле­мент дос­ту­пен для ре­дак­ти­ро­ва­ния,
        и false – в про­тив­ном слу­чае.

        Эле­мент мо­жет быть дос­ту­пен для ре­дак­ти­ро­ва­ния
        вслед­ст­вие ус­та­нов­ки свой­ст­ва contenteditable в нем или в его ро­ди­те­ле,
        или вслед­ст­вие ус­та­нов­ки свой­ст­ва designMode вме­щаю­ще­го объ­ек­та Document.


    .. py:attribute:: lang
        
        Зна­че­ние ат­ри­бу­та lang, оп­ре­де­ляю­щее код язы­ка для со­дер­жи­мо­го эле­мен­та.


    .. py:attribute:: lastElementChild

        Это свой­ст­во по­доб­но свой­ст­ву :py:attr:`Node.lastChild`,
        но оно иг­но­ри­ру­ет уз­лы Text и Comment и воз­вра­ща­ет толь­ко эле­мен­ты ти­па
        :py:class:`Element`.


    .. py:attribute:: localName
        
        Ло­каль­ное имя дан­но­го эле­мен­та без пре­фик­са.

        Зна­че­ние это­го свой­ст­ва от­ли­ча­ет­ ся от зна­че­ния ат­ри­бу­та tagName,
        ко­то­рое мо­жет вклю­чать пре­фикс про­стран­ст­ва имен,
        ес­ли та­ко­вой име­ет­ся
        (и все сим­во­лы ко­то­ро­го для HTML-эле­мен­тов пре­об­ра­зу­ют­ся в
        верх­ний ре­гистр).


    .. py:attribute:: name

        Значение атрибута `name`


    .. py:attribute:: readonly string namespaceURI
        
        URL-ад­рес, фор­маль­но оп­ре­де­ляю­щий про­стран­ст­во имен дан­но­го эле­мен­та.

        Мо­жет иметь зна­че­ние null или со­дер­жать стро­ку,
        та­кую как «http://www.w3.org/1999/xhtml».


    .. py:attribute:: nextElementSibling
        
        Это свой­ст­во по­доб­но свой­ст­ву :py:attr:`Node.nextSibling`,
        но оно иг­но­ри­ру­ет уз­лы Text и Comment и воз­вра­ща­ет толь­ко эле­мен­ты ти­па :py:class:`Element`.


    .. py:attribute:: offsetHeight

        Высота элемента в скомпонованной странице


    .. py:attribute:: offsetLeft
        
        Расстояние от левой границы элемента до левой границы элемента offsetParent

        
    .. py:attribute:: offsetParent
        
        Элемент , от которого ведутся расчеты сдвига текущего элемента

        
    .. py:attribute:: offsetTop
        
        Расстояние от верхней границы элемента до верхней границы элемента offsetParent

        
    .. py:attribute:: offsetWidth
        
        Ширина элемента в скомпонованной странице

    .. py:attribute:: outerHTML
        
        Раз­мет­ка HTML или XML, оп­ре­де­ляю­щая дан­ный эле­мент и его со­дер­жи­мое. Ес­ли при­сво­ить это­му свой­ст­ву стро­ку, она за­ме­нит дан­ный эле­мент (и все его со­дер­жи­мое) ре­зуль­та­том син­так­си­че­ско­го раз­бо­ра но­во­го зна­че­ния как фраг­мен­та HTML- или XML-до­ку­мен­та.


    .. py:attribute:: prefix
        
        Пре­фикс про­стран­ст­ва имен для дан­но­го эле­мен­та. Обыч­но это свой­ст­во со­дер­жит зна­че­ние null. Ис­клю­че­ние со­став­ля­ют XML-до­ку­мен­ты, в ко­то­рых ис­поль­зу­ют­ся про­стран­ст­ва имен.


    .. py:attribute:: previousElementSibling
        
        Это свой­ст­во по­доб­но свой­ст­ву :py:attr:`Node.previousSibling, но оно иг­но­ри­ру­ет уз­лы Text и Comment и воз­вра­ща­ет толь­ко эле­мен­ты ти­па :py:class:`Element`.


    .. py:attribute:: scrollHeight
        
        Видимая высота прокручиваемого элемента

        
    .. py:attribute:: scrollLeft
        
        Возвращает или устанавливает размер прокрутки в окне влево для элемента

        
    .. py:attribute:: scrollTop
        
        Возвращает или устанавливает размер прокрутки в окне вниз для элемента

        
    .. py:attribute:: scrollWidth
        
        Видимая ширина прокручиваемого элемента


    .. py:attribute:: style
        
        :py:class:`CSSStyleDeclaration` CSS-сти­ли для эле­мен­та.


    .. py:attribute:: tagName

        Возвращает имя элемента

    .. py:attribute:: title
        
        Зна­че­ние ат­ри­бу­та title эле­мен­та. Мно­гие бро­узе­ры ото­бра­жа­ют зна­че­ние это­го ат­ри­бу­та в ви­де всплы­ваю­щей под­сказ­ки при на­ве­де­нии ука­за­те­ля мы­ши на эле­мент.


        
    .. py:function:: addEventListener()

        Задает обработчик некоторого события для элемента

        .. code-block:: js

            button.addEventListener('click', function(evt){});


    .. py:function:: Blur()
    .. py:function:: blur()

        Переносит фокус с текущего элемента


    .. py:function:: click()

        Симулирует щелчок по текущему элементу


    .. py:function:: dispatchEvent(event)

        Передает событие, связанное с этим элементом, в DOM


    .. py:function:: focus()

        Переносит фокус на текущий элемент

        .. code-block:: js

            login = document.querySelector("[name=login]");
            login.focus();


    .. py:function:: getAttribute(attrName)

        Возвращает значение атрибута


    .. py:function:: getAttributeNS(namespace, localName)

        Этот ме­тод дей­ст­ву­ет так же, как ме­тод :py:meth:`getAttribute`,
        кро­ме то­го, что ат­ри­бут зада­ет­ся ком­би­на­ци­ей URI про­стран­ст­ва имен и
        ло­каль­но­го име­ни, оп­ре­де­лен­но­го в дан­ном про­стран­ст­ве имен.


    .. py:function:: getBoundingClientRect()

        Возвращает :py:class:`ClientRect`, опи­сы­ваю­щий пря­мо­уголь­ник, ог­ра­ни­чи­ваю­щий дан­ный эле­мент.

        
    .. py:function:: getClientRects()
        
        Воз­вра­ща­ет объ­ект, по­доб­ный мас­си­ву, со­дер­жа­щий объ­ек­ты :py:class:`ClientRects`, ко­то­рые опи­сы­ва­ют один или бо­лее пря­мо­уголь­ни­ков, ог­ра­ни­чи­ваю­щих дан­ный эле­мент.


    .. py:function:: getElementsByClassName(elementClassName)

        Возвращает список :py:class:`NodeList` элементов с указанным классом


    .. py:function:: getElementsByTagName(tagName)

        Возвращает список :py:class:`NodeList` элементов с указанным тегом


    .. py:function:: getElementsByTagNameNS(namespace, localName)

        Этот ме­тод дей­ст­ву­ет по­доб­но ме­то­ду :js:func:`getElementsByTagName()`, за ис­клю­че­ни­ем то­го, что имя те­га тре­буе­мых эле­мен­тов ука­зы­ва­ет­ся как ком­би­на­ция URI про­стран­ст­ва имен и ло­каль­но­го име­ни в этом про­стран­ст­ве имен.


    .. py:function:: hasAttribute(name)

        Проверяет, есть ли у элемента атрибут


    .. py:function:: hasAttributeNS(namespace, localName)

        Этот ме­тод дей­ст­ву­ет так же, как ме­тод :js:func:`hasAttribute()`, за ис­клю­че­ни­ем то­го, что ат­ри­бут за­да­ет­ся ком­би­на­ци­ей URI про­стран­ст­ва имен и ло­каль­но­го име­ни в этом про­стран­ст­ве имен.


    .. py:function:: hasAttributes()

        Проверяет, есть ли у элемента атрибуты

    
    .. py:function:: insertAdjacentHTML(string position, string text)
        
        Встав­ля­ет раз­мет­ку HTML text в по­зи­цию position от­но­си­тель­но дан­но­го эле­мен­ та. 

        * `position` -

            * `beforebegin` - Встав­ля­ет текст пе­ред от­кры­ваю­щим те­гом эле­мен­та
            * `afterend` - Встав­ля­ет текст по­сле за­кры­ваю­ще­го те­га эле­мен­та
            * `afterbegin` - Встав­ля­ет текст сра­зу по­сле от­кры­ваю­ще­го те­га эле­мен­та
            * `beforeend` - Встав­ля­ет текст не­по­сред­ст­вен­но пе­ред за­кры­ваю­щим те­гом эле­мен­та


    .. py:function:: querySelector(string selectors)

        Метод поиска элементов.

        Возвращает элемент DOM дерева :py:class:`Element`,
        соответствующий CSS-селекторам selectors
        (это может быть единственный CSS-селектор или
        группа селекторов, разделенных запятыми).

        .. code-block:: js

            document.querySelector(".user-block")


    .. py:function:: querySelectorAll(string selectors)

        Метод поиска элементов.

        Возвращает объект :py:class:`NodeList`,
        содержащий все элементы, вложенные в  данный элемент,
        которые соответствуют селекторам selectors
        (это может быть единственный CSS-селектор
        или группа селекторов, разделенных запятыми).

        .. code-block:: js

            document.querySelectorAll("nav li")


    .. py:function:: removeAttribute(attrName)

        Удаляет указанный атрибут


    .. py:function:: removeAttributeNS(string namespace, string localName)
        
        Ме­тод дей­ст­ву­ет так же, как ме­тод :js:func:`removeAttribute()`, за ис­клю­че­ни­ем то­го, что уда­ляе­мый ат­ри­бут за­да­ет­ся URI про­стран­ст­ва имен и ло­каль­но­го име­ни.


    .. py:function:: removeAttributeNode()

        Удаляет указанный атрибутный узел

        
    .. py:function:: removeEventListener()

        Удаляет обработчик события для данного элемента

        .. code-block:: js

            button.removeEventListener('click', my_function)


    .. py:function:: scrollIntoView([boolean top])
    
        Ес­ли HTML-эле­мент в на­стоя­щий мо­мент на­хо­дит­ся за пре­де­ла­ми ок­на, этот ме­тод про­кру­тит до­ку­мент так, что эле­мент ока­жет­ся в пре­де­лах ок­на. Ар­гу­мент top яв­ ля­ет­ся не­обя­за­тель­ным и под­ска­зы­ва­ет ме­то­ду, дол­жен ли эле­мент ока­зать­ся бли­ же к верх­не­му или к ниж­не­му краю ок­на. Ес­ли он ра­вен true или от­сут­ст­ву­ет, бро­узер ста­ра­ет­ся вы­пол­нить про­крут­ку так, что­бы эле­мент ока­зал­ся бли­же к верх­не­му краю ок­на. Ес­ли он ра­вен false, бро­узер ста­ра­ет­ся вы­пол­нить про­крут­ку так, что­бы эле­мент ока­зал­ся бли­же к ниж­не­му краю ок­на. Для эле­мен­тов, при­ни­маю­щих фо­кус вво­да, та­ких как эле­мен­ты Input, ме­тод focus() не­яв­но вы­пол­ня­ет точ­но та­кую же опе­ра­цию про­крут­ки. 


    .. py:function:: setAttribute(string qualifiedName, string value)
        
        При­сваи­ва­ет ука­зан­ное зна­че­ние ат­ри­бу­ту с  ука­зан­ным име­нем. Ес­ли ат­ри­бут с та­ким име­нем еще не су­ще­ст­ву­ет, в эле­мент до­бав­ля­ет­ся но­вый ат­ри­бут. В HTML-до­ку­мен­тах пе­ред при­сваи­ва­ни­ем зна­че­ния сим­во­лы в име­ни ат­ри­бу­та пре­об­ра­зу­ют­ся в ниж­ний ре­гистр. Об­ра­ти­те вни­ма­ние: в HTML-до­ку­мен­те Ja­va­Script-свой­ст­ва, со­от­вет­ст­вую­щие всем стан­дарт­ным HTML-ат­ри­бу­там, оп­ре­де­ля­ют­ся объ­ек­та­ми HTMLElement. По­это­му дан­ный ме­тод обыч­но ис­поль­зу­ет­ся лишь для дос­ту­па к не­стан­дарт­ным ат­ри­бу­там.


    .. py:function:: setAttributeNS(string namespace, string qualifiedName, string value)
        
        Этот ме­тод дей­ст­ву­ет так же, как ме­тод :js:func:`setAttribute()`, за ис­клю­че­ни­ем то­го, что имя ат­ри­бу­та ука­зы­ва­ет­ся как ком­би­на­ция URI про­стран­ст­ва имен и ква­ли­фи­ци­ро­ван­но­го име­ни, со­стоя­ще­го из пре­фик­са про­стран­ст­ва имен, двое­то­чия и  ло­каль­но­го име­ни в этом про­стран­ст­ве имен.


HTMLAnchorElement
-----------------

Элемент `<a>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLAnchorElement

    .. py:attribute:: href

    .. py:attribute:: target

    .. py:attribute:: ping

    .. py:attribute:: rel

    .. py:attribute:: media

    .. py:attribute:: hreflang

    .. py:attribute:: type


HTMLAppletElement
-----------------

Элемент `<applet>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLAppletElement


HTMLAreaElement
---------------

Элемент `<area>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLAreaElement

    .. py:attribute:: alt

    .. py:attribute:: coords

    .. py:attribute:: shape

    .. py:attribute:: href

    .. py:attribute:: target

    .. py:attribute:: ping

    .. py:attribute:: rel

    .. py:attribute:: media

    .. py:attribute:: hreflang

    .. py:attribute:: type


HTMLBaseElement
---------------

Элемент `<base>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLBaseElement

    .. py::attribute:: href

    .. py::attribute:: target


HTMLBaseFontElement
-------------------

Элемент `<basefont>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLBaseFontElement


HTMLBodyElement
---------------

Элемент `<blockquote>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLBodyElement

    .. py:attribute:: onafterprint

    .. py:attribute:: onbeforeprint

    .. py:attribute:: onbeforeunload

    .. py:attribute:: onblur

    .. py:attribute:: onerror

    .. py:attribute:: onfocus

    .. py:attribute:: onhash­

    .. py:attribute:: change

    .. py:attribute:: onload

    .. py:attribute:: onmessage

    .. py:attribute:: onoffline

    .. py:attribute:: ononline

    .. py:attribute:: onpagehide

    .. py:attribute:: onpage­show

    .. py:attribute:: onpopstate

    .. py:attribute:: onredo

    .. py:attribute:: onresize

    .. py:attribute:: onscroll

    .. py:attribute:: onstorage

    .. py:attribute:: onundo

    .. py:attribute:: onunload


HTMLButtonElement
-----------------

Элемент `<button>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLButtonElement

    .. py:attribute:: autofocus

    .. py:attribute:: disabled

    .. py:attribute:: form

    .. py:attribute:: formaction

    .. py:attribute:: formenctype

    .. py:attribute:: formmethod

    .. py:attribute:: form­nova­

    .. py:attribute:: lidate

    .. py:attribute:: formtarget

    .. py:attribute:: name

    .. py:attribute:: type

    .. py:attribute:: value


HTMLBRElement
-------------

Элемент `<br>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLBRElement


HTMLDListElement
----------------

Элемент `<dl>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLDListElement


HTMLDirectoryElement
--------------------

Элемент `<dir>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLDirectoryElement


HTMLDivElement
--------------

Элемент `<div>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLDivElement


HTMLFieldSetElement
-------------------

Элемент `<fieldset>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLFieldSetElement

    .. py:attribute:: disabled
    
    .. py:attribute:: form
    
    .. py:attribute:: name


HTMLFontElement
---------------

Элемент `<font>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLFontElement


HTMLFormElement
---------------

Элемент `<from>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLFormElement

    .. py:attribute:: accept-charset

    .. py:attribute:: action

    .. py:attribute:: autocomplete
    
    .. py:attribute:: elements
    
    .. py:attribute:: enctype
    
    .. py:attribute:: method
    
    .. py:attribute:: name
    
    .. py:attribute:: novalidate
    
    .. py:attribute:: target

    .. py:attribute:: length

    .. py:function:: submit()

    .. py:function:: reset()

HTMLFrameElement
----------------

Элемент `<frame>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLFrameElement


HTMLFrameSetElement
-------------------

Элемент `<frameset>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLFrameSetElement


HTMLHeadElement
---------------

Элемент `<head>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLHeadElement


HTMLHeadingElement
------------------

Элемент `<h1> ... <h6>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLHeadingElement


HTMLHtmlElement
---------------

Элемент `<html>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLHtmlElement

    .. py:attribute:: manifest


HTMLHRElement
-------------

Элемент `<hr>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLHRElement


HTMLImageElement
----------------

Элемент `<image>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLImageElement

    .. py:attribute:: alt
    
    .. py:attribute:: src
    
    .. py:attribute:: usemap
    
    .. py:attribute:: ismap
    
    .. py:attribute:: width
    
    .. py:attribute:: height


HTMLInputElement
----------------

Элемент `<input>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLInputElement

    .. py:attribute:: accept

    .. py:attribute:: alt

    .. py:attribute:: autocomplete

    .. py:attribute:: autofocus

    .. py:attribute:: checked

    .. py:attribute:: defaultChecked
    
    .. py:attribute:: defaultValue

    .. py:attribute:: dirname

    .. py:attribute:: disabled

    .. py:attribute:: form

    .. py:attribute:: form­

    .. py:attribute:: ac­tion

    .. py:attribute:: formenctype

    .. py:attribute:: formmethod

    .. py:attribute:: formnovalidate

    .. py:attribute:: formtarget

    .. py:attribute:: height

    .. py:attribute:: list

    .. py:attribute:: max

    .. py:attribute:: maxlength

    .. py:attribute:: min

    .. py:attribute:: multiple

    .. py:attribute:: name

    .. py:attribute:: pattern

    .. py:attribute:: placeholder

    .. py:attribute:: readonly

    .. py:attribute:: required

    .. py:attribute:: size

    .. py:attribute:: src

    .. py:attribute:: step

    .. py:attribute:: type

    .. py:attribute:: value

    .. py:attribute:: width

    .. py:function:: blur()

    .. py:function:: click()

    .. py:function:: focus()

    .. py:function:: select()


HTMLIsIndexElement
------------------

Элемент `<isindex>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLIsIndexElement


HTMLIFrameElement
-----------------

Элемент `<iframe>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLIFrameElement

    .. py:attribute:: src
    
    .. py:attribute:: srcdoc
    
    .. py:attribute:: name
    
    .. py:attribute:: sandbox
    
    .. py:attribute:: seamless
    
    .. py:attribute:: width
    
    .. py:attribute:: height


HTMLLabelElement
----------------

Элемент `<label>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLLabelElement

    .. py:attribute:: form
    
    .. py:attribute:: for


HTMLLegendElement
-----------------

Элемент `<legend>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLLegendElement


HTMLLinkElement
---------------

Элемент `<li>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLLinkElement

    .. py:attribute:: href

    .. py:attribute:: rel

    .. py:attribute:: media

    .. py:attribute:: hreflang

    .. py:attribute:: type

    .. py:attribute:: sizes


HTMLLIElement
-------------

Элемент `<li>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLLIElement

    .. py:attribute:: value


HTMLMapElement
--------------

Элемент `<map>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLMapElement

    .. py:attribute:: map


HTMLMenuElement
---------------

Элемент `<menu>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLMenuElement

    .. py:attribute:: type

    .. py:attribute:: label


HTMLMetaElement
---------------

Элемент `<meta>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLMetaElement

    .. py:attribute:: name
    
    .. py:attribute:: http-equiv
    
    .. py:attribute:: content
    
    .. py:attribute:: charset


HTMLModElement
--------------

Элемент `<del>`, `<ins>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLModElement

    .. py:attribute:: cite

    .. py:attribute:: datetime


HTMLObjectElement
-----------------

Элемент `<object>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLObjectElement

    .. py:attribute:: data
    
    .. py:attribute:: type
    
    .. py:attribute:: name
    
    .. py:attribute:: usemap
    
    .. py:attribute:: form
    
    .. py:attribute:: width
    
    .. py:attribute:: height


HTMLOptGroupElement
-------------------

Элемент `<optgroup>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLOptGroupElement

    .. py:attribute:: disabled

    .. py:attribute:: label


HTMLOptionElement
-----------------

Элемент `<option>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLOptionElement

    .. code-block:: js

        var o = new Option(text, value, defaultSelected, selected);

    .. py:attribute:: form

    .. py:attribute:: defaultSelected

    .. py:attribute:: disabled
    
    .. py:attribute:: index

    .. py:attribute:: label
    
    .. py:attribute:: selected

    .. py:attribute:: text

    .. py:attribute:: value


HTMLOListElement
----------------

Элемент `<ol>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLOListElement

    .. py:attribute:: reversed

    .. py:attribute:: start


HTMLParagraphElement
--------------------

Элемент `<p>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLParagraphElement

    .. py:attribute:: cite


HTMLParamElement
----------------

Элемент `<param>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLParamElement

    .. py:attribute:: name
    
    .. py:attribute:: value


HTMLPreElement
--------------

Элемент `<pre>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLPreElement


HTMLQuoteElement
----------------

Элемент `<q>`, `<blockquote>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLQuoteElement

    .. py:attribute:: cite


HTMLScriptElement
-----------------

Элемент `<script>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLScriptElement

    .. py:attribute:: src
    
    .. py:attribute:: async
    
    .. py:attribute:: defer
    
    .. py:attribute:: type
    
    .. py:attribute:: charset


HTMLSelectElement
-----------------

Элемент `<select>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLSelectElement

    .. py:attribute:: autofocus

    .. py:attribute:: disabled

    .. py:attribute:: form

    .. py:attribute:: length

    .. py:attribute:: multiple

    .. py:attribute:: name

    .. py:attribute:: options

    .. py:attribute:: required

    .. py:attribute:: selectedIndex

    .. py:attribute:: size

    .. py:attribute:: tabIndex

    .. py:attribute:: type

    .. py:attribute:: value

    .. py:function:: add()

    .. py:function:: blur()

    .. py:function:: focus()

    .. py:function:: remove()


HTMLStyleElement
----------------

Элемент `<select>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLStyleElement

    .. py:attribute:: media
    
    .. py:attribute:: type
    
    .. py:attribute:: scoped


HTMLTableCaptionElement
-----------------------

Элемент `<caption>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLTableCaptionElement


HTMLTableCellElement
--------------------

Элемент `<td>`, `<th>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLTableCellElement

    .. py:attribute:: align

    .. py:attribute:: cellIndex

    .. py:attribute:: colspan
    
    .. py:attribute:: rowspan
    
    .. py:attribute:: headers

    .. py:attribute:: height

    .. py:attribute:: innerHTML

    .. py:attribute:: textContent

    .. py:attribute:: vAlign

    .. py:attribute:: width


HTMLTableColElement
-------------------

Элемент `<col>`, `<colgroup>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLTableColElement

    .. py:attribute:: span


HTMLTableElement
----------------

Элемент `<table>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLTableElement

    .. py:attribute:: border

    .. py:attribute:: caption

    .. py:attribute:: cellPadding

    .. py:attribute:: cellSpacing

    .. py:attribute:: rows[]

    .. py:attribute:: summary

    .. py:attribute:: tBodies[]

    .. py:attribute:: tFoot

    .. py:attribute:: tHead

    .. py:attribute:: width

    .. py:function:: createCaption()

    .. py:function:: createTFoot()

    .. py:function:: createTHead()

    .. py:function:: deleteCaption()

    .. py:function:: deleteTFoot()

    .. py:function:: deleteTHead()

    .. py:function:: deleteRow(index)

    .. py:function:: insertRow(index)


HTMLTableRowElement
-------------------

Элемент `<tr>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLTableRowElement

    .. py:attribute:: bgColor

    .. py:attribute:: cells

    .. py:attribute:: rowIndex

    .. py:attribute:: sectionRowIndex

    .. py:attribute:: vAlign

    .. py:function:: deleteCell(index)

    .. py:function:: insertCell(index)
    

HTMLTableSectionElement
-----------------------

Элемент `<tbody>`, `<tfoot>`, `<thead>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLTableSectionElement

    .. py:attribute:: align

    .. py:attribute:: rows

    .. py:attribute:: vAlign

    .. py:function:: deleteRow(index)

    .. py:function:: insertRow(index)


HTMLTextAreaElement
-------------------

Элемент `<textarea>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLTextAreaElement

    .. py:attribute:: autofocus
    
    .. py:attribute:: cols
    
    .. py:attribute:: defaultValue

    .. py:attribute:: disabled
    
    .. py:attribute:: form
    
    .. py:attribute:: maxlength
    
    .. py:attribute:: name
    
    .. py:attribute:: placeholder
    
    .. py:attribute:: readonly
    
    .. py:attribute:: requi­r­ed
    
    .. py:attribute:: rows
    
    .. py:attribute:: tabIndex

    .. py:attribute:: type

    .. py:attribute:: value

    .. py:attribute:: wrap

    .. py:function:: blur()

    .. py:function:: focus()

    .. py:function:: select()


HTMLTitleElement
----------------

Элемент `<title>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLTitleElement


HTMLUListElement
----------------

Элемент `<ul>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLUListElement


============ ========
Эле­мент      Ат­ри­бу­ты
============ ========
<audio>      src, preload, autoplay, loop, controls
<canvas>     width, height
<command>    type, label, icon, disabled, checked, radiogroup
<details>    open
<embed>      src, type, width, height
<keygen>     autofocus, challenge, disabled, form, keytype, name
<meter>      value, min, max, low, high, optimum, form
<output>     for, form, name
<progress>   value, max, form
<source>     src, type, media
<time>       datetime, pubdate
<track>      default, kind, label, src, srclang
<video>      src, poster, preload, autoplay, loop, controls, width, height
============ ========