/******** VIDEO SCRIPT ********/

document.addEventListener('DOMContentLoaded', function () {
    const videos = document.querySelectorAll('.video');
 
    // Function to ensure a video is playing
    function ensureVideoIsPlaying(video) {
       if (video.paused && !document.hidden) {
          video.play().catch(e => console.error("Error attempting to play video:", e));
       }
    }
 
    // Function to handle video play/pause based on page visibility
    function handleVisibilityChange() {
       videos.forEach(video => {
          if (document.hidden) {
             video.pause();
          } else {
             ensureVideoIsPlaying(video);
          }
       });
    }
 
    // Initialize video handling
    function setupVideos() {
       videos.forEach(video => {
          ensureVideoIsPlaying(video); // Ensure video is playing initially
 
          video.addEventListener('play', () => console.log('Video started playing'));
          video.addEventListener('pause', () => {
             console.log('Video paused');
             ensureVideoIsPlaying(video); // Restart video if paused unexpectedly
          });
       });
 
       // Monitor page visibility to pause/play videos
       document.addEventListener('visibilitychange', handleVisibilityChange);
    }
 
    // Call the setup function
    setupVideos();
 });
 
 
 /******** PROJECTS MODAL SCRIPT ********/
 
 // Handles dynamic image changes on the project modal list
 
 document.addEventListener("DOMContentLoaded", function () {
    const projectItems = document.querySelectorAll(".project-item");
    const projectsImgsContainer = document.querySelector(
       ".projects-imgs-container"
    );
    const originalImages = projectsImgsContainer.innerHTML;
 
    projectItems.forEach((item) => {
       const projectImageElement = item.querySelector(".list-image-url");
       const projectImage = projectImageElement ? projectImageElement.src : "";
 
       item.addEventListener("mouseenter", function () {
          if (projectImage) {
             projectsImgsContainer.innerHTML = "";
             projectsImgsContainer.classList.remove("projects-imgs-container");
             projectsImgsContainer.classList.add("project-img-container");
 
             // Create a new img element associated with the specific project
             const newImage = document.createElement("img");
             newImage.src = projectImage;
             newImage.alt = "Project Image";
             newImage.style.width = "100%";
             newImage.style.height = "auto";
             newImage.style.objectFit = "cover";
 
             // Add the new image to the container
             projectsImgsContainer.appendChild(newImage);
          }
       });
 
       item.addEventListener("mouseleave", function () {
          // Restore the original images and change the container class back
          projectsImgsContainer.innerHTML = originalImages;
          projectsImgsContainer.classList.remove("project-img-container");
          projectsImgsContainer.classList.add("projects-imgs-container");
       });
    });
 });




  