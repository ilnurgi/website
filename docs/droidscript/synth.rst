Synth - синтезатор
==================

.. js:class:: Synth

    :js:func:`CreateSynth`


    .. js:function:: PlayMidiTune()

        .. code-block:: js
            
            synth.PlayMidiTune("46:16,40:16,35:4");


    .. js:function:: PlayTone()

        .. code-block:: js
            
            synth.PlayTone(1000, 1400);


    .. js:function:: SetDelay(val)

    .. js:function:: SetFeedback()

    .. js:function:: SetFrequency()

        .. code-block:: js
            
            synth.SetFrequency(500 + 500 * Math.random());


    .. js:function:: SetNoteLength()

        .. code-block:: js

            synth.SetNoteLength(2.5);
        
        
    .. js:function:: SetPhaserEnabled(val)
    .. js:function:: SetDelayEnabled(val)
    .. js:function:: SetPhaserDryWet(val)
    .. js:function:: SetPhaserFeedback(val)
    .. js:function:: SetPhaserRange(val)
    .. js:function:: SetPhaserRate(val)


    .. js:function:: SetVca()

        .. code-block:: js
            
            synth.SetVca(10, 400, 0.8, 100);


    .. js:function:: SetVcaAttack(val)
    .. js:function:: SetVcaDecay(val)
    .. js:function:: SetVcaRelease(val)
    .. js:function:: SetVcaSustain(val)


    .. js:function:: SetVcf()

        .. code-block:: js
            
            synth.SetVcf(10, 400, 0.8, 100, 1000, 0.85, 2.0);


    .. js:function:: SetVcfAttack(val)
    .. js:function:: SetVcfCutoff(val)
    .. js:function:: SetVcaDecay(val)

    .. js:function:: SetVcfEnabled()

        .. code-block:: js
            
            synth.SetVcfEnabled(false);


    .. js:function:: SetVcaRelease(val)
    .. js:function:: SetVcaResonans(val)
    .. js:function:: SetVcaSustain(val)


    .. js:function:: SetVolume()

        .. code-block:: js
            
            synth.SetVolume(0.5, 0.5);


    .. js:function:: SetWaveShape()

        .. code-block:: js

            synth.SetWaveShape('Square');
            synth.SetWaveShape('Sin');
            synth.SetWaveShape('Saw');
            synth.SetWaveShape('White');


    .. js:function:: Start()
    .. js:function:: Stop()
        
        