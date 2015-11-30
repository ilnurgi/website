File
====

.. js:class:: File

    :js:func:`CreateFile`

    .. js:function:: Close()    

    .. js:function:: GetLength()    

    .. js:function:: GetPointer()   

    
    .. js:function:: File.ReadData( length,mode )    

        * `mode` - "Hex", "Int", "Text"

            
        .. code-block:: js
            
            file.ReadText(2) 


    .. js:function:: File.ReadNumber( type ) 
        
        * `types` - "Byte", "UByte", "Bool", "Float", "FloatLE", "Long", "LongLE", "Short", "UShort", "ShortLE", "UShortLE", "Int", "UInt", "IntLE", "UIntLE"

    
    .. js:function:: File.ReadText( type )  
    
        * `types` - 
            * `UTF` - reads a UTF-8 string with 2 byte header.
            * `Line` - reads a whole text line terminated by '\n', '\r', "\r\n"
            * `Char` - reads a big-endian 16-bit character    
        
        .. code-block:: js
            
            file.ReadText( "Line" )
    

    .. js:function:: Seek( offset )     

    .. js:function:: SetLength( length )    

    .. js:function:: Skip()     

    .. js:function:: WriteData( data,mode )
    
        * `mode` 
            * `Hex` - "FA,FB,FC"
            * `Int` - "250,251,252"
            * `Text` - "abc46" => Writes the low order 8-bit bytes.

        .. code-block:: js
            
            file.WriteData( "66,121,101", "Int" );
    

    .. js:function:: File.WriteNumber( data,type )   
    
        * `type` - "Byte", "UByte", "Bool", "Float", "FloatLE", "Long", "LongLE", "Short", "UShort", "ShortLE", "UShortLE", "Int", "UInt", "IntLE", "UIntLE"    

        .. code-block:: js
            
            file.WriteNumber( 77, "Byte" );
    

    .. js:function:: WriteText( data,type ) 
    
        * `type` - 
            * `Bytes` - Writes the low order 8-bit bytes.
            * `Chars` - Writes big-endian 16-bit characters.
            * `UTF` - Writes text encoded with UTF-8.    
            
        .. code-block:: js
            
            file.WriteText( "Hello", "Chars" );
    