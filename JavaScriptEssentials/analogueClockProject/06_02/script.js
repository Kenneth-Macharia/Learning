//Taget the id in HTML for the 3 clock arms
const HOURHAND = document.querySelector("#hour");
const MINUTEHAND = document.querySelector("#minute");
const SECONDHAND = document.querySelector("#second");

//Functions to re-run our code, see explanations as the end of this code block

/* OPTION 1: CLOCK TICK ACTION - Accurate and won't lead to JavaScript throttling
 by the browser, since the time comes from the the Date() object. Does not need
 the transform CSS property. */

function runTheClock() {
    //Create a date object to return the current time
    var date = new Date();
    //Get the various components of the date objects using it's methods
    let hr = date.getHours();
    let min = date.getMinutes();
    let sec = date.getSeconds();

    //console.log("Hrs: " + hr + " Mins: " + min + " Sec: " + sec);

    //Create block scope variables to hold the # of degrees to turn each of the arms
    let hrPosition = (hr*360/12) + (min*(360/60)/12);
    let minPosition = (min*360/60) + (sec*(360/60)/60); //Add the movement within the min
    let secPosition = sec*360/60;

    //Convert the values in the above variables to degrees in CSS and move the arms
    //Normal CSS syntax is transform : rotate(20deg);
    HOURHAND.style.transform = "rotate(" + hrPosition + "deg)";
    MINUTEHAND.style.transform = "rotate(" + minPosition + "deg)";
    SECONDHAND.style.transform = "rotate(" + secPosition + "deg)";

    /* Make the clock to update the time automatically, since currently the clock
     only updates when the browser is reloaded, i.e a static script */
    /* We need to re-run the above script after every second and this is done using
     the 'setInterval' method. */
    //https://goo.gl/zqQrex
    //Wrap the code in a function and then call the function at every interval
}

/* OPTION 2: CLOCK SMOOTH ACTION - Will lead to browser JS throttling as the
 we manually update the clock arm movement via math and not using the Date() object
 thus if we for example move to a differnt tab for a while the move back the
 clock will have to suddenly correct itself. This method will work together
 with the CSS transform property to achive the smooth arm action. */

// var date = new Date();
//
// let hr = date.getHours();
// let min = date.getMinutes();
// let sec = date.getSeconds();
//
// let hrPosition = (hr*360/12) + (min*(360/60)/12);
// let minPosition = (min*360/60) + (sec*(360/60)/60);
// let secPosition = sec*360/60;
//
// function runTheClock() {
//
//     hrPosition = hrPosition + (3/360);
//     minPosition = minPosition + (6/60);
//     secPosition = secPosition + 6;
//
//     HOURHAND.style.transform = "rotate(" + hrPosition + "deg)";
//     MINUTEHAND.style.transform = "rotate(" + minPosition + "deg)";
//     SECONDHAND.style.transform = "rotate(" + secPosition + "deg)";
// }


//run our function after every second
setInterval(runTheClock, 1000);
