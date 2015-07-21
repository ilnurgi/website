.. py:module:: java.lang

.. py:class:: StringBulder

    строка, переменной длины


    .. py:method:: StringBuilder()

        создает пустой объект с емкостью 16 символов

    
    .. py:method:: StringBuilder(int capacity)

        создает пустой объект заданной емкости capacity


    .. py:method:: StringBuilder(String str)

        создает объект емкостью str.length() + 16 , содержащий строку str


    .. py:method:: StringBuilder(CharSequence str)

        создает объект, содержащий строку str


    .. py:method:: append(String str)
    .. py:method:: append(Boolean vool)
    .. py:method:: append(Char char)
    .. py:method:: append(Integer int)
    .. py:method:: append(Long long)
    .. py:method:: append(Float float)
    .. py:method:: append(Double double)
    .. py:method:: append(Char[] char)
    .. py:method:: append(Object obj)
    .. py:method:: append(Char[] char, int offset, int len)

        добавляет строку в строку


    .. py:method:: insert(Integer ind, String str)
    .. py:method:: insert(Integer ind, Boolean vool)
    .. py:method:: insert(Integer ind, Char char)
    .. py:method:: insert(Integer ind, Integer int)
    .. py:method:: insert(Integer ind, Long long)
    .. py:method:: insert(Integer ind, Float float)
    .. py:method:: insert(Integer ind, Double double)
    .. py:method:: insert(Integer ind, Char[] char)
    .. py:method:: insert(Integer ind, Object obj)
    .. py:method:: insert(Integer ind, Char[] char, int offset, int len)
    .. py:method:: insert(int ind, СharSequence str);
    .. py:method:: insert(int ind, CharSequence sub, int start, int end);

        добавляет строку в строку


    .. py:method:: delete(int begin, int end)

        удаляет подстроку из строки


    .. py:method:: deleteCharAt(int ind)

        удаляет символ по индексу


    .. py:method:: capacity()

        возвращает емкость строки


    .. py:method:: ensureCapacity(int minCapacity)

        увеличивает емкость строки


    .. py:method:: length()

        возвращает длину строки


    .. py:method:: replace(int begin, int end, String str)

        меняет указанную последовательность строки на строку


    .. py:method:: reverse()

        меняет порядок расположения символово в строке


    .. py:method:: setLength(int newLength)

        устанавливает новую длину для строки, обрезая либо дополняя старую