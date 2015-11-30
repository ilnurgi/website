Database
========

.. js:class:: Database

    .. js:function:: Delete()

        Удаляет БД

        .. code-block:: js
            
            db.Delete()

    .. js:function:: ExequteSql(sql)

        Выполняет sql запрос

        .. code-block:: js
            
            db.ExequteSql('select * from table');
            db.ExecuteSql( "select * from test_table;", [], OnResult ); 

            function OnResult(result){
                var item = result[0]
                /*
                 * result.rows
                 * item.id
                 * item.data
                 * item.data_num
                 */
            }

            db.ExecuteSql("INSERT INTO test_table (data, data_num) VALUES (?,?)", ["test", 100], null, function(msg){});  

    .. js:function:: .Close()    

    .. js:function:: .Delete()   

    .. js:function:: .ExecuteSql( sql, params, success, error )  

    .. js:function:: .GetName()  

    .. js:function:: .GetType()  

    .. js:function:: .openError(e)   

    .. js:function:: .openSuccess()

