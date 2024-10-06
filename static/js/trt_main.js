/**
 *========================================================================================
 *    HTML5 Webpage for the TRT Watersystem website
 *      - utilizing the CodeIgniter and Bootstrap frameworks
 *      - designed utilizing the BootstrapMade template 'Rapid' (https://bootstrapmade.com)
 *
 *    (c) KaiserWare, Volker Petersen, October 2024
 *
 *========================================================================================
 */

	
function setPageHeight() {
	document.body.classList.add('vh-100');
	var height = document.body.clientHeight;
	height -= document.getElementById("topbar").clientHeight;
	height -= document.getElementById("navbar").clientHeight;
	height -= document.getElementById("footer").clientHeight;
	document.getElementById("main").style.minHeight = (height-33) + "px";
};

// Scroll back to top function
function scrollToTop() {
	$('html').animate({scrollTop: 0},800);
};

 // stuff to be executed after the entire document has be loaded and rendered
 $(document).ready(function ($) {
 	'use strict';    // strict just to keep concept of bootstrap


	// https://stackoverflow.com/questions/49307508/bootstrap-dropdown-not-working-in-mobile

	// dropdown menu on hover
	// make it as accordion for smaller screens
	if (window.innerWidth > 992) {
		document.querySelectorAll('.navbar .nav-item').forEach(function(everyitem){
			everyitem.addEventListener('mouseover', function(e){

				let el_link = this.querySelector('a[data-bs-toggle]');
				if(el_link != null){
					let nextEl = el_link.nextElementSibling;
					el_link.classList.add('show');
					nextEl.classList.add('show');
				}
			});
			everyitem.addEventListener('mouseleave', function(e){
				let el_link = this.querySelector('a[data-bs-toggle]');

				if(el_link != null){
					let nextEl = el_link.nextElementSibling;
					el_link.classList.remove('show');
					nextEl.classList.remove('show');
				}
			})
		});
	}
	// end if innerWidth
	 

 	// Back to top button
	$(window).scroll(function() {
    	if ($(this).scrollTop() > 100) {
      		$('.back-to-top').fadeIn('slow');
    	} else {
      		$('.back-to-top').fadeOut('slow');
    	}
  	});

   	// Header scroll class
   	$(window).scroll(function() {
     	if ($(this).scrollTop() > 100) {
       		$('#header').addClass('header-scrolled');
     	} else {
       		$('#header').removeClass('header-scrolled');
     	}
   	});

   	if ($(window).scrollTop() > 100) {
     	$('#header').addClass('header-scrolled');
   	}
	 
	// Bootstrap scrollspy menu
	$("#navbar ul li a[href^='#']").on('click', function(e) {
		// prevent default anchor click behavior
		e.preventDefault()
	
		// store link name url and remove the 1. character ('#')
		var hash = this.hash
		hash = hash.substring(1);
		//console.log("hash: "+hash)
		if (hash == 'Home' || typeof hash !== 'string') {
			document.title = "South Metro Chorale";
		}
		else {
			document.title = "SMC - " + hash;
		}

		// animate
		if ($(this.hash).offset()) {
			$('html, body').animate({
					scrollTop: $(this.hash).offset().top - 80
			}, 1000);
		}
	})
	 
   	// Porfolio isotope and filter
   	$(window).on('load', function () {
     	var portfolioIsotope = $('.portfolio-container').isotope({
       		itemSelector: '.portfolio-item'
     	});
     	$('#portfolio-flters li').on( 'click', function() {
       		$("#portfolio-flters li").removeClass('filter-active');
       		$(this).addClass('filter-active');

       		portfolioIsotope.isotope({ filter: $(this).data('filter') });
     	});
   	});

 });
