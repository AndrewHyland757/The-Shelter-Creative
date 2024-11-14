document.addEventListener('DOMContentLoaded', function() {
  var videos = document.querySelectorAll('.video');
  
  // Function to ensure a video is playing
  function ensureVideoIsPlaying(video) {
      if (video.paused) {
          video.play().catch(e => console.error("Error attempting to play video:", e));
      }
  }

  // Loop through each video and apply the functionality
  videos.forEach(function(video) {
      ensureVideoIsPlaying(video);
      
      setInterval(function() {
          ensureVideoIsPlaying(video);
      }, 1000);

      video.addEventListener('play', function() {
          console.log('Video started playing');
      });

      video.addEventListener('pause', function() {
          console.log('Video paused');
          ensureVideoIsPlaying(video);
      });
  });
});


