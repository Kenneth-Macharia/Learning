//Named function, ususal and invocked by referencing their names
function findBiggestFraction(a, b) {
    var result;
    a>b ? result = ['firstFraction', a] : result = ['secondFraction', b];
    return result;
}

var firstFraction = 1/25;
var secondFraction = 1/33;

console.log("Named function call: " + findBiggestFraction(firstFraction, secondFraction)[0] +
" is larger, with a value of: " + findBiggestFraction(firstFraction, secondFraction)[1]);

/*Anonymous function - tied to a variable or event etc, they dont have names,
 invoke the variable by referencing the variable that hold the function as if it
  were a fucntion (also passing arguments). If we reference the variable only, the
  function inside it will be returned, which may be of importance where we want the
  fucntion and not the result of the function */
var a  = 5/7;
var b = 18/25;

var theBiggest = function(a, b) {
    var result;
    a>b ? result = ['firstFraction', a] : result = ['secondFraction', b];
    return result;
}

console.log("Anonymous function call: " + theBiggest(a, b)[0] +
" is larger, with a value of: " + theBiggest(a, b)[1]);

/* Immediately invocked function run as soon as the browser encounters them.
 Created by taking an anonymous function and wrapping it in brackets then adding
 another set of brackets after, for the arguments. These are often used as event
 listeners */
 //Taking the above example:
 (function(a, b) {
     var result;
     a>b ? result = ['firstFraction', a] : result = ['secondFraction', b];
     return result;
 })();

 // We can then store the return value in a variable to print out the result:
 var theLargest = (function(a, b) {
     var result;
     a>b ? result = ['firstFraction', a] : result = ['secondFraction', b];
     return result;
 })(a, b);

 console.log("Immediately invoked function call: " + theLargest[0] +
 " is larger, with a value of: " + theLargest[1]);
