.. py:module:: java.io

DataInputStream - поток для работы с примитивами
================================================


.. py:class:: DataInputStream()

    Наследник :py:class::`java.io.InputStream`

    Реализует :py:class::`java.io.DataInput`

    :: 

        try {
            ByteArrayOutputStream out = new ByteArrayOutputStream();
            DataOutputStream outData = new DataOutputStream(out);
            outData.writeByte(128); // it would write -128, as casted to byte
            outData.writeInt(128);
            outData.writeLong(128);
            outData.writeDouble(128);
            outData.close();
            byte[] bytes = out.toByteArray();
            InputStream in = new ByteArrayInputStream(bytes);
            DataInputStream inData = new DataInputStream(in);
            System.out.println("Read data in order it was writen: ");
            System.out.println("readByte: " + inData.readByte());
            System.out.println("readInt: " + inData.readInt());
            System.out.println("readLong: " + inData.readLong());
            System.out.println("readDouble: " + inData.readDouble());
            inData.close();
            System.out.println("read the same data in other order (first byte is
            skipped):");
            in = new ByteArrayInputStream(bytes);
            inData = new DataInputStream(in);
            System.out.println("readInt: " + inData.readInt());
            System.out.println("readDouble: " + inData.readDouble());
            System.out.println("readLong: " + inData.readLong());
            inData.close();
        } catch (Exception e) {
            System.out.println("Impossible IOException occurs: " + e.toString());
            e.printStackTrace();
        }