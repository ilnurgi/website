MediaStore
==========

.. js:class:: MediaStore

    :js:func:`CreateMediaStore`


    .. js:function:: GetAlbumArt();

        .. code-block:: js
            
            var ok = media.GetAlbumArt( img, result[1].id, "external" );

            
    .. js:function:: QueryAlbums();

        .. code-block:: js
            
            media.QueryAlbums("", "", "external");


    .. js:function:: QueryArtists();

        .. code-block:: js
            
            media.ueryArtist("", "", "external");


    .. js:function:: QueryMedia();

        .. code-block:: js
            
            media.QueryMedia("", "artist,album", "external");


    .. js:function:: SetOnAlbumsResult(callback);

        .. code-block:: js
            
            media.SetOnAlbumsResult(media_OnAlbumResult);

            function media_OnAlbumResult(result){

                var item = result[0];
                /* item.id
                 * item.artist
                 * item.album
                 * item.numSongs
                 */
            }


    .. js:function:: SetOnArtistsResult(callback);

        .. code-block:: js
            
            media.SetOnMediaResult(media_OnArtistResult);

            function media_OnArtistResult(result){

                var item = result[0];
                /* item.id
                 * item.artist
                 * item.numAlbums
                 * item.numTracks
                 */
            }


    .. js:function:: SetOnMediaResult(callback);

        .. code-block:: js
            
            media.SetOnMediaResult(media_OnMediaResult);

            function media_OnMediaResult(result){

                var item = result[0];
                /* item.title
                 * item.albumId
                 * item.album
                 * item.artistId
                 * item.artist
                 * item.duration
                 * item.size
                 * item.uri
                 */
            }

MediaStore.GetAlbumArt( img,id,options )    
MediaStore.GetSongArt( img,id,options )     
MediaStore.QueryAlbums( filter,sort,options )   
MediaStore.QueryArtists( filter,sort,options )  
MediaStore.QueryMedia( filter,sort,options )    
MediaStore.SetOnAlbumsResult( callback )    
MediaStore.SetOnArtistsResult( callback )   
MediaStore.SetOnMediaResult( callback )