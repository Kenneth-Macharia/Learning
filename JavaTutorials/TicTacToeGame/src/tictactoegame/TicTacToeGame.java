/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tictactoegame;

import java.util.ArrayList;
import java.util.Random;
import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

public class TicTacToeGame extends Application {
    
    //Declare game properties
    int activePlayer = 1;
    ArrayList<Integer> player1Selections = new ArrayList<>();
    ArrayList<Integer> player2Selections = new ArrayList<>();
    
    // Initialize buttons
    Button btn1 = new Button();
    Button btn2 = new Button();
    Button btn3 = new Button();
    Button btn4 = new Button();
    Button btn5 = new Button();
    Button btn6 = new Button();
    Button btn7 = new Button();
    Button btn8 = new Button();
    Button btn9 = new Button();
    
    @Override
    public void start(Stage primaryStage) {
        
        // Lambda format for using a functional interface
        btn1.setOnAction(e -> {
            PlayGame(1, btn1);
        });
        
        btn2.setOnAction(e -> {
            PlayGame(2, btn2);
        });

        btn3.setOnAction(e -> {
            PlayGame(3, btn3);
        });
 
        btn4.setOnAction(e -> {
            PlayGame(4, btn4);
        });
   
        btn5.setOnAction(e -> {
            PlayGame(5, btn5);
        });

        btn6.setOnAction(e -> {
            PlayGame(6, btn6);
        });
 
        btn7.setOnAction(e -> {
            PlayGame(7, btn7);
        });

        btn8.setOnAction(e -> {
            PlayGame(8, btn8);
        });
   
        btn9.setOnAction(e -> {
            PlayGame(9, btn9);
        });
        
//        App Layout type
        GridPane grid = new GridPane();
        
        // Grid Styling properties
        grid.setAlignment(Pos.CENTER);
        grid.setHgap(10);
        grid.setVgap(10);
        grid.setPadding(new Insets(25, 25, 25, 25));
        
//        Add elements to layout
        grid.add(btn1, 0, 0);
        grid.add(btn2, 1, 0);
        grid.add(btn3, 2, 0);
        grid.add(btn4, 0, 1);
        grid.add(btn5, 1, 1);
        grid.add(btn6, 2, 1);
        grid.add(btn7, 0, 2);
        grid.add(btn8, 1, 2);
        grid.add(btn9, 2, 2);
        
//        Holds all the physical contents of the app
        Scene scene = new Scene(grid, 400, 400);
        
        //Connect an external CSS sheet to further style the Scene
        scene.getStylesheets().add(TicTacToeGame.class.getResource("style.css")
                .toExternalForm());
        
        // App display window and top-most JavaFX container class
        primaryStage.setTitle("TicTacToe Game");
        primaryStage.setScene(scene);
        primaryStage.show();
    }    
    
    void PlayGame (int CellId, Button selectedButton) {
        if (activePlayer == 1) {
           selectedButton.setText("X");
           player1Selections.add(CellId);
           activePlayer = 2;
           autoPlayer();
           
        } else if (activePlayer == 2) {
            selectedButton.setText("O");
            player2Selections.add(CellId);
            activePlayer = 1;
        }
        selectedButton.setDisable(true);
        checkWinner();
    }
    
    void checkWinner () {
        int winner = 0;
        String msg = "";
        
        if (player1Selections.contains(1) && player1Selections.contains(2) &&
                player1Selections.contains(3)) {
            winner = 1;
            
        } else if (player2Selections.contains(1) && player2Selections.contains(2)
                && player2Selections.contains(3)) {
            winner = 2;
        }
        
        if (player1Selections.contains(4) && player1Selections.contains(5) &&
                player1Selections.contains(6)) {
            winner = 1;
            
        } else if (player2Selections.contains(4) && player2Selections.contains(5)
                && player2Selections.contains(6)) {
            winner = 2;
        }
        
        if (player1Selections.contains(7) && player1Selections.contains(8) &&
                player1Selections.contains(9)) {
            winner = 1;
            
        } else if (player2Selections.contains(7) && player2Selections.contains(8)
                && player2Selections.contains(9)) {
            winner = 2;
        }
        
        if (player1Selections.contains(1) && player1Selections.contains(4) &&
                player1Selections.contains(7)) {
            winner = 1;
            
        } else if (player2Selections.contains(1) && player2Selections.contains(4)
                && player2Selections.contains(7)) {
            winner = 2;
        }
        
        if (player1Selections.contains(2) && player1Selections.contains(5) &&
                player1Selections.contains(8)) {
            winner = 1;
            
        } else if (player2Selections.contains(2) && player2Selections.contains(5)
                && player2Selections.contains(8)) {
            winner = 2;
        }
        
        if (player1Selections.contains(3) && player1Selections.contains(6) &&
                player1Selections.contains(9)) {
            winner = 1;
            
        } else if (player2Selections.contains(3) && player2Selections.contains(6)
                && player2Selections.contains(9)) {
            winner = 2;
        }
        
        if (player1Selections.contains(1) && player1Selections.contains(5) &&
                player1Selections.contains(9)) {
            winner = 1;
            
        } else if (player2Selections.contains(1) && player2Selections.contains(5)
                && player2Selections.contains(9)) {
            winner = 2;
        }
        
        if (player1Selections.contains(3) && player1Selections.contains(5) &&
                player1Selections.contains(7)) {
            winner = 1;
            
        } else if (player2Selections.contains(3) && player2Selections.contains(5)
                && player2Selections.contains(7)) {
            winner = 2;
        }
        
        if (winner != 0) {
            
            if (winner == 1) {
                msg = "Player 1 wins!";
                
            } else if (winner == 2) {
                msg = "Player 2 wins!";
            }
            
            //Alert dialogue box
            Alert info = new Alert(Alert.AlertType.INFORMATION);
            info.setTitle("Game Information");
            info.setHeaderText("Game Over!");
            info.setContentText(msg);
            info.show();
        }   
    }
    
    void autoPlayer () {
        ArrayList<Integer> emptyCells = new ArrayList<>();
        
        for (int cell = 0; cell < 10; cell++) {
            if (!(player1Selections.contains(cell) || player2Selections
                    .contains(cell))) {
                emptyCells.add(cell);
            }
        }
        
        Random rObj = new Random();
        int randomNumber = rObj.nextInt(emptyCells.size()-0) + 0;
        int cellId = emptyCells.get(randomNumber);
        Button selectedButton = null;
        
        // Get button selected
        switch (cellId) {
            case 1:
                selectedButton = btn1;
                break;
            case 2:
                selectedButton = btn2;
                break;
            case 3:
                selectedButton = btn3;
                break;
            case 4:
                selectedButton = btn4;
                break;
            case 5:
                selectedButton = btn5;
                break;
            case 6:
                selectedButton = btn6;
                break;
            case 7:
                selectedButton = btn7;
                break;
            case 8:
                selectedButton = btn8;
                break;
            case 9:
                selectedButton = btn9;
                break;
            default:
                System.out.println("No button for player 2 clicked!");
                break;
        }
        
        PlayGame(cellId, selectedButton);
    }
    
    
    public static void main(String[] args) {
        launch(args);
    }
    
}
