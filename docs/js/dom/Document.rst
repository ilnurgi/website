Document(HTMLDocument) - корневой элемент дерева
================================================

.. py:class:: Document()
.. py:class:: HTMLDocument()


    Наследник :py:class:`Node`


    .. code-block:: js

        document.getElementById('name')


    .. code-block:: html

        <script>
            var form = document.test,
                input = document.test.test_input,
                elem = form.elements[0];
        </script>

        <form name='test'>
            <input name='test_input'/>
        </form>


    .. py:attribute:: activeElement
        
        Элемент документа :py:class:`Element`, владею­щий в настоящий момент фокусом ввода.


    .. py:attribute:: all

        Коллекция, :py:class:`HTMLAllCollection`,
        всех элементов дерева, в порядке их появления в разметке

        .. code-block:: js

            document.all;
            // HTMLAllCollection[11]


    .. py:attribute:: anchors

        Список `<a>` элементов страницы с атрибутом `name`


    .. py:attribute:: applets

        Список `<applet>` элементов страницы


    .. py:attribute:: async

        Определяет, будет ли загрузка XML документа с сервера осуществяться асинхронно


    .. py:attribute:: body

        Тело документа


    .. py:attribute:: bgColor

        Цвет фона документа


    .. py:attribute:: characterSet
        
        Ко­ди­ров­ка сим­во­лов до­ку­мен­та


    .. py:attribute:: charset
        
        Ко­ди­ров­ка сим­во­лов до­ку­мен­та. Это свой­ст­во по­доб­но свой­ст­ву characterSet, но его зна­че­ние мож­но из­ме­нить, что­бы сме­нить ко­ди­ров­ку до­ку­мен­та.


    .. py:attribute:: compatMode
        
        Это свой­ст­во со­дер­жит стро­ку «BackCompat», ес­ли до­ку­мент ото­бра­жа­ет­ся в «ре­жи­ме со­вмес­ти­мо­сти» для об­рат­ной со­вмес­ти­мо­сти со старыми браузерами


    .. py:attribute:: cookie
        
        Сслыка на куки

        .. code-block:: js

            document.cookie = "info=123; max-age=604800";


    .. py:attribute:: defaultCharset
        
        Ко­ди­ров­ка сим­во­лов в бро­узе­ре по умол­ча­нию.


    .. py:attribute:: defaultView
        
        Объ­ект :py:class:`Window` бро­узе­ра, в ко­то­ром ото­бра­жа­ет­ся дан­ный до­ку­мент.


    .. py:attribute:: designMode
        
        Ес­ли это свой­ст­во име­ет зна­че­ние «on», до­ку­мент це­ли­ком дос­ту­пен для ре­дак­ти­ро­ва­ния. Ес­ли это свой­ст­во име­ет зна­че­ние «off», до­ку­мент це­ли­ком не­дос­ту­пен для ре­дак­ти­ро­ва­ния. (Но при этом дос­туп­ны­ми для ре­дак­ти­ро­ва­ния мо­гут быть от­ дель­ные эле­мен­ты с ус­та­нов­лен­ным свой­ст­вом contenteditable.) 


    .. py:attribute:: dir

        В  HTML-до­ку­мен­тах это свой­ст­во со­от­вет­ст­ву­ет ат­ри­бу­ту dir эле­мен­та <html>. То есть это то же са­мое зна­че­ние, что и documentElement.dir.


    .. py:attribute:: doctype

        Узел :py:class:`DocumentType`, пред­став­ляю­щий объ­яв­ле­ние <!DOCTYPE> до­ку­мен­та.


    .. py:attribute:: documentElement

        Возвращает корневой элемент документа :py:class:`Element`


    .. py:attribute:: domain

        Доменное имя сервера


    .. py:attribute:: embeds
            
        Объ­ект, по­доб­ный мас­си­ву, со­дер­жа­щий эле­мен­ты <embed>, при­сут­ст­вую­щие в до­ку­мен­те.


    .. py:attribute:: forms

        Список `<form>` элементов страницы


    .. py:attribute:: head

        В HTML-до­ку­мен­тах это свой­ст­во ссы­ла­ет­ся на эле­мент <head>.


    .. py:attribute:: inputEncoding

        Возвращает входную кодировку документа


    .. py:attribute:: images

        Список `<img>` элементов страницы


    .. py:attribute:: implementation

        Ссылка на :py:class:`DOMImplementation`


    .. py:attribute:: lastModified

        Дата последнего изменения документа


    .. py:attribute:: links

        Список `<a>` элементов с атрибутом `href`


    .. py:attribute:: location

        Ссылка на урл :py:class:`Location` документа


    .. py:attribute:: plugins

        Синоним embed

    .. py:attribute:: readyState

        Это свой­ст­во со­дер­жит стро­ку «loading», по­ка про­дол­жа­ет­ся за­груз­ка до­ку­мен­та, и стро­ку «complete» по ее окон­ча­нии. Ко­гда это свой­ст­во по­лу­ча­ет зна­че­ние «comp­le­te», бро­узер воз­бу­ж­да­ет со­бы­тие «readystatechange» в объ­ек­те Document.


    .. py:attribute:: referrer

        Адрес документа, содержащего ссылку, которая привела на текущую страницу


    .. py:attribute:: scripts
        
        Коллекция, содержащий все элементы <script>, присутствующие в документе.


    .. py:attribute:: styleSheets
        
        Коллекция стилей, :py:class:`CSSStyleSheet`, присутсвующих в документе


    .. py:attribute:: title

        Заголовок окна


    .. py:attribute:: xmlEncoding

        Возвращает XML кодировку документа


    .. py:method:: adoptNode(node)
        
        Уда­ля­ет узел node из лю­бо­го до­ку­мен­та, ча­стью ко­то­ро­го он яв­лял­ся на мо­мент вы­зо­ва, и  за­пи­сы­ва­ет в  свой­ст­во ownerDocument уз­ла ссыл­ку на те­ку­щий до­ку­мент, под­го­тав­ли­вая его к  до­бав­ле­нию в  те­ку­щий до­ку­мент. 

        По­хо­жий на не­го ме­тод importNode() ко­пи­ру­ет узел из дру­го­го до­ку­мен­та, не уда­ляя его.

        Возвращает :py:class:`Node`

    .. py:method:: close()
        
        За­кры­ва­ет по­ток вы­во­да до­ку­мен­та, от­кры­тый ме­то­дом open(), за­став­ляя вы­вес­ти все бу­фе­ри­зо­ван­ные дан­ные.


    .. py:method:: createAttribute(name)

        Возвращает :py:class:`Attr`, создает атрибутный узел с указанным именем


    .. py:method:: createComment(data)

        Создает и возвращает узел :py:class:`Comment`


    .. py:method:: createDocumentFragment()

        Создает и возвращает :py:class:`DocumentFragment` пустой фрагмент документа


    .. py:method:: createElement(tagname)

        Создает и возвращает новый :py:class:`Element`, указанного типа

        .. code-block:: js

            var input_element = document.createElement('input');


    .. py:method:: createElementNS(namespace, qualifiedName)

        Создает и возвращает новый уникальный :py:class:`Element`


    .. py:method:: createProcessingInstruction(target, data)

        Возвращает :py:class:`ProcessingInstruction` узел


    .. py:method:: createEvent(eventInterface)

        Создает и возвращает неинициализированный объект :py:class:`Event`

        * `eventInterface`

            * `Event`

            * `UIEvent`

            * `MouseEvent`

            * `MessageEvent`


    .. py:method:: createProcessingInstruction(target, data)

        Создает и возвращает новый узел :py:class:`ProcessingInstruction`


    .. py:method:: createTextNode(data)

        Возвращает текстовый узел :py:class:`Text`


    .. py:method:: elementFromPoint(x, y)

        Возвращает самый глубоко вложенный :py:class:`Element` с оконными координатами


    .. py:method:: execCommand(commandId[, showUI, [value]])

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



    .. py:method:: getElementById(elementId)
        
        Возвращает элемент :py:class:`Element` по id


    .. py:method:: getElementsByClassName(elementClassName)

        Возвращает список :py:class:`NodeList` элементов с указанным классом


    .. py:method:: getElementsByName(elementName)

        Возвращает список :py:class:`NodeList` элементов с указанным именем


    .. py:method:: getElementsByTagName(tagName)

        Возвращает список :py:class:`NodeList` элементов с указанным тегом


    .. py:method:: hasFocus()

        Документ в фокусе


    .. py:method:: importNode(node, deep)

        Возвращает узел :py:class:`Node` определенный в другом документе.

        * `deep` - копировать потомки узла


    .. py:method:: open(url, name, features[, replace])

        Возвращает :py:class:`Window`, аналог :js:func:`Window.open`


    .. py:method:: open([type='text/html'[, replace]])

        Возвращает :py:class:`Document`


    .. py:method:: queryCommandEnabled(string commandId)
    
        Воз­вра­ща­ет true, ес­ли в на­стоя­щий мо­мент мож­но пе­ре­дать ко­ман­ду commandId ме­то­ ду execCommand(), и false – в про­тив­ном слу­чае. На­при­мер, бес­смыс­лен­но пе­ре­да­вать ко­ман­ду «undo», ко­гда не­че­го от­ме­нять. 


    .. py:method:: queryCommandIndeterm(string commandId)
    
        Воз­вра­ща­ет true, ес­ли commandId на­хо­дит­ся в со­стоя­нии, для ко­то­ро­го query­Com­mand­State() не мо­жет вер­нуть ка­кое-то оп­ре­де­лен­ное зна­че­ние. Ко­ман­ды, оп­ре­де­ляе­мые спе­ци­фи­ка­ци­ей HTML5, не мо­гут на­хо­дить­ся в не­оп­ре­де­лен­ном со­стоя­нии, но ко­ман­ды, оп­ре­де­ляе­мые бро­узе­ром, – мо­гут. 


    .. py:method:: queryCommandState(string commandId)
    
        Воз­вра­ща­ет со­стоя­ние ко­ман­ды commandId. Не­ко­то­рые ко­ман­ды ре­дак­ти­ро­ва­ния, та­кие как «bold» и  «italic», име­ют со­стоя­ние true, ес­ли под тек­сто­вым кур­со­ром или в вы­де­лен­ной об­лас­ти на­хо­дит­ся текст, на­бран­ный кур­си­вом, и false – в про­тив­ном слу­чае. Од­на­ко боль­шин­ст­во ко­манд не име­ют со­стоя­ния, и для них этот ме­тод все­гда воз­вра­ща­ет false. 


    .. py:method:: queryCommandSupported(string commandId)
    
        Воз­вра­ща­ет true, ес­ли бро­узер под­дер­жи­ва­ет ука­зан­ную ко­ман­ду, и false – в про­тив­ном слу­чае. 


    .. py:method:: queryCommandValue(string commandId)
    
        Воз­вра­ща­ет со­стоя­ние ука­зан­ной ко­ман­ды в ви­де стро­ки. 


    .. py:method:: querySelector(selector)

        Выборка элементов из дом дерева по селектору

        Возвращает :py:class:`HTMLElement` или :py:class:`Element`

        .. code-block:: js

            document.querySelector('.some_class')


    .. py:method:: write(text[, text1 [...]])

        Записываем строку в документ


    .. py:method:: writeln(text)

        Записываем строку в документ с переводом каретки
