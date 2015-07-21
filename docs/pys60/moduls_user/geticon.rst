.. py:module:: geticon

geticon 
=======

.. py:method:: get(uid, size) 

    :param uid: uid приложения
    :type uid: int
    :param size: размер изображения
    :type size:  y

    Возвращает список битмап картинок (иконка и маска) приложения UID с размерами x,y

    >>> _img = geticon.get(0xa89fd974, (48,48))
    >>> img = Image.from_cfbsbitmap(_img[0])
    >>> img_mask = Image.from_cfbsbitmap(_img[1])