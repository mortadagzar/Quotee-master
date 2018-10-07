
  window.scroll({
   
    behavior: 'smooth' 
  });


  $(window).scroll(function() {
 
    if ($(this).scrollTop()>50)
     {
        $('.button-out').stop().animate({ // menu goes out
            marginLeft:' 79%',
            transform:' scale(1.2)',
           
            
        });

    
     }
    
     

 });