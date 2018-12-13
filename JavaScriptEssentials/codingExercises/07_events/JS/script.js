/* We want to hide the book now button using the .hide class and display an alert
 message */

//Set up tow consts for the button and the booking area
const CTA = document.querySelector(".cta a");
const ALERT = document.querySelector("#booking-alert");

/* If JavaScript is enabled, then the secton will be as is ie. no button + alert
 message, else they get the book button and the alert is hidden */
CTA.classList.remove("hide");
ALERT.classList.add("hide");

//Create a function to toggle the .hide class on or off
function reveal(e) {
    e.preventDefault(); /* cancel the button follow link action via the 'e' event
                        object attirbute, passed as an argument in to the function */
    CTA.classList.toggle("hide");
    ALERT.classList.toggle("hide");
}

//Build an event handler to run the function upon click of the button
//CTA.onclick = reveal;  /* Dont use the brackets at the end to ensure the function
                        //function does not run on page load */

//Refactoring the above code for event listeners
//CTA.addEventListener("click", reveal, false);  //event 1
//CTA.addEventListener("click", function() {console.log("Button clicked");}, false); //event 2

//Passing arguments to an event function
//Function refactored to accept arguments
function reveal2(e, clickedObject) {
    e.preventDefault(); /* cancel the button follow link action via the 'e' event
                        object attirbute, passed as an argument in to the function */
    /* Use a ternary operator to check the link text. If is reads "book now" change it
    to 'Ooops!' and vice versa, on click */
    /* We shall pass in the clicked object as an argument and check it's innerHTML
    attribute and ammend it as above. */
    clickedObject.innerHTML == "Book Now" ? CTA.innerHTML = "Oooops!" : CTA.innerHTML = "Book Now";
}

/* Refactored event listener. We will also pass in the 'e' event object to prevent
 the linsk default behaviour of trying to navigate to a source, as well as 'this'
 which is the clicked object, the button link CTA */
CTA.addEventListener("click", function(e) { reveal2(e, this);}, false);
