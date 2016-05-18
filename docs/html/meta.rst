meta - мета информация
===============

.. code-block:: js

    <head>
        <meta charset="utf-8"/>
    <head>


charset
-------

Кодировка документа

.. code-block:: html

    <meta charset="utf-8"/>


format-detection
----------------

Автоматическое обнаружение иноформации на странице

    * telephone

        .. code-block:: html
        
            <meta name="format-detection" content="telephone=no"/>
name
----

    * description - описание

        .. code-block:: html
        
            <meta name="description" content="description"/>

    * keyword - ключевые слова

        .. code-block:: html
        
            <meta name="keyword" content="kw1, kw2"/>

    * viewport - задает логически размеры и масштабирование для окна браузера

        <meta name="viewport" content="user-scalable=no, width=device-width, initial-scale=1.0"/>

        * width = число или device-width - ширина области просмотра

        * height = число или device-height - высота области просмотра

        * user-scalable = no или yes - может ли пользователь увеличивать или уменьшать размеры контента

        * initial-scale = float число - исходный коэффициент масштабирования

        * maximum-scale = float число - максимальный лимит пользовательского увеличения

        * minimum-scale = float число - минимальный лимит пользовательского увеличения


