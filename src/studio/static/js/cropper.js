const imageInput = document.getElementById('imageInput');
const imagePreview = document.getElementById('imagePreview');
const avatarImage = document.getElementById('avatarImage');
const cropButton = document.getElementById('cropButton');
const modal = document.getElementById('imageModal');
const span = document.getElementsByClassName('close')[0];
let cropper;

//  file input 
document.getElementById('changeAvatar').addEventListener('click', (event) => {
    event.preventDefault();
    imageInput.click();
});

imageInput.addEventListener('change', (event) => {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = () => {
            imagePreview.src = reader.result;
            modal.style.display = 'block';  // Show the modal

            // Initialize cropper 
            cropper = new Cropper(imagePreview, {
                viewMode: 1,
                cropBoxResizable: false,
                ready() {
                    // Set the initial crop box 
                    const cropBoxData = cropper.getCropBoxData();
                    cropper.setCropBoxData(cropBoxData);
                },
            });
        };
        reader.readAsDataURL(file);
    }
});

// cropButton
cropButton.addEventListener('click', () => {
    const croppedCanvas = cropper.getCroppedCanvas();

    const croppedImage = croppedCanvas.toDataURL();

    // Replace the avatar image with the cropped image
    avatarImage.src = croppedImage;

    // Send the cropped image to the server
    fetch('/upload-profile-image/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({ image: croppedImage})
        
        
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {

            alert('Profile image updated successfully!');
        } else {

            alert('Failed to update profile image.');
        }
    });
    
    // destroy cropper instance
    modal.style.display = 'none';
    cropper.destroy();
});

//  get CSRF token from cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }

    return cookieValue;
}

span.onclick = function() {
    modal.style.display = 'none';
    cropper.destroy();
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = 'none';
        cropper.destroy();
    }
}



