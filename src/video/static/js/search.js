
$(document).ready(function() {
    const searchForm = $('#search-form');
    const searchInput = $('#search-input');
    const searchResultsContainer = $('.search-results-container');
    const micButton = document.querySelector('.mic'); // Reference to the microphone icon

    // Handle form submission for text-based search
    searchForm.on('submit', function(event) {
        event.preventDefault();
        const query = searchInput.val();
    
        // Update the URL without reloading the page
        const newUrl = `/search?q=${query}`;
        history.pushState(null, '', newUrl);
    
        console.log(newUrl);
        $.ajax({
            url: newUrl,
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            },
            success: function(data) {
                searchResultsContainer.empty(); // Clear previous results
    
                if (data.search_results.length === 0) {
                    // If no search results found
                    const noResultsElement = $(`
                        <div class="container-fluid p-5 py-3 search-results-container">
                            <div class="row margin-row">
                                <div class="col-12 col-md-6 col-lg-4 col-xl-3">
                                    No results found.
                                </div>
                            </div>
                        </div>
                    `);
                    searchResultsContainer.append(noResultsElement);
                } else {
                    data.search_results.forEach(video => {
                        const videoElement = $(`
                                <div class="row margin-row">
                                    <div class="col-12 col-md-6 col-lg-4 col-xl-3">
                                        <a href="${video.url}" class="card card-video border-0 bg-transparent mb-4">
                                            <img src="${video.image_url}" alt="${video.title}" class="img-fluid">
                                            <h4>${video.title}</h4>
                                        </a>
                                    </div>
                                </div>
                           
                        `);
                        searchResultsContainer.append(videoElement);
                    });
                }
            },
        });
    });
    

    // Check if the browser supports the Web Speech API
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

    if (SpeechRecognition) {
        const recognition = new SpeechRecognition();
        recognition.lang = 'en-US'; // Set the language
        recognition.interimResults = false; // We don't need interim results
        recognition.maxAlternatives = 1;

        // Event listener for the microphone button
        micButton.addEventListener('click', () => {
            recognition.start(); // Start voice recognition
        });

        // Event listener for when voice recognition gets a result
        recognition.addEventListener('result', (event) => {
            const transcript = event.results[0][0].transcript;
            searchInput.val(transcript); // Populate the search input with the recognized text
            searchForm.submit(); // Automatically submit the form
        });

        // Handle errors
        recognition.addEventListener('error', (event) => {
            console.error('Speech recognition error:', event.error);
        });

        // Change mic icon color when listening starts
        recognition.addEventListener('start', () => {
            micButton.style.color = 'red'; // Example: change icon color when listening
        });

        // Reset mic icon color when listening ends
        recognition.addEventListener('end', () => {
            micButton.style.color = ''; // Reset icon color when done
        });
    } else {
        console.warn('Web Speech API is not supported in this browser.');
    }
});

