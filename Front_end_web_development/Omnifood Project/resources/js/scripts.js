// Every js file will start with this declaration to ensure this code runs after
  //the document has been loaded.
$(document).ready(function() {
  // Select the element ie. 'h1' and when clicked the body of the function will
    //be executed.
  $('h1').click(function() {
    // The back color of 'this', the element referenced, will be changed when
      //clicked.
    $(this).css('background-color', '#ff0000');
  })

});


// Implementing the waypoint plugin to enable the sticky_nav functionality.
// http://imakewebthings.com/waypoints/guides/jquery-zepto/ has implementation
  //  details for this.
$(document).ready(function() {

  $('.js_section_features').waypoint(function(direction) {
    if (direction == "down") {
      $('nav').addClass('sticky_nav');
    } else {
      $('nav').removeClass('sticky_nav');
    }
  },
  //Enable the sticky_nav 60px before hitting the 'section-features'.
  { offset: '60px;'});

// Scrolling to the various section upon corresponding button click
  // I'm hungry > price section
  $('.js_scroll_to_plan').click(function() {
    $('html, body').animate({scrollTop: $('.js_plans_section').offset().top}, 1000);
  });

    // Show me more > features-section
  $('.js_scroll_to_start').click(function() {
    $('html, body').animate({scrollTop: $('.js_section_features').offset().top}, 1000);
  });

  // Smooth scrolling for the nav links
  // Works by defining anchors in the links' href, corresponding to an id in the
    // sections to scroll to
  // Source:https://css-tricks.com/snippets/jquery/smooth-scrolling/ (Devin Sturgeon)
  $(function() {
    $('a[href*=#]:not([href=#])').click(function() {
      if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
        var target = $(this.hash);
        target = target.length ? target : $('[name=' + this.hash.slice(1) +']');

        if (target.length) {
          $('html,body').animate({
            scrollTop: target.offset().top
           }, 1000);
           return false;
        }
      }
    });
  });


});









  }
