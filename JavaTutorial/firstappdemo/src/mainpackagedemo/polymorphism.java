package mainpackagedemo;

/*  
    Polymorphism (having many shapes) in programming is a languages ability to process various
    types and classes through a single, uniform interface.

    Compile time/ static polymorphism > Function overloading: Having more than one functions
    with the same name but different number/order of parameters. The function to be executed
    will be the one with matching number & order of parameters and is determined by the
    complier at compile time.

    Runtime/ dynamic polymorphism > Function overriding: Having a child class function with
    same signature (name & parameters) as a parent class function, but adding on the features
    of the parent class function. When the function call is made, Java waits until runtime to
    determine which object reference made the call and hence will run it's class overriden
    function.
*/

public class polymorphism {

    public static void main (String [] args) {

        // Overloaded function calls
        System.out.println("Overloading:");

        System.out.println(new overloading().overloadedFunc(2,4));
        System.out.println(new overloading().overloadedFunc(2,4,3));
        System.out.println(new overloading().overloadedFunc(15.4,4));

        System.out.print("\n");
        System.out.println("Overriding:");

        // Overridden function calls
            /* 
                Create an variable of the parent class's type and store an object of the parent
                class in it and call the overriden function.
            */

            overridingParent obj1 = new overridingParent();
            System.out.println( obj1.overriddenFunc(1, 2));

            /* 
                Create an variable of the parent class's type and store an object of the child
                class in it and call the overriden function.
            */

            overridingParent obj2 = new overridingChild();
            System.out.println( obj2.overriddenFunc(1, 2));
    }

}

class overloading {

    int overloadedFunc (int a, int b) {
        return (a-b);
    }

    int overloadedFunc (int a, int b, int c) {
        return ((a+b)-c);
    }

    double overloadedFunc (double a, int b) {
        return ((a/b));
    }
}

class overridingParent {

    int overriddenFunc (int a, int b) {
        return (a-b);
    }
}

class overridingChild extends overridingParent{

    int overriddenFunc (int a, int b) {
        return (a+b);
    }
}
