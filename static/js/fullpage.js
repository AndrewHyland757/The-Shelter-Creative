/******** FULLPAGE.JS SCRIPT ********/

// Generate anchors
const sections = document.querySelectorAll('.section');
let anchorsArray = [];

sections.forEach((section, index) => {
   // Check if it's the projects section
   if (section.classList.contains('section--projects')) {
      anchorsArray.push('projects-section');
   } else {
      // Generate a default numbered anchor for other sections
      anchorsArray.push((index + 1).toString());
   }
});


new fullpage("#fullpage", {

   licenseKey: '1MJ47-09EP9-8JUB7-7T6OK-OTCAO',
   scrollingSpeed: 800,
   autoScrolling: true,
   scrollHorizontally: true,
   verticalCentered: false,
   anchors: anchorsArray,
   lockAnchors: true,
   scrollOverflow: true,
   normalScrollElements: ".scrollable-content",
   bigSectionsDestination: "bottom",
   controlArrows: false,
   slidesNavigation: false,
   continuousVertical: true,
   scrollOverflow: true,
   normalScrollElements: '.projects-list-container',
   touchSensitivity: 5,
   fitToSection: false,

   afterRender: function () {
      createCustomNavigation();
      setupSwipeEvents(); // Initialize swipe functionality
   },
   afterSlideLoad: function (section, origin, destination, direction) {
      updateCustomNavigation(section.index, destination.index);
   },
   onLeave: function (origin, destination, direction) {
      // Update custom navigation when changing sections
      updateCustomNavigation(destination.index, 0);
   },
});

function createCustomNavigation() {
   var sections = document.querySelectorAll(".section");
   var navContainer = document.createElement("div");
   navContainer.className = "custom-nav";

   sections.forEach(function (section, index) {
      if (index === 2) {
         var slides = section.querySelectorAll(".slide");
         if (slides.length > 0) {
            var sectionNav = document.createElement("div");
            sectionNav.className = "section-nav";
            sectionNav.setAttribute("data-section", index);

            slides.forEach(function (slide, slideIndex) {
               var indicator = document.createElement("span");
               indicator.className = "slide-indicator";
               if (slideIndex === 0) indicator.classList.add("active");
               sectionNav.appendChild(indicator);
            });

            navContainer.appendChild(sectionNav);
         }
      }
   });

   document.body.appendChild(navContainer);

   // Add click events for left and right navigation
   document.addEventListener("click", function (e) {
      // Check if the click is inside the header or modal
      if (!e.target.closest(".header") && !e.target.closest(".modal")) {
         var halfWidth = window.innerWidth / 2;
         if (e.clientX < halfWidth) {
            fullpage_api.moveSlideLeft();
         } else {
            fullpage_api.moveSlideRight();
         }
      }
   });
}

function updateCustomNavigation(sectionIndex, slideIndex) {
   var sectionNav = document.querySelector(
      `.section-nav[data-section="${sectionIndex}"]`
   );
   if (sectionNav) {
      var indicators = sectionNav.querySelectorAll(".slide-indicator");
      indicators.forEach((indicator, index) => {
         if (index === slideIndex) {
            indicator.classList.add("active");
         } else {
            indicator.classList.remove("active");
         }
      });
   }
}

// Function to handle swipe events
function setupSwipeEvents() {
   var touchStartX = 0;
   var touchEndX = 0;
   var swipeThreshold = 50;

   // Add touch event listeners to the entire fullPage element to ensure all sections respond
   var sectionSlides = document.querySelector(".section--slides");

   if (sectionSlides) {
      sectionSlides.addEventListener(
         "touchstart",
         function (e) {
            e.preventDefault();
            touchStartX = e.changedTouches[0].screenX;
         }, {
            passive: false
         }
      ); // Mark passive as false to allow preventDefault()

      sectionSlides.addEventListener(
         "touchmove",
         function (e) {
            e.preventDefault();
            touchEndX = e.changedTouches[0].screenX;
         }, {
            passive: false
         }
      ); // Mark passive as false to allow preventDefault()

      sectionSlides.addEventListener(
         "touchend",
         function (e) {
            e.preventDefault();
            var swipeDistance = touchEndX - touchStartX;

            if (swipeDistance < -swipeThreshold) {
               fullpage_api.moveSlideRight();
            } else if (swipeDistance > swipeThreshold) {
               fullpage_api.moveSlideLeft();
            }
         }, {
            passive: false
         }
      ); // Mark passive as false to allow preventDefault()
   } else {
      console.error("Swipe setup failed: .section--slides not found");
   }
}