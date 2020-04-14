// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []

// Create the functions for the tasks

// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array

function addNew (name) {
    roster.push(name);
    alert(name + " added");
}

// REMOVE STUDENT

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//

function remove (name) {
    let indexToRemove = roster.indexOf(name);

    if (indexToRemove !== -1) {
        roster.splice(indexToRemove, 1);
        alert(name + " removed!");
    } else {
        alert ("Name not found!");
    }
}

// DISPLAY ROSTER

// Create a function called display that prints out the roster to the console.

function display () {
    console.log(roster);
}

// Start by asking if they want to use the web app

// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.

var start = prompt("Would you like to start the roster app? y/n");

if (start === "y") {

    while (action !== "quit") {
        var action = prompt("Please select an action: add, remove, display, quit");

        if (action === "add") {
            let name = prompt("What name would you like to add?");
            if (name != "") {
                addNew (name);
            } else {
                alert("Please enter a name")
            }

        } else if (action === "remove") {
            let name = prompt("What name would you like to remove?");
            if (name != "") {
                remove (name);
            } else {
                alert("Please enter a name")
            }

        } else if (action === "display") {
            display ();

        } else {
            alert("That is not a valid action, please try!");
        }
    }
    
    alert("Thanks for using the app, refresh the page to start over.")
}


