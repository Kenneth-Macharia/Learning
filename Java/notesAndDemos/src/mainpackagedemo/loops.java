package mainpackagedemo;

import java.util.Scanner;

public class loops {
	
	/*
	 * Continue: keyword skips the block of code immediately following it in a loop but resumes the next iteration
	 * Break: Keyword stops loop execution once encountered 
	 */
	
	static Scanner reader = new Scanner(System.in);
	
	public static void main (String [] args) {
//		For loop demo
		
		System.out.println("For loop starting...");
		
		for (int i=0; i<10; i++) {
			System.out.println("Count:" + i);
		}
		
		System.out.println("For loop ended. \n");
		System.out.println("-------------------------");
		
//		While loop demo: Evaluates the condition before executing the loop block
		
		System.out.println("While loop starting...");
		System.out.print("Enter a random greater than zero....");
		
		int i = reader.nextInt();

		while (i>=0) {
			if (i % 4 == 0) {
				System.out.println(i + " is a multiple of 4");
			}
			i--;
		}
		System.out.println("While loop ended. \n");
		System.out.println("-------------------------");
		
//		Do while demo: Executes the loop block once before evaluating the condition
		
		System.out.println("Do While loop starting... \n");
		System.out.print("Enter a random greater than zero....");
				
		int j = reader.nextInt();

		
		do {
			if (j % 4 == 0) {
				System.out.println(j + " is a multiple of 4");
			}
			j--;
	
		} while (j>=0);
		System.out.println("Do While loop ended.");
	}
}
