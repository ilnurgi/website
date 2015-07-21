.. py:module:: uic

uic - вспомогательный модуль, для работы с ui-фалйами, сгенерированными в дизайнере
===================================================================================

.. py:method:: loadUi(path[, instance])

    :param path: путь к файлу
    :param instance: экземпляр класса

    Возвращает ссылку на объект формы, сконвертированный из формы диайнера в питон объект. 

    Если задан второй параметр `instance`, то заполняет его


.. py:method:: loadUiType()

    Возвращает кортеж из двух элементов, ссылки на клас формы и ссылки на базовый класс. 

    После создания экземпляра, необходмо вызвать метод `setupUi`.

    .. code-block:: py

        class MyWindow(Qwidget):
            def __init__(self, parent=None):
                super(MyWindow, self).__init__(parent)

                Form, Base = uic.loadUiType('myform.uic')
                self.ui = Form()
                self.ui.setupUi(self)