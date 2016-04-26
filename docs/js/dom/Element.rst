Element(HTMLElement) - элемент узла дом дерева
==============================================

.. js:class:: Element()

    Наследник :js:class:`Node`, :js:class:`EventTarget`


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

============ ========
Эле­мент      Ат­ри­бу­ты
============ ========
<a>          href, target, ping, rel, media, hreflang, type
<area>       alt, coords, shape, href, target, ping, rel, media, hreflang, type
<audio>      src, preload, autoplay, loop, controls
<base>       href, target
<blockquote> cite
<body>       onafterprint, onbeforeprint, onbeforeunload, onblur, onerror, onfocus, onhash­, change, onload, onmessage, onoffline, ononline, onpagehide, onpage­show, onpopstate, onredo, onresize, onscroll, onstorage, onundo, onunload
<button>     autofocus, disabled, form, formaction, formenctype, formmethod, form­nova­, lidate, formtarget, name, type, value
<canvas>     width, height
<col>        span
<colgroup>   span
<command>    type, label, icon, disabled, checked, radiogroup
<del>        cite, datetime
<details>    open
<embed>      src, type, width, height
<fieldset>   disabled, form, name
<form>       accept-charset, action, autocomplete, enctype, method, name, novalidate, target
<html>       manifest
<iframe>     src, srcdoc, name, sandbox, seamless, width, height
<img>        alt, src, usemap, ismap, width, height
<input>      accept, alt, autocomplete, autofocus, checked, dirname, disabled, form, form­, ac­tion, formenctype, formmethod, formnovalidate, formtarget, height, list, max, maxlength, min, multiple, name, pattern, placeholder, readonly, required, size, src, step, type, value, width
<ins>        cite, datetime
<keygen>     autofocus, challenge, disabled, form, keytype, name
<label>      form, for
<li>         value
<link>       href, rel, media, hreflang, type, sizes
<map>        name
<menu>       type, label
<meta>       name, http-equiv, content, charset
<meter>      value, min, max, low, high, optimum, form
<object>     data, type, name, usemap, form, width, height
<ol>         reversed, start
<optgroup>   disabled, label
<option>     disabled, label, selected, value
<output>     for, form, name
<param>      name, value
<progress>   value, max, form
<q>          cite
<script>     src, async, defer, type, charset
<select>     autofocus, disabled, form, multiple, name, required, size
<source>     src, type, media
<style>      media, type, scoped
<table>      summary
<td>         colspan, rowspan, headers
<textarea>   autofocus, cols, disabled, form, maxlength, name, placeholder, readonly, requi­r­ed, rows, wrap
<th>         colspan, rowspan, headers, scope
<time>       datetime, pubdate
<track>      default, kind, label, src, srclang
<video>      src, poster, preload, autoplay, loop, controls, width, height
============ ========