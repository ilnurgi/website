.. py:module:: java.lang

Thread - представляет вычислительный поток в Java
=================================================

Что бы реализовать выполнение некоторого кода в отдельном потоке, можно:

a. первый метод

    1. Написать класс, реализующий интерфейс Runnable, поместив код для выполнения в метод run(). 

    2. Создать объект класса Thread, передав конструктору объект этого класса.

    3. Запустить выполнение в отдельном потоке, вызвав у объекта Thread метод start().

        ::
            public static void main(String[] args) {
                class RunCode implements Runnable{
                    public void run(){
                        System.out.println("RunCode.run() begins");
                        System.out.println("RunCode.run() ends");
                    }
                }
                Runnable run = new RunCode();
                Thread thread = new Thread(run);
                thread.start();
                System.out.println("main finish");
            }

            // RunCode.run() begins
            // main finish
            // RunCode.run() ends

b. второй метод

    1. Написать класс, унаследовав его от Thread. При этом в метод run() поместить код, который должен выполняться в отдельном потоке. 

    2. После этого достаточно будет создать объект этого класса, и вызвать у него метод start().

    ::

        public static void main(String[] args) {
            class RunCode extends Thread{
                public void run(){
                    System.out.println("RunCode.run() begins");
                    System.out.println("RunCode.run() ends");
                }
            }
            Thread thread = new RunCode();
            thread.start();
            System.out.println("main finish");
        }

Функциональных различий в использовании двух приведенных путях создания новых потоков нет. Класс Thread реализует интерфейс Runnable, и если объект этого класса был создан без передачи конструктору объекта Runnable, в качестве этого объекта будет использоваться сам объект Thread (через ссылку this).


.. py:class:: Thread()


    .. py:method:: start()

        `public void`

        Производит запуск выполнения нового потока


    .. py:method:: join()

        `public final void`

        Приостанавливает выполнение потока, из которого был вызван этот метод до тех пор, пока не закончит выполнение поток, у объекта Thread которого был вызван этот метод


    .. py:method:: yield()

        `public static void`

        Поток, из которого вызван этот метод, временно приостановится(отдаст процессорное время), что бы дать возможность выполняться другим потокам


    .. py:method:: sleep(long millis)

        `public static void`

        Поток, из которого вызван этот метод, перейдет в состояние "сна" на время millis миллисекунд, после чего сможет продолжить выполнение.

        При этом нужно учесть, что поток именно сможет продолжить выполнение, а НЕ продолжит.

        То есть через время millis миллисекунд, этому потоку может быть выделено процессорное время (механизм распределения определяется реализацией Java-машины). Правильней было бы говорить, что поток продолжит выполнение НЕ раньше чем через время millis миллисекунд.
