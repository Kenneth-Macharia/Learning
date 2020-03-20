/* -------- GAME INPUTS --------- */
// Ask for player names and assign them their colors
var player1Name = prompt('Player One: Enter your name, you will be BLUE');
var player1Color = 'rgb(86, 151, 255)';  // jQuery expects colors in this exact RGB format

var player2Name = prompt('Player Two: Enter your name, you will be RED');
var player2Color = 'rgb(237, 45, 73)';

// Fetch all the table rows
var allRows = $('table tr');  // Node list of all rows in the table

/* --------- FUNCTIONS -------- */
// Change the color of a known cell by row & col index, table origin is top-left cell and starts at (0, 0);
function changeCellColor (rowIndex, colIndex, colorToChange) {
    allRows.eq(rowIndex).find('td').eq(colIndex).find('input').css('background-color', colorToChange);
}

// Retrieve the current color of a given cell
function geCellColor (rowIndex, colIndex,) {
    return allRows.eq(rowIndex).find('td').eq(colIndex).find('input').css('background-color');
}

// Check the next availble cell to drop a color. If a cell is clicked we shall get the col index and start searching in that column the last availale cell to color. Since the rows are 6, wwe shall start searching from the bottom row (#5), coming up.
function getLastAvailableCell (colIndex) {
    var currentCellColor;

    for (var row = 5; row > -1; row--) {
        // For each cell, retrieve it's color and store it
        currentCellColor = geCellColor(row, colIndex);

        // Return the row at which the availble cell has been found. 'rgb(146, 140, 140)' is the default cell color.
        if (currentCellColor === 'rgb(146, 140, 140)') {
            return row
        }
    }
}

// Check for 4 consequtive matching color. E.g. starting with first cell in a row, if then next 3 don't match its color, move to cell 2 in that row and check if the next 3 after it match and so on until this you are out of the table, ensuring we also check that they are not of the same default color.
function cellColorMatch(cell1Color, cell2Color, cell3Color, cell4Color) {
    return (cell1Color === cell2Color && cell1Color === cell3Color && cell1Color === cell4Color && cell1Color != 'rgb(146, 140, 140)' && (cell1Color !== 'undefined' || cell4Color !== 'undefined'));
}

// Check for horizontal wins using the cellColorMatch function above
function checkHorizontalWins () {
    for (var row = 0; row < 6; row++) {
        for (var col = 0; col < 4; col++) {
            // check for color matches at each 4-cell interval / row
            if  (colorMatchCheck(geCellColor(row, col), geCellColor(row, col+1), geCellColor(row, col+2), geCellColor(row, col+3))) {
                // If there is a matching set of 4 cells, there is win, return TRUE
                return true;
            } else {
                // If not win, continue with the game
                continue;
            }
        }
    }
}

// Using the same logic as for horizontal win checks, check for vertical wins
function checkVerticalWins () {
    for (var col = 0; col < 7; col++) {
        for (var row = 0; row < 3; row++) {
            // check for color matches at each 4-cell interval / row
            if  (colorMatchCheck(geCellColor(row, col), geCellColor(row+1, col), geCellColor(row+1, col), geCellColor(row+1, col))) {
                // If there is a matching set of 4 cells, there is win, return TRUE
                return true;
            } else {
                // If not win, continue with the game
                continue;
            }
        }
    }
}

// Check for diagonal wins, stating at (0,0) and checking all -ve slope diagonals then all +ve slope diagonals
function diagonalWinCheck() {
    for (var col = 0; col < 5; col++) {
      for (var row = 0; row < 7; row++) {
        if (colorMatchCheck(returnColor(row,col), returnColor(row+1,col+1), returnColor(row+2,col+2), returnColor(row+3,col+3))) {
          console.log('diag');
          reportWin(row,col);
          return true;
        } else if (colorMatchCheck(returnColor(row,col), returnColor(row-1,col+1) ,returnColor(row-2,col+2), returnColor(row-3,col+3))) {
          console.log('diag');
          reportWin(row,col);
          return true;
        } else {
          continue;
        }
      }
    }
}

/* ------------ GAME LOGIC ---------- */
// Initiaze the start game properties
var currentPlayer = 1;
var currentPlayerName = player1Name;
var currentPlayerColor = player1Color;

// Display text for player one to start playing
$('h4').text(currentPlayerName + ' its your turn to pick a column..');

// Get the column clicked by the current player, by adding a 'click' event listener to all inputs in the table, then getting the column number of the closest table cell to the clicked input.
allRows.on('click', function () {
    var columnIndexClicked = $(this).closest('td').index();

    // Get the {row number} of the next available cell in this column that will be colored by the current player
    var nextAvailableCellRowNumber = getLastAvailableCell(columnIndexClicked);

    // Change the color of the available cell found above
    changeCellColor(nextAvailableCellRowNumber, columnIndexClicked, currentPlayerColor);

    // Check for a win {OR TIE??}
    if (horizontalWinCheck() || verticalWinCheck() || diagonalWinCheck()) {
        $('h1').text(currentPlayerName + ' has won!!');
        $('h3').text('Refresh the browser to play again...')
        $('h4').text('');
        $('table').slideUp(3000);
    }

    // Change player and continue playing 
    currentPlayer = currentPlayer * -1;

    if (currentPlayer == 1) {
        currentPlayerName = player1Name;
        currentPlayerColor = player1Color;
        $('h4').text(currentPlayerName + ' its your turn to pick a column..');

    } else {
        currentPlayerName = player2Name;
        currentPlayerColor = player2Color;
        $('h4').text(currentPlayerName + ' its your turn to pick a column..');
    }
}); 




