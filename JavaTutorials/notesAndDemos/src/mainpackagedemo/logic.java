package mainpackagedemo;

import java.util.Scanner;

public class logic {
	
	/*
	 * Truth table (Math & Electronics)
	 * Logic operations (>, <, >=, <=, ==, !=)
	 * Logic gates (&&(AND), ||(OR), !(Not)
	 * Decision making (if, else, else if, switch)
	 */
	
	static Scanner reader = new Scanner(System.in);
	
	public static void main (String [] args) {
//		Switch demo
		
		System.out.print("Enter index");
		int index = reader.nextInt();
		
		switch(index) {
		
		case 1:System.out.println("Male");
		break;
		
		case 2:System.out.println("Female");
		break;
		
		default:System.out.println("Unknown");
		
		}
	}
}
