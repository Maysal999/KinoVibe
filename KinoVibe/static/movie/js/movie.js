const video = document.getElementById('video-player');
const playPauseBtn = document.getElementById('play-pause');
const rewindBtn = document.getElementById('rewind');
const forwardBtn = document.getElementById('forward');
const muteUnmuteBtn = document.getElementById('mute-unmute');
const volumeBar = document.getElementById('volume-bar');
const seekBar = document.getElementById('seek-bar');

// Play or Pause the video
playPauseBtn.addEventListener('click', () => {
    if (video.paused || video.ended) {
        video.play();
        playPauseBtn.textContent = '⏸';
    } else {
        video.pause();
        playPauseBtn.textContent = '⏯';
    }
});

// Rewind 10 seconds
rewindBtn.addEventListener('click', () => {
    video.currentTime -= 10;
});

// Forward 10 seconds
forwardBtn.addEventListener('click', () => {
    video.currentTime += 10;
});

// Mute or Unmute the video
muteUnmuteBtn.addEventListener('click', () => {
    if (video.muted) {
        video.muted = false;
        muteUnmuteBtn.textContent = '🔊';
    } else {
        video.muted = true;
        muteUnmuteBtn.textContent = '🔇';
    }
});

// Volume control
volumeBar.addEventListener('input', () => {
    video.volume = volumeBar.value;
});

// Seek bar update
video.addEventListener('timeupdate', () => {
    const value = (100 / video.duration) * video.currentTime;
    seekBar.value = value;
});

// Seek bar control
seekBar.addEventListener('input', () => {
    const time = (video.duration / 100) * seekBar.value;
    video.currentTime = time;
});
