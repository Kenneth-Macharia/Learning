/* Set a cosntant that points at the desired element, since we will not change its
contents */
const CTAELEMENT = document.querySelector(".cta a");

//Check what attributes are currently assigned to the element, in this case only href
//console.log(CTAELEMENT.attributes);

//Access the href aatribute target property to see if it has a value and if not assign one:
if (CTAELEMENT.hasAttribute("target")) {
  console.log(CTAELEMENT.getAttribute("target"));
} else {
  CTAELEMENT.setAttribute("target", "_blank");
}

console.log(CTAELEMENT.attributes);
