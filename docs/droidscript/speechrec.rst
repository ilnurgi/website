SpeechRec
=========

.. js:class:: SpeechRec

    :js:func:`CreateSpeechRec`

    .. js:function:: Cancel()

    .. js:function:: GetRMS()

    .. js:function:: IsListening()
    
    .. js:function:: SetOnReady( callback )

        Устанавливает обработчик


    .. js:function:: SetOnResult(callback)

        Устанавливает обработчик, в который передается результат работы

        .. code-block:: js
            
            speech.SetOnResult(speech_OnResult);

            function speech_OnResult(results, partial){

            }


    .. js:function:: SetOnError( callback )

        Устанавливает обработчик обработки ошибок

        
    .. js:function:: Recognize()