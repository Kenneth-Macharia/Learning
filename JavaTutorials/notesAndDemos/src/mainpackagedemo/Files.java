package mainpackagedemo;

import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.Scanner;

// A simple CLI app for manipulating files
class Files {
    static File file;
 
    static void deleteFile (String fileName) {
        try {
            file = new File(fileName);
            file.delete();         

        } catch (Exception e) {
            System.out.println("\nERROR occured deleting file, try again.\n");
        }
        System.out.println("\nOUTPUT: " + fileName + " deleted.\n");
    }

    static void updateFile (String fileName, String fileData) {
        try {
            // true parameter to File writer constructor, enables data appending to existing file contents. Without it, new data written to existing file will overwrite its previous contents.

            FileWriter writerObj = new FileWriter(fileName, true);
            writerObj.write("\n" + fileData);
            writerObj.close();

        } catch (Exception e) {
            System.out.println("\nERROR occured updating file, try again.\n");
        }
        System.out.println("\nOUTPUT: " + fileName + " updated. \n");
    }

    static void readFile (String fileName) {
        int characters;

        try {
            FileReader readObj = new FileReader(fileName);
            // Files are read char by char and returned in their ASCII format (integers), they will then need to be cast back to char to be displayed.
            // The file char will be read and displayed simulateanously using a while loop

            System.out.print("\nOUTPUT: ");
            while ((characters = readObj.read())!= -1) {
                System.out.print((char) characters);
            }
            readObj.close();

        } catch (Exception e) {
            System.out.println("\nERROR occured reading file, try again.\n");
        }
        System.out.println("\n");
    }

    static void writeFile (String fileName, String fileData) {
        
        try {
            FileWriter writerObj = new FileWriter(fileName);
            writerObj.write(fileData);
            writerObj.close();
        
        } catch (Exception e) {
            System.out.println("\nERROR occured creating file, try again.\n");
        }

        System.out.println("\nOUTPUT: " + fileName + " created.\n");
    }

    static boolean fileExists (String fileName) {
        file = new File(fileName);
        return file.exists();
    }

    public static void main (String [] args) {
        System.out.println("--------------------------------------");
        System.out.println("WELCOME TO THE FILE MANAGEMENT CLI APP");
        System.out.println("Use it to manipulate text files");
        System.out.println("--------------------------------------");

        int actionOption = 0;

        Scanner dataReader = new Scanner(System.in);
        Scanner actionReader = new Scanner(System.in);

        while (actionOption != 5) {
            try {
                System.out.print("App actions: 1-Create file, 2-Read file, 3-Update file 4-Delete file, 5-Quit app: ");
                actionOption = actionReader.nextInt();

            } catch (Exception e) {
                System.out.println();
                System.out.println("ERROR: App option input can only be whole numbers between 1 and 5!\n");
                actionReader.nextLine();
                continue;
            }

            String fileData;
            String fileName;

            switch (actionOption) {
                case 1:
                System.out.println("\n*** CREATE FILE ***");
                System.out.print("Enter file name ['exit' to cancel]: ");
                fileName = dataReader.nextLine();

                if (fileExists(fileName)) {
                    System.out.println("WARNING: " + fileName.concat(".txt") + " already exists and will be overwritten by this action, select [3-UPDATE] option instead.\n");
        
                } else {
                    System.out.print("Enter text to save to new file ['exit' to cancel]: ");
                    fileData = dataReader.nextLine();
                    writeFile(fileName, fileData);
                }
                break;

                case 2:
                System.out.println("\n*** READ FILE ***");
                System.out.print("Enter file name ['exit' to cancel]: ");
                fileName = dataReader.nextLine();

                if (!fileExists(fileName)) {
                    System.out.println("\nOUTPUT: " + fileName.concat(".txt") + " does not exist.\n");
        
                } else {
                    readFile(fileName);
                }
                break;

                case 3:
                System.out.println("\n*** UPDATE FILE ***");
                System.out.print("Enter file name ['exit' to cancel]: ");
                fileName = dataReader.nextLine();

                if (!fileExists(fileName)) {
                    System.out.println("\nOUTPUT: " + fileName.concat(".txt") + " does not exist.\n");
        
                } else {
                    System.out.print("Enter text to add to file ['exit' to cancel]: ");
                    fileData = dataReader.nextLine();
                    updateFile(fileName, fileData);
                }
                break;

                case 4:
                System.out.println("\n*** DELETE FILE ***");
                System.out.print("Enter file name ['exit' to cancel]: ");
                fileName = dataReader.nextLine();

                if (!fileExists(fileName)) {
                    System.out.println("\nOUTPUT: " + fileName.concat(".txt") + " does not exist.\n");
        
                } else {
                    deleteFile(fileName);
                }
                break;

                default:
                System.out.println("\nOUTPUT: App option input can only be whole numbers between 1 and 5!\n");
                break;
            }
        }
        dataReader.close();
        actionReader.close();
        System.out.println("\nThank you for using the File CLI APP.");
        System.out.println("--------------------------------------");
    }
}