datarel
=======


.. code-block:: html
    
    <a href='#page2' data-rel='dialog'>Показать диалоговое окно</a>

    <div id='page2' data-role='page'>
        <div data-role='header'>Заголовок</div>
        <div data-role='content'>
            Содержимое
            <a href='#' data-role='button' data-rel='back'>
                Закрыть 
            </a>
        </div>
    </div>