Document(HTMLDocument) - корневой элемент дерева
================================================

.. js:class:: Document()
.. js:class:: HTMLDocument()


    Наследник :js:class:`Node`


    .. code-block:: js

        document.getElementById('name')


    .. code-block:: js

        <form name='test'>
            <input name='test_input'/>
        </form>

        var form = document.test,
            input = document.test.test_input,
            elem = form.elements[0];


    .. js:attribute:: activeElement
        
        Элемент документа :js:class:`Element`, владею­щий в настоящий момент фокусом ввода.


    .. js:attribute:: all

        Коллекция, :js:class:`HTMLAllCollection`,
        всех элементов дерева, в порядке их появления в разметке

        .. code-block:: js

            document.all;
            // HTMLAllCollection[11]

    .. js:attribute:: anchors

        Массив якорей страницы


    .. js:attribute:: async

        Определяет, будет ли загрузка XML документа с сервера осуществяться асинхронно


    .. js:attribute:: body

        Тело документа


    .. js:attribute:: bgColor

        Цвет фона документа


    .. js:attribute:: characterSet
        
        Ко­ди­ров­ка сим­во­лов до­ку­мен­та


    .. js:attribute:: charset
        
        Ко­ди­ров­ка сим­во­лов до­ку­мен­та. Это свой­ст­во по­доб­но свой­ст­ву characterSet, но его зна­че­ние мож­но из­ме­нить, что­бы сме­нить ко­ди­ров­ку до­ку­мен­та.


    .. js:attribute:: compatMode
        
        Это свой­ст­во со­дер­жит стро­ку «BackCompat», ес­ли до­ку­мент ото­бра­жа­ет­ся в «ре­жи­ме со­вмес­ти­мо­сти» для об­рат­ной со­вмес­ти­мо­сти со старыми браузерами


    .. js:attribute:: cookie
        
        Сслыка на куки

        .. code-block:: js

            document.cookie = "info=123; max-age=604800";


    .. js:attribute:: defaultCharset
        
        Ко­ди­ров­ка сим­во­лов в бро­узе­ре по умол­ча­нию.


    .. js:attribute:: defaultView
        
        Объ­ект :js:class:`Window` бро­узе­ра, в ко­то­ром ото­бра­жа­ет­ся дан­ный до­ку­мент.


    .. js:attribute:: designMode
        
        Ес­ли это свой­ст­во име­ет зна­че­ние «on», до­ку­мент це­ли­ком дос­ту­пен для ре­дак­ти­ро­ва­ния. Ес­ли это свой­ст­во име­ет зна­че­ние «off», до­ку­мент це­ли­ком не­дос­ту­пен для ре­дак­ти­ро­ва­ния. (Но при этом дос­туп­ны­ми для ре­дак­ти­ро­ва­ния мо­гут быть от­ дель­ные эле­мен­ты с ус­та­нов­лен­ным свой­ст­вом contenteditable.) 


    .. js:attribute:: dir

        В  HTML-до­ку­мен­тах это свой­ст­во со­от­вет­ст­ву­ет ат­ри­бу­ту dir эле­мен­та <html>. То есть это то же са­мое зна­че­ние, что и documentElement.dir.


    .. js:attribute:: doctype

        Узел :js:class:`DocumentType`, пред­став­ляю­щий объ­яв­ле­ние <!DOCTYPE> до­ку­мен­та.


    .. js:attribute:: documentElement

        Возвращает корневой элемент документа :js:class:`Element`


    .. js:attribute:: domain

        Доменное имя сервера


    .. js:attribute:: embeds
            
        Объ­ект, по­доб­ный мас­си­ву, со­дер­жа­щий эле­мен­ты <embed>, при­сут­ст­вую­щие в до­ку­мен­те.


    .. js:attribute:: forms

        Коллекция всех форм, :js:class:`Form`, на странице


    .. js:attribute:: head

        В HTML-до­ку­мен­тах это свой­ст­во ссы­ла­ет­ся на эле­мент <head>.


    .. js:attribute:: inputEncoding

        Возвращает входную кодировку документа


    .. js:attribute:: images

        Массив :js:class:`Image` на странице


    .. js:attribute:: implementation

        Ссылка на :js:class:`DOMImplementation`


    .. js:attribute:: lastModified

        Дата последнего изменения документа


    .. js:attribute:: links

        Коллекция ссылок на странице


    .. js:attribute:: location

        Ссылка на урл :js:class:`Location` документа


    .. js:attribute:: plugins

        Синоним embed

    .. js:attribute:: readyState

        Это свой­ст­во со­дер­жит стро­ку «loading», по­ка про­дол­жа­ет­ся за­груз­ка до­ку­мен­та, и стро­ку «complete» по ее окон­ча­нии. Ко­гда это свой­ст­во по­лу­ча­ет зна­че­ние «comp­le­te», бро­узер воз­бу­ж­да­ет со­бы­тие «readystatechange» в объ­ек­те Document.


    .. js:attribute:: referrer

        Адрес документа, содержащего ссылку, которая привела на текущую страницу


    .. js:attribute:: scripts
        
        Коллекция, содержащий все элементы <script>, присутствующие в документе.


    .. js:attribute:: styleSheets
        
        Коллекция стилей, :js:class:`CSSStyleSheet`, присутсвующих в документе


    .. js:attribute:: title

        Заголовок окна


    .. js:attribute:: xmlEncoding

        Возвращает XML кодировку документа


    .. js:function:: adoptNode(node)
        
        Уда­ля­ет узел node из лю­бо­го до­ку­мен­та, ча­стью ко­то­ро­го он яв­лял­ся на мо­мент вы­зо­ва, и  за­пи­сы­ва­ет в  свой­ст­во ownerDocument уз­ла ссыл­ку на те­ку­щий до­ку­мент, под­го­тав­ли­вая его к  до­бав­ле­нию в  те­ку­щий до­ку­мент. 

        По­хо­жий на не­го ме­тод importNode() ко­пи­ру­ет узел из дру­го­го до­ку­мен­та, не уда­ляя его.

        Возвращает :js:class:`Node`

    .. js:function:: close()
        
        За­кры­ва­ет по­ток вы­во­да до­ку­мен­та, от­кры­тый ме­то­дом open(), за­став­ляя вы­вес­ти все бу­фе­ри­зо­ван­ные дан­ные.


    .. js:function:: createAttribute(name)

        Возвращает :js:class:`Attr`, создает атрибутный узел с указанным именем


    .. js:function:: createComment(data)

        Создает и возвращает узел :js:class:`Comment`


    .. js:function:: createDocumentFragment()

        Создает и возвращает :js:class:`DocumentFragment` пустой фрагмент документа


    .. js:function:: createElement(tagname)

        Создает и возвращает новый :js:class:`Element`, указанного типа

        .. code-block:: js

            var input_element = document.createElement('input');


    .. js:function:: createElementNS(namespace, qualifiedName)

        Создает и возвращает новый уникальный :js:class:`Element`


    .. js:function:: createProcessingInstruction(target, data)

        Возвращает :js:class:`ProcessingInstruction` узел


    .. js:function:: createEvent(eventInterface)

        Создает и возвращает неинициализированный объект :js:class:`Event`

        * `eventInterface`

            * `Event`

            * `UIEvent`

            * `MouseEvent`

            * `MessageEvent`


    .. js:function:: createProcessingInstruction(target, data)

        Создает и возвращает новый узел :js:class:`ProcessingInstruction`


    .. js:function:: createTextNode(data)

        Возвращает текстовый узел :js:class:`Text`


    .. js:function:: elementFromPoint(x, y)

        Возвращает самый глубоко вложенный :js:class:`Element` с оконными координатами


    .. js:function:: execCommand(commandId[, showUI, [value]])

        Выполняет команду редактирования.

        * `bold`

        * `createLi`

        * `delete`

        * `formatBloc`

        * `forwardDelete`

        * `insertImage`

        * `insertHTML`

        * `insertLineBreak`

        * `insertOrderedList`

        * `insertUnorderedList`

        * `insertParagraph`

        * `insertText`

        * `italic`

        * `redo`

        * `selectAll`

        * `subscript`

        * `superscript`

        * `undo`

        * `unlink`

        * `unselect`



    .. js:function:: getElementById(elementId)
        
        Возвращает элемент :js:class:`Element` по id


    .. js:function:: getElementsByClassName(elementClassName)

        Возвращает список :js:class:`NodeList` элементов с указанным классом


    .. js:function:: getElementsByName(elementName)

        Возвращает список :js:class:`NodeList` элементов с указанным именем


    .. js:function:: getElementsByTagName(tagName)

        Возвращает список :js:class:`NodeList` элементов с указанным тегом


    .. js:function:: hasFocus()

        Документ в фокусе


    .. js:function:: importNode(node, deep)

        Возвращает узел :js:class:`Node` определенный в другом документе.

        * `deep` - копировать потомки узла


    .. js:function:: open(url, name, features[, replace])

        Возвращает :js:class:`Window`, аналог :js:func:`Window.open`


    .. js:function:: open([type='text/html'[, replace]])

        Возвращает :js:class:`Document`


    .. js:function:: queryCommandEnabled(string commandId)
    
        Воз­вра­ща­ет true, ес­ли в на­стоя­щий мо­мент мож­но пе­ре­дать ко­ман­ду commandId ме­то­ ду execCommand(), и false – в про­тив­ном слу­чае. На­при­мер, бес­смыс­лен­но пе­ре­да­вать ко­ман­ду «undo», ко­гда не­че­го от­ме­нять. 


    .. js:function:: queryCommandIndeterm(string commandId)
    
        Воз­вра­ща­ет true, ес­ли commandId на­хо­дит­ся в со­стоя­нии, для ко­то­ро­го query­Com­mand­State() не мо­жет вер­нуть ка­кое-то оп­ре­де­лен­ное зна­че­ние. Ко­ман­ды, оп­ре­де­ляе­мые спе­ци­фи­ка­ци­ей HTML5, не мо­гут на­хо­дить­ся в не­оп­ре­де­лен­ном со­стоя­нии, но ко­ман­ды, оп­ре­де­ляе­мые бро­узе­ром, – мо­гут. 


    .. js:function:: queryCommandState(string commandId)
    
        Воз­вра­ща­ет со­стоя­ние ко­ман­ды commandId. Не­ко­то­рые ко­ман­ды ре­дак­ти­ро­ва­ния, та­кие как «bold» и  «italic», име­ют со­стоя­ние true, ес­ли под тек­сто­вым кур­со­ром или в вы­де­лен­ной об­лас­ти на­хо­дит­ся текст, на­бран­ный кур­си­вом, и false – в про­тив­ном слу­чае. Од­на­ко боль­шин­ст­во ко­манд не име­ют со­стоя­ния, и для них этот ме­тод все­гда воз­вра­ща­ет false. 


    .. js:function:: queryCommandSupported(string commandId)
    
        Воз­вра­ща­ет true, ес­ли бро­узер под­дер­жи­ва­ет ука­зан­ную ко­ман­ду, и false – в про­тив­ном слу­чае. 


    .. js:function:: queryCommandValue(string commandId)
    
        Воз­вра­ща­ет со­стоя­ние ука­зан­ной ко­ман­ды в ви­де стро­ки. 


    .. js:function:: write(text[, text1 [...]])

        Записываем строку в документ


    .. js:function:: writeln(text)

        Записываем строку в документ с переводом каретки


Узлы дерева
-----------

.. js:class:: Node()

    
    .. js:attribute:: action

        `form`


    .. js:attribute:: checked

        `input`


    .. js:attribute:: cols

        `textarea`


    .. js:attribute:: currentStyle

        Текущие CSS стили для IE


    .. js:attribute:: data

        Текст узла

    
    .. js:attribute:: dataset

        Датасет

        .. code-block:: js

            <input ... data-val="1" data-val-msg="123" />

            var value = elem.dataset.val,
                message = elem.dataset.valMsg;
        

    .. js:attribute:: defaultChecked

        `input`
        

    .. js:attribute:: defaultselected

        `option`
        

    .. js:attribute:: defaultValue

        `input, textarea`


    .. js:attribute:: disabled

        `textarea, select, option`


    .. js:attribute:: elements

        `form`


    .. js:attribute:: enctype

        `form`


    .. js:attribute:: form

        ссылка на форму, в которой находится элемент

        `input, textarea, select, option`


    .. js:attribute:: index

        `option`


    .. js:attribute:: innerHTML

        HTML Содержание узла


    .. js:attribute:: label

        `option`


    .. js:attribute:: length

        `form, select`


    .. js:attribute:: maxLength

        `input`


    .. js:attribute:: method

        `form`


    .. js:attribute:: multiple

        `select`


    .. js:attribute:: name

        имя элемента управления

        `form, name, select`


    .. js:attribute:: onabort

        Обработчик, прерывание загрузки изображения

        `img`


    .. js:attribute:: onblur

        Обработчик, элемент теряет фокус

        `button, input, label, select, textarea, body`


    .. js:attribute:: onchange

        Обработчик, элемент потерял фокус и его значение с момента получения фокуса изменилось

        `input, select, textarea`


    .. js:attribute:: onclick

        Обработчик, нажата или отпущена клавиша мыши


    .. js:attribute:: oncontextmenu

        Отображается контекстоное меню


    .. js:attribute:: ondblclick

        Обработчик, двойной щелчок


    .. js:attribute:: ondrag 

        бук­си­ров­ка про­дол­жа­ет­ся (воз­бу­ж­да­ет­ся в эле­мен­те-ис­точ­ни­ке)


    .. js:attribute:: ondragend 

        бук­си­ров­ка за­вер­ше­на (воз­бу­ж­да­ет­ся в эле­мен­те-ис­точ­ни­ке)


    .. js:attribute:: ondragenter 

        бук­си­руе­мые дан­ные ока­за­лись над эле­мен­том (воз­бу­ж­да­ет­ся в эле­мен­те-при­ем­ни­ке)


    .. js:attribute:: ondragleave 

        бук­си­руе­мые дан­ные вы­шли за гра­ни­цы эле­мен­та (воз­бу­ж­да­ет­ся в эле­мен­те-при­ем­ни­ке)


    .. js:attribute:: ondragover 

        бук­си­ров­ка про­дол­жа­ет­ся (воз­бу­ж­да­ет­ся в эле­мен­те-при­ем­ни­ке)


    .. js:attribute:: ondragstart 

        поль­зо­ва­тель на­чал опе­ра­цию бук­си­ров­ки (воз­бу­ж­да­ет­ся в эле­мен­те-ис­точ­ни­ке)


    .. js:attribute:: ondrop 

        поль­зо­ва­тель за­вер­шил бук­си­ров­ку (воз­бу­ж­да­ет­ся в эле­мен­те-при­ем­ни­ке)


    .. js:attribute:: onerror

        Обработчик, ошибка загрузки изображения

        `img`


    .. js:attribute:: onfocus

        Обработчик, элемент получил фокус

        `button, input, label, select, textarea, body`


    .. js:attribute:: oninput 

        вы­пол­нен ввод в эле­мент фор­мы (воз­бу­ж ­да­ет­ся зна­чи­тель­но ча­ще, чем onchange)


    .. js:attribute:: onkeydown

        Обработчик, клавиши нажата

        `body, form etc`


    .. js:attribute:: onkeypress

        Обработчик, клавиши нажата или отпущена

        `body, form etc`


    .. js:attribute:: onkeyup

        Обработчик, клавиши отпущена

        `body, form etc`


    .. js:attribute:: onload

        Обработчик, загрузка завершена

        `body, frameset, img`


    .. js:attribute:: onmousedown

        Обработчик, нажата кнопка мыши


    .. js:attribute:: onmousemove

        Обработчик, перемещение указателя мыши


    .. js:attribute:: onmouseout

        Обработчик, указатель мыши выходит за границы элемента


    .. js:attribute:: onmouseover

        Обработчик, указаетль мыши входит в границы элемента


    .. js:attribute:: onmouseup

        Обработчик, отпущена кнопка мыши

    .. js:attribute:: onmousewheel 

        поль­зо­ва­тель по­вер­нул ко­ле­си­ко мы­ши


    .. js:attribute:: onreset

        Обработчик, запрос на очистку полей формы

        `form`


    .. js:attribute:: onresize

        Обработчик, изменени размеры окна

        `body, frameset`
        

    .. js:attribute:: onscroll

        Прокрутка элемента


    .. js:attribute:: onselect

        Обработчик, выбор текста

        `input, textarea`


    .. js:attribute:: onsubmit

        Обработчик, запрос на передачу данных формы

        `form`


    .. js:attribute:: onunload

        Документ выгружен

        `body, frameset`


    .. js:attribute:: ownerDocument


    .. js:attribute:: options

        `select`


    .. js:attribute:: readOnly

        `textarea`


    .. js:attribute:: rows

        `textarea`


    .. js:attribute:: selected

        `option`


    .. js:attribute:: selectedIndex

        `select`


    .. js:attribute:: size

        `input, select`


    .. js:attribute:: style

        CSS стили узла


    .. js:attribute:: tabIndex

        `textarea, select`


    .. js:attribute:: target

        `form`


    .. js:attribute:: text

        `option`


    .. js:attribute:: type

        тип элемента управления

        `input, textarea, select`


    .. js:attribute:: value
            
        Значение элемента

        `input, textarea, select, option`


    .. js:attribute:: ELEMENT (1)

        Элемент


    .. js:attribute:: ATTRIBUTE (2)

        Атрибут элемента


    .. js:attribute:: TEXT (3)

        Текстовый узел


    .. js:attribute:: CDATASECTION (4)

        Раздел CDATA (его содержимое не будет обрабатываться парсером)


    .. js:attribute:: entityreference (5)

        Имя ссылки на сущность


    .. js:attribute:: entity (6)

        Сущность


    .. js:attribute:: processinginstruction (7)

        Процессуальная инструкция


    .. js:attribute:: COMMENT (8)

        Комментарии


    .. js:attribute:: DOCUMENT (9)

        Весь документ


    .. js:attribute:: DocumentType (10)

        Декларация типа документа


    .. js:attribute:: DocumentFragment (11)

        Часть документа


    .. js:attribute:: Notation (12)

        Имя нотации


    .. js:function:: add()

        `select`


    .. js:function:: addEventListener(event, handler, capture)

        Добавляем свой обработчик элементу.

        * event - имя события, строка

        * handler - функция обраотчик

        * capture - true-обработчик срабатывает на этапе перехвата, false-обработчик срабатывает на этапе всплывания

        Доступно на DOM lvl.2


    .. js:function:: attachEvent(event, handler)

        Аналог :js:func:`addEventListener`, для IE


    .. js:function:: blur()

        `input, textarea, select`


    .. js:function:: click()

        `input`


    .. js:function:: cloneNode(bool)

        Создать копию узла, аргумент - в доме или нет.


    .. js:function:: detachEvent(event, handler)

        Аналог :js:func:`removeEventListener`, для IE


    .. js:function:: focus()

        `input, textarea, select`


    .. js:function:: getComputedStyle(element, null)

        Возвращает вычисляемые CSS стили


    .. js:function:: remove()

        `select`


    .. js:function:: removeAttribute(attr)

        Удаляет атрибут из узла      


    .. js:function:: removeEventListener(event, handler, capture)

        Удаляет обработчик из элемента, :js:func:`addEventListener`

        Доступно на DOM lvl.2


    .. js:function:: reset()

        `form`


    .. js:function:: select()

        `input, textarea`


    .. js:function:: setAttribute(attr, value)

        Устанавливает атрибут для узла



    .. js:function:: submit()

        `form`


Ивент события
-------------

.. js:class:: Eent()

    Ивент события


    .. js:attribute:: altKey

        Булево, нажата кнопка Альт


    .. js:attribute:: bubbles

        Булево, событие может всплывать по дереву элементов. 

        События `blur, focus, load, unload` не всплывают


    .. js:attribute:: button

        Номер кнопки мыши, 0 - левая, 1 - средняя, 2 - правая (1,2,4 для IE)


    .. js:attribute:: cancelable

        Булево, с этим событием связано действие по умолчанию и его можно отменить с помощью метода :js:func:`preventDefault`


    .. js:attribute:: cancelBubble

        Аналог :js:func:`stopPropagation()` для IE


    .. js:attribute:: charCode

        Код клавиши события


    .. js:attribute:: clientX, clientY

        Координаты относительно левого верхнего угла документа


    .. js:attribute:: ctrlKey

        Булево, кнопка Ctrl нажата


    .. js:attribute:: currentTarget

        Элемент, событие которого исполняется в данное время


    .. js:attribute:: eventPhase

        Число, указывающее этап 

        * Event.CAPTURING_PHASE
        * Event.AT_TARGET
        * Event.BUBBLING_PHASE    


    .. js:attribute:: keyCode

        Код клавииш для события 


    .. js:attribute:: offsetX, offsetY

        Координаты, относительно элемента, в котором произошло событие. Для IE


    .. js:attribute:: returnValue

        Аналог :js:func:`preventDefault` для IE
        

    .. js:attribute:: screenX, screenY

        Координаты относительно экрана


    .. js:attribute:: shiftKey

        Булево, кнопка Shift нажата


    .. js:attribute:: srcElement

        Отправитель события, для IE


    .. js:attribute:: target

        Элемент, который был инициатором события


    .. js:attribute:: timeStamp

        Дата события


    .. js:attribute:: type

        Тип события


    .. js:function:: preventDefault();

        Прекращает выполнение стандртной операции (сабмит формы)


    .. js:function:: stopPropagation();

        Отменить распространение события другому узлу


Option
------

.. code-block:: js

    var o = Option(text, value, defaultSelected, selected);