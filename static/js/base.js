document.addEventListener('DOMContentLoaded', function() {
  var videos = document.querySelectorAll('.video'); // Get all elements with the class 'video'

  // Function to ensure a video is playing
  function ensureVideoIsPlaying(video) {
      if (video.paused) {
          video.play().catch(e => console.error("Error attempting to play video:", e));
      }
  }

  // Loop through each video and apply the functionality
  videos.forEach(function(video) {
      // Ensure each video is playing
      ensureVideoIsPlaying(video);
      
      // Set an interval to check each video
      setInterval(function() {
          ensureVideoIsPlaying(video);
      }, 1000);

      // Handle video play/pause events for each video
      video.addEventListener('play', function() {
          console.log('Video started playing');
      });

      video.addEventListener('pause', function() {
          console.log('Video paused');
          ensureVideoIsPlaying(video);
      });
  });
});


