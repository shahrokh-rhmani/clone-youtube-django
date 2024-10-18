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
