package mainpackagedemo;

import java.util.Scanner;

public class arrays {
	
	/*
	 * Arrays are a sequence of elements stored under the same name.
	 * strings are also arrays of characters, use charAt() method to get chars at specific indices of a string
	 * You can us other String class methods to manipulate strings e.g split words according to a specific
	 * criteria e.g spaces in between i.e sentence.split(" ")
	 * 
	 */

	static Scanner reader = new Scanner(System.in);
	
	public static void main (String [] args) {
//		One dimensional array demo
		
		String[] jobs = new String[4];
		
		System.out.println("Enter job titles:");
		
		for (int i=0; i<4; i++) {
			jobs[i] = reader.nextLine();		
		}
		
		System.out.println("Printing out the job titles...");
		
		for (int j=0; j<4; j++) {
			System.out.println(jobs[j]);
		}
		
//		Two dimensional array demo: Cell reference starts with row index then column index,
//		starting from zero.
		
//		Problem 1: Populate a 2-dimensional integer array of size 3*3 and retrive the elements in its diagonal
		
		Integer [][] myArray = new Integer[3][3];
		
		System.out.println("Enter 9 integers for our array:");
		
		for (int i=0; i<3; i++) {
			for (int j=0; j<3; j++) {
				myArray[i][j] = reader.nextInt();			
			}
		}
		
		System.out.println("Printing array diagonal values:");
		
		for (int i=0; i<3; i++) {
			for (int j=0; j<3; j++) {
				if (i == j) {
					System.out.print(myArray[i][j]);
				}
				System.out.print("\t");
			}
			System.out.println("\n");
			System.out.println("\n");
		}
		
//		Problem 2: Print values in the lower triangle of the array diagonal
		
		System.out.println("Printing values in the lower triangle of the array diagonal:");
		
		for (int i=0; i<3; i++) {
			for (int j=0; j<3; j++) {
				if (i > j) {
					System.out.print(myArray[i][j] + "\t");
				}
			}
			System.out.println("\n");
			System.out.println("\n");
		}
		
		
	}
}
