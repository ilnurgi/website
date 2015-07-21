.. py:module:: fullscreenwrapper2

FullScreenWrapper2 Framework
============================


.. py:class:: FullScreenWrapper2App()

    
    главный объект фреймверка, не надо создавать экземпляры данного класса, надо только использовать методы класса


    .. py:method:: close_layout()

        закрытвает лэйаут, если данный лейаут был отображен поверх другого. то на экране отобразится родительский.


    .. py:method:: event_loop()

        активизирует эвентлуп
        

    .. py:method:: exit_FullScreenWrapper2App()

        выходит из приложения


    .. py:method:: get_android_instance()

        возвращает текущий экземпляр дроида


    .. py:method:: get_property_value(id, property)

        возвращает значение атрибута объекта

        :param id: иди объекта
        :param property: атрибут объекта


    .. py:method:: initialize(droid)

        инициализация фреймверка

        :param droid: droid.Android()


    .. py:method:: set_list_contents(id, list)

        задает новый список для вью

        :param id: иди объекта
        :param list: новый список


    .. py:method:: set_property_value(id, property, value)

        задает новое свойство для атрибута объекта

        :param id: иди объекта
        :param property: атрибут объекта
        :param value: значение


    .. py:method:: show_layout(layout, show_mode=SHOW_LAYOUT_PUSH_OVER_CURRENT)

        отображает лэйаут

        :param layout: :py:class:`Layout`
        :param show_mode: тип отображения лейаута


    .. py:attribute:: SHOW_LAYOUT_PUSH_OVER_CURRENT

        отображать лейаут поверх старого


    .. py:attribute:: SHOW_LAYOUT_REPLACING_CURRENT

        отображает лейаут заменив текущий



.. py:class:: Layout(xml, title)

    Абстрактный объект, типа активити. Необходимо создать свой лейаут, отнаследовавшись от этого объекта и перекрыть методы on_show и on_close.

    :param str xml: активити в формате xml
    :param str title: заголовк окна


    .. py:method:: add_event(eventhandler)

        вешает обработчик на сам активити

        :param eventhandler: :py:class:`click_EventHandler`, `key_EventHandler`, 'itemclick_EventHandlers'


    .. py:method:: on_close()

        закрытие активити
        

    .. py:method:: on_show()

        отображает активити на экране, перед этим инициализируя все объекты активити. Без этого метода ни один из объектов активити не инициализируется. И все работы с объектами активити необходимо проводить тут, навешивание хендлеров и т.п.


    .. py:method:: remove_event(self,event_name)

        удаляет определнный евент из активити


    .. py:attribute:: views

        атрибут, через которые можно обращаться ко всем контролам активити. Представляет из себя словарь, к ключам которым можно обращаться как через точку, так и обычно, как в словарях.


.. py:class:: click_EventHandler(view, handler_function=None)

    класс, для навешивания обработчиков на клик по объектам активити

    :param view: какой-то контролл
    :param handler_function: функция обработчик


.. py:class:: itemclick_EventHandlers(view, handler_function=None)

    класс, для навешивания обработчиков

    :param view: какой-то контролл
    :param handler_function: функция обработчик


.. py:class:: key_EventHandler(key_match_id="4", view=None,handler_function=None)

    класс, для навешивания обработчиков на кнопки

    :param key_match_id: иди кнопки, по дефолту = 4, кнопка назад
    :param handler_function: функция обработчик
    :param view: вью


::

    import android, random
    from fullscreenwrapper2 import *

    class DemoLayout(Layout):
        def __init__(self):
            super(DemoLayout,self).__init__(xmldata,"FullScreenWrapper Demo")
            
        def on_show(self):
            self.add_event(key_EventHandler(handler_function=self.close_app))
            self.views.but_change.add_event(click_EventHandler(self.views.but_change, self.change_color))
            self.views.but_exit.add_event(click_EventHandler(self.views.but_exit, self.close_app))
            self.views.txt_colorbox.background="#ffffffff"
            
        def on_close(self):
            pass
        
        def close_app(self,view,event):
            FullScreenWrapper2App.exit_FullScreenWrapper2App()

        def change_color(self,view, event):
            colorvalue = "#ff"+self.get_rand_hex_byte()+self.get_rand_hex_byte()+self.get_rand_hex_byte()
            self.views.txt_colorbox.background=colorvalue
        
        def get_rand_hex_byte(self):
            j = random.randint(0,255)
            hexrep = hex(j)[2:]
            if(len(hexrep)==1):
                hexrep = '0'+hexrep   
            return hexrep 

    if __name__ == '__main__':
        droid = android.Android()
        random.seed()
        FullScreenWrapper2App.initialize(droid)
        FullScreenWrapper2App.show_layout(DemoLayout())
        FullScreenWrapper2App.eventloop()