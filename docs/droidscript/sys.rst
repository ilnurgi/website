Sys
===

.. js:class:: Sys

    .. js:function:: Sys.Out( cmd )  

        cmd will be passed to shell. For example, “echo hi >/sdcard/out.txt\n”. To obtain execution results, redirect standard out (>) and/or stderr (2>) to a temporary file in a writable directory, then read it back in using app.ReadFile(). NOTE: It is important to include the newline character at the end (\n). Otherwise, your system procedure will only work the first time, and subsequent times will delay output until the DroidScript's termination. Also note that output may not be immediately available. As a workaround, If the output file does not exist yet, you can use setTimeout() to poll for output repeatedly until it arrives.


    .. js:function:: ReadFileAsByte( filename )  

        Return the decimal number for the ASCII code of the first byte of the named file.


    .. js:function:: WriteToFile( filename, string ) 

        Write the specified string to the named file. (app.WriteFile does the same)