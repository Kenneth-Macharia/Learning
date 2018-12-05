/* After running the doSomeMath() function, only the result is accessible but not
the local variables a, b and sum. */
// function doSomeMath() {
// 	var a = 5;
// 	var b = 4;
// 	var sum = a + b;
//
// 	return sum;
// }
//
// var theResult = doSomeMath();
//
// console.log("The result: ", theResult);

/* In place of the sum variable, add a child function, to try and highlight closure
 this returns the multiply function, not the it's result, os again everything
 inside doSomeMath() is discarded */
// function doSomeMath() {
// 	var a = 5;
// 	var b = 4;
//
// 	function multiply() {
// 		var result = a*b;
// 		return result;
// 	}
//
// 	return multiply;
// }
//
// var theResult = doSomeMath();
//
// console.log("The result: ", theResult);

/* To get the result of the multiply() functions run the result variable as if it
was a function, this is closure in action */
// function doSomeMath() {
// 	var a = 5;
// 	var b = 4;
//
// 	function multiply() {
// 		var result = a*b;
// 		return result;
// 	}
//
// 	return multiply;
// }
//
// var theResult = doSomeMath();
//
// console.log("The result: ", theResult() );

//Application of closures, calculating Ems in CSS:
// function giveMeEms(pixels) {
// 	var baseValue = 16;
//
// 	function doTheMath() {
// 		return pixels/baseValue;
// 	}
// 	return doTheMath;
// }
//
// //Calculate various Ems values and return:
// var smallSize = giveMeEms(12);
// console.log("Small size: ", smallSize());
// var largeSize = giveMeEms(24);
// console.log("Large size: ", largeSize());
