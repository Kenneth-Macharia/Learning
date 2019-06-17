package mainpackagedemo;

import java.util.Scanner;

class Exceptions {

    static Scanner reader = new Scanner(System.in);

    public static void main (String[] args) {
       
        try {
            System.out.print("Enter input:");
            int x = reader.nextInt();
            System.out.println(x);
            
        } catch (Exception e) {
            System.out.println(e);  //e methods like getmessage()

        } finally {
            System.out.println("After try-catch");
        }

        System.out.println("Regardless of try-catch");
    }
}