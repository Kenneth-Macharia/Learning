var fname = prompt("Hello and welcome. Please enter your name:");
var lname = prompt("PLease enter your last name:");
var age = prompt("How old are you?");
var height = prompt("What is your height in centimeters?");
var pet = prompt("What is the name of your pet?");

if ((fname[0] === lname[0]) && (age>20 && age<30) && (height>=170) && (pet[pet.length-1] === 
"y")) {
    console.log("Welcome Comrade! You've passed the Spy test");
} else {
    console.log("Sorry, nothing to see here")
}