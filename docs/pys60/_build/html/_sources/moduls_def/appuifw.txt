.. py:module:: appuifw

appuifw
=======

Стандартный модуль для создания графичекого интерфейса программы. 

Диалоговые окна
---------------

.. py:method:: multy_selection_list(list [,style='checkbox', search_field=1])

    :param list: список элементов окна
    :type list: list
    :param style: тип отображения (cheskbox, checkmark)
    :param search_field: отображать ли поле для поиска

    Создает окно со списком для множественного выбора. Возвращает индекс выбранной строки.

    >>> appuifw.selection_list([u'1',u'2',u'3'])

    .. image:: appuifw_selection_list.jpg

.. py:method:: multi_query(label1, label2) 
    
    :param label1: заголовок первого поля ввода
    :type label1: unicode
    :param label2: заголовок второго поля ввода
    :type label2: unicode

    Создает окно с запросом ввода двух данных. Возвращает две строки

    >>> appuifw.multi_query(u'Enter 1', u'Enter 2')    
    
    .. image:: appuifw_multy_query.jpg    

.. py:method:: note(title[, type[, global]) 

    :param title: заголовок уведомления
    :type title: unicode
    :param type: тип уведомления

        * info - информационное
        * error - ошибка
        * conf - просто окно, выполнено
        * time - время
        * cod - пароль, ввод закрывается звездочками
        * query - окно с запросом, без ввода, ответ на который да или нет.

    :param global: 0|1 отображать поверх всех окон

    Создает окно с уведомлением

    >>> appuifw.note(u'Привет','info')

    .. image:: appuifw_note.jpg    
    

.. py:method:: popup_menu(list [, title]) 

    :param list: список для выбора
    :type list: list
    :param title: заголовок окна
    :type title: unicode

    Создает всплывающее окно со списком для выбора. Возвращает индекс выбранной строки.

    >>> appuifw.popup_menu([u'1',u'2',u'3'],u'Select')

    .. image:: appuifw_popup_menu.jpg    

.. py:method:: query(title, type[, default]) 

    :param title: заголовк запроса
    :type title: unicode
    :param type: тип ввода данных, соответственно возвращаемый тип.
        
        * text - строка
        * number - числа
        * float - вещественное число
        * date - дата
        * time - время
        * cod - пароль, ввод закрывается звездочками
        * query - окно с запросом, без ввода, ответ на который да или нет.

    :param default: стандартное значение, выводимое при запросе
    
    Создает окно с запросом ввода данных

    >>> appuifw.query(u'Введите текст','text')

    .. image:: appuifw_query.jpg    

.. py:method:: selection_list(list [, search_field])

    :param list: список для выбора
    :type list: list
    :param search_field: 0|1 строка поиска

    Создает окно со списком для выбора. Возвращает индекс выбранной строки.

    >>> appuifw.selection_list([u'1',u'2',u'3'], 1)

    .. image:: appuifw_selection_list.jpg    


.. py:method:: available_fonts() 
    
    Возвращает список, установленных шрифтов
    
    >>> appuifw.available_fonts()
    [u'Alpi12', u'Albi12', u'Alp13', u'Alpi13', u'Albi13', ... u'Series 60 ZDigi']

.. py:method:: touch_enabled() 
    
    Возвращает True если устройство сенсорное, иначе возвращает False.

app
---

.. py:class:: app

    Объект, который не нужно создавать, так как это уже произошло при загрузке модуля - просто используем его возможности. 

.. py:class:: app.body 
    
    Отвечает за рабочую область приложения (его «тело»). Может быть присвоен один из трех объектов: Text, Canvas, Listbox

    appuifw.app.body=t=appuifw.Text()

    .. py:method:: clear() 
        
        Очищает экран.
        
        >>> appuifw.app.body.clear()

.. py:attribute:: app.exit_key_handler 
    
    Обработчик кнопки выхода

    >>> def my_exit():
            pass
    >>> appuifw.app.exit_key_handler = my_exit

.. py:attribute:: app.focus 
    
    Обработчик выхода приложения в и из фокуса
    
    >>> def callback(focus):
            if focus==0:
                print u'приложение свернуто'
            elif focus==1:
                print u'приложение активно'
    >>> appuifw.app.focus = callback

.. py:attribute:: app.directional_pad 
    
    Включение отображения экранной клавиатуры

.. py:attribute:: app.menu 
    
    Список для создания меню (вызывается при нажатии на левую софт-клавишу).
    
    >>> appuifw.app.menu = [(caption1, callback1),(caption2,((caption3,callback3),(caption4, callback4)))]

    .. image:: appuifw_menu.jpg

.. py:attribute:: app.orientation 
    
    Ориентация экрана.

        * avtomatic - автоматический режим
        * portrait - вертикальный режим
        * landscape - горизонтальный режим
    
    >>> appuifw.app.orientation = 'avtomatic'

.. py:attribute:: app.screen 
    
    Размер видимой части экрана приложения.
        
        * normal - обычное отображение
        * large - без антенного бара
        * full - без антенного бара и без софт кнопок.
    
    >>> appuifw.app.screen = 'normal'

.. py:attribute:: app.title 
    
    Заголовок приложения
    
    appuifw.app.title = 'моя программа'

.. py:attribute:: app.track_allocations 
    
    Что то связанное с утечкой памяти 

.. py:method:: app.activate_tab(index) 
    
    Делает активным вклдку с номером index 

.. py:method:: app.full_name() 
    
    Возвращает полный путь к программе
    
    >>> appuifw.app.full_name()
    u'c:\\system\\apps\\Python\\Python.app'

.. py:method:: app.set_tabs(tabs [, callback])

    :param tabs: Список заголовков вкладок
    :type tabs: list
    :param calback: функция, которая выполянется при перемещении между вкладками, в которую передается индекс активной вкладки.

    Создает окно с вкладками
    
    >>> app1 = appuifw.Text(u'Text1')
    >>> app2 = appuifw.Text(u'Text2')
    >>> def callback(index):
            if index == 0:
                appuifw.app.body = app1
            elif index == 1:
                appuifw.app.body = app2

    >>> appuifw.app.set_tabs([u"One", u"Two"], callback)

    .. image:: appuifw_set_tabs.jpg    

.. py:method:: app.activate_tab(index) 
    
    Активирует указанную вкладку 

    >>> appuifw.app.activate_tab(2)

.. py:method:: app.set_exit() 
    
    Выход из программы
    
    >>> appuifw.app.set_exit()

.. py:method:: app.uid() 
    
    Возвращает строку, uid программы
    
    >>> appuifw.app.uid()
    u'10209876456'

.. py:method:: app.layout(id) 

    Метод возвращает информацию о размере (первый кортеж) и положение (второй кортеж) элементов интерфейса: экрана, различных панелей и т.д. Координаты отсчитываются с левого верхнего угла. Нужная информация выводится в зависимости от переменной id:

        * appuifw.EScreen - размер экрана
        * appuifw.EApplicationWindow - часть экрана, доступная для приложений
        * appuifw.EStatusPane - часть экрана, где находятся общие элементы для приложений - иконка, название, вкладки и т.д.
        * appuifw.EMainPane - часть экрана, где располагается главная панель приложений (рабочая область).
        * appuifw.EControlPane - часть экрана, где находится контрольная панель приложений (надписи над левой и правой софт-клавишами).
        * appuifw.ESignalPane - часть экрана, где располагается индикатор уровня сети.
        * appuifw.EBatteryPane - часть экрана, где находится индикатор уровня заряда батареи.
        * appuifw.EContextPane - часть экрана, где находится иконка приложения.
        * appuifw.ETitlePane - часть экрана, где располагается название приложения.
        * appuifw.ENaviPane - часть экрана, где расположена навигационная панель (вкладки в Настройках, например).
        * appuifw.EFindPane - часть экрана, где находится панель поиска (в нижней части Контактов, например).
        * appuifw.EWallpaperPane - часть экрана, где расположены обои (на рабочем столе).
        * appuifw.EIndicatorPane - часть экрана, где располагаются индикаторы наличия входящих SMS, включенного Bluetooth, подключенного кабеля, активированного будильника и т.д.
        * appuifw.EAColumn - часть экрана, которая используется для отображения мелких рисунков и флажков (например, иконки файлов и папок в Диспетчере файлов).
        * appuifw.EBColumn - часть экрана, которая используется для отображения списков строк (например, имена файлов и папок в Диспетчере файлов).
        * appuifw.ECColumn - часть экрана, которая используется для отображения данных, вводимые пользователем. Пересекается с EDColumn.
        * appuifw.EDColumn - часть экрана, которая используется для отображения дополнительных иконок. Пересекается с ECColumn.
        * appuifw.EStaconTop - верхняя левая часть панели контроля и статуса при ландшафтной ориентации экрана (только для Symbian 9).
        * appuifw.EStaconBottom - нижняя правая часть панели контроля и статуса при ландшафтной ориентации экрана (только для Symbian 9).
        * appuifw.EControlPaneTop - верхняя левая часть панели контроля при ландшафтной ориентации экрана:
        * appuifw.EControlPaneBottom - нижняя правая часть панели контроля при ландшафтной ориентации экрана (только для Symbian 9).
        * appuifw.EStatusPaneTop - верхняя левая часть панели статуса при ландшафтной ориентации экрана.
        * appuifw.EStatusPaneBottom - нижняя часть панели статуса при ландшафтной ориентации экрана (только для Symbian 9).
        * appuifw.EUniversalIndicatorPane - часть экрана, где располагаются индикаторы наличия входящих SMS, включенного Bluetooth, подключенного кабеля, активированного будильника и т.д. (только для Symbian 9).
    
    >>> appuifw.app.layout(appuifw.EScreen)
    ((176, 208), (0, 0))

Canvas()
--------

.. py:class:: Canvas([redraw_callback = None, event_callback = None, resize_callback = None])

    Данный объект представляет из себя «холст» который можно вывести на экран. 

    :param redraw_callback: функция, которая будет вызываться при обновлении экрана (после свертывания\развертывания программы, после выбора из меню Функции нужного пункта и т.д.). При вызове ей передается кортеж из 4 чисел - координаты левого-верхнего и правого-нижнего угла обновляемой области;
    :param event_callback: функция, которая будет вызываться при нажатии на клавиши клавиатуры. 

        При вызове ей передается словарь из 4 элементов (для сенсорных экранов 3):

        * 'type' - тип нажатия. Для определения используются переменные модуля :py:mod:`key_codes`:
        * 'keycode' - код клавиши;
        * 'scancode' - скан-код клавиши;
        * 'modifiers' - модификатор нажатия (обычное, удерживание и т.д.)
    
        Для сенсорных экранов:

        * 'type' - тип нажатия. Для определения используются переменные модуля :py:mod:`key_codes`: 
            * key_codes.EButton1Up(нажатие на экран) == 297;
            * key_codes.EButton1Down(отпускание экрана) == 303;
            * key_codes.EDrag(перемещение по экрану) == 299.       
        * 'pos' - кортеж координат;
        * 'modifiers' - модификатор нажатия (обычное, удерживание и т.д.)

    :param resize_callback: функция, которая будет вызываться при изменении размера видимой области экрана (например, при изменении переменной appuifw.app.screen). В качестве аргумента этой функции передается кортеж из 2 чисел - новая длина и высота.

    После создания, все, что мы сделаем с Canvas, немедленно отобразится на экране. А какие методы у него есть? Это все функции для работы с изображением из модуля :py:mod:`graphics`. 

    >>> canvas = appuifw.Canvas()
    >>> appuifw.app.body = canvas

.. py:attribute:: Canvas.size

    Размер

.. py:method:: Canvas.begin_redraw([(x1, y1, x2, y2)]), end_redraw() 
    
    Включает автоматическую прорисвоку UI сервера.

.. py:method:: Canvas.end_redraw() 
    
    Выключает автоматическую прорисвоку UI сервера.

.. py:method:: Canvas.bind(pointer_event, callable[, ((x1, y1), (x2, y2)) ]) 

    :param pointer_event: нажимаемая клавиша
    :param callable: функция обработчик    
    :param ((x1, y1), (x2, y2)): координаты области, в которой выполняется нажатие

    Привязывавыет нажатия клавиш/экрана на канвасе. 

.. py:method:: Canvas.blit(img, [target]) 
    
    :param img: отображаемое изображение
    :param target: смещение
    
    Отображает на канвасе изображение

    >>> canvas.blit(img, target=(10,100))

.. py:class:: Content_hadler()

Content_hadler()
----------------

Объект для открытия файлов различных типов.

    >>> new_name = appuifw.Content_handler()

.. py:method:: Content_hadler.open(filename) 
    
    Открывает файл, причем в зависимости от его типа запускается соответствующее приложение (например, картинки открываются через просмотрщик изображений).

    >>> content = appuifw.Content_handler()
    >>> content.open(u'c:\\others\\image\\my_image.jpg')

.. py:method:: Content_hadler.open_standalone(filename) 
    
    Аналогичен предыдущей функции, но приложение запускается отдельно и независимо от программы Python.

    >>> content = appuifw.Content_handler()
    >>> content.open_standalone(u'c:\\others\\image\\my_image.jpg')

Form()
------

Данный объект предсавляет диалоговое окно, элементы которого можно редактировать по своему усмотрению.

.. py:class:: Form(fields [, flags])

    :param fields: список кортежей каждый из которых отвечает за один элемент формы [(label, type [, value]),......]
        
        * label - название элемента строки
        * type - тип поля элемента
            * text - текст
            * number - целое число
            * float - вещественное число
            * date - дата
            * time - время
            * combo - список
        * value - значение элемента по умолчанию

    :param flags: настраивает вид элементов формы:
            
        * appuifw.FFormViewModeOnly - устанавливает, что поля элементов формы доступны только для просмотра (их редактирование не допускается).
        * appuifw.FFormEditModeOnly - устанавливает, что поля элементов формы доступны и для редактирования.
        * appuifw.FFormAutoLabelEdit - разрешает возможность редактирования не только полей элементов, но и их названий.
        * appuifw.FFormAutoFormEdit - разрешает динамически изменять содержимое формы (т.е. удалять и добавлять элементы прямо по ходу работы).
        * appuifw.FFormDoubleSpaced - указывает представить элементы в двухстрочном виде: на первой строке расположено имя, на втором - поле.

.. py:attribute:: Form.menu 
    
    Меню формы которому необходимо присвоить список, состоящий из кортежей. Каждый кортеж отвечает за один пункт меню. [(title, callback),..]
        * title - имя пункта
        * callback - имя функции, вызываемой сразу после нажатия на пункт.

    Меню должно быть только одноуровневым (т.е. никаких вложений). Кроме того, в случае когда установлен флаг FFormEditModeOnly (редактирования полей) появится пункт меню «Изменить». 

.. py:attribute:: From.save_hook 
    
    Этому атрибуту присваивается имя функции, которой передается единственный аргумент - содержимое формы. Задача save_hook - проверить верность введенных данных и вернуть логическое значение: True, если новое содержимое принимается как дозволенное, False - данные неприемлемы. 

.. py:method:: Form.execute() 
    
    Активирует форму
    
    >>> form.execute()

.. py:method:: Form.lenght() 
    
    Возвращает количество элементов формы 

.. py:method:: Form.insert(index, field) 
    
    Вставляет новый элемент field после элемента с индексом index 

.. py:method:: Form.pop() 
    
    Возвращает значение последнего элемента и сразу же удаляет.

Icon()
------

.. py:class:: Icon()

    Объект для работы с изображениями \*.mbm
    
    >>> icon = appuifw.Icon(u"z:\\resource\\apps\\avkon2.mbm", 28, 29)


InfoPopup()
-----------

Информационное окно 

.. py:class:: InfoPopup()

.. py:method:: InfoPopup.show(text, [(x, y), time_shown, time_before, alignment ]) 
    
    :param text: сообщение
    :type text: unicode
    :param (x, y): координаты окна
    :param time_shown: время отображения в миллисекундах
    :param time_before: время до отображения в миллисекундах
    :param alignment: выравнивание текста в окне

        * appuifw.EHLeftVTop - горизонталь - левый, вертикаль - верх
        * appuifw.EHLeftVCenter - горизонталь - левый, вертикаль - центр
        * appuifw.EHLeftVBottom - горизонталь - левый, вертикаль - низ
        * appuifw.EHCenterVTop - горизонталь - центр, вертикаль - верх
        * appuifw.EHCenterVCenter - горизонталь - центр, вертикаль - центр
        * appuifw.EHCenterVBottom - горизонталь - центр, вертикаль - низ
        * appuifw.EHRightVTop - горизонталь - правый, вертикаль - верх
        * appuifw.EHRightVCenter - горизонталь - правй, вертикаль - центр
        * appuifw.EHRightVBottom - горизонталь - правый, верх - низ

    Создает информационное окно:

    >>> import appuifw
    >>> popup = appuifw.InfoPopup()
    >>> popup.show(u'www.ilnurgi.ru\ndjango,python, pys60', (100,100),2000,2000)

    .. image:: appuifw_infopopup.jpg

.. py:method:: InfoPopup.hide() 
    
    Скрывает информационное окно.

Listbox()
---------

.. py:class:: Listbox(list, callback)

    :param list: список элементов списка
    :param callback: функция обработчик
    
    Данный объект модуля создает поле со списком строк. Для создания двухуровневого списка необходимо передать список кортежей
    
    .. code-block:: python

        import appuifw

        def callback():
            pass
        
        listbox = appuifw.Listbox([u'Part1', u'Part2', u'Part3'], callback)
        appuifw.app.body = listbox

.. py:method:: Listbox.bind(event_code, callback) 
    
    Привязывает запуск функции callback к нажатию на клавишу с кодом event_code 

.. py:method:: Listbox.current() 
    
    Возвращает номер активной строки (т.е. та, которая выделена на данный момент). 

.. py:method:: Listbox.set_list(list [,current]) 
    
    Устанавливает новый список list с уже активной строкой current (если отсутствует, то активна первая строка). 

.. py:attribute:: Listbox.position 
    
    Координаты (тупл) верхнего левого угла листбокса 

.. py:attribute:: Listbox.size 
    
    Возвращает размер листбокса

Text()
------

.. py:class:: Text()

Данный объект модуля создает текстовое тело программы.

    >>> t = appuifw.Text()

.. py:attribute:: Text.color 
    
    Определяет цвет текста
    
    >>> t.color
    (0, 128, 0)

.. py:attribute:: Text.focus 
    
    Определяет, будет ли виден курсор. По умолчанию - True (т.е. виден мигающий курсор). Если ему присвоить значение False, то он перестанет быть видимым. На проведение операции (ввод, копирование) это никак не влияет.
    
    >>> t.focus = False

.. py:attribute:: Text.font 
    
    Кортеж, который определяет: шрифт, размер шрифта, сглаживание (16-выкл/32-вкл) выводимого текста:

    >>> t.font    
    (u'Nokia Hindi S60', 15, 16)

.. py:attribute:: Text.highlight_color 
    
    Определяет цвет выделения.
    
    >>> t.hightlight_color = red

.. py:attribute:: Text.style 
    
    Определяет цвет выводимого текста:
    
    * appuifw.STYLE_BOLD - текст получается жирным.
    * appuifw.STYLE_UNDERLINE - текст получается подчеркнутым
    * appuifw.STYLE_ITALIC - текст получается курсивом.
    * appuifw.STYLE_STRIKETHROUGH - текст получается перечеркнутый линией.
    * appuifw.HIGHLIGHT_STANDARD - текст получается выделенным.
    * appuifw.HIGHLIGHT_ROUNDED - текст получается с округленным выделением.
    * appuifw.HIGHLIGHT_SHADOW - текст получается с тенью.
    
    >>> t.style = STYLE_BOLD

.. py:method:: Text.add(text) 
    
    Добавляет text в текстовое поле.
    
    >>> t.add(u'привет')

.. py:method:: Text.bind(event_code, callback) 
    
    Привязывает к нажатию клавиши с кодом event_code вызов функции по имени callback. 

.. py:method:: Text.clear() 
    
    Очищает текстовое поле.

    >>> t.clear()

.. py:method:: Text.delete([pos = 0,length=len()]) 
    
    >>> Удаляет участок текста от позиции курсора pos и длиной lenght
    
    >>> t.delete(10,20)

.. py:method:: Text.get([pos = 0,length=len()]) 

    Возвращает участок текста от позиции курсора pos и длиной lenght
    
    >>> t.get(10,20)

.. py:method:: Text.get_pos() 
    
    Возвращает текущую позицию курсора.
    
    >>> t.get_pos()
    20

.. py:method:: Text.len() 
    
    Возвращает число, длину всего текста.

    >>> t.len()
    123

.. py:method:: Text.set(text) 
    
    Очишает поле и устанавливает его как text
    
    >>> t.set(u'ilnurgi')

.. py:method:: Text.set_pos(pos) 
    
    Устанавливает курсор в позицию pos в текстовом поле.
    
    >>> t.set_pos(5)