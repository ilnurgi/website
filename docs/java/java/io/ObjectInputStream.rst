.. py:module:: java.io

ObjectInputStream - 
================================================


.. py:class:: ObjectInputStream()

    Реализует :py:class::`java.io.ObjectInput`

    ::

        ByteArrayOutputStream os = new ByteArrayOutputStream();
        Object objSave = new Integer(1);
        ObjectOutputStream oos = new ObjectOutputStream(os);
        oos.writeObject(objSave);

        // можно просмотреть содержимое массива
        byte[] bArray = os.toByteArray();

        // можно десериализовать его из этого массива
        ByteArrayInputStream is = new ByteArrayInputStream(bArray);
        ObjectInputStream ois = new ObjectInputStream(is);
        Object objRead = ois.readObject();

        objSave.equals(objRead); // true