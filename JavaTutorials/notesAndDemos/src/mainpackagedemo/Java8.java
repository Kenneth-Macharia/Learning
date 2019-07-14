package mainpackagedemo;

import java.util.StringJoiner;

import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;

// import java.util.ArrayList;
// import java.util.function.Predicate;

// JAVA 8 NEW FEATURES
/*
    1. Lambda expressions in Java8 are a way to simplify code e.g a Functional Interface @FunctionalInterface is an interface with only one method e.g Runnable which has only one abstract method to be implemented.

    Demos belows

    2. Coupling: Decreasing the relatinship between classes so as to reduece components affected when making changes.
    Cohesion: Increasing the relationship between objects of theh same class thus decreasing time to modify code when changes are made.
    Java8 has decreased class inheritance layout bu using the to concepts above and strengthening interface implementation:
    
        1. Declaring interface methods with the 'default' keyword ensure they are implemented within the interface and limit their numerous implementation in implementing classes.
        2. Declaring interface methods with the 'static' keyword ensure that the methods are shared i.e interface methods and not interface object methods.
        
        public inteface operations {

            // normal abstract interface method
            int sum (int x, int y);

            // default method already implemented
            default void display () {
                System.out.println(//do stuff);
            }
            
            static interface method
            static void staticDisplay () {
                System.out.println("//Do stuff");
            }
        }

        class Main implements operations {
            public static void main (String [] args) {

                // implement normal interface abstract method (A)
                @Override
                int sum (int x, int y) {
                    //Do your own stuff
                }

                // implement normal interface abstract method (B)
                operations myoperation = ()-> { //Do stuff}

                // implement default interface method
                new Main().defaultDisplay();

                // implement static interface method
                operations.staticDisplay();
            }
        }

    3. Collections filtering using the Predicate interface.

    Demo below.

    4. Run JavaScript code: using the 'nashorn' script engine.

    Demo below.

    5. Joining string (concatenation): joinig string via "+=" is not efficient and will result in multiple strig objects because in each re-assignment, the a new object is created rather that adding to the joined string variable because Strings are ** IMMUTABLE **. To solve this problem Java8 has a StringJoiner class that creates only one object for the entrie concatenation since Objects are ** MUTABLE **.
    
    Demo below

*/

/* Collections filtering using Predicate: From a collection of user login details, lets retrive
   and print out the users with weak passwords
*/ 

class UserLogin {
    String userName;
    String UserPassword;

    UserLogin (String userName, String UserPassword) {
        this.userName = userName;
        this.UserPassword = UserPassword;
    }

    // Method to verify passwords lengths
    Boolean isWeak() {
        if (UserPassword.length() < 4) {
            return true;
        } else {
            return false;
        }
    }
}


// Implementing a functional interface
@FunctionalInterface
interface functionInterface {

    void playGame (String msg);  //abstract interface function
}

// Lambda expressions demos
// Demo1
class Languages {
    String language;
    int yearReleased;

    Languages (String language, int yearReleased) {
        this.language = language;
        this.yearReleased = yearReleased;
    }
}

// Demo2
class myRunnable1 implements Runnable {

    public void run () {
        System.out.println("Thread is working");
    }

    public static void main(String[] args) {

        //Demo1: Runner code
        // ArrayList<Languages> langs = new ArrayList<Languages>();
        // langs.add(new Languages("Python", 2000));
        // langs.add(new Languages("Java", 1996));
        // langs.add(new Languages("JavaScript", 1995));

        // langs.forEach((language)-> {
        //     System.out.println(language.language + " : " + language.yearReleased);
        // });

        // Demo2: Prior to Java8
        // myRunnable1 r = new myRunnable1();
        // Thread t = new Thread(r);
        // t.start();

        // In Java8, no need to create and instantiate a runnable class, not the lambda expression ()->, where if Runnable's run takes an argument, it can be passed in the brackets of the lambda expression.
        // Runnable someRunnable = ()-> {System.out.println("Thread is running")};
        // Thread t = new Thread(someRunnable);
        // t.start();

        // // Run functional interface
        // functionInterface myFunctionalInterface = (msg)-> {
        //     System.out.println(msg);
        // };

        // // Implement interface function
        // myFunctionalInterface.playGame("Hello World");

        // Collections filtering implementation
        // ArrayList<UserLogin> users = new ArrayList<UserLogin>();

        // users.add(new UserLogin("Ken", "abcd"));
        // users.add(new UserLogin("Shee", "1234"));
        // users.add(new UserLogin("Chris", "xyz"));
        
        //     // Add predicate rules, can be more than one
        // Predicate<UserLogin> predicateRules = (p) -> p.isWeak() == true;
        
        //     // implement the test() of the Predicate interface to test each item of the Arraylist
        // users.forEach((password) -> {
        //     if (predicateRules.test(password)) {
        //         // return and print password, holding the weak passwords
        //         System.out.println("User: " + password.userName + " has a weak password: " + password.UserPassword);
        //     }
        // });
        
        // JS script runner
        // ScriptEngineManager manager = new ScriptEngineManager();
        // ScriptEngine engine = manager.getEngineByName("nashorn");

        // String jsScript = "var name = 'Kenneth Macharia'; name";

        // try {
        //     Object scriptResult = engine.eval(jsScript);
        //     System.out.println(scriptResult);

        // } catch (ScriptException e) {
        //     e.printStackTrace();
        // }
        
        // StringJoiner implementation
        String [] names = {"Ken", "Shee", "Chris", "Mum"};

            // Join the above words into one String.
            // NOT ADVISABLE: take up unnecessary memory space
        // String allNames = "{";

        // for (String name: names) {
        //     allNames += name + ",";
        // }

        // allNames +="}";
        // System.out.println(allNames);

            // ADVISABLE: Creates only one object
        StringJoiner joinerObject = new StringJoiner(",", "{", "}");
        
        for (String name: names) {
            joinerObject.add(name);
        }

        System.out.println(joinerObject);
    }
}

