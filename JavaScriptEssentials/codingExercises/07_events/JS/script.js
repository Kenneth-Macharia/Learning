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
CTA.addEventListener("click", reveal, false);  //event 1
CTA.addEventListener("click", function() {console.log("Button clicked");}, false); //event 2
