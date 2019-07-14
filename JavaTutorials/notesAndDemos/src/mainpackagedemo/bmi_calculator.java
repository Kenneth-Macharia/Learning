package mainpackagedemo;

import java.util.Scanner;

class Bmi {

    static double bmiCalculator (int mass, double height) {
        return (mass/Math.pow(height, 2));
    }

    public static void main(String[] args) {
        int mass;
        double height;

        System.out.print("Enter your mass in Kgs: ");
        mass = massReader.nextInt();
        System.out.print("Enter your height in Meters: ");
        height = heightReader.nextDouble();

        System.out.println("Your BMI is " + bmiCalculator(mass, height));       
    }
}