package mainpackagedemo;

/* 
    Classes, the foundation of OOP, are instructions or blueprints for how object of specific
    types will be created. Public classes must be defined in their own files.

    Objects are self-contained components consisiting of charateristics (properties) and
    actions (methods) to make a particular type of data useful.

    OOP is a programming paradim that breaks down a problem into these sel-contained, re-usable
    components that deal with a particular section of the entire problem only, then define
    how the components will interact with each other to achieve the intended solution.

    Constructors: Are methods in a class invoked whenever an object of th class is instantiated.
    They have the same name as the name of the class. They can be more than one per class,
    depending on how the class will be initialized. They do not return values.

    Deconstructors: Are methods that tear down clas object. Java does not have these as it is a
    garbage collected language.

    Static modifier is used to define either class variables and methods i.e those shared by all
    members of the class, static blocks of code and nested classes. Static methods can only be
    used by static members.

    Inheritance (IS-A relationship): in Java when a class extends another (child) thus
    automatically get all the members of the class inheriting from (Parent). This is a two-relationship.

    Encapsulation: Information hidding by limiting access to certain class attributes from outside the class. This is achieved via the 'private' & 'protected' access modifiers that can used for either attributes or methods. When a class memeber is declared without any of the two keywords, its considered public and can be accessed directly from outside the class using an instance of the class or via inheritance (extends). {if no key word is used in the declaration, then the member is public}. Private members cannot be accessed via inheritance nor class instances and can only be accessed via class setter and getter methods. Protected members can only be accessed via inheritance and not by class instances.

    Overriding methods > See polymorphism file. Demo below.

    this: this is used to refer to the members of the current class especially where there may be a reference confusion e.g. initializing a class attribute using a setter method parameter that has the same name i.e

    class Person {
        int age;

        void setMethod (int age) {
            age = age; instead use this.age = age;
        }
    }

    super is used when the intention is to refer to a parent class member in a child e.g when methods have been overridden or when intending to use the parent class constructor when instead of the child class constructor to initialize the child class i.e super(), super(int age) in the child consturctor body.

    Aggregation: (Has-A relationship): In OOP, this means between tow classes, on of them has a relationship to the other but the reverse is not true e.. between a student and address class, every student has an address but not every addresss has a student related. This enhances code re-usability thus many classes by creating an instance of the common class in all the classes that require it and preventing repetition of these details in all those classes.
        Demo: Student, Faculty, Address example

    Nested /inner classes: are classes delacred inside other other classes so as to control access to outter class memmbers. Modifiers including abstract and final can be used on them so as to define the relationship with the outter clases:

        1. Inner class defination: in this case the inner class can access all the members of its top level class including the private myVar.

        //Top level class definition
        class MyOuterClassDemo {
        private int myVar= 1;

        // inner class definition
        class MyInnerClassDemo {
            public void seeOuter () {
                System.out.println("Value of myVar is :" + myVar); {ALLOWED}
            }
            }
        }

        Inner classes are instanitated through live instances of the outter class e.g

        class MyOuterClassDemo {
        private int x= 1;
        public void innerInstance()
        {
            MyInnerClassDemo inner = new MyInnerClassDemo();
            inner. seeOuter();
        }
        public static void main(String args[]){
            MyOuterClassDemo obj = new MyOuterClassDemo();
            obj.innerInstance();
        }
        // inner class definition
        class MyInnerClassDemo {
            public void seeOuter () {
                System.out.println("Outer Value of x is :" + x);
            }
        }   
        }

        OR

        public static void main(String args[]){
            MyOuterClassDemo.MyInnerClassDemo inner = new MyOuterClassDemo().new MyInnerClassDemo();
            inner. seeOuter();
        }

        2. Method-local inner class: is an innner class defined inside a method of the outter class. Inner classes can only be instantiated inside the method in which they are and can only access 'final' variables of the method in which they are in. They can however access all other members of the outter class that are declared outside the method they are in:

        /Top level class definition
        class MyOuterClassDemo {
        private int x= 1;

        public void doThings(){
            final String name ="local variable";
            // inner class defined inside a method of outer class
            class MyInnerClassDemo {
                public void seeOuter () {
                System.out.println("Outer Value of x is :" + x); {ALLOWED}
                System.out.println("Value of name is :" + name); {ALLOWED - only if final}
                }
            }
        }
        }

        3. Anonymous inner classes: inner classes that have no name (thus no constructors), cannot be static, declared inside a method or code block ending with a }; can only be instantiated once and is only accessible where defined:

        // conventional declaration
        class Pizza {
            public void eat() {
                System.out.println("pizza");
            }
        }

        // Anonymous declaration
        class Food {

            Pizza p = new Pizza(){

                public void eat() {
                    System.out.println("anonymous pizza");
                }

            };
        }

        4. Static nested classes: Have no special relationship with the outter class other than they cannot access non-static members of the outter class:

        // Declaration
        class Outer{
            static class Nested{}
        }

        // Instantiation
        class Demo{

            public static void main(string[] args) {
                // use both class names
                Outer.Nested n= new Outer.Nested();
            }
        }

    Abstraction: is hidding unecessary and often complex details of a system away from the user and allowing exposing only what the user needs to implement it. In OOP, this means a user of a clas only need to know how to use a class but what the components of the class are. This is usually enforced by inheritance and in Java, class abstraction is implemeted by declaring a class with an 'abstract modifier' thus only allowind use of the class by inheriting it and not by instantiating it.

    Interfaces are abstract classes (only have have abstract declaration of methods which are public by default and static constants). They exist to enable multiple inheritance since in Java, extending more than one classes is not allowed but implementing more than one interfaces to get functionality from both is allowed. A class can extend a class and implement many interfaces at the same time.

    public class Animal {
        *its attributes
        *its methods (NOT abstract, already have functionality) i.e.
        void makeSound () {
            // some fucntionality to make a sound
        }
        *its constructor(s)
    }

    public interface Pet {
        abstract methods i.e. NOT defined functionality just declararation
        void keepCompany () {}
    }

    public class Dog extends Animal implements Pet {
        // Will get all fuctionality from both the Animal class and the Pet interface.
    }

    Enumarators (Enums in Java) are object types of the Java Enum class, that are used to represent a group of named constants that all possible values for them are known at compile time e.g days of the week, gender, menus for the day etc. They are useful in validating data and preventing illegal inputs. Theri implemetation is very elaborate: https://www.geeksforgeeks.org/enum-in-java/. Simple Demo below:

    Casting: involves converting a variable type to another comaptible variable type so as tomuch effectively work with the covnerted type especially in downcasting where a type is covnerted from a more abstract type to a more specific type e.g from a super class to a sub class. Note however upcasting is also legal. Java will handle casting automatically if a type cast4ed to is bigger than the orign type e.g int to double else explicit casting is required e.g.
        double = (double) int
    

*/  

// Enums Demo
enum Gender {
    Male,
    Female
}

class Student {
    String name;
    Gender studentGender;

    Student (String name, Gender studentGender) {
        this.name = name;
        this.studentGender = studentGender;
    }

    public static void main(String [] args) {
        Student newStudent = new Student("Ken", Gender.Male);
        System.out.println("My name is " + newStudent.name + " and gender is " + newStudent.studentGender);
    }
}

class Truck extends Car {
    boolean trailer;

    void hasTrailer () {
        if (trailer == true) {
            System.out.println("I have a trailor");
        } else {
            System.out.println("I don't have a trailor");
        }   
    }

    // Overidding method in parent class
    @Override
    double getPrice () {
        return (cost - (50*mileage));
    }

    Truck (boolean trailer) {
        // Deciding which parent constructor to call (constructor without parameters commented out)
        super("Mercedes", 2010, 10000000, 21198);
        this.trailer = trailer;
        System.out.println("Truck constructor fired!");
    }
}

class Car {
    // Class properties
    String model;
    int yearOfManufacture;
    double cost;
    int mileage;
    static String owner;

    //Class methods
    String getDetails () {
        return ("My make is: " + model + ", year of manufacture is: " + 
        yearOfManufacture + " and owner is: " + owner);
    }

    double getPrice () {
        return (cost - (100*mileage));
    }

    // Class Constructors
    Car () {
        System.out.println("Car constructor 1 fired!");
    }

    Car (String model, int yearOfManufacture, double cost, int mileage) {
        this.model = model;
        this.yearOfManufacture = yearOfManufacture;
        this.cost = cost;
        this.mileage = mileage;

        System.out.println("Car constructor 2 fired!");
    }
}

// Common class
class Address {
    // Attributes
    String street_name;
    String city;
    String state;
    String country;

    // constructor
    Address (String street_name, String city, String state, String country) {
        this.street_name = street_name;
        this.city = city;
        this.state = state;
        this.country = country;
    }
}

// HAS-A relationship to Address
class Student {
    int rollNum;
    String name;
    Address studentAdd;

    Student (int rollNum, String name, Address studentAdd) {
        this. rollNum = rollNum;
        this.name = name;
        this.studentAdd = studentAdd;
    }
}
// HAS-A relationship to Address
class Faculty {
    int facultyNum;
    String name;
    Address facultyAdd;

    Faculty (int facultyNum, String name, Address facultyAddress) {
        this.facultyNum = facultyNum;
        this.name = name;
        this.facultyAdd = facultyAddress;
    }
}

// Main class
public class classes {

    public static void main(String [] args) {

        System.out.println("--------------------------");

        // Static member shared between class objects
        Car.owner = "Smith";

        // Class objects
        Car Toyota = new Car();
        Toyota.model = "MacX";
        Toyota.yearOfManufacture = 2014;
        Toyota.cost = 2500000.00;
        Toyota.mileage = 3097;
        System.out.println(Toyota.getDetails());
        System.out.println("My current market price is: " + Toyota.getPrice());

        System.out.println("--------------------------");

        Car BMW = new Car("M3", 2015, 3500000, 2415);
        System.out.println(BMW.getDetails());
        System.out.println("My current market price is: " + BMW.getPrice());

        System.out.println("--------------------------");

        Truck Scania = new Truck(true);
        // Scania.model = "552";
        // Scania.yearOfManufacture = 2012;
        // Scania.cost = 8000000;
        // Scania.mileage = 17856;
        System.out.println(Scania.getDetails());
        System.out.println("My current market price is: " + Scania.getPrice());
        Scania.hasTrailer();

        System.out.println("--------------------------");

        // Create a student instance
        Address student1_Address = new Address("Orange Street", "LA", "California", "USA");
        Student student1 = new Student(302, "Kenneth", student1_Address);
        System.out.println(student1.name + " lives on " + student1.studentAdd.street_name);

        System.out.println("--------------------------");

        // Create faculty instance
        Address faculty1Adddress = new Address("West Habour Street", "LA", "California", "USA");
        Faculty faculty1 = new Faculty(22, "Jose", faculty1Adddress);
        System.out.println(faculty1.name + " lives on " + faculty1.facultyAdd.street_name);

        System.out.println("--------------------------");
    }
}