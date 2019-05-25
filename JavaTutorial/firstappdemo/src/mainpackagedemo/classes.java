package mainpackagedemo;

/* 
    Classes, the foundation of OOP, are instructions or blueprints for how object of specific
    types will be created.

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

    Static keyword is used to define either class variables and methods i.e those shared by all
    members of the class, static blocks of code and nested classes. Static methods can only be
    used by static members.

    Inheritance (IS-A relationship): in Java when a class extends another (child) thus
    automatically get all the members of the class inheriting from (Parent).
*/

class Truck extends Car {

    boolean trailer;

    void hasTrailer () {
        if (trailer == true) {
            System.out.println("I have a trailor");
        }
        System.out.println("I don't have a trailor");
    }

    Truck (boolean trailer) {
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
        return (cost - (10*mileage));
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
        Scania.model = "552";
        Scania.yearOfManufacture = 2012;
        Scania.cost = 8000000;
        Scania.mileage = 17856;
        System.out.println(Scania.getDetails());
        System.out.println("My current market price is: " + Scania.getPrice());
        Scania.hasTrailer();

        System.out.println("--------------------------");
    }
}