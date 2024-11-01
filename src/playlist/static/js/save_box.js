// save box
document.addEventListener('DOMContentLoaded', function() {
    var shareBtn = document.getElementById('saveBtn');
    var saveDialog = document.getElementById('saveDialog');
    var closeBtn = document.getElementsByClassName('close-save')[0];

    shareBtn.onclick = function() {
        saveDialog.style.display = 'block';
    }

    closeBtn.onclick = function() {
        saveDialog.style.display = 'none';
    }

    window.onclick = function(event) {
        if (event.target == saveDialog) {
            saveDialog.style.display = 'none';
        }
    }
});

//  check-box playlist
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.playlist-checkbox').forEach(function(checkbox) {
        checkbox.addEventListener('change', function() {
            const playlistId = this.value;
            const videoId = this.dataset.videoId;
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
            console.log(csrfToken);

            const formData = new FormData();
            formData.append('playlist', playlistId);
            formData.append('action', this.checked ? 'add' : 'remove'); // condition ? valueIfTrue : valueIfFalse; 

            console.log(`Sending request to /video/${videoId}/add-to-playlist/ with playlist ID ${playlistId}`);

            fetch(`/video/${videoId}/add-to-playlist/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken
                },
                body: formData
            })
            .then(response => response.json()) // => anonymous functions 
            .then(data => {
                if (data.success) {
                    if (data.action === 'added') {
                        alert('Video added to playlist!');
                    } else if (data.action === 'removed') {
                        alert('Video removed from playlist!');
                    }
                } else {
                    alert(`Failed to ${this.checked ? 'add' : 'remove'} video from playlist: ${data.error}`);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred. Please try again.');
            });
        });
    });
});


// check-box Watch-Later
document.addEventListener('DOMContentLoaded', function() {
    const watchLaterCheckbox = document.getElementById('watch-later-checkbox');
    
    if (watchLaterCheckbox) {
        watchLaterCheckbox.addEventListener('change', function() {
            const videoId = this.dataset.videoId;
            
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
            

            const formData = new FormData();
            formData.append('action', this.checked ? 'add' : 'remove');
            fetch(`/watch-later/add/${videoId}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken
                },
                body: formData
            })
            .then(response => response.json())
            .then(data => {console.log(data);
                if (data.success) {
                    alert(`Video ${data.action === 'added' ? 'added to' : 'removed from'} Watch Later!`);
                } else {
                    alert(`Failed to ${this.checked ? 'add' : 'remove'} video from Watch Later: ${data.error}`);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred. Please try again.');
            });
        });
    }

});

console.log('aiiiiiiaooooooo');
