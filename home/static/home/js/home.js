document.addEventListener('DOMContentLoaded', function() {

  var videos = document.querySelectorAll('.video');

  // Function to ensure all videos are playing
  function ensureVideosArePlaying() {
      videos.forEach(function(video) {
          if (video.paused) {
              video.play().catch(e => console.error("Error attempting to play video:", e));
          }
      });
  }

  ensureVideosArePlaying();
  setInterval(ensureVideosArePlaying, 1000);

  // Handle video play/pause events for each video
  videos.forEach(function(video) {
      video.addEventListener('play', function() {
          console.log('Video started playing');
      });

      video.addEventListener('pause', function() {
          console.log('Video paused');
          ensureVideosArePlaying(); // Ensure it tries to play again if paused
      });
  });
});