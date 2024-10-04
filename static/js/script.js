// Function to fetch quotes for a character
function getCharacterQuotes(characterName) {
    const quotesContainer = $('#quotesContainer'); // Get the container
    quotesContainer.text("Loading..."); // Clear previous quotes

    quotesContainer.append(`<h4>${characterName}'s Quotes'</h4>`);
    $.ajax({
        url: `/get_book_quotes`, // Your Flask route
        type: 'GET',
        data: { character: characterName }, // Send the character name as a query parameter
        success: function(response) {
            // Handle success response
            displayQuotes(response, characterName); // Assuming response contains the quotes
        },
        error: function(xhr, status, error) {
            console.error('Error fetching quotes:', error);
        }
    });
}

// Function to display the quotes in the HTML
function displayQuotes(data, characterName) {
    const quotesContainer = $('#quotesContainer'); // Get the container
    quotesContainer.empty(); // Clear previous quotes

    quotesContainer.append(`<h4>${characterName}'s Quotes'</h4>`);
    if (data.quotes && data.quotes.length > 0) {
        // Loop through and append each quote
        var x = 1;
        data.quotes.forEach(function(quote) {
            console.log("${quote.dialog}");
            quotesContainer.append(`<p><span>${x} &nbsp;</span>${quote.dialog}</p>`);
            x++;
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

    // Attach a click event listener to all character names
    $('.character-name').click(function(event) {
        event.preventDefault();

        // Get the character ID from the data-id attribute
        var characterId = $(this).data('id');

        // Find the corresponding details div and toggle slide effect
        var detailsDiv = $('#details-' + characterId);

        detailsDiv.slideToggle(); // Slide the div open/closed
    });


});
