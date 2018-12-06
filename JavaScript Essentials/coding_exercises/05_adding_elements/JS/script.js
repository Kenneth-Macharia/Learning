//Problem: The image inside the main-area class does not have a caption.
/*Solution: Take the image description in the alt attribute and create a new <figure>
 element under the image <figure> element and insert the description into it, then
 finally delete the description from the img attribute element */

 //declare constants for the <figure> and the image inside the <figure>:
 const FEATURED = document.querySelector(".featured-image");

 /* Use the <figure> constant to quickly reference the image inside it, in it's
 query selector, useful when working with nested elements */
 const THEIMAGE = FEATURED.querySelector("img");

//Get the image alt attribute text and hold it in a variable
var altText = THEIMAGE.getAttribute("alt");

//Create the <figure> and hold it in a variable
var captionElement = document.createElement("figcaption");

//Create a new text node
var captionText = document.createTextNode(altText);

//Append the new text node inside the new caption element
captionElement.appendChild(captionText);

//Test the captionElement in the console
console.log(captionElement);
