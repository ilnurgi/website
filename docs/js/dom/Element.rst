Element - элемент узла дом дерева
=================================

.. js:class:: Element()
.. js:class:: HTMLElement()

    Наследник :js:class:`Node`, :js:class:`EventTarget`

    `<abbr>`, `<acronym>`, `<address>`, `<b>`, `<bdo>`, `<big>`, `<center>`, `<cite>`, `<code>`, `<dd>`, `<dfn>`, `<dt>`, `<em>`, `<i>`, `<kbd>`, `<noframes>`, `<noscript>`, `<s>`, `<samp>`, `<small>`, `<span>`, `<strike>`, `<strong>`, `<sub>`, `<sup>`, `<tt>`, `<u>`, `<var>`


    .. js:attribute:: Attributes

        Возвращает :js:class:`NamedNodeMap` список атрибутов элемента


    .. js:attribute:: attributes

        Возвращает массив атрибутов :js:class:`Attr` элемента


    .. js:attribute:: childElementCount
        
        Ко­ли­че­ст­во до­чер­них эле­мен­тов (не до­чер­них уз­лов), ко­то­рые име­ет дан­ный эле­мент.


    .. js:attribute:: children
        
        Объ­ект, по­доб­ный мас­си­ву, со­дер­жа­щий до­чер­ние эле­мен­ты (ис­клю­чая до­чер­ние уз­лы, не яв­ляю­щие­ся эле­мен­та­ми Element, та­кие как Text и Comment).


    .. js:attribute:: classList

        Ссылка на :js:class:`DOMTokenList`, множество лексем в виде строки


    .. js:attribute:: className

        Это свой­ст­во пред­став­ля­ет ат­ри­бут class эле­мен­та.


    .. js:attribute:: clientHeight

        Внутренняя высота элемента


    .. js:attribute:: clientLeft

        Ширина левой границы элемента


    .. js:attribute:: clientTop

        Ширина верхней границы элемента


    .. js:attribute:: clientWidth

        Внутреннняя ширина элемента


    .. js:attribute:: currentStyle
    
        Это свой­ст­во :js:class:`CSSStyleDeclaration`, реа­ли­зо­ван­ное толь­ко в IE, яв­ля­ет­ся пред­став­ле­ни­ем кас­кад­но­го на­бо­ра всех CSS-свойств, при­ме­няе­мых к эле­мен­ту. В IE вер­сии 8 и ни­же его мож­но ис­поль­зо­вать как за­ме­ну стан­дарт­но­му ме­то­ду Window.getComputedStyle().

    .. js:attribute:: dataset
        
        С лю­бым HTML-эле­мен­том мож­но свя­зать лю­бые зна­че­ния, при­сваи­вая их ат­ри­бу­там, име­на ко­то­рых на­чи­на­ют­ся с  пре­фик­са «data-». Дан­ное свой­ст­во dataset пред­став­ля­ет мно­же­ст­во ат­ри­бу­тов с дан­ны­ми и уп­ро­ща­ет ра­бо­ту с ни­ми.

        Зна­че­ние это­го свой­ст­ва ве­дет се­бя как обыч­ный объ­ект. Ка­ж­дое свой­ст­во объ­ек­та со­от­вет­ст­ву­ет од­но­му ат­ри­бу­ту с дан­ны­ми. Ес­ли эле­мент име­ет ат­ри­бут с име­нем data-x, объ­ект dataset по­лу­чит свой­ст­во с име­нем x, и dataset.x бу­дет воз­вра­щать то же зна­че­ние, что и вы­зов getAttribute("data-x").

        Опе­ра­ции чте­ния и при­сваи­ва­ния зна­че­ний свой­ст­вам объ­ек­та dataset бу­дут чи­тать и  при­сваи­вать зна­че­ния со­от­вет­ст­вую­щим ат­ри­бу­там с  дан­ны­ми это­го эле­мен­та. Опе­ра­тор delete мож­но ис­поль­зо­вать для уда­ле­ния ат­ри­бу­тов с дан­ны­ми, а цикл for/in – для их пе­ре­чис­ле­ния.

    .. js:attribute:: firstElementChild
        
        Это свой­ст­во по­доб­но свой­ст­ву :js:attr:`Node.firstChild`, но оно иг­но­ри­ру­ет уз­лы Text и Comment и воз­вра­ща­ет толь­ко эле­мен­ты ти­па :js:class:`Element`.


    .. js:attribute:: id

        Идентификатор элемента


    .. js:attribute:: innerHTML

        Содержимое элемента

        .. code-block:: js

            Element.innerHTML = '<div>Потомок</div>'


    .. js:attribute:: isContentEditable
        
        Это свой­ст­во име­ет зна­че­ние true, ес­ли эле­мент дос­ту­пен для ре­дак­ти­ро­ва­ния, и false – в про­тив­ном слу­чае. Эле­мент мо­жет быть дос­ту­пен для ре­дак­ти­ро­ва­ния вслед­ст­вие ус­та­нов­ки свой­ст­ва contenteditable в нем или в его ро­ди­те­ле, или вслед­ст­вие ус­та­нов­ки свой­ст­ва designMode вме­щаю­ще­го объ­ек­та Document.


    .. js:attribute:: lang
        
        Зна­че­ние ат­ри­бу­та lang, оп­ре­де­ляю­щее код язы­ка для со­дер­жи­мо­го эле­мен­та.


    .. js:attribute:: lastElementChild

        Это свой­ст­во по­доб­но свой­ст­ву :js:attr:`Node.lastChild`, но оно иг­но­ри­ру­ет уз­лы Text и Comment и воз­вра­ща­ет толь­ко эле­мен­ты ти­па :js:class:`Element`.

    .. js:attribute:: localName
        
        Ло­каль­ное имя дан­но­го эле­мен­та без пре­фик­са. Зна­че­ние это­го свой­ст­ва от­ли­ча­ет­ ся от зна­че­ния ат­ри­бу­та tagName, ко­то­рое мо­жет вклю­чать пре­фикс про­стран­ст­ва имен, ес­ли та­ко­вой име­ет­ся (и все сим­во­лы ко­то­ро­го для HTML-эле­мен­тов пре­об­ра­зу­ют­ся в верх­ний ре­гистр).


    .. js:attribute:: name

        Значение атрибута `name`


    .. js:attribute:: readonly string namespaceURI
        
        URL-ад­рес, фор­маль­но оп­ре­де­ляю­щий про­стран­ст­во имен дан­но­го эле­мен­та. Мо­жет иметь зна­че­ние null или со­дер­жать стро­ку, та­кую как «http://www.w3.org/1999/xhtml».


    .. js:attribute:: nextElementSibling
        
        Это свой­ст­во по­доб­но свой­ст­ву :js:attr:`Node.nextSibling`, но оно иг­но­ри­ру­ет уз­лы Text и Comment и воз­вра­ща­ет толь­ко эле­мен­ты ти­па :js:class:`Element`.


    .. js:attribute:: offsetHeight

        Высота элемента в скомпонованной странице


    .. js:attribute:: offsetLeft
        
        Расстояние от левой границы элемента до левой границы элемента offsetParent

        
    .. js:attribute:: offsetParent
        
        Элемент , от которого ведутся расчеты сдвига текущего элемента

        
    .. js:attribute:: offsetTop
        
        Расстояние от верхней границы элемента до верхней границы элемента offsetParent

        
    .. js:attribute:: offsetWidth
        
        Ширина элемента в скомпонованной странице

    .. js:attribute:: outerHTML
        
        Раз­мет­ка HTML или XML, оп­ре­де­ляю­щая дан­ный эле­мент и его со­дер­жи­мое. Ес­ли при­сво­ить это­му свой­ст­ву стро­ку, она за­ме­нит дан­ный эле­мент (и все его со­дер­жи­мое) ре­зуль­та­том син­так­си­че­ско­го раз­бо­ра но­во­го зна­че­ния как фраг­мен­та HTML- или XML-до­ку­мен­та.


    .. js:attribute:: prefix
        
        Пре­фикс про­стран­ст­ва имен для дан­но­го эле­мен­та. Обыч­но это свой­ст­во со­дер­жит зна­че­ние null. Ис­клю­че­ние со­став­ля­ют XML-до­ку­мен­ты, в ко­то­рых ис­поль­зу­ют­ся про­стран­ст­ва имен.


    .. js:attribute:: previousElementSibling
        
        Это свой­ст­во по­доб­но свой­ст­ву :js:attr:`Node.previousSibling, но оно иг­но­ри­ру­ет уз­лы Text и Comment и воз­вра­ща­ет толь­ко эле­мен­ты ти­па :js:class:`Element`. 


    .. js:attribute:: scrollHeight
        
        Видимая высота прокручиваемого элемента

        
    .. js:attribute:: scrollLeft
        
        Возвращает или устанавливает размер прокрутки в окне влево для элемента

        
    .. js:attribute:: scrollTop
        
        Возвращает или устанавливает размер прокрутки в окне вниз для элемента

        
    .. js:attribute:: scrollWidth
        
        Видимая ширина прокручиваемого элемента


    .. js:attribute:: style
        
        :js:class:`CSSStyleDeclaration` CSS-сти­ли для эле­мен­та. 


    .. js:attribute:: tagName

        Возвращает имя элемента

    .. js:attribute:: title
        
        Зна­че­ние ат­ри­бу­та title эле­мен­та. Мно­гие бро­узе­ры ото­бра­жа­ют зна­че­ние это­го ат­ри­бу­та в ви­де всплы­ваю­щей под­сказ­ки при на­ве­де­нии ука­за­те­ля мы­ши на эле­мент.


        
    .. js:function:: addEventListener()

        Задает обработчик некоторого события для элемента

        .. code-block:: js

            button.addEventListener('click', function(evt){});


    .. js:function:: Blur()
    .. js:function:: blur()

        Переносит фокус с текущего элемента


    .. js:function:: click()

        Симулирует щелчок по текущему элементу


    .. js:function:: dispatchEvent(event)

        Передает событие, связанное с этим элементом, в DOM


    .. js:function:: focus()

        Переносит фокус на текущий элемент


    .. js:function:: getAttribute(attrName) 

        Возвращает значение атрибута


    .. js:function:: getAttributeNS(namespace, localName) 

        Этот ме­тод дей­ст­ву­ет так же, как ме­тод :js:funct:`getAttribute()`, кро­ме то­го, что ат­ри­бут за­ да­ет­ся ком­би­на­ци­ей URI про­стран­ст­ва имен и ло­каль­но­го име­ни, оп­ре­де­лен­но­го в дан­ном про­стран­ст­ве имен.


    .. js:function:: getBoundingClientRect()

        Возвращает :js:class:`ClientRect`, опи­сы­ваю­щий пря­мо­уголь­ник, ог­ра­ни­чи­ваю­щий дан­ный эле­мент.

        
    .. js:function:: getClientRects()
        
        Воз­вра­ща­ет объ­ект, по­доб­ный мас­си­ву, со­дер­жа­щий объ­ек­ты :js:class:`ClientRects`, ко­то­рые опи­сы­ва­ют один или бо­лее пря­мо­уголь­ни­ков, ог­ра­ни­чи­ваю­щих дан­ный эле­мент.


    .. js:function:: getElementsByClassName(elementClassName)

        Возвращает список :js:class:`NodeList` элементов с указанным классом


    .. js:function:: getElementsByTagName(tagName)

        Возвращает список :js:class:`NodeList` элементов с указанным тегом


    .. js:function:: getElementsByTagNameNS(namespace, localName)

        Этот ме­тод дей­ст­ву­ет по­доб­но ме­то­ду :js:func:`getElementsByTagName()`, за ис­клю­че­ни­ем то­го, что имя те­га тре­буе­мых эле­мен­тов ука­зы­ва­ет­ся как ком­би­на­ция URI про­стран­ст­ва имен и ло­каль­но­го име­ни в этом про­стран­ст­ве имен.


    .. js:function:: hasAttribute(name) 

        Проверяет, есть ли у элемента атрибут


    .. js:function:: hasAttributeNS(namespace, localName) 

        Этот ме­тод дей­ст­ву­ет так же, как ме­тод :js:func:`hasAttribute()`, за ис­клю­че­ни­ем то­го, что ат­ри­бут за­да­ет­ся ком­би­на­ци­ей URI про­стран­ст­ва имен и ло­каль­но­го име­ни в этом про­стран­ст­ве имен.


    .. js:function:: hasAttributes() 

        Проверяет, есть ли у элемента атрибуты

    
    .. js:function:: insertAdjacentHTML(string position, string text)
        
        Встав­ля­ет раз­мет­ку HTML text в по­зи­цию position от­но­си­тель­но дан­но­го эле­мен­ та. 

        * `position` -

            * `beforebegin` - Встав­ля­ет текст пе­ред от­кры­ваю­щим те­гом эле­мен­та
            * `afterend` - Встав­ля­ет текст по­сле за­кры­ваю­ще­го те­га эле­мен­та
            * `afterbegin` - Встав­ля­ет текст сра­зу по­сле от­кры­ваю­ще­го те­га эле­мен­та
            * `beforeend` - Встав­ля­ет текст не­по­сред­ст­вен­но пе­ред за­кры­ваю­щим те­гом эле­мен­та


    .. js:function:: querySelector(string selectors)
        
        Воз­вра­ща­ет пер­вый вло­жен­ный эле­мент :js:class:`Element`, со­от­вет­ст­вую­щий CSS-се­лек­то­рам selec­tors (это мо­жет быть един­ст­вен­ный CSS-се­лек­тор или груп­па се­лек­то­ров, раз­де­лен­ных за­пя­ты­ми).


    .. js:function:: querySelectorAll(string selectors)

        Воз­вра­ща­ет объ­ект :js:class:`NodeList`, со­дер­жа­щий все эле­мен­ты, вло­жен­ные в  дан­ный эле­мент, ко­то­рые со­от­вет­ст­ву­ют се­лек­то­рам selectors (это мо­жет быть един­ст­вен­ный CSS-се­лек­тор или груп­па се­лек­то­ров, раз­де­лен­ных за­пя­ты­ми). 


    .. js:function:: removeAttribute(attrName) 

        Удаляет указанный атрибут


    .. js:function:: removeAttributeNS(string namespace, string localName)
        
        Ме­тод дей­ст­ву­ет так же, как ме­тод :js:func:`removeAttribute()`, за ис­клю­че­ни­ем то­го, что уда­ляе­мый ат­ри­бут за­да­ет­ся URI про­стран­ст­ва имен и ло­каль­но­го име­ни.


    .. js:function:: removeAttributeNode() 

        Удаляет указанный атрибутный узел

        
    .. js:function:: removeEventListener()

        Удаляет обработчик события для данного элемента

        .. code-block:: js

            button.removeEventListener('click', my_function)


    .. js:function:: scrollIntoView([boolean top])
    
        Ес­ли HTML-эле­мент в на­стоя­щий мо­мент на­хо­дит­ся за пре­де­ла­ми ок­на, этот ме­тод про­кру­тит до­ку­мент так, что эле­мент ока­жет­ся в пре­де­лах ок­на. Ар­гу­мент top яв­ ля­ет­ся не­обя­за­тель­ным и под­ска­зы­ва­ет ме­то­ду, дол­жен ли эле­мент ока­зать­ся бли­ же к верх­не­му или к ниж­не­му краю ок­на. Ес­ли он ра­вен true или от­сут­ст­ву­ет, бро­узер ста­ра­ет­ся вы­пол­нить про­крут­ку так, что­бы эле­мент ока­зал­ся бли­же к верх­не­му краю ок­на. Ес­ли он ра­вен false, бро­узер ста­ра­ет­ся вы­пол­нить про­крут­ку так, что­бы эле­мент ока­зал­ся бли­же к ниж­не­му краю ок­на. Для эле­мен­тов, при­ни­маю­щих фо­кус вво­да, та­ких как эле­мен­ты Input, ме­тод focus() не­яв­но вы­пол­ня­ет точ­но та­кую же опе­ра­цию про­крут­ки. 


    .. js:function:: setAttribute(string qualifiedName, string value)
        
        При­сваи­ва­ет ука­зан­ное зна­че­ние ат­ри­бу­ту с  ука­зан­ным име­нем. Ес­ли ат­ри­бут с та­ким име­нем еще не су­ще­ст­ву­ет, в эле­мент до­бав­ля­ет­ся но­вый ат­ри­бут. В HTML-до­ку­мен­тах пе­ред при­сваи­ва­ни­ем зна­че­ния сим­во­лы в име­ни ат­ри­бу­та пре­об­ра­зу­ют­ся в ниж­ний ре­гистр. Об­ра­ти­те вни­ма­ние: в HTML-до­ку­мен­те Ja­va­Script-свой­ст­ва, со­от­вет­ст­вую­щие всем стан­дарт­ным HTML-ат­ри­бу­там, оп­ре­де­ля­ют­ся объ­ек­та­ми HTMLElement. По­это­му дан­ный ме­тод обыч­но ис­поль­зу­ет­ся лишь для дос­ту­па к не­стан­дарт­ным ат­ри­бу­там.


    .. js:function:: setAttributeNS(string namespace, string qualifiedName, string value)
        
        Этот ме­тод дей­ст­ву­ет так же, как ме­тод :js:func:`setAttribute()`, за ис­клю­че­ни­ем то­го, что имя ат­ри­бу­та ука­зы­ва­ет­ся как ком­би­на­ция URI про­стран­ст­ва имен и ква­ли­фи­ци­ро­ван­но­го име­ни, со­стоя­ще­го из пре­фик­са про­стран­ст­ва имен, двое­то­чия и  ло­каль­но­го име­ни в этом про­стран­ст­ве имен.


HTMLAnchorElement
-----------------

Элемент `<a>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLAnchorElement

    .. js:attribute:: href

    .. js:attribute:: target

    .. js:attribute:: ping

    .. js:attribute:: rel

    .. js:attribute:: media

    .. js:attribute:: hreflang

    .. js:attribute:: type


HTMLAppletElement
-----------------

Элемент `<applet>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLAppletElement


HTMLAreaElement
-----------------

Элемент `<area>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLAreaElement

    .. js:attribute:: alt

    .. js:attribute:: coords

    .. js:attribute:: shape

    .. js:attribute:: href

    .. js:attribute:: target

    .. js:attribute:: ping

    .. js:attribute:: rel

    .. js:attribute:: media

    .. js:attribute:: hreflang

    .. js:attribute:: type


HTMLBaseElement
-----------------

Элемент `<base>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLBaseElement

    .. js::attribute:: href

    .. js::attribute:: target


HTMLBaseFontElement
-----------------

Элемент `<basefont>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLBaseFontElement


HTMLBodyElement
-----------------

Элемент `<blockquote>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLBodyElement

    .. js:attribute:: onafterprint

    .. js:attribute:: onbeforeprint

    .. js:attribute:: onbeforeunload

    .. js:attribute:: onblur

    .. js:attribute:: onerror

    .. js:attribute:: onfocus

    .. js:attribute:: onhash­

    .. js:attribute:: change

    .. js:attribute:: onload

    .. js:attribute:: onmessage

    .. js:attribute:: onoffline

    .. js:attribute:: ononline

    .. js:attribute:: onpagehide

    .. js:attribute:: onpage­show

    .. js:attribute:: onpopstate

    .. js:attribute:: onredo

    .. js:attribute:: onresize

    .. js:attribute:: onscroll

    .. js:attribute:: onstorage

    .. js:attribute:: onundo

    .. js:attribute:: onunload


HTMLButtonElement
-------------

Элемент `<button>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLButtonElement

    .. js:attribute:: autofocus

    .. js:attribute:: disabled

    .. js:attribute:: form

    .. js:attribute:: formaction

    .. js:attribute:: formenctype

    .. js:attribute:: formmethod

    .. js:attribute:: form­nova­

    .. js:attribute:: lidate

    .. js:attribute:: formtarget

    .. js:attribute:: name

    .. js:attribute:: type

    .. js:attribute:: value


HTMLBRElement
-------------

Элемент `<br>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLBRElement


HTMLDListElement
-------------

Элемент `<dl>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLDListElement


HTMLDirectoryElement
-------------

Элемент `<dir>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLDirectoryElement


HTMLDivElement
-------------

Элемент `<div>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLDivElement


HTMLFieldSetElement
-------------

Элемент `<fieldset>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLFieldSetElement

    .. js:attribute:: disabled
    
    .. js:attribute:: form
    
    .. js:attribute:: name


HTMLFontElement
-------------

Элемент `<font>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLFontElement


HTMLFormElement
-------------

Элемент `<from>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLFormElement

    .. js:attribute:: accept-charset

    .. js:attribute:: action

    .. js:attribute:: autocomplete
    
    .. js:attribute:: elements
    
    .. js:attribute:: enctype
    
    .. js:attribute:: method
    
    .. js:attribute:: name
    
    .. js:attribute:: novalidate
    
    .. js:attribute:: target

    .. js:attribute:: length

    .. js:function:: submit()

    .. js:function:: reset()

HTMLFrameElement
-------------

Элемент `<frame>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLFrameElement


HTMLFrameSetElement
-------------

Элемент `<frameset>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLFrameSetElement


HTMLHeadElement
-------------

Элемент `<head>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLHeadElement


HTMLHeadingElement
-------------

Элемент `<h1> ... <h6>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLHeadingElement


HTMLHtmlElement
-------------

Элемент `<html>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLHtmlElement

    .. js:attribute:: manifest


HTMLHRElement
-------------

Элемент `<hr>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLHRElement


HTMLImageElement
-------------

Элемент `<image>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLImageElement

    .. js:attribute:: alt
    
    .. js:attribute:: src
    
    .. js:attribute:: usemap
    
    .. js:attribute:: ismap
    
    .. js:attribute:: width
    
    .. js:attribute:: height


HTMLInputElement
-------------

Элемент `<input>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLInputElement

    .. js:attribute:: accept

    .. js:attribute:: alt

    .. js:attribute:: autocomplete

    .. js:attribute:: autofocus

    .. js:attribute:: checked

    .. js:attribute:: defaultChecked
    
    .. js:attribute:: defaultValue

    .. js:attribute:: dirname

    .. js:attribute:: disabled

    .. js:attribute:: form

    .. js:attribute:: form­

    .. js:attribute:: ac­tion

    .. js:attribute:: formenctype

    .. js:attribute:: formmethod

    .. js:attribute:: formnovalidate

    .. js:attribute:: formtarget

    .. js:attribute:: height

    .. js:attribute:: list

    .. js:attribute:: max

    .. js:attribute:: maxlength

    .. js:attribute:: min

    .. js:attribute:: multiple

    .. js:attribute:: name

    .. js:attribute:: pattern

    .. js:attribute:: placeholder

    .. js:attribute:: readonly

    .. js:attribute:: required

    .. js:attribute:: size

    .. js:attribute:: src

    .. js:attribute:: step

    .. js:attribute:: type

    .. js:attribute:: value

    .. js:attribute:: width

    .. js:function:: blur()

    .. js:function:: click()

    .. js:function:: focus()

    .. js:function:: select()


HTMLIsIndexElement
-------------

Элемент `<isindex>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLIsIndexElement


HTMLIFrameElement
-------------

Элемент `<iframe>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLIFrameElement

    .. js:attribute:: src
    
    .. js:attribute:: srcdoc
    
    .. js:attribute:: name
    
    .. js:attribute:: sandbox
    
    .. js:attribute:: seamless
    
    .. js:attribute:: width
    
    .. js:attribute:: height


HTMLLabelElement
-------------

Элемент `<label>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLLabelElement

    .. js:attribute:: form
    
    .. js:attribute:: for


HTMLLegendElement
-------------

Элемент `<legend>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLLegendElement


HTMLLinkElement
-------------

Элемент `<li>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLLinkElement

    .. js:attribute:: href

    .. js:attribute:: rel

    .. js:attribute:: media

    .. js:attribute:: hreflang

    .. js:attribute:: type

    .. js:attribute:: sizes


HTMLLIElement
-------------

Элемент `<li>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLLIElement

    .. js:attribute:: value


HTMLMapElement
-------------

Элемент `<map>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLMapElement

    .. js:attribute:: map


HTMLMenuElement
-------------

Элемент `<menu>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLMenuElement

    .. js:attribute:: type

    .. js:attribute:: label


HTMLMetaElement
-------------

Элемент `<meta>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLMetaElement

    .. js:attribute:: name
    
    .. js:attribute:: http-equiv
    
    .. js:attribute:: content
    
    .. js:attribute:: charset


HTMLModElement
-------------

Элемент `<del>`, `<ins>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLModElement

    .. js:attribute:: cite

    .. js:attribute:: datetime


HTMLObjectElement
-------------

Элемент `<object>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLObjectElement

    .. js:attribute:: data
    
    .. js:attribute:: type
    
    .. js:attribute:: name
    
    .. js:attribute:: usemap
    
    .. js:attribute:: form
    
    .. js:attribute:: width
    
    .. js:attribute:: height


HTMLOptGroupElement
-------------

Элемент `<optgroup>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLOptGroupElement

    .. js:attribute:: disabled

    .. js:attribute:: label


HTMLOptionElement
-------------

Элемент `<option>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLOptionElement

    .. code-block:: js

        var o = new Option(text, value, defaultSelected, selected);

    .. js:attribute:: form

    .. js:attribute:: defaultSelected

    .. js:attribute:: disabled
    
    .. js:attribute:: index

    .. js:attribute:: label
    
    .. js:attribute:: selected

    .. js:attribute:: text

    .. js:attribute:: value


HTMLOListElement
-------------

Элемент `<ol>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLOListElement

    .. js:attribute:: reversed

    .. js:attribute:: start


HTMLParagraphElement
-------------

Элемент `<p>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLParagraphElement

    .. js:attribute:: cite


HTMLParamElement
-------------

Элемент `<param>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLParamElement

    .. js:attribute:: name
    
    .. js:attribute:: value


HTMLPreElement
-------------

Элемент `<pre>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLPreElement


HTMLQuoteElement
-------------

Элемент `<q>`, `<blockquote>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLQuoteElement

    .. js:attribute:: cite


HTMLScriptElement
-------------

Элемент `<script>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLScriptElement

    .. js:attribute:: src
    
    .. js:attribute:: async
    
    .. js:attribute:: defer
    
    .. js:attribute:: type
    
    .. js:attribute:: charset


HTMLSelectElement
-------------

Элемент `<select>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLSelectElement

    .. js:attribute:: autofocus

    .. js:attribute:: disabled

    .. js:attribute:: form

    .. js:attribute:: length

    .. js:attribute:: multiple

    .. js:attribute:: name

    .. js:attribute:: options

    .. js:attribute:: required

    .. js:attribute:: selectedIndex

    .. js:attribute:: size

    .. js:attribute:: tabIndex

    .. js:attribute:: type

    .. js:attribute:: value

    .. js:function:: add()

    .. js:function:: blur()

    .. js:function:: focus()

    .. js:function:: remove()


HTMLStyleElement
-------------

Элемент `<select>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLStyleElement

    .. js:attribute:: media
    
    .. js:attribute:: type
    
    .. js:attribute:: scoped


HTMLTableCaptionElement
-------------

Элемент `<caption>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLTableCaptionElement


HTMLTableCellElement
-------------

Элемент `<td>`, `<th>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLTableCellElement

    .. js:attribute:: align

    .. js:attribute:: cellIndex

    .. js:attribute:: colspan
    
    .. js:attribute:: rowspan
    
    .. js:attribute:: headers

    .. js:attribute:: height

    .. js:attribute:: innerHTML

    .. js:attribute:: textContent

    .. js:attribute:: vAlign

    .. js:attribute:: width


HTMLTableColElement
-------------

Элемент `<col>`, `<colgroup>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLTableColElement

    .. js:attribute:: span


HTMLTableElement
-------------

Элемент `<table>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLTableElement

    .. js:attribute:: border

    .. js:attribute:: caption 

    .. js:attribute:: cellPadding

    .. js:attribute:: cellSpacing

    .. js:attribute:: rows[] 

    .. js:attribute:: summary

    .. js:attribute:: tBodies[] 

    .. js:attribute:: tFoot 

    .. js:attribute:: tHead 

    .. js:attribute:: width 

    .. js:function:: createCaption()

    .. js:function:: createTFoot()

    .. js:function:: createTHead()

    .. js:function:: deleteCaption()

    .. js:function:: deleteTFoot()

    .. js:function:: deleteTHead()

    .. js:function:: deleteRow(index)

    .. js:function:: insertRow(index)


HTMLTableRowElement
-------------

Элемент `<tr>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLTableRowElement

    .. js:attribute:: bgColor

    .. js:attribute:: cells

    .. js:attribute:: rowIndex

    .. js:attribute:: sectionRowIndex

    .. js:attribute:: vAlign

    .. js:function:: deleteCell(index)

    .. js:function:: insertCell(index)
    

HTMLTableSectionElement
-------------

Элемент `<tbody>`, `<tfoot>`, `<thead>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLTableSectionElement

    .. js:attribute:: align

    .. js:attribute:: rows

    .. js:attribute:: vAlign

    .. js:function:: deleteRow(index)

    .. js:function:: insertRow(index)


HTMLTextAreaElement
-------------

Элемент `<textarea>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLTextAreaElement

    .. js:attribute:: autofocus
    
    .. js:attribute:: cols
    
    .. js:attribute:: defaultValue

    .. js:attribute:: disabled
    
    .. js:attribute:: form
    
    .. js:attribute:: maxlength
    
    .. js:attribute:: name
    
    .. js:attribute:: placeholder
    
    .. js:attribute:: readonly
    
    .. js:attribute:: requi­r­ed
    
    .. js:attribute:: rows
    
    .. js:attribute:: tabIndex

    .. js:attribute:: type

    .. js:attribute:: value

    .. js:attribute:: wrap

    .. js:function:: blur()

    .. js:function:: focus()

    .. js:function:: select()


HTMLTitleElement
-------------

Элемент `<title>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLTitleElement


HTMLUListElement
-------------

Элемент `<ul>`

Наследник :js:class:`HTMLElement`

.. js:class:: HTMLUListElement


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