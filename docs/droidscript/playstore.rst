PlayStore
=========

.. js:class:: PlayStore

    :js:func:`CreatePlayStore`
            

    .. js:function:: GetBillingInfo()

        .. code-block:: js
                        
            playStore.GetBillingInfo( prodIDs, OnStoreInfo );
            //Show Play Store prices.
            function OnStoreInfo( items )
            {
                //Show prices.
                for( var i=0; i<items.length; i++ )
                {
                    var prodId = items[i].productId;
                    var price = items[i].price;
                    alert( prodId + " = " + price );
                }
            }


    .. js:function:: GetPurchases()

        .. code-block:: js
                        
            playStore.GetPurchases(function(items){
                item = items[0];
                /* item.productId
                 * item.purchaseState
                 */
            });


    .. js:function:: Purchase()

        .. code-block:: js
            
            playStore.Purchase( prodId, "xbxrandomxbx", OnPurchased );

            //Handle completed purchase.
            function OnPurchased( prodId )
            {
                //Update purchase items array.
                purchases[prodId] = true;
                
                alert( "OnPurchased" + prodId );
            }