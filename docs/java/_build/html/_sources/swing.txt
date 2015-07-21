swing
=====

::

    import java.swing.JFrame;

    public class HelloWorld extends JFrame {
        
        public HelloWorld() {

            setSize(200, 300);
            setTitle("Title");
            setVisible(true);

        }

        public static void main(String[] args){
            HelloWorld helloWorld = new HelloWorld();
        }
    }

    JButton myButton = new JButton("click me"); 

    Layout Managers

    FlowLayout
    GridLayout
    BoxLayout
    BorderLayout
    CardLayout
    GridBagLayout