//Nmaed function
function findBiggestFraction(a, b) {
    var result;
    a>b ? result = ['firstFraction', a] : result = ['secondFraction', b];
    return result;
}

var firstFraction = 1/25;
var secondFraction = 1/33;

console.log(findBiggestFraction(firstFraction, secondFraction));

//Anonymous function - tied to a variable or event etc, they dont have names
var a  = 5/7;
var b = 18/25;

var theBiggest = function(a, b) {
    var result;
    a>b ? result = ['firstFraction', a] : result = ['secondFraction', b];
    return result;
}

console.log(theBiggest(a, b));
