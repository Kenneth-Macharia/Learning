/* 
    Multi-threading or parallel processing involves excuting more that on task at the same. This enables background processes to run while the UI is still active without interference e.g. interacting with a news app while its fetching updated information from the back-end at the same time so as to ensure a smooth and continous user experience.

    This is also know as a asynchrony, where a task doses not have to wait until the preceeding task finishes before it can start, saving compute time. Previously only synchrony existed and follows classic program execution flow.

    In Java, multi-threaded classes must extend the Thread class to get multi-tthreading capability,then override the super class run() with your class functionality.

    Demo below

    Runnable is a Java interface that has multi-threaded capabilties just like the Thread class. It exists to address the inheritance short-comings of classes. To implement Runnable, create a runnable class, then instantiate it and pass the instance to a Thread class object to run the Runnable object.

    Demo below

    synchronized blocks of code can only be invoked by one process at any one time. Another process requiring the block code will have to wait until the previous process is done. This is helpful for example where these code blocks are shared e.g static class members. To use synchornized blocks, use the 'synchronized' key word in the block header.
    
    Demo below

    wait(), join() and notify() used with mutli-threaded processes to manage when each should start.

    Deadlock is a situation where one process is waiting on a resource to be released by another process, which maus t also be managed to ensure it does not occur.


*/

package mainpackagedemo;

//Multi-threading demo
class Multi_threading extends Thread {

    String threadName;
    boolean loopController = true;

    // class constructor
    Multi_threading (String threadName) {
        this.threadName = threadName;        
    }

    @Override
    public void run () {
        //A never ending while loop
        int counter = 0;

        while (loopController) {
            System.out.println(threadName + " : " + counter);
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {}
            
            counter +=1;
        }
    }
}

// Runnable demo
class myRunnable implements Runnable {

    @Override
    public void run () {
        //A never ending while loop
        int counter = 0;

        while (true) {
            System.out.println("Runnable" + " : " + counter);
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {}
            
            counter +=1;
        }
    }

    // public static void main(String [] args) {
    //     myRunnable r = new myRunnable();
    //     Thread tr = new Thread(r);
    //     tr.start();
    // }

}

// synchronized demo
class Synchronized extends Thread {

    static String threadName;

    // class constructor
    Synchronized (String threadName) {
        Synchronized.threadName = threadName;       
    }

    @Override
    public void run () {
        display();
    }

    synchronized static void display () {
        //synchronized shared block
        int counter = 0;

        while (counter < 11) {
            System.out.println(counter);
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {}
            
            counter +=1;
        }
    }
    
    public static void main (String [] args) {
	
        Synchronized t1 = new Synchronized("thread1");
        Synchronized t2 = new Synchronized("thread2"); 
        t1.start();       
        t2.start();
	}
}