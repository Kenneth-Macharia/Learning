# Getting Started

- JavaScript is a scripting language that allows the crafting of small programs
  that run on the browser to change the HTML and CSS of the current HTML document
  upon a user interaction or triggered event.
- JavaScript terminology:

    1.ECMAScript:the evolving coding conformity standard for scripting languages
    like JavaScript. Browsers use it to interpret JavaScript, thus browsers must
    also evolve alongside, however this is not the case:
          a)Currently (Early 2017), ECMAScript 5.1 (2011) is the version fully
          supported but outdated.
          b)ECMAScript 2015 (ES6) is the emerging standard but not fully supported
          and needs a transpiler e.g Babel to translate it to old JavaScript so as
          to work on some browsers.
          c)ECMAScript 2016 (ES7) is in development and has no real support.
      2.jQuery is a library of JavaScript functions which simplifies the use of
      JavaScript in websites. Its an abstraction of the core JavaScript language.
      3.AngularJS, React and Vue.js are JavaScript are front end application
      frameworks used to simplify the building of advanced interactive web apps.
      These frameworks run on the front end and just pull the data required from
      the back unlike technologies like PHP which generate the pages in the server
      then push them to the browsers.
      4.Node.js allows the use of JavaScript as a server side programming language.

## Tools for developing in Javascript

- A text editor e.g. Atom
- Atom-live-server: An atom package for updating the browser automatically when a
 file is changed. It also simulates the written JavaScript, as if it's being served
 from a real server. It achieves this by spinning up a small web server in atom.
 Start the server using 'Ctrl+alt+l' > it will open a browser window on localhost
 port 3000 and track and display code outputs (console) from the project opened in atom.
 Stop the server using 'Ctrl+alt+q'
- A modern browser with developer tools e.g. Chrome. In the developer tools we use
 the 'console' tab to run JavaScript on the fly to test out this on a HTML doc. This
 is similar to the 'elements' tab used to view HTML & CSS elements of a doc and
 experiments with them. Changes made to these tabs are not saved to the doc or
 the actual document code.

## Working with Javascript

- JavaScript render blocking: where a browser halts page loading to download and
 execute any JavaScript it encounters in the HTML document. This has the impact
 of slowing page rendering. Thus where to place JavaScript scripts (either in the
 &lt;header> or after the &lt;body> is key to site performance). To solve this JavaScript
 references would be placed after the &lt;body>, whether or not they were to run
 before or after the page renders.
- HTML/2 the emerging web protocol partially solves this problem by allowing the
 the page and JavaScript files to be downloaded asynchronously and only halts
 page rendering to execute the JavaScript before continuing the page render.
- After HTML/2 we have 3 options:

    1.Load JavaScript right away: &lt;script src="script.js"></script>, default render
     blocking.
    2.Asynchronously: &lt;script src="script.js" async></script>, partial render
     blocking as above.
    3.Deferred: &lt;script src="script.js" defer></script>, JavaScript execution
     only happens when everything has been downloaded and rendered.

- Rules for writing GOOD JavaScript:

    1.JavaScript is caps-sensitive.
    2.Naming convention is camelCase.
    3.variable names start with a lowercase
    4.Object and Class names start with an uppercase
    5.CONSTANTS are all caps.
    6.White spaces don't matter to JavaScript but they do for human readable code.
    7.Add semicolons at the end of each statements, though not enforced by JavaScript,
     to enhance code readability.
    8.Single line comments us // and multi-line comments use /**/

- Always declare a variable using the 'var' keyword, if not the variable gets a
 global scope automatically. You can also use other keywords to define variables:

  (a) Const - declares a constant
  (b) Let - declares block scope variable, so as not to confuse these with other
   'var' declared variables that are locally e.g a variable to be used only
    within an 'if' statement, local to function

- Determine the type of data to be held by assigning a value in the created
 variable. Use \"quote\" to quote some string within a string.
- Other data types are 'boolean', 'null' and 'undefined' - variable created but not
 set to anything.
- Use 'typeof' to find out the type of a variable.
- Arithmetic operators in JavaScript: + - * / =(assignment)
- Other allowed operations: += -= *= /+
 -Unary operations: i.e: a = a + 1; > a++; also a--; which adds one to a, if used
  in console.log() then the original value of a gets printed. To add the one and
  print out the updated value use ++a; Also: --a;
- (NB) NaN > 'not a number' appears in console when you try to use an operator,
 other than '+' on operands that are not of type 'number'.
- Conditional statements: if statements:

      if (condition) {
        do something
      } else {
        do something else
      }

  - Conditional operators: == (equal), === (strict equality test for contents
   including type), < <= => >, != (not equal), !== (strict no equality test)
  - Boolean conditions:
    1.True: ie. if (a == false) {} or if (a) {}
    2.False: ie. if (a != true) {} or if (!a) {}
  - Logical operators: use to evaluate two logical conditions ie.:

    1.AND > && eg. if (a==b && c==d){} Both conditions MUST be TRUE for the entire
     expression to evaluate to TRUE.
    2.OR > || eg. if (a==b || c==d){} Either the 1st or the 2nd or both MUST be
      TRUE for the condition to evaluate to TRUE.
    3.XOR (Does not exist in Javascript) Either the 1st or the 2nd ONLY must be
     TRUE for the expressing to evaluate to TRUE. eg. if((a==b || c==d) && (a==b
     != c==d))

  - Ternary Operator: condition ? true action : false action eg. a==b ? console.log
   ('Match') : console.log('No match'). Ensure it' use is readable to humans and
   where it's not obvious use comments.

- Array: variable type that can hold many items at the same time, of different types.
- Functions: mini programs used to segment code blocks and enhance code re-usability.

    -Types:
        1.Named - run when called by name.
        2.Anonymous - run when triggered by an event.
        3.Immediately invoked functions - run when encountered by the browser.

    _See code examples for illustrations_

- OOP in Javascript

  1. Dot notation ie. course.title can be used to access an objects properties,
   normally.
  2. Bracket notation ie. course["title"] can also be used normally as the dot
   notation but is of more use when properties are not named conventionally eg.
   course["WP:image"] where the dot notation would not work.
  3. Closures: when functions have been invoked and are done running, they are closed
   down and everything inside discarded, meaning trying to access them eg. local
   local variable will result in a reference error because we are outside the
   function scope, where any local to it does not exist, except the returned value,
   if any.
    -Closures are functions inside other functions that rely on variables defined
     in the parent functions to work. See code examples for implementation and
     further reading on <https://developer.mozilla.org/en/docs/Web/JavaScript/Closures>

- Loops are of three types:

   1)For loops when you know how the number of iterations required;
       Syntax: for (var i = 0; i<10; i++) {do stuff;}
   2)While loop when you don't know the number of iterations required and some
    external condition determines loop termination;
       Syntax: var i = 0; while (i<10) {do stuff; i++}
   3)Do while loop similar to while loop but important when the loop must iterate
    at least once before the condition is checked;
       Syntax: var i = 0; do {do stuff; i++;} while (i < 10);

- Break: terminates the current loop and jumps to the next statement in the script.
- Continue: jumps the current iteration and proceeds to the next iteration.

## The Document Object Model (DOM)

- The browser window is an object and the document and it displays is an object as well.
- The window, the document displayed (together with its components) are modeled by
 the B.O.M (browser object model).
- Because all these are object you can interact wit them as you would any other
 object eg. to get the viewport width: window.innerWidth, to open a new tab:
 window.open(). Window is the top level object in the BOM. A list of properties
 of what it displays are available at <https://developer.mozilla.org/en/docs/Web/JavaScript/Reference>
- The most widely accessed object in the BOM is the document object which contains
 the current document displayed in the window. This can be access via window.document
 or directly as #document in the console, since JavaScript lives inside the current
 displayed document. It has its own model called the DOM.
- DOM has all elements in the HTML document as objects and when a document is loaded
 by a browser, a Node tree is created for each of the elements in the HTML document
 arranged in a hierarchical order, depending on how they are nested in the HTML
 document.

- Targeting elements in the DOM

  1.Some elements in the document such as body, title & URL can be accessed
    directly e.g document.body or document.title or document.URL.
  2.To get to a node or group of nodes inside the body, we use methods eg.
    a)document.getElementById("ID"); //get element with specific ID
    b)document.getElementByClassName("classname"); //elements by classname as an array
    c)document.getElementByTagName("HTML tag"); //elements by tag name as an array
  3.To get access nested elements, the above would not be the most efficient. To
    access those we use querySelector method which use CSS selectors i.e

    a)document.querySelector(".main-nav a");  //get the 1st occurring anchor
      links nested in the .main-nav class element.
    b)document.querySelectorAll(".post-content p")  //get all elements matching
      the specified CSS selector(s).
    c)Other usage examples:
      (i)document.querySelector(".menu .has-children a");
      (ii)document.querySelectorAll(".social-nav a[href*='linkedin.com']");
      (iii)document.querySelectorAll(".menu li a, .social-nav li a"); //all a elements
        inside either the .menu li or .social-nav li
    d)More on these methods at <https://developer.mozilla.org/en-US/docs/Web/API/document>

- Working with targeted element properties & methods: this is the whole point of
using JavaScript in making a static HTML/CSS webpage interactive, by having the
ability to change various elements at will.

  1. A full list of DOM element properties can be viewed at <https://developer.mozilla.org/en-US/docs/Web/API/Element>
  2. Examples of how to access the element properties:

    (a) `document.querySelector(".main-title").innerHTML`  //returns the contents of
      element with the specified class name.
    (b) `document.querySelector(".main-title").outerHTML`  //returns the entire HTMl
      tag + its contents.

  3. Changing various elements via their properties examples:

    (a) Change an elements value i.e document.querySelector(".main-title").innerHTML = "A different heading"
    (b) Change an elements id i.e document.querySelector("#showcase").id = "slideshow"
    (c) Change class identifiers:

      (i) ClassName: returns the classname of the element referenced and if more than
        one, returns the a space-separated string of all the class names i.e
        document.querySelector(".masthead").className
      (ii) ClassList: returns all the names of an element in an array so as to access them
        individually i.e `document.querySelector(".masthead").classList` then access
        each classname i.e `document.querySelector(".masthead").className[1]`

      _Some of these properties e.g classLists are READ-ONLY (see documentation), thus cannot be changed as above. To change these, we must use methods_

    (d) Changing READ ONLY elements: <https://developer.mozilla.org/en-US/docs/Web/API/Element/classList>

      For classList, we have a couple of methods:

      (i) Add a new class: `document.querySelector(".masthead").classList.add("new-class")`
      (ii) Remove a class: `document.querySelector(".masthead").classList.remove("new-class")`
      (iii) Toggle a class on & off: `document.querySelector(".masthead").classList.toggle("new-class")`
        switches the class off and the element with that classname is removed from the viewport,
        running the script again switches the class on and the element re-appears in the viewport.
      (iv) Checks if a class name exists: `document.querySelector(".masthead").classList.contains("new-class")`

      _For attributes e.g "href", we have methods to access the attribute names and values separately as they come in pairs: <https://developer.mozilla.org/en-US/docs/Web/API/Element>_

      _Code examples 05_ _attributes highlights how to work with attributes_

  4. Adding DOM elements can be done via innerHTML & outerHTML elements but a better
    way is to break up he individual elements and add them to the DOM tree e.g to a caption
    to an image: _See code exercise 05_

    (a) Create the element to add : .createElement()
    (b) Create the text node that goes inside the element: .createTextNode()
    (c) Add the text node to the created element: .appendChild()
    (d) Add the element to the DOM tree.

  5. Adding inline CSS to elements:

    (a) Use JavaScript to access/add CSS inline properties/styles to an element
      via the 'style' attribute in the DOM.
    (b) Using the 'style' attribute:<https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/styles>
      e.g `document.querySelector(".cta a").style;` _check the inline styles that can be applied and applied to the specified element_

    _The 'style' attribute cannot access styles applied by external sources e.g separate style files or internal styles in the &lt;header>_

    (c) Adding styles: `document.querySelector(".cta a").style.color = "green";`
    Changes the color of the selected element to "green" and add this inline
    style to the element.

    _Use camel case for the CSS properties instead of the '-' e.g. background-color will be backGround in JavaScript code_
    _Properties already applied to an element will not be overwritten by adding new style. To change the older style use a new statement to change the old style_

- Use the 'cssText' attribute to apply multiple css styles at once, using the std CSS syntax e.g.
    `document.querySelector(".someClass").style.cssText = "padding: 1px; color: white; background-color:red"`

- Because 'style' is an attribute like any other e.g 'alt', we can then use the methods to interact with it:

    (i) .hasAttribute('style', 'style/list of styles');
    (ii) .getAttribute('style', 'style/list of styles');
    (iii) .setAttribute('style', 'style/list of styles');
    (iv) .removeAttribute('style', 'style/list of styles');

- Working with DOM events: All actions in the browser are events, from opening a window, clicking, looking up a URL etc. - We work with event by event handling:

  1.ID the DOM node the interactive behaviour will be attached to e.g button
  2.ID the event the to attach to the DOM node e.g click
  3.Create the function that will run when the event occurs.

- Event are categorized into two, and all are available via JavaScript:

  1.Browser-level events e.g load, window resize
  2.DOM-level events e.g click, focus, submit
  Full list of events: <https://developer.mozilla.org/en-US/docs/Web/Events>

- Events are managed by either:

  1.Event handlers e.g node/element.onclick = DoSomething; whereby the event
    of interest is click and the node/element can be a button. This method
    however is not effective when we have more than one events.
  2.Event listeners effective when tying functions to browser-level events,
    tying an event to multiple functions and vice versa. It listens to a
    specified event and passes it over to the specified function.

- Passing arguments to an event listener function is a bit tricky because we cannot
  call the function the old fashion way with brackets at the end of its name, because
  this would cause the function to run when read by the browser and not when the
  target event happens. To solve this we can nest the function in an Anonymous
  function and then pass the arguments to the Anonymous function then to the event
  function. See 07_events for illustration.

## Troubleshooting, Validating and Minifying Javascript

- The console is the primary tool use to troubleshoot and debug Javascript. It will
  highlight all syntax errors and via the console.log() method be used to debug other
  types of errors e.g. logic errors.
- Resource for console : <https://developer.mozilla.org/en-US/docs/Web/API/Console>
- The MDM page give a host of console functions to use to assist in debugging JavaScript
  code.
- The developer tools also has the 'sources' tab used to inspect code execution
  line-by-line, includes breakpoints, step-into and other debugging functionalities.
- Online JavaScript linting tools:

  1. JSLint: <http://jslint.com>, the gold std tool for JavaScript code qaulity, however
  will pick up even the smallest irrelevant issues e.g non-use of white spaces,
  which will most likely be minified out before deploying the code.
  2. JShint: <http://jshint.com>, a more lenient tool and focuses on actual problems. To
   use just like jslint, ensure ES6 is enabled.

- Automating script linting via 'eslint' package for atom, but set up in conjuction
 with npm (node package manager).
- Minification meaning removing whitespaces and comments make the code easier to
 download and run for the browser. This makes the code unreadabel to humans though,
 thus you would minify to a different file e.g. 'script-min.js' and then reference
 that file in index.html instead of the full version.

  _When viewing the minified JS version in developer tools, 'source' tab, you can_
  _you can temporarily unminify the file by clicking on 'pretty print {}' icon at the_
  _bottom_

- Online minifying tool: <http://www.minifier.org>
- Automated minification via 'uglify js', again set up is via npm.

## More on Javascript

- Full documentation: <https://developer.mozilla.org/en-US/docs/Web/JavaScript>
- Bookmark feature links from the above website.
- Other courses to look at:

  1. jQuery essentials {Joe Marini}
  2. React.js essnetial training {Eve Porcello}
  3. Angular 2 essential training {Justin Schwartzenberger}
