DocumentFragment - смежные узлы и их поддеревья
===============================================

Вставка в документ большого количества элементов влияет на производительность,
для облегчения пользуются фрагментами,
которые представляют собой контейнеры для других элементов.


.. js:class:: DocumentFragment()

    Наследник :js:class:`Node`

    .. code-block:: js

        var fragment = document.createDocumentFragment();
        fragment.appendChild(element);
