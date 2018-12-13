const testWrapper = document.querySelector(".test-wrapper");
const testArea = document.querySelector("#test-area");
const resetButton = document.querySelector("#reset");
const theTimer = document.querySelector(".timer");
var originText;

//The timer array (min:sec:centiseconds:miliseconds)
var timer = [0, 0, 0, 0];

//variable to hold and reference the 'setInterval method'
var interval;
var timerRunning = false;  //when script loads the timer is not running

//Generate a random sentence, populate the #text <p> and the originText var
window.onload = function() {

    var subjects = ['I','You','Bob','John','Sue','Kate','The lizard people'];
    var verbs = ['will search for','will get','will find','attained','found','will start interacting with','will accept','accepted'];
    var objects = ['Billy','an apple','a Triforce','the treasure','a sheet of paper'];
    var endings = [ '.',', right?','.',', like I said.','.',', just like your momma!'];

    var wawah = document.querySelector("#text");

    originText = text.innerHTML += subjects[Math.round(Math.random()*(subjects.length-1))] +
    ' '+ verbs[Math.round(Math.random()*(verbs.length-1))] +' '+ objects[Math.round(Math.random()*(objects.length-1))] +
     endings[Math.round(Math.random()*(endings.length-1))];
}

function leadingZero(time) {
    if (time <= 9) {
        time = "0" + time;
    }
    return time;
}

// Run a standard minute/second/hundredths timer:
function runTimer() {
    //build a timer String
    let currentTime = leadingZero(timer[0]) + ":" + leadingZero(timer[1]) + ":" + leadingZero(timer[2]);
    theTimer.innerHTML = currentTime;

    //incremement timer[3] by 1 each time the function runs, via setInterval
    timer[3]++;

    //define minutes
    timer[0] = Math.floor((timer[3]/100/60));

    //define seconds > reset the seconds to zero each time they reach 60
    timer[1] = Math.floor((timer[3]/100) - (timer[0] * 60));

    //define centiseconds > reset the minutes and the seconds as well
    timer[2] = Math.floor(timer[3] - (timer[1] * 100) - (timer[0] * 6000));
}

// Match the text entered with the provided text on the page:
function spellCheck() {
    let textEntered = testArea.value;  //what is in the text area
    let originTextMatch = originText.substring(0, textEntered.length);

    if (textEntered == originText) {
        /* If the text matches the test text completly, then turn textarea border
        color to green */
        //https://goo.gl/4V01Vb
        clearInterval(interval);  //clear the set interval
        testWrapper.style.borderColor = "#05a210";
    } else {
        /* if the text entered curently matches the corresponding substring of
         the original text at that length typed, turn border blue */
        if (textEntered == originTextMatch) {
            testWrapper.style.borderColor = "#65CCf3";
        } else {
            /*If the complete or substring text does not match the orignal text,
            turn border red */
            testWrapper.style.borderColor = "#f51c1c";
        }
    }
}

// Start the timer:
function start() {
    let textEnteredLength = testArea.value.length;
    /* When the text length is 0, then we start timing, by recalling the timer
     at set intervals */
    if (textEnteredLength === 0 && !timerRunning) /* i.e false */ {
        timerRunning = true; // if true the timer can't start
        interval = setInterval(runTimer, 10);  //every thousandth of a sec
    }
}

// Reset everything:
function reset() {
    clearInterval(interval); //clear the current interval
    interval = null; //ensure that running the app again does not create a new indexed interval (save ressources)
    timer = [0, 0, 0, 0]; //resets the timer
    timerRunning = false; //reset the timer check so that the timer can run again
    testArea.value = "";  //clear the textarea
    theTimer.innerHTML = "00:00:00";
    testWrapper.style.borderColor = "grey";
}

// Event listeners for keyboard input and the reset button:
testArea.addEventListener("keypress", start, false);
testArea.addEventListener("keyup", spellCheck, false);
resetButton.addEventListener("click", reset, false);
