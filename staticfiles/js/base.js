document.addEventListener('DOMContentLoaded', function() {
    var video = document.querySelector('.video'); // Get the first element with the class 'video'
  
    // Function to ensure video is playing
    function ensureVideoIsPlaying() {
      if (video.paused) {
        video.play().catch(e => console.error("Error attempting to play video:", e));
      }
    }
  
    ensureVideoIsPlaying();
    setInterval(ensureVideoIsPlaying, 1000);
  
    // Handle video play/pause events
    video.addEventListener('play', function() {
      console.log('Video started playing');
    });
  
    video.addEventListener('pause', function() {
      console.log('Video paused');
      ensureVideoIsPlaying();
    });
  });