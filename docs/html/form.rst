Формы и её элементы
===================

button
------

Кнопка, строчный элемент

* autofocus

    .. note:: HTML5

* disabled

    Блокирует элемент

* form

    .. note:: HTML5

    Идентификатор формы элемента

* formaction

    .. note:: HTML5    

    Ссылка обработчик кнопки

* formenctype

    .. note:: HTML5

    Тип контента

* formmethod

    .. note:: HTML5

    Метод HTTP для передачи данных формы

* formnovalidate

    .. note:: HTML5

    Не проверять форму при передачи данных

* formtarget

    .. note:: HTML5

    Окно, в котором отображаются результаты передачи данных формы.

* menu

    .. note:: HTML5

    Если тип кнопки меню, то это ссылка на элемент меню

* name

    Обязательное поле, название элемента

* type

    Поведение кнопки

    * submit - по умолчанию, кнопка передачи данных

    * reset - сброс формы

    * button - кнопка, управляемая через JavaScript

    * menu - меню

* value

    Значение элемента

.. code-block:: html

    <Ьutton type="reset" name="reset">
        <img src = "thumbs-down.gif" alt="thumbs-down icon">
        Попробуйте cнoвa
    </button>


fieldset
--------

Группа элементов управления формой

* disabled - отключает элементы группы

* form - идентификатор формы

    .. note:: HTML5

* name - имя элемента

    .. note:: HTML5

.. code-block:: html

    <form>
        <fieldset id="customer">
            <legend>...</legend>
            <label>...<input></label>
            <label>...<input></label>
        </fieldset>
    </form>


form
----

Интерактивная форма

* accept-charset - список кодировок символов входящих данных

* action - ссылка на ресурс, обработчик формы

* autocomplete - автозаполнение

    * on

    * off

* enctype - тип контента

* method - метод отправки формы

    * post

    * get

* name - имя формы

* novalidate - форма не была верифицирована при передаче данных

    .. note:: HTML5

* target - цель результатов передачи данных формы, которые должны быть загружены

    * _bottom

    * _top

    * _parent

    * _self
    
.. code-block:: html
    
    <form></form>