package mainpackagedemo;

import java.util.Calendar;
import java.util.Scanner;

public class MyAge {
	
	static Scanner reader = new Scanner(System.in);
	
	public static void main(String [] args) {
		
		System.out.print("Enter your DOB:");
		int DOB = reader.nextInt();
		int currentYear = Calendar.getInstance().get(Calendar.YEAR);		
		System.out.println("Your age is: " + (currentYear - DOB) + " years");

	}

}
