.. py:module:: matplotlib.pyplot

pyplot
======

Оснвные методы для построения:

    * :py:func:`plot` - графики
    * :py:func:`semilogy` - график логарифметический
    * :py:func:`hist` - гистограммы
    * :py:func:`errorbar` - графики с ошибками
    * :py:func:`bar` - диаграмма вертикальная, + ошибки
    * :py:func:`barh` - диаграмма горизонтальная, + ошибки
    * :py:func:`pie` - круги, куски пирога
    * :py:func:`scatter` - распределние значений
    * :py:func:`polar` - полярная система координат


annotate()
----------

.. py:function:: annotate(text, xy, xytext, arrowprops)

    Добавляет аннотацию указанных точек и возвращает :py:class:`matplotlib.text.Text`

    * arrowprops - словарь, описание указателя на точку

        * alpha

        * arrowstyle - стиль стрелки

            * -
            * -> -> head_length=0.4, head_width=0.2
            * -[ -> WidthB=1.0, lengthB=0.2, angleB=None
            * <- -> head_length=0.4, head_width=0.2
            * <-> -> head_length=0.4, head_width=0.2
            * fancy -> head_length=0.4, head_width=0.4, tail_width=0.4
            * simple -> head_length=0.5, head_width=0.5, tail_width=0.2
            * wedge -> tail_width=0.3, shrink_factor=0. 5

        * color

        * connectionstyle - стиль соединения с точкой

            * arc -> angleA=0, angleB=0, armA=None, armB,=None, rad=0.0
                * arc,angleA=10,armA=30,rad=15

            * arc3 -> rad=0.0
                * arc3,rad=.2
                * arc3,rad=-.2

            * angle -> angleA=90, angleB=0, rad=0.0
            * angle3 -> angleA=90, angleB=0
            * bar -> armA=0.0,armB=0.0,fraction=0.3,angle=None

        * facecolor - цвет курсора

        * frac

        * headwidth

        * linestyle

        * linewidth

        * mutation_scale

        * shrink - отступ от точки

        * width

    * text - сообщение

    * xy - кортеж, координата точки

    * xytext - кортеж, координата где отображать текст

    .. code-block:: py

        annotate(
            'message',
            xy=(6, 30),
            xytext=(8, 31.5),
            arrowprops={
                'facecolor': 'black',
                'shrink': 0.05
            });


arrow()
-------

.. py:function:: arrow(x, y, dx, dy)

    Рисует стрелку на графике


axis()
------

.. py:function:: axis([new_axis])

    Устанавливает или возвращает предельные координаты по осям: [xmin, xmax, ymin, ymax]

    Также можно задать параметры через kwargs

    .. code-block:: py

        axis()
        (1.0, 4.0, 0.0. 12.0)

        axis([0, 5, -1, 13])


bar()
-----

.. py:function:: bar(x, y, **kwargs)

    * align - выравнивание столбцов относительно значения

        * edge
        * center

    * bottom
    * color - цвета столбцов
    * edgecolor - цвета границ столбцов
    * width - ширина столбцов, по умолчанию 0.8
    * xerr
    * yerr

    Диаграмма вертикальная


barh()
------

.. py:function:: barh()

    Диаграмма горизонтальная, аналогичная :py:func:`matplotlib.pyplot.bar`


draw()
------

.. py:function:: draw()

    Рисует изображение


errorbar()
----------

.. py:function:: errorbar(x, y, yerr, xerr, fmt, ecolor, elinewidth, capsize)

    Строит какой то график

    .. code-block:: py

        errorbar(
            numpy.arange(0, 4, 0.2),
            numpy.exp(-x),
            0.1 * numpy.abs(
                numpy.random.randn(len(y))),
            fmt=".-"
        )

        errorbar(x, y, yerr=e1, xerr=e2)
        errorbar(x, y, yerr=[e1, e2])


figtext()
---------

.. py:function:: figtext()

     Возвращает :py:class:`matplotlib.text.Text`


figure()
--------

.. py:function:: figure(figsize)

    Возвращает :py:class:`matplotlib.figure.Figure`


    .. code-block:: py

        fig = figure(figsize=(3, 3))


grid()
------

.. py:function:: grid(bool)

    Включает отображение сетки по значениям осей

    .. code-block:: py

        grid(True)


hist()
------

.. py:function:: hist(values[, bin=10])

    Строит гистограмму для входящих данных.

    По умолчанию делит данные на 10 отрезков

    .. code-block:: py

        hist([1, 1, 1, 0])


hold()
------

.. py:function:: hold(bool)

    Отображает пустое окно

    .. code-block:: py

        hold(True)


interactivity()
---------------

.. py:function:: interactivity(bool)

    Включает интерактинвый режим, изображение перерисовывается
    при каждом вызове метода :py:func:`plot`.

    Смотрите также:

        * :py:func:`ioff`
        * :py:func:`ion`
        * :py:func:`isinteractive`

    .. code-block:: py

        interactivity(True)


ioff()
------

.. py:function:: ioff()

    Выключает интерактинвый режим

    Смотрите также:

        * :py:func:`ion`
        * :py:func:`interactivity`
        * :py:func:`isinteractive`

    .. code-block:: py

        ioff()


ion()
-----

.. py:function:: ion()

    Включает интерактинвый режим

    Смотрите также:

        * :py:func:`ioff`
        * :py:func:`interactivity`
        * :py:func:`isinteractive`

    .. code-block:: py

        ion()


isinteractive()
---------------

.. py:function:: isinteractive()

    Возвращает :py:class:`bool`, включен интерактинвый режим

    Смотрите также:

        * :py:func:`ioff`
        * :py:func:`ion`
        * :py:func:`interactivity`

    .. code-block:: py

        isinteractive()
        # True


legend()
--------

.. py:function:: legend([**kwargs])

    Возвразает или отображаем легенду :py:class:`matplotlib.legend.Legend`

    * borderaxespad - величина зазора между осями и легендой

    * legend_names - список названии легенд, лучше задавать при построении графика

    * loc - местоположение вывода данных легенды, можно задачть как числом так и строкой,
      а также кортежом позиции

        * 0 - best
        * 1 - upper right
        * 2 - upper left
        * 3 - lower left
        * 4 - lower right
        * 5 - right
        * 6 - center left
        * 7 - center right
        * 8 - lower center
        * 9 - upper center
        * 10 - center



    .. code-block:: py

        legend()
        legend(['Legend1', 'Legend2'])
        legend(loc=(-0.1, 0.9))
        legend(loc='best')
        legend(loc=3)

    * mode

        * expand - растянуть легенду по всей ширине

    * ncol - количество столбцов для легенды


pie()
-----

.. py:function:: pie(x, **kwargs)

    Кусок пирога

    * colors - цвета секторов
    * explode - список уровней выдвижения секторов
    * labels - список заголовков секторов
    * shadow - булево, добавить тень
    * labeldistance
    * autopct
    * pctdistance

    .. code-block:: py

        pie([10, 30, 60], ['Red', 'Green', 'Blue'])
        pie(
            x,
            labels,
            explode=[0.2, 0.1, 0.0],
            autopct="%1.1f%%",
        )


plot()
------

.. py:function:: plot(*args, **kwargs)

    Создает график

    * color - цвет линии

    * label - строка легенды

    * line_format - идет сразу после координат,
      тип линии, цвет линии, маркер точек, задается строкой

        Типы линии

        * - - сплошная линия
        * -- - пунктирная линия
        * -. - пнутирная с точкой
        * : - точечный график

        Цвета

        * b - синий
        * c - голубой
        * g - зеленый
        * k - черный
        * m - фиолетовый
        * r - красный
        * w - белый
        * y - желтый
        * 'red'
        * '#ff00ff' - hex
        * (1, 0, 1, 1) - RGBA
        * '0.7' - оотенки серого

        Маркеры точек

        * ., , - точка
        * \*, +, \|, - -
        * V, ^, <, > - треуголник
        * 1, 2, 3, 4 -
        * o - круг
        * D - ромбик
        * d -
        * H -
        * h -
        * s - квадрат
        * p - пятиуголник
        * X -
        * x -

    * linestyle  - стиль линии

    * linewidth - ширина линии

    * marker - маркер точек

    * markeredgecolor - цвет граней маркера

    * markeredgewidth - ширина грней маркера

    * markerfacecolor - цвет заливки маркера

    * markersize - размер маркера



    .. code-block:: py

        # строит график по указанным у координатам
        # каждой у соответсвует х от 0
        plot([1, 3, 2, 4])

        # строит график по указанным x, y координатам
        x = range(6)
        y = [i**2 for i in x]
        plot(x, y)

    .. code-block:: py

        # строит график по указанным x, y координатам
        x = range(6)
        y = [i**2 for i in x]
        y1 = [i*3 for i in x]
        plot(x, y, x, y1)

    .. code-block:: py

        # график с красной линией
        plot([1, 3, 2, 4], 'r')

        # графики с цветами
        plot(
            x, y, 'r',
            x, y1, 'y')

        # типы линии
        plot(
            x, y, '--',
            x, y1, '-.')

        plt.plot(

            # голубой, пунктирный, маркеры - х
            y, 'cx--',

            # фиолетовый, точечный, маркер - круг
            y+1, 'mo:',

            # черный, тире и точка, маркер - пятиуголник
            y+2, 'kp-.')

        plt.plot(
            y,
            color='blue',
            linestyle='dashdot',
            linewidth=4,
            marker='o',
            markerfacecolor='red',
            markeredgecolor='black',
            markeredgewidth=3,
            markersize=12);


polar()
-------

.. py:function:: polar()

    Полярная система координат

    .. code-block:: py

        # окружность от 0 до 2pi
        theta = numpy.arange(0., 2., 1./180.)*numpy.pi

        # спираль
        plt.polar(3*theta, theta/5);

        # цветок
        plt.polar(theta, numpy.cos(4*theta));

        # круг
        plt.polar(theta, [1.4]*len(theta));


rgrid()
-------

.. py:function:: rgrid([radii, labels, angle=22.5])

    Используется для полярных систем :py:func:`polar`

    Настройка круговых линии

    Возвращает два занчения, линии окружности и их заголовки или соответственно задает

    * radii - растояние между радиальных окружностей сетки

    * labels - заголовки

    * angle - шаг отображения градусов

    .. code-block:: py

        # отображаем радиальные углы
        plt.rgrids(np.arange(0.2, 3.1, .7), angle=0)


savefig()
---------

.. py:function:: savefig(file_path[, dpi])

    Сохраняет график в файл или любой другой записываемый объект,
    с параметрами по умолчанию

    * dpi - количество точек на дюйм

    .. code-block:: py

        savefig("some_plot.png")
        savefig(open("some_plot.png", 'w'))


scatter()
---------

.. py:function:: scatter(x, y, s, c, marker)

    Распределение значений

    * s - размер маркера, как для 1 значения так и для списка

    * color - цвет маркера, как для 1 значения так и для списка

    .. code-block:: py

        scatter(x, y)


semilogy()
----------

.. py:function:: semilogy()

    Логарифмическая диаграмма

    Аналогично :py:func:`plot`


setp()
------

.. py:function:: setp()

    Устаналивает свойства для объектов

    .. code-block:: py

        # задаем свойства для текстовых элементов
        setp(text, fontsize=16, color='green')

        # задает свойство для всех текстовых элементов ax элемента
        setp(ax.get_ticklabels(), fontsize=5.)


show()
------

.. py:function:: show()

    Отображает окно с графиком

    .. code-block:: py

        show()


suptitle()
----------

.. py:function:: suptitle()

     Возвращает :py:class:`matplotlib.text.Text`


text()
------

.. py:function:: text(x, y, text, **kwargs)

    Рисует указанный текст на указанной позиции и
    возвращает :py:class:`matplotlib.text.Text` (withdash=False) или
    :py:class:`matplotlib.text.TextWithDash` (withdash=True)

    * alpha - прозрачность

    * background - цвет фона шрифта

        * blue
        * r
        * #11aa55
        * (0.4, 0.5, 0.3)
        * 0.7

    * bbox - словарь, описание рамки вокруг текста

        * edgecolor - цвет рамки
        * facecolor - цвет заливки рамки
        * fill - булево, заливка
        * linestyle - стиль рамки
            * solid - обычная рамка
            * dashed - штрих-пунктир
            * dashdot - штрихпунктир
            * dotted - точечный
        * linewidth - толщина линии рамки
        * hatch - штриховка внутри рамки
            * "/"
            * "\"
            * "|"
            * "-"
            * "+"
            * "x"
            * "o"
            * "O"
            * "."
            * "*"
        * visible - булево, рамка видима
        * boxstyle - внешний вид рамки
            * square
            * sawtooth
            * roundtooth
            * rarrow
            * larrow
            * round64
            * round

    * color - цвет шрифта

        * blue
        * r
        * #11aa55
        * (0.4, 0.5, 0.3)
        * 0.7

    * family - семейство шрифта

        * sans-serif
        * serif
        * fantasy
        * monospace
        * verdana

    * fontdict - словарь, описывающий шрифт

        * family

    * rotation - поворот текста

        * horizontal
        * vertical
        * 45

    * size - размер шрифта

        * xx-small
        * x-small
        * small
        * medium
        * large
        * x-large
        * xx-large

    * style - стиль

        * normal
        * italic
        * oblique

    * weight - толщина шрифта

        * ultralight
        * light
        * normal
        * regular
        * book
        * medium
        * roman
        * semibold
        * demibold
        * demi
        * bold
        * heavy
        * bold
        * black
        * 200

    * withdash - :py:class:`bool`, текст с линией

    .. code-block:: py

        text(0.1, -0.04, "text")


thetagrid()
-----------

.. py:function:: thetagrid([angles, labels, frac])

    Используется для полярных систем :py:func:`polar`

    Настройка линии для углов

    .. code-block:: py

        # отображаем только углы от 45 до 360 с шагом 90
        thetagrids(range(45, 360, 90))


title()
-------

.. py:function:: title(label)

    Устанавливает подпись для графика и возвращает :py:class:`matplotlib.text.Text`

    .. code-block:: py

        title("Plot")


xkcd()
------

.. py:function:: xkcd(scale=1, length=100, randomness=2)

    Включает эффект рисования от руки

    Можно использовать как контекстный процессор

    .. code-block:: py

        with xkcd():
            pass


xlabel()
--------

.. py:function:: xlabel(label)

    Устанавливает подпись для оси х и возвращает :py:class:`matplotlib.text.Text`

    .. code-block:: py

        xlabel("X axis")


xlim()
------

.. py:function:: xlim([new_xlim])

    Аналогично :py:func:`matplotlib.pyplot.axis` возвращает или устанавливает
    предельные значения по оси х

    .. code-block:: py

        xlim()
        # (1.0, 4.0)

        xlim([0, 5])


xticks()
--------

.. py:function:: xticks([locations [, labels]])

    Возвращает или задает настройки для х оси

    .. code-block:: py

        locations, labels = xticks()

        # меняем символы на точках оси
        xticks(
            range(len(x)),
            ['a', 'b', 'c'])

        # отображаем только указанные точки
        xticks(range(len(1, 8, 2)))


yticks()
--------

.. py:function:: yticks([locations [, labels]])

    Возвращает или задает настройки для y оси

    Аналогично :py:func:`xticks`


ylabel()
--------

.. py:function:: ylabel(label)

    Устанавливает подпись для оси y и возвращает :py:class:`matplotlib.text.Text`

    .. code-block:: py

        ylabel("Y axis")


ylim()
------

.. py:function:: ylim([new_ylim])

    Аналогично :py:func:`matplotlib.pyplot.axis` возвращает или устанавливает
    предельные значения по оси y

    .. code-block:: py

        ylim()
        # (0.0, 12.0)

        ylim([-1, 13])
