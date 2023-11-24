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

function refreshTable() {
    $.getJSON('/api/product', function(data) {
        var rows = '';
        $.each(data, function(index, product) {
            rows += '<tr>';
            rows += '<td>' + product[0] + '</td>';
            rows += '<td>' + product[1] + '</td>';
            rows += '<td>' + product[2] + '</td>';
            rows += '<td>' + product[3] + '</td>';
            rows += '<td>';
            rows += '<button class="btn btn-primary" onclick="viewProduct(' + product[0] + ')">View</button>';
            rows += '<button class="btn btn-danger" onclick="deleteProduct(' + product[0] + ')">Delete</button>';
            rows += '<button class="btn btn-warning" onclick="updateProduct(' + product[0] + ')">Update</button>';
            rows += '</td>';
            rows += '</tr>';
        });
        $('#product-table tbody').html(rows);
    });
}

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

function addProduct() {
    var name = $('#name').val();
    var color = $('#color').val();
    var quantity = $('#quantity').val();
    $.ajax({
        url: '/api/product',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            name: name,
            color: color,
            quantity: quantity
        }),
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



