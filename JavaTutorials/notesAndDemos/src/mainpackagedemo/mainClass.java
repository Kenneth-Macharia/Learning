package mainpackagedemo;

public class mainClass {
	
	public static void main (String [] args) {
		// Runs the Multi-threaded class
        Multi_threading t1 = new Multi_threading("thread1");
        Multi_threading t2 = new Multi_threading("thread2");

        //Run both threads
        t1.start();
        t2.start();
	}
}
