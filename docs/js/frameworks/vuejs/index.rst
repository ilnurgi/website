Mustache


отображаем данные в элементе
<div id='todos' data-title='{{title}}'></div>

отображаем элементы из списка
<ul>
    <li v-repeat='tasks'>{{title}}</li>
    внутри цикла достцпны перменные $index, $key, $value
</ul>
<ul>
    <li v-repeat='task: tasks'>{{title}}</li>
    внутри цикла достцпны перменные $index, $key, $value
    <span v-show='task != editTask' v-on='dblclick: editTask = task' v-class='text-primary : task.done'>{{ task.title }}</span>
    <input v-show='task == editTask' type='text' v-model='editTask.title' v-on='keyup: editTask = null | key "enter"'>
</ul>

обработка формы
<form v-on='submit: addTask'>
    <input lazy v-model='newTask'>
    lazy - данные попадут в модель после события change

    <span v-on='click: removeTask($index)'>
</form>

фильтр, выводим значение переменной в json формате
<pre>
    {{ $data | json }}
</pre>


================================================================================

var Todos = Vue.extend({
    name: 'todos'
});

var vm = new Todos({
    el: '#todos', // элемент внутри которого работаем
    data: {
        title: 'todos'
    },
    ready: function(){
        console.log('viewmodel ready!');
    }
});

var vm2 = new Todos({

    // элемент внутри которого работаем, селектор или сам элемент
    el: '#todos',

    // данные вьюхи
    data: {
        tasks: [
            {
                title: '1',
                done: true
            }, {
                title: '2',
                done: false
            }
        ],
        newTask: '',
        editTask: ''
    },
    // фильтры
    filters: {
        openTasks: function(){
            return this.tasks.filter(function(item){
                return item.done;
            });
        }
    },
    // методы
    methods: {
        addTask: function(event){
            // обработчик сабмита формы

            e.preventDefault();
            console.log('Task added');
            this.tasks.push({title: this.newTask, done: false})
            this.newTask = '
        },
        removeTask: function(index){
            this.tasks.$remove(index);
        }
    }
    ready: function(){
        console.log('viewmodel ready!');
    }
});

// познеесвязывание представления с вьюмоделью
vm.$mount('todos');

// изменение данных в ВМ
vm.$data.title = '123'

// добавление данных в ВМ
vm.$data.$add('title', 'NewTitle);



Директивы
=========

v-text - текстовое содержимое элемента, textContent
<span v-text='variable'></span>

v-html - innerHTML
<span v-html='html'></span>

v-attr - attributes
<img v-attr="width: '100px', height: '100px'"/>

v-class - добавляет классы
<span v-class="red: true"></span>

v-style - css-style
<span v-style="css.string, css.object">

v-show, v-if - display
<span v-show="true">
<span v-if="false">

v-on - добавляет обработчик событий
<span v-on="click: callback, blur: red = !red">
<form v-on="submit: callback($event)">
<textarea v-on="keyup: callback($event) | key 13"> // enter
<textarea v-on="keyup: callback($event) | key 'enter'"> // enter

v-el - задает идентификатор элементу
<textarea v-el="comment" v-on="submit: callback($event)">

callback: function(event){
    this.$$.comment.value;
}

v-pre - элемент не используется для дата биндинга

v-repeat - цикл, track-by - ключ, идентификатор, для того чтобы не перерисовывать объект

v-model- lazy, debounce - таймер для синхронизации, number - преобразовать к числу если возможно

Vue.directive('test', {
    bind: function(){
        // привязываем элемент к директиве

    },
    unbind: function(){
        // удаляем директиву из элемента
    },
    update: function(newValue, oldValue){
        // значение будет изменено
    }
})
Vue.directive('test', function(){
        // удаляем директиву из элемента
    }
})
<span v-test=''/>


Vue.elementDirective('like', {
    bind: function(){
    },

});
<like/>


Фильтры
=======

Vue.filter('filter-name', {
    read: function(value){
    },
    write: function(newValue, oldValue){
    }
})
Vue.filter('filter-name', function(value, ends){
    },
})

- json
- capitalize
- uppercase
- lowercase
- currence 'RUB'
- pluralize 'item'
- pluralize 'ый' 'ой'
- filterBy 't' - поиск во всех свойствах
- filterBy 't' in 'title' - поиск в указанных свойствах
- orderBy 'id' true


Вычисляемые поля
================

var vm = new Vue({
    el: '#container',
    data: {},
    computed: {
        full_name: {
            get: function(){},
            set: function(value){},
        },
        initials: function(){
            // сеттер нам не нужен
        },

    }
});