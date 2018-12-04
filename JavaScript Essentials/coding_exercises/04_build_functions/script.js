//Nmaed function
function findBiggestFraction(a, b) {
    var result;
    a>b ? result = ['firstFraction', a] : result = ['secondFraction', b];
    return result;
}

var firstFraction = 1/25;
var secondFraction = 1/33;

console.log("The " + findBiggestFraction(firstFraction, secondFraction)[0] +
" is the largest, and it's value is " + findBiggestFraction(firstFraction, secondFraction)[1]);

//Anonymous function - tied to a variable or event etc, they dont have names
var a  = 5/7;
var b = 18/25;

var theBiggest = function(a, b) {
    var result;
    a>b ? result = ['firstFraction', a] : result = ['secondFraction', b];
    return result;
}

console.log(theBiggest(a, b));

//Immediately invocked fucntion - run as soon as th ebrowser encounters them.
/*Created by taking an Anonymous function and wrapping it in brackets then adding
 another set of brackets after, for the arguments*/
 //Taking the above example:
 (function(a, b) {
     var result;
     a>b ? result = ['firstFraction', a] : result = ['secondFraction', b];
     return result;
 })();

 // We can then store the return value in a variable to print out the result:
 var theBiggest = (function(a, b) {
     var result;
     a>b ? result = ['firstFraction', a] : result = ['secondFraction', b];
     return result;
 })();    
