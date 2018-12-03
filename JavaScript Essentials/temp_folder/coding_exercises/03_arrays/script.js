//Create an undefined variable
var pens;
//Populate the variable with the arryay itesm
pens = ['red', 'blue', 'green', 'orange'];  //shot form
console.log(pens);

//Long form arryay declaration
var pens2 = new Array('red', 'blue', 'green');
console.log(pens2);

//Arrays can hold different type data at once
var multiItems = new Array('keys', 5, false, 10.5, null);
console.log(multiItems);

//Accessing & changing array items via indices
console.log(pens2[0]);
pens[0] = 'purple';
console.log(pens);
