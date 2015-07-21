.. py:module:: java.io

FileInputStream - поток, считывающий данные из файла
===============================================


.. py:class:: FileInputStream()

    Наследник :py:class::`java.io.InputStream`

    Возбуждает исключение :py:class::`java.io.FileNotFoundException`

    ::

        byte[] bytesToWrite = {1, 2, 3};
        byte[] bytesReaded = new byte[10];
        String fileName = "d:\\test.txt";

        try {
            // Создать выходной поток
            FileOutputStream outFile = new FileOutputStream(fileName);
            
            // Записать массив
            outFile.write(bytesToWrite);
            
            // По окончании использования должен быть закрыт
            outFile.close();
            
            // Создать входной поток
            FileInputStream inFile = new FileInputStream(fileName);
            
            // Узнать, сколько байт готово к считыванию
            int bytesAvailable = inFile.available();
            
            // Считать в массив
            int count = inFile.read(bytesReaded,0,bytesAvailable);
            
            inFile.close();

        } catch (FileNotFoundException e) {
            System.out.println("Невозможно произвести запись в файл: " + fileName);
        } catch (IOException e) {
            System.out.println("Ошибка ввода/вывода: " + e.toString());
        }