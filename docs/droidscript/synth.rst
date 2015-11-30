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
        


    .. js:function:: GetType() 
    
    .. js:function:: PlayMidiTune( p1) 
    
    .. js:function:: PlayNote( p1) 
    
    .. js:function:: PlayTone( p1,p2)  
    
    .. js:function:: SetDelay( p1 )    
    
    .. js:function:: SetDelayEnabled( p1 ) 
    
    .. js:function:: SetFeedback( p1 ) 
    
    .. js:function:: SetFrequency( p1 )    
    
    .. js:function:: SetNoteLength( dur )  
    
    .. js:function:: SetPhaser( p1,p2,p3,p4 )  
    
    .. js:function:: SetPhaserDryWet( p1 ) 
    
    .. js:function:: SetPhaserEnabled( p1 )    
    
    .. js:function:: SetPhaserFeedback( p1 )   
    
    .. js:function:: SetPhaserRange( p1 )  
    
    .. js:function:: SetPhaserRate( p1 )   
    
    .. js:function:: SetVca( p1,p2,p3,p4 ) 
    
    .. js:function:: SetVcaAttack( AttackTimeInMS )    
    
    .. js:function:: SetVcaDecay( DecayTimeInMS )  
    
    .. js:function:: SetVcaEnabled( OnOff )    
    
    .. js:function:: SetVcaRelease( ReleaseTimeInMS )  
    
    .. js:function:: SetVcaSustain( SustainLevel ) 
    
    .. js:function:: SetVcf( p1,p2,p3,p4,p5,p6,p7 )    
    
    .. js:function:: SetVcfAttack(AttackTimeInMS ) 
    
    .. js:function:: SetVcfCutoff( CutoffFrequencyInHz )   
    
    .. js:function:: SetVcfDecay( DecayTimeInMS )  
    
    .. js:function:: SetVcfDepth( Depth )  
    
    .. js:function:: SetVcfEnabled( OnOff )    
    
    .. js:function:: SetVcfRelease(ReleaseTimeInMS )   
    
    .. js:function:: SetVcfResonance( float Resonance )    0-1 = 0 - 100%
    
    .. js:function:: SetVcfSustain(float SustainLevel )    0 = Silent, 1= 100%
    
    .. js:function:: SetVolume( p1,p2 )    
    
    .. js:function:: SetWaveShape( p1 )    
    
    .. js:function:: Start()
    
