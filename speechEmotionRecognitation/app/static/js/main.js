$(document).ready(function() {
    $('#uploadForm').submit(function(event) {
        event.preventDefault(); // Prevent default form submission

        var formData = new FormData($(this)[0]);

        $.ajax({
            url: 'upload.php', // Replace 'upload.php' with your server-side script URL
            type: 'POST',
            data: formData,
            async: false,
            cache: false,
            contentType: false,
            processData: false,
            success: function(response) {
                $('#result').html(response); // Update the content of the 'result' div
            },
            error: function(xhr, textStatus, errorThrown) {
                alert('Error occurred while uploading the file.');
                console.log(xhr.responseText);
            }
        });

        return false;
    });
});