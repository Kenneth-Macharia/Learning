//Using objects to model this course.
//Creat the course object:
var course = new Object();

//Set the course object properties (Long-hand);
// course.title = "JavaScript Essentials";
// course.instructor = "Morten Rand-Hendriksen";
// course.level = 1;
// course.published = true;
// course.views = 0;

//Short-hand version:
var course = {
  title:"JavaScript Essentials",
  instructor:"Morten Rand-Hendriksen",
  level:1,
  published:true,
  views:0,
  //Create an object method (an anonymous function)
  updateViews: function() {
    return ++course.views;
  }
}

console.log(course);
console.log(course.views);
course.updateViews();
console.log(course.views);

/*Object constructor are templates that define object properties and can be
 re-used to create instances of the object without defining all the object
 properties again */
 //Creating an object constructor (for the course):
  /*Create a function to set up the object and pass to it the desired object
  properties */
 function Course (title, instructor, level, published, views) {
   this.title = title;
   this.instructor = instructor;
   this.level = level;
   this.published = published;
   this.views = views;
   this.updateViews = function() {
     return ++this.views;
   };
 }

 //Create an new course object using the above constructor:
 var course01 = new Course("JavaScript Essentials", "Morten Rand-Hendriksen",
  1, true, 0);

  console.log(course01);

//create a second object:
var course02 = new Course("Getting started with ECMAScript6", "Eve Porcello",
 1, true, 12357);

console.log(course02);

//You can create an array of multiple objects:
var courses = [
  new Course("JavaScript Essentials", "Morten Rand-Hendriksen",
   1, true, 0),
  new Course("Getting started with ECMAScript6", "Eve Porcello",
   1, true, 12357)
];

console.log(courses);
