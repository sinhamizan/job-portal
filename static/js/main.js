$(document).ready(function(){

	//wow-js-active
	new WOW().init();
	//====================
	// menu fixed
	$(window).scroll(function(){

		var top = $(window).scrollTop();
		if (top > 120) {
			$('header').addClass('header-bg');
		}
		else{
			if ($('header').hasClass('header-bg')){
				$('header').removeClass('header-bg');
			}
		} 
	});
	//=======================
	// header-slider start
	$('.slider_active').owlCarousel({
	    loop:true,
	    nav:true,
	    dots: false,
	    autoplay: true,
	    autoplayHoverPause: true,
	    autoplaySpeed:2000,
	    responsive:{
	        0:{
	            items:1
	        },
	        600:{
	            items:1
	        },
	        1000:{
	            items:1
	        }
	    }
	})

	$('.new_slider').owlCarousel({
		    loop:true,
		    nav:true,
		    dots: false,
		    autoplay: true,
		    autoplaySpeed:2000,
		    autoplayHoverPause: true,
		    responsive:{
		        0:{
		            items:1
		        },
		        600:{
		            items:2
		        },
		        1000:{
		            items:4
		        }
		    }
		})


	$('.new_slider').owlCarousel({
		    loop:true,
		    nav:true,
		    dots: false,
		    autoplay: true,
		    autoplaySpeed:2000,
		    autoplayHoverPause: true,
		    responsive:{
		        0:{
		            items:1
		        },
		        600:{
		            items:2
		        },
		        1000:{
		            items:4
		        }
		    }
		})


	$(function(){

	  $(".single_imge").exzoom({
	    "navWidth": 60,
	    "navHeight": 60,
	    "navItemNum": 5,
	    "navItemMargin": 7,
	    "navBorder": 1,
	    "autoPlay": false,
	    
	  });

	});


	
	$(function(){

	  $('input[type="number"]').niceNumber();

	});



	// header slider end
	//==================
	
	//go to top
	$(window).scroll(function(){
		if($(this).scrollTop() > 100)
		{
			$('#gotopbtn').fadeIn();
		}
		else{
			$('#gotopbtn').fadeOut();
		}
	});
	$('#gotopbtn').click(function(){

		$('html ,body').animate({scrollTop : 0},800);

	});

	//=======================
	// slick nav
	$(function(){
        $('#menu').slicknav({
        	'label' : '',
        });
    });
	
	




})