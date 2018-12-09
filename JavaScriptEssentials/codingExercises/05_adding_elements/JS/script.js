// METHOD 1 (LONG BUT RECOMMENDED) : ADDING ELEMENTS (SUPPORTED BY ALL BROWSERS)

/* Set up two constants to hold <figure> and th other for the image in the
figure */
const FEATURED = document.querySelector(".featured-image");
/* Use the 'FEATURED' variable which has the <figure>, to reference the <img>,
instead fo their parent element, the document. This si a great way to reference
nested elements */
const THEIMAGE = FEATURED.querySelector("img");

//Get the imeg 'alt' attribute and store it
var altText = THEIMAGE.getAttribute("alt");

//Create the <figure> caption element and store it
var captionElement = document.createElement("figcaption");

//Create a textnode to hold the alt text
var captionText = document.createTextNode(altText);

//Append the alt text inside the fig caption element
captionElement.appendChild(captionText);

//Append the new caption element to the image figure element
FEATURED.appendChild(captionElement);

//Remove the old image alt attribute contents
THEIMAGE.setAttribute("alt", "");

//Test the fig caption element
console.log(captionElement);


//METHOD 2 (SHORT): ADDING ELEMENTS (NOT SUPPORTED BY ALL BROWSERS)

// const FEATURED = document.querySelector(".featured-image");
// const THEIMAGE = FEATURED.querySelector("img");
// var altText = THEIMAGE.getAttribute("alt");
// var captionElement = document.createElement("figcaption");
//
// /* Skips the creation of the textnode and appeding of the alt text, by using the
// 'append' method instead of the 'appendChild' method.  */
// captionElement.append(altText);
// FEATURED.append(captionElement);
// THEIMAGE.setAttribute("alt", "");
//
// //Test the fig caption element
// console.log(captionElement);

/*READ THE DOCUMENTATION TO SEE HOW TO PROVIDE FALL-BACKS FOR OLDER BROWSERS:
https://developer.mozilla.org/en-US/docs/Web/API/ParentNode/append */
