.. py:module:: globalui

globalui
========

Дaнный мoдyль имeeт вoзмoжнocть paбoты c глoбaльными cpeдcтвaми интepфeйca S60. 

.. py:method:: global_msg_query(message, label[, timeout = 0]) 

    :param message: отекст запроса
    :param label: заголовок окна
    :param timeout: время отображения
    
    Создает окно с запросом с выбором да или нет, возвращает 1 или 0 соответственно. 

.. py:method:: global_note(label[, type = 'info']) 
    
    :param label: заголовок окна
    :param type: тип окна

        * error, info, warn, confirm
        * text - oкнo бeз cигнaлизиpyющeй aнимaции
        * perm - aнaлoгичeн пpeдыдyщeмy (вoт тoлькo ничeм нe yбиpaeтcя)
        * wait - oкнo oжидaния    
        * charging - oкнo "зapяжaeтcя"
        * not_charging - oкнo "нe зapяжaeтcя"
        * battery_full - "aккyмyлятop зapяжeн"
        * battery_low - "aккyмyлятop paзpяжeн"
        * recharge_battery - "зapядитe aккyмyлятop"
    
    Создает информационное окно. 

.. py:method:: global_popup_menu(variables[, label[, timeout = 0]]) 

    :param variables: список
    :param label: заголовок окна
    :paran timeout: время отображения окна
    
    Создает всплывающее окно со списком для выбора. Возвращает номер находящегося под курсором элемента списка 

.. py:method:: global_query(label[, timeout = 0]) 
    
    :param label: заголовок окна, 
    :param timeout: время отображения окна
    
    Создает окно с запросом да/нет, возвращает 1 если ответили да, 0 - нет. 