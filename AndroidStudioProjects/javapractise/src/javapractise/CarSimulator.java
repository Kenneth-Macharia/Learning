package javapractise;

public class CarSimulator {

    public static void main(String[] args) {
        
        System.out.println("Launching the car simulator......");
        
        Car myToyota = new Car("blue", "Wood");        
        Car myHonda = new Car();
        myHonda.drive();
        
        SelfDrivingCar autoBot = new SelfDrivingCar("Yellow", "Plastic");
        autoBot.drive();
        
        System.out.println("autoBot is " + autoBot.mColor + " in color");
        System.out.println("autoBot has a " + autoBot.mInterior + " interior");
        
        autoBot.drive();
        
    }  
}
