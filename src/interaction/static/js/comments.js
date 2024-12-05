const commentInput = document.querySelector('.comment-input');

const cancelBtn = document.querySelector('.cancel-btn');
const commentButtons = document.querySelector('.comment-buttons');

const oldCommentSection = document.querySelector('#oldcomment');


commentInput.addEventListener('focus', function() {
    commentButtons.style.display = 'flex';
    commentInput.style.display = 'block'; 
});



cancelBtn.addEventListener('click', function(event) {
    event.preventDefault(); 
    commentInput.value = ''; 
    commentButtons.style.display = 'none'; 
});




$(document).ready(function() {
    $('#commentForm').submit(function(event) {
        event.preventDefault();
        // Serialize form data
        var formData = $(this).serialize();
        var form = $(this);
        // AJAX request
        $.ajax({
            type: 'POST',
            url: $(this).attr('action'),
            data: formData,
            success: function(response) {
                if (response.bool == true){
                    console.log('success')   
                    $("#oldcomment").load(window.location.href + " #oldcomment > *");
                    form.trigger('reset');
                    // location.reload();
                    
                }
            },
            error: function(error) {
                console.error('Error adding comment:', error);
            }
        });
    });


    
});

$(document).ready(function() {
    $(document).on('submit', '.commentFormChild', function(event) {
        event.preventDefault();
        var formDataChild = $(this).serialize();

        var formDataArray = $(this).serializeArray();
        formDataArray.forEach(function(field) {
            console.log(field.name + ': ' + field.value);
        });

        var form = $(this);
        $.ajax({
            type: 'POST',
            url: form.attr('action'),
            data: formDataChild,
            success: function(response) {
                if (response.bool == true){
                    console.log('success child');
                    $("#oldcomment").load(window.location.href + " #oldcomment > *");
                    form.trigger('reset');
                }
            },
            error: function(error) {
                console.error('Error adding comment:', error);
            }
        });
    });
});


// old comment
oldCommentSection.addEventListener('click', function(event) {
    if (event.target.classList.contains('replay')) {
        event.preventDefault();

        // Find the closest old-comment div and then its next sibling which is the replies form
        const oldCommentDiv = event.target.closest('.old-comment');
        const replyForm = oldCommentDiv.nextElementSibling;

        // Ensure that the next sibling is indeed the replies form
        if (replyForm && replyForm.classList.contains('replies')) {
            replyForm.style.display = 'block';
        }
    }

    if (event.target.classList.contains('cancel-replay')) {
        event.preventDefault();
        
        // Hide the closest replies form
        const replyForm = event.target.closest('.replies');
        if (replyForm) {
            replyForm.style.display = 'none';
        }
    }
});