// Part 6 - Objects Exercise

////////////////////
// PROBLEM 1 //////
//////////////////

// Given the object:
var employee1 = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  nameLength: function () {
    console.log(this.name.length);
  }
}

// Add a method called nameLength that prints out the
// length of the employees name to the console.


///////////////////
// PROBLEM 2 /////
/////////////////

// Given the object:
var employee2 = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  alertProperties: function () {
    for (key in this) {
      alert(this[key]);
    }
  }
}

// Write program that will create an Alert in the browser of each of the
// object's values for the key value pairs. For example, it should alert:

// Name is John Smith, Job is Programmer, Age is 31.



///////////////////
// PROBLEM 3 /////
/////////////////

// Given the object:
var employee3 = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  lastName: function () {
    console.log(this.name.split(" ")[1]);
  }
}

// Add a method called lastName that prints
// out the employee's last name to the console.

// You will need to figure out how to split a string to an array.
// Hint: http://www.w3schools.com/jsref/jsref_split.asp

// Random color changer (DOM implementation)

// Generate a random color
function randomColorGenerator () {
  let possibleHexChars = "0123456789ABCDEF";
  let randomHex = "#";

  for (let i = 1; i<=6; i++) {
    randomHex += possibleHexChars[Math.floor(Math.random() * 16)]
  }
  return randomHex;
}

// Change the H1 color
function affectHtmlElement () {
  let H1ObjElement = document.querySelector("h1");
  H1ObjElement.style.color = randomColorGenerator();
}

// Change element color after every 1 second
setInterval(affectHtmlElement, 1000);
