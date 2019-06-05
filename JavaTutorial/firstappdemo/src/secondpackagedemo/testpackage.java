package secondpackagedemo; //Comment out when running from terminal

// Run from terminal in src folder, compile javac <file>, then then run java file <args>

class testpackage {

    static void printInputs(String [] args) {
        for (String i: args) {
            System.out.printf("%s\t\n", i);
        }
    }

    public static void main (String [] args) {      
        printInputs(args);
    }
}