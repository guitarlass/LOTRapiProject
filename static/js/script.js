// Function to fetch quotes for a character
function getCharacterQuotes(characterName) {
    $.ajax({
        url: `/get_book_quotes`, // Your Flask route
        type: 'GET',
        data: { character: characterName }, // Send the character name as a query parameter
        success: function(response) {
            // Handle success response
            displayQuotes(response); // Assuming response contains the quotes
        },
        error: function(xhr, status, error) {
            console.error('Error fetching quotes:', error);
        }
    });
}

// Function to display the quotes in the HTML
function displayQuotes(data) {
    alert("hello");
    const quotesContainer = $('#quotesContainer'); // Get the container
    quotesContainer.empty(); // Clear previous quotes

    if (data.quotes && data.quotes.length > 0) {
        // Loop through and append each quote
        data.quotes.forEach(function(quote) {
            quotesContainer.append(`<p>${quote}</p>`);
        });
    } else {
        quotesContainer.append('<p>No quotes found for this character.</p>');
    }
}
$(document).ready(function(){
// Event listener for when the Enter key is pressed
    $('#characterQuote').on('keypress', function(event) {
        if (event.key === 'Enter') {
            const characterName = $(this).val(); // Get the value from the input field
            getCharacterQuotes(characterName); // Call the function to fetch quotes
            $(this).val(''); // Clear the input field
        }
    });
});
