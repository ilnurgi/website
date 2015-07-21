packages - пакеты
=================

Пакет java.lang не надо импортировать, он всегда и везде импортирован.

::

    package ru.ilnurgi1.packageName;

    import ru.ilnurgi1.packageName.className;
    import ru.ilnurgi1.packageName.*;

    // импорт всех статических методов класса
    import static java.lang.Math.*;