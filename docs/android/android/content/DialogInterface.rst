android.content.DialogInterface
===============================


.. py:class:: android.content.DialogInterface()


OnClickListener
---------------

.. py:class:: android.content.DialogInterface.OnClickListener()

    .. py:method:: onClick(DialogInterface dialog, int which)

        .. code-block:: java

            OnClickListener myClickListener = new OnClickListener() {

                public void onClick(DialogInterface dialog, int which) {
                  switch (which) {
                  // положительная кнопка
                  case Dialog.BUTTON_POSITIVE:
                    break;
                  // негаитвная кнопка
                  case Dialog.BUTTON_NEGATIVE:
                    break;
                  // нейтральная кнопка
                  case Dialog.BUTTON_NEUTRAL:
                    break;
                  }
            }