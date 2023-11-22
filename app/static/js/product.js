function viewProduct(id) {
    $.ajax({
        url: '/api/product/' + id,
        type: 'GET',
        success: function(response) {
            // Display the response in a modal dialog
            $('#modal-title').text(response.name);
            $('#modal-body').html('<p><strong>Color:</strong> ' + response.color + '</p><p><strong>Quantity:</strong> ' + response.quantity + '</p>');
            $('#modal').modal('show');
        },
        error: function(xhr, status, error) {
            // Display an error message
            alert('Error: ' + error);
        }
    });
}

function deleteProduct(id) {
    $.ajax({
        url: '/api/product/' + id,
        type: 'DELETE',
        success: function(response) {
            // Reload the page
            location.reload();
        },
        error: function(xhr, status, error) {
            // Display an error message
            alert('Error: ' + error);
        }
    });
}

function updateProduct(id) {
    // Redirect to the update page
    window.location.href = '/update/' + id;
}
