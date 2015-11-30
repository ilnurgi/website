HTML - приложение
=================

Можно писать прям HTML приложение

.. code-block:: js
    
    <html>
    <head>
        <meta name="viewport" content="width=device-width">        
        <script src=file:///android_asset/app.js></script>
        <script src="file:///android_asset/Html/jquery/jquery.min.js"></script>
    </head>
        
    <script>
        //Initialise variables.                
        function OnStart() {};
    </script>

    <style>
        body 
        {  
            font: 1.5em Helvetica, Arial, sans-serif;
            vertical-align: middle;
            background: #383838; 
        }
    </style>
        
    <body onload="app.Start()">
    </body>
    </html>