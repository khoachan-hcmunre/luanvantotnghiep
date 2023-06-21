$(function(){
   	
   	'use strict';

    //onePageNav
    $(document).ready(function() {
       $('#nav').onePageNav();
    });

    // SMOOTH SCROLL
    $("a").on('click', function(event) {

      if (this.hash !== "") {
        event.preventDefault();

        var hash = this.hash;

        $('html, body').animate({

          scrollTop: $(hash).offset().top

        }, 850, function(){

          window.location.hash = hash;

        });

      }

    });

    // NAVBAR COLLAPSE HIDE ON CLICK
    $('.nav a').click(function(){
        $('.navbar-collapse').collapse('hide');
    });

    // menu filter container
    $('.filtr-container').filterizr();

    // menu filter
    $('.simplefilter li').click(function() {
        $('.simplefilter li').removeClass('active');
        $(this).addClass('active');
    });

    // MENU IMAGE POPUP
    $('.image-popup').magnificPopup({
    
        type: 'image',
        removalDelay: 300,
        mainClass: 'mfp-fade'
        
    });

    // NAVBAR ON SCROLL
    $(window).scroll(function() {
      
      if ($(document).scrollTop() > 50) { 
        
        $(".navbar-fixed-top").css({"background-color": "rgb(68, 68, 68)","border-bottom": "1px solid #fff"});

      } else {
        
        $(".navbar-fixed-top").css({"background-color": "transparent"});

      }

    });

    // TESTIMONIALS
    $("#owl-testimonial").owlCarousel({

      items: 1,
      slideSpeed: 350,
      itemsMobile : [640,1]

    });

    // slider
    $("#slider-home").owlCarousel({

        navigation: true,
        slideSpeed: 300,
        paginationSpeed: 400,
        singleItem: true

    });

     // loader
    $('#fakeLoader').fakeLoader({
      
      zIndex: 999,
      spinner: "spinner3",
      bgColor: "#ff6363"

    });

});