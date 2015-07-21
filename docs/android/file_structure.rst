Описание файловой структуры проектов
====================================

* `src` – все исходные коды
* `gen` – генерируемые средой файлы, необходимые для приложения. Здесь лучше ничего не трогать. (Если этой папки нет что-нибудь измените в проекте и нажмите кнопку сохранить).
* `Android x.x.x` – необходимые для приложения Android-библиотеки
* `assets` – папка для файлов-ресурсов различного типа
* `res` – папка для файлов-ресурсов различного типа
  
  * `anim` - содержит анимации, alpha (затемнение), scale (масштабирование), translate (перемещение) или rotate (поворот)

  * `drawable` - содержит изображения

  * `values-???-???...` - ресурсы приложения по модификаторам

    * `Мобильный код страны и код мобильного оператора (MCC/MNC)` - http://en.wikipedia.org/wiki/Mobile_Network_Code
    * `Язык и регион` - en, fr ....
    * `Размер экрана` - small (меньше, чем HVGA), medium (HVGA или меньше, чем VGA) или large (VGA или больше)
    * `Высота и ширина экрана` - long или notlong
    * `Ориентация экрана в пространстве` - port (портретный), land (альбомный) и square (если высота экрана равна ширине)
    * `Плотность пикселов на экране` - ldpi, mdpi и hdpi
    * `Тип сенсорного экрана` - notouch, stylus или finger
    * `Наличие клавиатуры` - keysexposed, keyshidden или keyssoft
    * `Тип ввода` - nokeys, qwerty или 12key
    * `Способ навигации` - nonav, dpad, trackball или wheel

  * `values` - ресурсы приложения    

    * `string` - строковые ресурсы

      ::

        <string name='name'>value</string>

    * `color` - ресурсы цвета (RGB, ARGB)

      ::

        <color name='name'>#001100</color>

    * `dimen` - ресурсы размеров (px, in, pt, mm, dp, sp)

      ::

        <dimen name="standard_border">5dp</dimen>

    * `style` - стиль

      ::

        <style name="StyleName" parent="ParentStyleName">
          <item name="attributeName">value</item>
          <item name="android:textSize">14sp</item>
        </style>  

  * `layout` - папка лейауты для вертикалей

  * `layout-land` - папка лейауты для горизонтали

  * `menu` - папка с меню

    ::

        <menu>
            <item
                android:id="@+id/menu_copy"
                android:orderInCategory="1"
                android:title="copy">
            </item>
            <group android:id="@+id/group1">
                <item
                    android:id="@+id/menu_copy"
                    android:orderInCategory="1"
                    android:title="copy">
                </item>
            </group>
        </menu>

* `AndroidManifest.xml` – манифест или конфиг-файл приложения

  * `manifest` - включает в себя узлы, описывающие программные компоненты, настройки безопасности, классы для тестирования и требования, из которых состоит приложение. 

    * `package` - пакет проекта
    * `android:versionCode` - внутренняя версия, число
    * `android:versionName` - внешняя версия, строка
    * `uses-sdk`  - версии SDK, которые должны быть доступны на устройстве, чтобы приложение смогло правильно функционировать. Основываясь на версии SDK, можно ограничить круг устройств, способных запускать приложение.

      * `minSDKVersion` - указывает на минимальную версию SDK, содержащую API, которая используется в вашей программе. Если не зададите минимальную версию, применится значение по умолчанию, а ваше приложение не сможет корректно работать, если попытается получить доступ к API, которые недоступны на текущем устройстве.
      * `maxSDKVersion` - позволяет определить самую позднюю версию, которую вы готовы поддерживать. Ваше приложение будет невидимым в Android Market для устройств, управляемых системой с более свежей версией. Устанавливать значение для этого атрибута рекомендуется только в том случае, если вы абсолютно уверены, что приложение не работает на платформе с версией, выше заданной.
      * `targetSDKVersion` - позволяет указать платформу, для которой вы разрабатывали и тестировали приложение. Устанавливая значение для этого атрибута, вы сообщаете системе, что для поддержки этой конкретной версии не требуется никаких изменений, связанных с прямой или обратной совместимостью.

    * `uses-configuration` - механизмы ввода данных, поддерживаемые вашим приложением

      * `reqFiveWayNav` — true, если необходимо устройство ввода, поддерживающее навигацию вверх, вниз, влево, вправо, а также нажатие выделенного элемента; в эту категорию входят как трекболы, так и манипуляторы D-pad;
      * `reqHardKeyboard` — если вашему приложению нужна аппаратная клавиатура, укажите значение true;
      * `reqKeyboardType` — позволяет задать тип клавиатуры — nokeys, qwerty, twelvekey или undefined;
      * `reqNavigation` — если требуется устройство для навигации, укажите одно из следующих значений — nonav, dpad, trackball, wheel или undefined;
      * `reqTouchScreen` — если вашему приложению понадобится сенсорный экран, выберите одно из следующих значений — notouch, stylus, finger или undefined.
    
    * `uses-feature` - аппаратные возможности. Это предотвратит установку программы на устройства, которые не соответсвуют аппаратным требованиям. 

      * `android.hardware.camera` - если для работы приложения нужна аппаратная камера
      * `android.hardware.camera.autofocus` - если требуется камера с автоматической фокусировкой
      * `android:glEsVersion` - версия OpenGL ES в виде целого числа. Первые 16 бит соответствуют мажорной версии, а последние — минорной ("0x00010001")
      * http://developer.android.com/guide/topics/manifest/uses-feature-element.html.

    * `supports-screens` - экранные размеры, которые поддерживаются (и не поддерживаются) вашим приложением.

      * `smallScreens` — экраны с разрешением меньшим, чем обычное HVGA, как правило, речь идет о QVGA;
      * `normalScreens` — используется для описания экранов стандартных мобильных телефонов, как минимум HVGA, включая HVGA и WQVGA;
      * `largeScreens` — экраны больших размеров, значительно больше, чем у мобильного телефона;
      * `anyDensity` — установите значение true, если ваше приложение способно масштабироваться для отображения на экране с любым разрешением.
    
    * `аpplication` - метаданные приложения (включая его название, значок и визуальный стиль). 

      * `аctivity` - требуется для каждой Активности, которую отображает приложение.

        * `name` - имя класса Активности.
        * `label` - заголовок Активности.
        * `theme` - тема для Активности
        * `configChanges` - обработка событий при изменений конфигурации

          * `оrientation` — положение экрана изменено с портретного на альбомное (или наоборот);
          * `keyboardHidden` — клавиатура выдвинута или спрятана;
          * `fontScale` — пользователь изменил предпочтительный размер шрифта;
          * `locale` — пользователь выбрал новые языковые настройки;
          * `keyboard` — изменился тип клавиатуры; например, телефон может иметь 12-клавишную панель, при повороте которой появляется полноценная клавиатура;
          * `touchscreen` или `navigation` — изменился тип клавиатуры или способ навигации. Как правило, такие события не встречаются.

        * `intent-filter` - Намерения Активности

    * `service` - каждый класс Сервиса должен иметь тег service

      * `intent-filter` - Намерения Сервиса

    * `provider` - все Провайдеры в приложении.

    * `receiver` - регистрация Широковещательного приемника, не запуская при этом приложение. 

    * `uses-permission` - описывают полномочия, которые, по вашему мнению, нужны приложению для полноценной работы. 

    * `permission` - ограничения доступа к компоненту приложения

    * `instrumentation` - Классы, производные от Instrumentation, предоставляют фреймворк для тестирования программных компонентов во время их выполнения. Они содержат методы-перехватчики, с помощью которых отслеживаются работа программы и ее взаимодействия с системными ресурсами.

::

  <manifest 
    xmlns:android=http://schemas.android.com/apk/res/android
    package="com.my_domain.my_app"
    android:versionCode="1"
    android:versionName="0.9 Beta">
      
      <uses-sdk 
        android:minSdkVersion="4"
        android:targetSdkVersion="5">
      </uses-sdk>

      <uses-configuration 
        android:reqTouchScreen=["finger"]
        android:reqNavigation=["trackball"]
        android:reqHardKeyboard=["true"]
        android:reqKeyboardType=["qwerty"/>

      <uses-configuration 
        android:reqTouchScreen=["finger"]
        android:reqNavigation=["trackball"]
        android:reqHardKeyboard=["true"]
        android:reqKeyboardType=["twelvekey"]/>

      <uses-feature 
        android:glEsVersion=" 0x00010001"
        android:name="android.hardware.camera" />

      <supports-screens 
        android:smallScreens=["false"]
        android:normalScreens=["true"]
        android:largeScreens=["true"]
        android:anyDensity=["false"] />

      <application 
        android:icon="@drawable/icon"
        android:theme="@style/my_theme"
        android:name="MyApplication"
        android:debuggable="true">

        <activity 
          android:name=".MyActivity" 
          android:label="@string/app_name"
          android:theme="@style/ToDoTheme"
          android:configChanges="orientation|keyboardHidden">
            <intent-filter>
              <action android:name="android.intent.action.MAIN" />
              <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>

        <service 
          android:enabled="true" 
          android:name=".MyService">
        </service>

        <provider 
          android:permission="com.paad.MY_PERMISSION"
          android:name=".MyContentProvider"
          android:enabled="true"
          android:authorities="com.paad.myapp.MyContentProvider">
        </provider>

        <receiver 
          android:enabled="true"
          android:label="My Intent Receiver"
          android:name=".MyIntentReceiver">
        </receiver>

        <uses-permission 
          android:name="android.permission.ACCESS_LOCATION"/>

        <permission 
          android:name="com.paad.DETONATE_DEVICE"
          android:protectionLevel="dangerous"
          android:label="Self Destruct"
          android:description="@string/detonate_description">
        </permission>

        <instrumentation 
          android:label="My Test"
          android:name=".MyTestClass"
          android:targetPackage="com.paad.aPackage">
        </instrumentation>

      </application>
  
  </manifest>


@+id/obj 

@string/text

@color/text