generics - настраиваемые типы
=============================

::

    class MyGenericClass<T>{
        
        private T data;
        
        public MyGenericClass(){}
        
        public MyGenericClass(T data){
            this.data = data;
        }
        
        public T getData(){
            return data;
        }

        public void setData(T data){
            this.data = data;
        }
    }

    class MyGenericClassDemo{
        public static void main(String[] args){
            
            MyGenericClass<Integer> iMyGen = new MyGenericClass<Integer>(55);
            Integer n = iMyGen.getData();

            MyGenericClass<Double> dMyGen = new MyGenericClass<>(-37.3456);
            Double x = dMyGen.getData();
        }
    }

    class Average<T extends Number> {}
    class Average<T super Number> {}
    class Average<T, S> {}