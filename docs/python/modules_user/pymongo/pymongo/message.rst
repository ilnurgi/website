.. py:module:: pymongo.message

message - инструмент для создания сообщении, отправляемых в БД
==============================================================

.. py:method:: delete(collection_name, spec, safe, last_error_args, opts, flags=0)

    Возвращает удаляемое сообщение

    * `opts` -  CodecOptions

    * `flags` - битовая маска флагов


.. py:method:: get_more(collection_name, num_to_return, cursor_id)

    Возвращает getMore сообщение


.. py:method:: insert(collection_name, docs, check_keys, safe, last_error_args, continue_on_error, opts)

    Возвращает вставляемое сообщение


.. py:method:: kill_cursors(cursor_ids)

    Возвращает killCursors сообщения


.. py:method:: query(options, collection_name, num_to_skip, num_to_return, query, field_selector, opts)

    Возвращает query сообщение


.. py:method:: update(collection_name, upsert, multi, spec, doc, safe, last_error_args, check_keys, opts)

    Возвращает update сообщение