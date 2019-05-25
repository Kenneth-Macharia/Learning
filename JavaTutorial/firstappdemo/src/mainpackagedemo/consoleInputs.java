package mainpackagedemo;

public class consoleInputs {
	
	public static void main (String [] args) {
	
/*	Input from the console/terminal using String [] args
 * 	Remove the package name when running the app from terminal
 *  Compile source code first before running: javac example.java
 *  Run complied class file: java example
 */
		
		String name = args[0];
		String gender = args[1];
		
		System.out.println("Name:" + name);
		System.out.println("Gender:" + gender);
	}

}
