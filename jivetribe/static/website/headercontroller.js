// headercontroller.js
$(document).ready(function(){
  initial();
});


function initial(){
  var triggerPosition = $('.sticky-nav').position().top;

  $('.nav-item-middle').hide();
  $(window).on('scroll', function(){
    var scrollPosition = scrollY || pageYOffset;
    console.log(scrollPosition);
    console.log(triggerPosition);
    if(scrollPosition > triggerPosition){
      var height = $('.sticky-nav').height();
      $('.sticky-nav-ghost').height(height);
      $('.sticky-nav').addClass('sticky-nav-fixed');
      $('.sticky-nav-ghost').show();
      $('.nav-item-middle').fadeIn(500);

    }
    if(scrollPosition < triggerPosition){
      $('.sticky-nav').removeClass('sticky-nav-fixed');
      $('.sticky-nav-ghost').hide();
      $('.nav-item-middle').fadeOut(500);

    }

  });
}
