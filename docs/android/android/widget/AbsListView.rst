android.widget.AbsListView
==========================

.. py:class:: android.widget.AbsListView()


OnScrollListener
----------------

.. py:class:: android.widget.AbsListView.OnScrollListener()

    Интерфейс обработки скрола


    .. py:attribute:: SCROLL_STATE_IDLE

        Константа, список закончил прокрутку


    .. py:attribute:: SCROLL_STATE_TOUCH_SCROLL

        Константа, список начал прокрутку


    .. py:attribute:: SCROLL_STATE_FLING

        Константа, список прокручивается по инерции


    .. py:method:: onScroll(AbsListView view, int firstVisibleItem, int visibleItemCount, int totalItemCount)


    .. py:method:: onScrollStateChanged(AbsListView view, int scrollState)

        * scrollState

            * :py:attr:`android.widget.AdapterView.OnScrollListener.SCROLL_STATE_IDLE`
            * :py:attr:`android.widget.AdapterView.OnScrollListener.SCROLL_STATE_TOUCH_SCROLL`
            * :py:attr:`android.widget.AdapterView.OnScrollListener.SCROLL_STATE_FLING`