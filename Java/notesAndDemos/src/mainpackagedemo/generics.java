package mainpackagedemo;

/*
    - Generic methods and classes allow working  with multiple types using the same code block i.e the method or class.
    - By specifying a generic return type for a method, it can accept non-speciific types and return the non-specific type as well, instead of declaring different methods to handle each type.
    - Rules for generic methods:

        1. All generic method declarations have a type parameter section delimited by angle brackets (< and >) that precedes the method's return type.
        2. Each type parameter section contains one or more type parameters separated by commas. A type parameter, also known as a type variable, is an identifier that specifies a generic type name.
        3. The type parameters can be used to declare the return type and act as placeholders for the types of the arguments passed to the generic method, which are known as actual type arguments.
        4. A generic method's body is declared like that of any other method. Note that type parameters can represent only reference types, not primitive types (like int, double and char)
        5. For code readability the letters used for type variables should be:
            - E - element
            - K - key
            - V - value
            - N - Number
            - T - Type
            - S,U,V - for consequtive types when T is already in use

    - Demo below:

    - Bounded type: restricting the generic type e.g to numerics only (class Numbers and its sub-classes only). Achieved by using the extends keyword after the type parameter then the upper bound e.g. in a case of comparing numbers to determine the largest, 'comparable'

    - Demo below:

    - A generic class declaration looks like a non-generic class declaration, except that the class name is followed by a type parameter section. As with generic methods, the type parameter section of a generic class can have one or more type parameters separated by commas. These classes are known as parameterized classes or parameterized types because they accept one or more parameters.

    - Demo below:

*/

// Generic class
class Box <T> {
    private T t;

    public void add(T t) {
       this.t = t;
    }

    public T get() {
       return t;
    }
}

// Generic methods demo
class Generics {

    // Suppose a couple of arrays of primitive types
    static int [] someInts = {1, 2, 3};
    static String [] someStrs = {"Ken", "Shee", "Chris"};
    static double [] someDbls = {1.7, 2.3, 5.6};

    // methods to print out the arrays of different types
    static void printInts(int [] args) {
        for (int s: args) {
            System.out.print(s + "\n");
        }
    }

    static void printStrs(String [] args) {
        for (String i: args) {
            System.out.print(i + "\n");
        }
    }

    static void printDbls(double [] args) {
        for (double j:args) {
            System.out.print(j + "\n");
        }
    }

    /* By having a generic method, we can replace the 3  type specific methods with a generic one that takes a generic type T */
    // Note the type must not be primitve, rather reference types (referring to objects)

    static Integer [] someIntsRef = {1, 2, 3};
    static String [] someStrsRef = {"Ken", "Shee", "Chris"};
    static Double [] someDblsRef = {1.7, 2.3, 5.6};

    static <T> void printAllTypes(T [] args) {
        for (T s:args) {
            System.out.println(s);
            System.out.printf("%s", s + "\n\n"); //printf used where a output string may need formatting
        }
    }

    // Bounded types
    // determines the largest of three Comparable objects

    static public <T extends Comparable <T> > T maximum(T x, T y, T z) {
        T max = x;   // assume x is initially the largest

        if(y.compareTo(max) > 0) {
            max = y;   // y is the largest so far
        }

        if(z.compareTo(max) > 0) {
            max = z;   // z is the largest now
        }

        return max;   // returns the largest object
    }

    public static void main(String [] args) {
        // Specific tyoe methods
        printInts(someInts);
        printStrs(someStrs);
        printDbls(someDbls);

        // Generic type method
        printAllTypes(someIntsRef);
        printAllTypes(someStrsRef);
        printAllTypes(someDblsRef);

        //Bounded types
        System.out.printf("Max of %d, %d and %d is %d\n\n",
        3, 4, 5, maximum( 3, 4, 5 ));

        System.out.printf("Max of %.1f,%.1f and %.1f is %.1f\n\n",
        6.6, 8.8, 7.7, maximum( 6.6, 8.8, 7.7 ));

        System.out.printf("Max of %s, %s and %s is %s\n\n","pear",
        "apple", "orange", maximum("pear", "apple", "orange"));

        // Using generic classes
        Box<Integer> integerBox = new Box<Integer>();
        Box<String> stringBox = new Box<String>();

        integerBox.add(new Integer(10));
        stringBox.add(new String("Hello World"));

        System.out.printf("Integer Value :%d\n\n", integerBox.get());
        System.out.printf("String Value :%s\n\n", stringBox.get());
    }
}