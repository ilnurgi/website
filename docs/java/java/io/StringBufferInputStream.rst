.. py:module:: java.io

StringBufferInputStream - считывает данные из других двух и более входных потоковss
===============================================

При этом можно указать два потока или их список. Данные будут вычитываться
последовательно - сначала все данные из первого потока в списке, потом из второго, и так далее. 

Конец потока SequenceInputStream будет достигнут только тогда, когда будет достигнут конец потока, последнего в списке.


.. py:class:: StringBufferInputStream()

    Наследник :py:class::`java.io.InputStream`

    ::

        FileInputStream inFile1 = null;
        FileInputStream inFile2 = null;
        SequenceInputStream sequenceStream = null;
        FileOutputStream outFile = null;

        try {
            inFile1 = new FileInputStream("file1.txt");
            inFile2 = new FileInputStream("file2.txt");
            sequenceStream = new SequenceInputStream(inFile1, inFile2);
            outFile = new FileOutputStream("file3.txt");
            int readedByte = sequenceStream.read();
            
            while(readedByte!=-1){
                outFile.write(readedByte);
                readedByte = sequenceStream.read();
            }
        } catch (IOException e) {
            System.out.println("IOException: " + e.toString());
        } finally {
            try{
                sequenceStream.close();
            } catch(IOException e) {};
            
            try{
                outFile.close();
            } catch(IOException e) {};
        }