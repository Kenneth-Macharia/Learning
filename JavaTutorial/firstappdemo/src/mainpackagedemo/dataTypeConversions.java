package mainpackagedemo;

public class dataTypeConversions {
	
	public static void main (String [] args) {
		
//		Conversions are achieved through parsing or casting. Convrsion between different type categories e.g numbers and strings
//		is only possible through parsing.
		
		int age = 35;
		double salary = 250000.50;
		boolean isTrue = true;
		String rate = "35.5";
		
//		convert to String
		String newAge = String.valueOf(age);
		String newSalary = String.valueOf(salary);
		String newIsTrue = String.valueOf(isTrue);
	
//		convert to int
//		int newRateParse = Integer.parseInt(rate);
		int newSalaryCast = (int) salary;
		
//		convert to double
		double xtraNewrateParse = Double.parseDouble(rate);
		double newAgecast = (double) age;
		
		System.out.println(age + " vs " + newAge);
		System.out.println(salary + " vs " + newSalary + " vs " + newSalaryCast);
		System.out.println(isTrue + " vs " + newIsTrue);
//		System.out.println(rate + "vs" + newRateParse);
		System.out.println(rate + " vs " + xtraNewrateParse);
		System.out.println(age + " vs " + newAgecast);
		
	}

}
