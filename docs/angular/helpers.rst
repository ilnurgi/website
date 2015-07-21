Вспомогательные функции
=======================


.. code-block:: js

    <p ng-if='keys.length'></p>

    <p ng-init='names=[1,2,3,]'></p>



    <div ng-repeat='key in keys'></div>

    <b ng-bind='value'></b>
    <b ng-bind-template='value'></b>
    <b ng-bind-html='value'></b>

    <p ng-class="{strike: deleted, bold: important, red: error}">Map Syntax Example</p>
    <input type="checkbox" ng-model="deleted"> deleted (apply "strike" class)<br>
    <input type="checkbox" ng-model="important"> important (apply "bold" class)<br>
    <input type="checkbox" ng-model="error"> error (apply "red" class)
    <hr>
    <p ng-class="style">Using String Syntax</p>
    <input type="text" ng-model="style" placeholder="Type: bold strike red">
    <hr>
    <p ng-class="[style1, style2, style3]">Using Array Syntax</p>
    <input ng-model="style1" placeholder="Type: bold, strike or red"><br>
    <input ng-model="style2" placeholder="Type: bold, strike or red"><br>
    <input ng-model="style3" placeholder="Type: bold, strike or red"><br>

    // применяет стили на каждый нечетный элемент
    <p ng-class-odd="'odd'"></p>
    // применяет стили на каждый четный элемент
    <p ng-class-even="'even'"></p>

    <div compile='html'></div>

    <a ng-href='/'></a>
    <a ng-disabled='var'></a>
    <a ng-checked='var'></a>
    <a ng-readonly='var'></a>
    <a ng-selected='var'></a>
    <a ng-open='var'></a>
    <a ng-show='var'></a>

    <form name="myForm" ng-controller="Ctrl" class="my-form">
        userType: <input name="input" ng-model="userType" required>
        <span class="error" ng-show="myForm.input.$error.required">Required!</span><br>
        <tt>userType = {{userType}}</tt><br>
        <tt>myForm.input.$valid = {{myForm.input.$valid}}</tt><br>
        <tt>myForm.input.$error = {{myForm.input.$error}}</tt><br>
        <tt>myForm.$valid = {{myForm.$valid}}</tt><br>
        <tt>myForm.$error.required = {{!!myForm.$error.required}}</tt><br>
    </form>

    <input ng-model="val" ng-pattern="/^\d+$/" name="anim" class="my-input" />
    /*
    при ошибках применятся следующие свойства
    .my-input.ng-invalid {
        color:white;
        background: red;
    }
    */

    <div id="template1" ng-cloak>{{ 'hello' }}</div>
    <div id="template2" ng-cloak class="ng-cloak">{{ 'hello IE7' }}</div>

    <button ng-mousedown="count = count + 1" ng-init="count=0">

    <button ng-mouseover="count = count + 1" ng-init="count=0">

    <button ng-mouseenter="count = count + 1" ng-init="count=0">

    <button ng-mouseleave="count = count + 1" ng-init="count=0">

    <button ng-mousemove="count = count + 1" ng-init="count=0">

    <input ng-keydown="count = count + 1" ng-init="count=0">

    <input ng-keyup="count = count + 1" ng-init="count=0">

    <input ng-keypress="count = count + 1" ng-init="count=0">


    <form ng-submit="submit()" ng-controller="Ctrl">
        Enter text and hit enter:
        <input type="text" ng-model="text" name="text" />
        <input type="submit" id="submit" value="Submit" />
        <pre>list={{list}}</pre>
    </form>

    <input ng-copy="copied=true" ng-init="copied=false; value='copy me'" ng-model="value">
    <input ng-cut="cut=true" ng-init="cut=false; value='cut me'" ng-model="value">
    <input ng-paste="paste=true" ng-init="paste=false" placeholder='paste here'>

    <select ng-model="template" ng-options="t.name for t in templates">
        <option value="">(blank)</option>
    </select>

    <div class="slide-animate" ng-include="template.url"></div>

    <div ng-non-bindable>Ignored: {{1 + 2}}</div>

    <ng-pluralize count="personCount"
                  when="{'0': 'Nobody is viewing.',
                         'one': '1 person is viewing.',
                         'other': '{} people are viewing.'}">
    </ng-pluralize><br>

    <div class="check-element animate-show" ng-show="checked">
    <div class="check-element animate-show" ng-hide="checked">

    <input type="button" value="clear" ng-click="myStyle={}">
    <span ng-style="myStyle">Sample Text</span>

    <div class="animate-switch-container"
         ng-switch on="selection">
        <div class="animate-switch" ng-switch-when="settings">Settings Div</div>
        <div class="animate-switch" ng-switch-when="home">Home Span</div>
        <div class="animate-switch" ng-switch-default>default</div>
    </div>

    angular.isDefined(stop)

    <button ng-click="$log.log(message)">log</button>
    <button ng-click="$log.warn(message)">warn</button>
    <button ng-click="$log.info(message)">info</button>
    <button ng-click="$log.error(message)">error</button>

.. js:function:: $location.hash()

.. js:function:: $cacheFactory.get()
.. js:function:: $cacheFactory.info()
