Лейауты, вьюхи
==============

Основные виды лейаутов:
-----------------------

* :ref:`android.widget.LinerLayout` - отображает view-элементы в виде одной строки (вертикальный экран) или одного столбца (горизонтальный экран)
* :ref:`android.widget.TableLayout` - отображает view-элементы в виде таблицы, по строкам и столбцам. Он состоит из строк TableRow (TR). Каждая TR в свою очередь содержит View-элементы, формирующие столбцы. Т.е. кол-во View в TR - это кол-во столбцов. Но кол-во столбцов в таблице должно быть равным для всех строк. Поэтому, если в разных TR разное кол-во View-элементов (столбцов), то общее кол-во определяется по TR с максимальным кол-вом.
* :ref:`android.widget.RelativeLayout` - для каждого элемента настраивается его положение относительно других элементов
* :ref:`android.widget.AbsoluteLayout` - для каждого элемента указывается явная позиция на экране в системе координат, возможно уберут в будущем
* :ref:`android.widget.FrameLayout` - элементы добавляются слева в верхний угол

Основные виды вьюх:
-------------------

* :ref:`android_widget_TextView`

* :ref:`android_widget_EditText`

* :ref:`android_view_ListView`

* android:id - иденификатор 
  
  * "@+id/textView1"

* android:layout_width, android:layout_height - лэйаут заполнения по горизонтали/верткали

  * "wrap_content" - по содержимому
  * "match_parent" - по родителю
  * "100dp"

* android:layout_weight - цифра, характеризует область, в которой распологается элемент
    
  * 1, 2, 3 ...

* android:layout_gravity - расположение внутри родителя относительно краев
    
  * top\left\right\bottom\center

* android:layout_x, android:layout_y - абсолютные расположения

* android:layout_toLeftOf, android:layout_toRightOf, android:layout_above, android:layout_below - расположение элемента относительно указанного, слева, справа, сверху, снизу

  * "@+id/label" - указатель на элемент по id

* android:layout_alignLeft, android:layout_alignRight, android:layout_alignTop, android:layout_alignBottom - выравнивание элемента относительно укзанного по краям, слева, справа, сверху, снизу

* android:layout_alignParentLeft, android:layout_alignParentRight, android:layout_alignParentTop, android:layout_alignParentBottom - выравнивание элемента относительно родителя, слева, справа, сверху, снизу

* android:layout_centerVertical, android:layout_centerHorizontal, android:layout_centerInParent - выравнивание элемента по центру вертикально, по центру горизонтально, по центру веритикально и горизонтально относительно родителя

  * "true"

* android:layout_margin, android:layout_marginLeft, android:layout_marginRight, android:layout_marginBottom, android:layout_marginTop - отступы

  * "10dip"

* android:background 

* android:orientation - ориентация

  * "vertical"
  * "horizontal"

* android:text - текст

  * "@string/helo_world"

* android:textSize - размер текста


* android:paddingBottom 
* android:paddingLeft
* android:paddingRight
* android:paddingTop
* android:padding
* android:scrollbars
* android:fadingEdge
* tools:context

* android:onClick - имя метода обрабочика



dp или dip - Density-independent Pixels. Абстрактная ЕИ, позволяющая приложениям выглядеть одинаково на
различных экранах и разреш ениях.
sp - Scale-independent Pixels. То же, что и dp, только используется для размеров ш рифта в View элементах
pt - 1/72 дюйма, определяется по физическому размеру экрана. Эта ЕИ из типографии.
px – пиксел, не рекомендуется использовать т.к. на разных экранах приложение будет выглядеть по-разному.
mm – миллиметр, определяется по физическому размеру экрана
in – дюйм, определяется по физическому размеру экрана