.. py:module:: java.io

PipedInputStream - поток
===============================================


.. py:class:: PipedInputStream()

    Наследник :py:class::`java.io.InputStream`
    
    ::

        try {
            int countRead = 0;
            byte[] toRead = new byte[100];
            
            PipedInputStream pipeIn = new PipedInputStream();
            PipedOutputStream pipeOut = new PipedOutputStream(pipeIn);
            
            // Считвать в массив, пока он полностью не будет заполнен
            while(countRead<toRead.length){
                
                // Записать в поток некоторое количество байт
                for(int i=0; i<(Math.random()*10); i++){
                    pipeOut.write((byte)(Math.random()*127));
                }
                
                // Считать из потока доступные данные,
                // добавить их к уже считанным.
                int willRead = pipeIn.available();
                if(willRead+countRead>toRead.length) {
                    
                    //Нужно считать только до предела массива
                    willRead = toRead.length-countRead;
                    countRead += pipeIn.read(toRead, countRead, willRead);
                }
            }
        } catch (IOException e) {
            pr("Impossible IOException occur: ");
            e.printStackTrace();
        }