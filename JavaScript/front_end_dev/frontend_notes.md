# Front End Notes

- Colors are represented by the RGB model on a range between 0 - 255 for either
  color.
- Hexadecimal values (#xxxxx) are used to pick any color combination of the 3 primary colors
  to yield any desired color.
- Rgb values can also be used to pick any color as well but have also an option
  for color transparency. _{rgb(31,61,0,0.48) > Red-31, Green-61, Blue-0, 48% transparency}_
- A class can be used to style as many elements as required, but I.ds can only be
  used once in the same HTML document. Class use is more encouraged even when we
  only have one class.

## CSS Box Model

- All HTML elements are box elements.
- It helps define spaces between elements and contains:

    1. Margins:Space between boxes
    2. Borders:Surrounds the elements
    3. Padding:Area around the content
    4. Content:Texts & images
    5. Box:defined by the margins

- Box-sizing:enables setting the height & width of the content to fit the box.
- Block elements: e.g paragraphs occupy the width of the browser.
- In-line elements: e.g. images, links, &lt;strong> etc, you can set their height &
  widths.
- Browsers add default margins and padding when they are not specified.
- Divs (divide) are used to split a webpage into sections (boxes) to hold various
  page contents.
- Relatively positioned elements depend on the position of other elements.
- Absolutely positioned elements can be placed anywhere inside their parent
  elements.
- Floats used to move elements across the page, need to be cleared after used else
  other sections/elements will be be affected by the uncleared floats. This happens
  when sections overlap andone start wjere another is starting causing alignment
  issues e.g a section having a zero px height. This is sorted using the clearfix
  css class. #

  _See implementation in style.css under basic setup_

## Web Design Guidelines

- Typography:the art and technique of arranging type to make written language
  readable and beautiful.
- Guidelines for good typography:

  1. Use a font-size of between 15-25 px
  2. Headlines:60px if the more reduce the weight of the text to make it blend
    with the rest of the web page texts.
  3. Use a line-spacing of 120-150% of the font-size.
  4. Use 45-90 characters per line.
  5. Pick a good font-type e.g. sans-serif as opposed to the traditional serifs,
    get more from google web fonts. When choosing a font-type:

      (a) The right font for the look and feel of the website.
      (b) Use 1-2 typefaces only
      (c) Decide between sans-serif or serif typeface.

  6. For colors:

    (a) Use one main base color (other than black, white or grey)
    (b) Flat UI color is a good tool for choosing base colors.
    (c) Create a color palette to be used for the project, which are different shades
      of the base color. 02-255 is a good tool for this.
    (d) To use multiple colors use adobe color cc to get a color combination that
      makes sense.
    (e) Using color to draw attention mainly to elements that you want user see,
      e.g action buttons.
    (f) Never use black in a design.
    (g) Color suggestions: use the right color to convey the correct tone. Brighter
      tones are more energetic and darker tones convey power and elegance.

      (i) Red - passion, strength
      (ii) Orange - cheerful, creativity, courage
      (iii) Yellow - intelligence, happiness, curiosity
      (iv) Green - harmony, nature, health, money
      (v) Blue - patience, peace, trustworthy, stability, professionalism
      (vi) Purple - wisdom, wealth, nobility, luxury
      (vii) Pink - Affection, care, peace
      (viii) Brown - relaxation, confidence, durability, comfort, reliability

  7. Using images: websites with images convert better than text only websites:

    (a) Use texts directly on an image only if they are of different shades.
    (b) Overlay a color over an image to help with the above e.g black to turn a
      a bright image darker if the text is also bright. Other colors can also be
      used.
    (c) Use color gradients to improve the look in the above.
    (d) Use texts in a box on top of an image with a white transparent color or
      any other color tat matches the color palette of the website.
    e)Also use image blur when overlying texts images.
    f)Use floor fade i.e. images fading into a black color and overlay the white
      texts on the faded section.

  8. Using icons:to shows features, products or steps to a process. Allows quick
    browsing of a page. Also use them for links/actions but:

    (a) The icons should recognizable immediately
    (b) Label the icons
    (c) Icons should play a support role rather than be the main features of the page
    (d) Use 'vector icon fonts' instead of 'static image icons' as the later uses
      smooth vector images that will always look sharp even when scaled up or down.

  9. Using whitespace between all elements of the page to mage the page more elegant
    pleasant to look at. Put white spaces:

    (a) Between elements
    (b) Between element groups
    (c) Between website sections
    (d) to define content hierarchy i.e what the user should see first and then
      next and so forth.

  10. User experience: the overall experience a user has with the product, from
    interacting with the user interface (the presentation of he product).

    _"It's not just what it looks and feels like. Design is how it works" Steve Jobs_

  11. Design inspiration:

    (a) Collect designs that you like
    (b) try to understand everything about them
    (c) Why do they look good?
    (d) What do these sites have in common?
    (e) How were they built in HTMl and CSS? Use browser developer tools.

## STEPS TO DEVELOPING A FUNCTIONING WEBSITE

1. Define the goal of the project
2. Define the audience
3. Plan the content e.g. text, images, videos, icons etc. Think about the visual
  hierarchy. Content first approach: defining the content first before building.
4. Define the navigation and site structure
5. Get inspired and with the idea in mind, sketch it. Never star designing without
  an ideas of what is required.
6. After the site is built, optimize for speed and search engines.
7. After launch, monitor the site for user interactions and make changes anywhere
  necessary or ensure content is updated.

## RESPONSIVE WEB DESIGN

- Building websites that display content correctly depending on the screen size
  of the device used to view them.
- Ingredients to responsive web design:

    1. Using the fluid grid: all layout elements are sized in relative units e.g
    % instead of absolute units e.g pixels
    2. Using flexible images: images are also sized in relative units
    3. Using media queries: which allow us to specify different CSS style rules
    for different browser widths.

- Setting media query breakpoints for responsive webpages:

    1. When starting out use known screen width for various breakpoints e.g.
    iPhone, iPad etc.
    2. As you get more experienced, define custom breakpoints based on the design
    of the website i.e they will be determined by the look of the site at different
    screen sizes.
    3. A starter guide can be:

      (a) 0 - 480px: old iPhone screen width
      (b) 480px - 768px: iPad screen width in portrait mode
      (c) 768Px - 1024px: iPad screen in landscape model
      (d) 1024px - 1280px: old Macbook

## CSS browser prefixes & old browser support

- These ensure that css3 works the same across all browsers.
- They enable browser makers to add support support for new css features for a certain
  period.
- The various browser prefixes are:

    1. Android: -webkit-
    2. Chrome: -webkit-
    3. Firefox: -moz-
    4. IE: -ms-
    5. iOS: -o-
    6. Safari: -webkit-

- Implementation example of the css 'border-radius' property that ensures it works
  even on the various older browsers which usually cause the biggest css problems:

   -webkit-border-radius: 25px;
   -moz-border-radius: 25px;
   -o-border-radius: 25px;
   border-radius: 25px;

- To prefix all required css properties, use the 'autoprefixer' package to auto
  the required lines in your css file.
- In atom:

    1. Select all the code in a css file
    2. Run autoprefixer _from the command palette - Ctrl-Shift-P > Autoprefixer_

- The very old browsers are still not immune to new css defination but we can use
  some JavaScript code to enable functionality of these new feature in the older
  browsers:

    1. Navigate to jsdelivr.com, search for the desired js script.
    2. Downlownd the zip file containing the script file and save it in the appropriate
      project folder.
    3. Include a &lt;script> tag link to the js file in the HTML code as the last items
      in the &lt;body> section, so that the are called after the entire webpage is loaded.

- You can use 'caniuse.com' to check whether a specific css property is supoorted
  on various browsers or not and whether to include css prefixes depending on the
  browser of interest.

## Jquery (Add atom-ternjs package for js)

- Used to select and manipulate HTMl elements, create animations and develop
  Ajax applications { }
- Some JQuery plugins (more in the course e-book):

    1. Magnific popup - for page pop ups e.g. videos, modal dialogs, images etc
    2. Tooltipster - for tooltips on hover over elements
    3. Maplace.js - for embedding maps & markers
    4. Typer.js - that types. Can show multiple content on a single line.
    5. OnPageScroll - enable whole section scrolling, with sections filling the
      the entire viewport height.

- Including JQuery in a project and create a new js file:

  1.Navigate to the google hosted libraries distributed network.
  2.Under JQuery, copy and paste the &lt;script> in the HTML file.

- Adding a map using the 'gmaps.js JQuery pluggin':

    1.Download it at 'hpneo.github.oi/gmaps'
    2.Add the file to HTML
    3.Get the basic jQuery code from the examples section of the above site and
      include in scripts.js
    4.Add a div in HMTL to display the map and style it in css.
    5.Add the google maps API js link from <https://github.com/hpneo/gmaps> to HTML

## Website Optimization

- Favicons are important for site identity purposes. Create one for your site
  using 'realfavicongenerator.net':

    1.choose an image atleast 260*260px
    2.Upload to realfavicongenerator.
    3.Tweek the resulting images for the various platforms.
    4.Indicate the path where you will store the icons in your project for the
      &lt;link> code to be generated.
    5.Copy the HTMl code generated to your HTML file.
    6.Download and save the icon package in the location specified in 4 above.

- Optimize page load speeds by:

    1. Reducing image sizes to twice the width of their largest display size as
     shown in the browser developer tool. On mac you can use 'preview'
    2. Use 'optimizilla.com' to compress, huge important images e.g header images.
    3. Minify CSS and JavaScript code by removing unnecessary spaces, comments
     using, links to tool for this in the course e-book. This however make code
     very hard to read and would only be necessary when we have very large code
     files.

- Search Engine Optimization (SEO): increases search engine ranking of you site
  by search engines thereby increasing the overall potential traffic to your
  site. This can be accomplished via:

    1. Including a well crafted 'description' &lt;meta>
    2. Validate your HTML code, valid HTML is preferred by search engines like
     Google as its follows HTML best practices, is not buggy and will more likely
     work on a variety of browsers. Use 'https://validator.w3.org/' for this.
    3. Content is King, ensure quality and up-to-date content always.
    4. Keywords: use these strategically, as users find information online using
     them. Use them in your headers, meta tags, title and links but don't over use.
    5. Backlinks: links that link back to your site and act as recommendations. Get
     other site to link to yours.
    6. Other SEO resources in the course e-book.

- Site maintenance: use 'google analytics' to monitor your website and get stats
  that can help you know were to improve the site:

    1. Create a google analytics account
    2. Specify the website to track and get stats on.
    3. Generate tracking ID in form of a JavaScript script
    4. Add this script to the each of the pages of your site.
    5. Re-upload changes made.
    6. You can then view the site stats
