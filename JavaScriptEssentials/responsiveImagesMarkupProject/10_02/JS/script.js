/* Responsive images markup makes use of the 'srcset' attribute (HTML5), which is
 a list of comma separated image sources that can be used by the different clients of
 the website. The correct image will then be chosen for the correct client from
 this set. The src attributes in this set must follow a specified format which
 can be generated for the available images (proper image filing and naming a must),
 using JS code. It also uses a 'sizes' attribute (HTML5), which is also a list of
 comma separated strings indicating the sizes for the 'srcset'. This also must follow
 a standard format as specified in the developer documentation:
 https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/img */

/* This project will generate repsonsive image HTML5 markup for all the images on
on this project page, having an 'srcset' (with a URL and width descriptor) and
coresponding 'sizes' (with a media query/condition and source size value) attributes
and inject them into the doc */

//Step 1 : Create an array to hold all the images on the page
const IMAGES = document.querySelectorAll("img");

/*Step 2 : For each image category, specified by the custom 'data-type' attribute,
generate the image sizes required for desired viewport width. Create an image
categories object, listing the size attribute for each category at various viewport widths */
const IMG_CAT_SIZE = {
    //These images are always 100% of the viewport
    showcase: "100vw",
    /*These have one media query; for viewport sizes of less than 800px, the img
    will be 100% of the viewport and for larger viewport sizes than this, they are
    372px wide */
    reason: "(max-width: 799px) 100vw, 372px",
    feature: "(max-width: 799px) 100vw, 558px",
    stories: "(max-width: 799px) 100vw, 558px",
};

// Step 3 : Create a function to generate the 'srcset' for all the possible images
function makeSrcSet(imgSrc) {
   //Array to hold the Set
   let markup = [];
   //Smallest image width, in this case the sizes incease by 400 between (400-2000px)
   let imgWidth = 400;

   //Loop to generate the image markup for all the images on our site
   for (let i = 0; i < 5; i++) {
       //std formatf for an srcset
       markup[i] = imgSrc + "-" + imgWidth + ".jpg " + imgWidth + "w";
       //Get the next size image
       imgWidth+=400;
   }

   //return markup as a comma separated list
   return markup.join();
}

//Step 4 : Loop through the page images and ... :
for (let i = 0; i < IMAGES.length; i++) {
    // (a) Get and slice out 8 characters from the 'src' attribute from the right
    //https://goo.gl/WcgjZ3 (slice())
    let imgSrc = IMAGES[i].getAttribute("src").slice(0, -8);
    /* (b) Generate the 'srcset' attribute for each image found on the site. NOTE there
    must be an image size available for each src generated, stored in the same location as
    the currently displayed image */
    let srcset = makeSrcSet(imgSrc);

    // (c) Get the img category attribute
    let imgCat = IMAGES[i].getAttribute("data-type");

    /* (d) Get the image size for each category img at various viewport sizes. For each
    image category we retrieve, we will look into the cat size object and retrieve
    it's sizes. Here we implement the [] object notation instead of the . object
    notation */
    let imgSize = IMG_CAT_SIZE[imgCat];

    /* (e) Set add the newly created 'srcset' & 'sizes' attributes into the HTML doc */
    IMAGES[i].setAttribute("srcset", srcset);
    IMAGES[i].setAttribute("sizes", imgSize);

    //console.log(imgCat + " | " + imgSize);
    //console.log(srcset);

}
