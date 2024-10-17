document.addEventListener('DOMContentLoaded', function() {
    var shareBtn = document.getElementById('shareBtn');
    var shareDialog = document.getElementById('shareDialog');
    var closeBtn = document.getElementsByClassName('close-share')[0];

    shareBtn.onclick = function() {
        shareDialog.style.display = 'block';
    }

    closeBtn.onclick = function() {
        shareDialog.style.display = 'none';
    }

    window.onclick = function(event) {
        if (event.target == shareDialog) {
            shareDialog.style.display = 'none';
        }
    }
});


function copyLink() {
    var copyText = document.getElementById('shareLink');
    
    // Clipboard API to copy the link
    navigator.clipboard.writeText(copyText.value)
    .then(() => {
        alert('Copied the link: ' + copyText.value);
    })
    .catch(err => {
        console.error('Failed to copy: ', err);
    });
}
