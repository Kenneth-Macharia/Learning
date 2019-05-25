package mainpackagedemo;

import java.util.Scanner;

public class Inputs {
	
	static Scanner reader = new Scanner(System.in);
	static Scanner nextReader = new Scanner(System.in);
	
	public static void main (String [] args) {
		
		System.out.print("Enter name:");
		String name = reader.nextLine();
		System.out.print("Enter age:");
		int age = reader.nextInt();
		System.out.print("Enter salary:");
		double salary = reader.nextDouble();
		System.out.print("Enter gender:");
		String genderInput = nextReader.next();
		char gender = genderInput.charAt(0);
		
		System.out.println(name);
		System.out.println("Age:" + age);
		System.out.println("Salary:" + salary);
		System.out.println("Gender:" + gender);
	}

}
