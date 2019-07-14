/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package newpackage;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;


class DbConnect {
    
    public static void main(String[] args) throws ClassNotFoundException, 
            InstantiationException, IllegalAccessException {  
        Connection conn = null;

        try {
             Class.forName("org.sqlite.JDBC").newInstance();
            conn = DriverManager.getConnection("jdbc:sqlite:test.db");
            System.out.println("Connections successfull");

        } catch (SQLException e) {
            System.out.println("Connection failed!");
            System.out.println(e.getCause());
            System.exit(0);
        }
    }    
}
