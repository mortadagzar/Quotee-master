$(document).ready(function() {
  // Optimalisation: Store the references outside the event handler:
  var $window = $(window);
  var $pane = $('.owl');

  function checkWidth() {
      var windowsize = $window.width();
      if (windowsize > 440) {
         
        $( '.owl' ).css( "left", "12%" );
        $( '.owl' ).css( "width", "72px" );

      }
      
  }
  // Execute on load
  checkWidth();
  // Bind event listener
  $(window).resize(checkWidth);
});



$(function(){
  var $elems = $('.quoteb');
  var winheight = $(window).height();
  var fullheight = $(document).height();
 
  $(window).scroll(function(){
    animate_elems();
  });

  function animate_elems() {
    wintop = $(window).scrollTop(); // calculate distance from top of window
 
    // loop through each item to check when it animates
    $elems.each(function(){
      $elm = $(this);
 
 
      topcoords = $elm.offset().top; // element's distance from top of page in pixels
 
      if(wintop >200) {
        // animate when top of the window is 3/4 above the element
        $( '.quoteb' ).css( "opacity", "1" );      }
    });
  } // end animate_elems()
});

