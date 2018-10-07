$(function(){
    var $elems = $('.tto');
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
 
      if(wintop<topcoords) {
        // animate when top of the window is 3/4 above the element
        $elm.animate({

            opacity:1, 
        })
      }
    });
  } // end animate_elems()
});