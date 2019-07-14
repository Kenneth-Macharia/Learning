
/*  COLLECTIONS > DATA STRUCTURES: They have their own methods for manipulating the data.
    Arraylists are Javas dynamic arrays. They very useful when storing data once then reading multiple times. Regular updates to them are slow e.g if an item is removed then, items have to be 'scooted' over to occupy the position vacated. This scotting over of items make arraylists updating slow. New items are added at the end of the array.

    Linkedlist: each element in the list are linked positionaly to the next, meaning each item has a referene to the next element, making this data structure faster than the arraylist especially when updating elements regulary. Your can use a java iterator to read from a linked list.

    Hashmaps are key-value pair Java structures, where the key and the values can be of any type including objects. Data type declaraton for them must be reference types not primitive types.

    HashSets are similar to LinkedList but data must be unique, thus if attempting to store duplicate values on one will be stored.

    Treeset are also similar to Hashset, but they sort values automatically as well.
*/

package mainpackagedemo;

import java.util.ArrayList;
// import java.util.HashMap;
// import java.util.Iterator;
// import java.util.Map;

// Hashmaps demo
class HashMapsdemo {
    String employee;
    String title;

    HashMapsdemo(String employee, String title) {
        this.employee = employee;
        this.title = title;
    }
}

//Linked List demo
class LinkedListDemo {

    String emloyeeTitle;

    LinkedListDemo (String title) {
        this.emloyeeTitle = title;
    }
}

// Arraylist class demo
class Employee {

    String employeeName;
    int emloyeeID;

    Employee (String name, int ID) {
        this.employeeName = name;
        this.emloyeeID = ID;
    }
}

// Simple arraylist demo
class ArrayListsDemo {

    void exampleArrayList () {
        
        ArrayList<String> names = new ArrayList<String>();

        names.add("Ken");
        names.add("Shee");
        names.add("Chris");

        for (String name: names) {
            System.out.println(name);
        }
    }
}

class Main {
    // Runner class

    public static void main(String[] args) {
        // Run simple arraylist demo
        // new ArrayListsDemo().exampleArrayList();

        // Run Arralylist class demo
        // ArrayList<Employee> employee = new ArrayList<Employee>();
        // employee.add(new Employee("Ken", 001));
        // employee.add(new Employee("Shee", 002));
        // System.out.println(employee.get(1).employeeName);

        // Run LinkedList class demo
        // LinkedList<LinkedListDemo> titles = new LinkedList<LinkedListDemo>();
        // titles.add(new LinkedListDemo("Software Engineer"));
        // titles.add(new LinkedListDemo("Interior Designer"));
        // titles.add(new LinkedListDemo("Medical Rep"));

        // System.out.println(titles.getLast());
        
        // Iterator<LinkedListDemo> iterator = titles.iterator();

        // while (iterator.hasNext()) {
        //     LinkedListDemo listItem = iterator.next();
        //     System.out.println(listItem.emloyeeTitle);
        // }

        //Run Hashmap class demo
        // HashMap<Integer, HashMapsdemo> languages = new HashMap<Integer, HashMapsdemo>();
        // languages.put(1, new HashMapsdemo("Kenneth", "Software Engineer"));
        // languages.put(2, new HashMapsdemo("Shee", "Interior Designer"));
        // languages.put(3, new HashMapsdemo("Chris", "Medical Rep"));

        // for (Map.Entry<Integer, HashMapsdemo> ltracker:languages.entrySet()) {
        //     System.out.println(ltracker.getKey() + ":" + ltracker.getValue().employee
        //     + " - " + ltracker.getValue().title);
        // }

    }
}

