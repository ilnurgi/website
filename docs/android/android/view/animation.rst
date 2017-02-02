android.view.animation.Animation
================================

.. py:class:: android.view.animation.Animation


android.view.animation.AnimationUtils
=====================================

.. py:class:: android.view.animation.AnimationUtils()


    .. py:method:: currentAnimationTimeMillis()

        Возвращает long, время воспроизведения анимации


    .. py:method:: loadAnimation(Context context, int id)

        Статический метод, возвращает загруженную анимацию :py:class:`android.view.animation.Animation`

        Возбуждает исключения:

        * :py:class:`android.content.res.Resources.NotFoundException` - если ресурс не найден

        .. code-block:: java

            Animation anim = AnimationUtils.loadAnimation(this, R.anim.some_anim);
            btn.startAnimation(anim);