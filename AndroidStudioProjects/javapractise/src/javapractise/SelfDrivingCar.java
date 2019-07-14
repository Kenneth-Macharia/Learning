package javapractise;

public class SelfDrivingCar extends Car {

    public SelfDrivingCar(String chosenColor, String chosenInterior) {
        super(chosenColor, chosenInterior); // calls the super class constructor that has those arguments
        System.out.println("Constructing self-driving car");
    }
    
   
    @Override
   public void drive() {
       super.drive();
       System.out.println("driving to Googleplex");
   }
}
