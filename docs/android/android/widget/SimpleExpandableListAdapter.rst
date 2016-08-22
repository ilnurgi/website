android.widget.SimpleExpandableListAdapter
==========================================


.. py:class:: android.widget.SimpleExpandableListAdapter(Context context)

    .. code-block:: java

        SimpleExpandableListAdapter adapter = new SimpleExpandableListAdapter(

            // контекст
            this,

            // коллекция для групп
            // ArrayList<Map<String, String>>
            groupData,

            // слой для отображения группы
            android.R.layout.simple_expandable_list_item_1,

            // список атрибутов групп для чтения
            // String[]
            groupFrom,

            // список идентификаторов вью элементов,
            // в которые будут помещены атрибуты груп
            // int[]
            groupTo,

            // коллекция для коллекции элементов
            // ArrayList<ArrayList<Map<String, String>>>
            childData,

            // слой для отображений элемента группы
            android.R.layout.simple_list_item_1,

            // список атрибутов элементов для чтения
            // String[]
            childFrom,

            // список идентификаторов вью элементов
            // в которые будут помещены аттрибуты элементов
            // int[]
            childTo);