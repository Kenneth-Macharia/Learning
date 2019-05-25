package mainpackagedemo;

import java.util.Scanner;

public class functions {

    static Scanner reader = new Scanner(System.in);

    void draw () {
        for (int i=0; i<10; i++) {
            for (int j=0; j<i; j++) {
                System.out.print("-");
            }
            System.out.println("*");
        }
    }

    float sum (float x, float y) {
        return (x + y);
    }

    public static void main (String [] args) {

        // Call functions
        new functions().draw();

        System.out.println("Enter two floats to add:");
        float first_arg = reader.nextFloat();
        float second_arg = reader.nextFloat();
        System.out.println("Result: " + new functions().sum(first_arg, second_arg));

    }
}