package javapractise;

public class Car {
    
    public String mColor = "black";
    private int mNumberOfSeasts = 5;
    protected String mInterior;
    
    public Car (String chosenColor, String chosenInterior) {
        mColor = chosenColor;
        mInterior = chosenInterior;
        
    }
    
    public Car () {
        mInterior = "leather";
    }

    public int getmNumberOfSeasts() {
        return mNumberOfSeasts;
    }

    public String getmInterior() {
        return mInterior;
    }
    
    public void drive () {
        System.out.println("Car is moving...");
    }   
    
}
