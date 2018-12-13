//Making sure that all external links have their 'target' attributes set to _blank

//Get & save in an array all links starting with 'http'  i.e external links
var extLinks = document.querySelectorAll('a[href^="http"]');

//Loop through the Array
for (var i = 0; i < extLinks.length; i++) {
    if (!extLinks[i].hasAttribute("target")) {
        extLinks[i].setAttribute("target", "_blank");
    }
}
