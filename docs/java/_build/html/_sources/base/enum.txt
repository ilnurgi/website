enum - перечисления
===================

::

    enum Lights { RED, YELLOW, GREEN, ERROR }

    public class EnumMethods{
        public static void main(String[] args){
        
            for (Lights light: Lights.values()){
                System.out.println("Тип: " + light.getDeclaringClass());
                System.out.println("Числовое значение: " + light.ordinal());
            }
        }
    }