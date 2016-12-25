$(function() {
    $("#upload-file-btn").click(function() {
        var form_data = new FormData($('#upload-file')[0]);
        $.ajax({
            type: 'POST',
            url: '/',
            data: form_data,
            contentType: false,
            cache: true,
            processData: false,
            async: true,
            success: function(data) {
                console.log('Success !');
                $("#myImg").attr('src', 'static/uploads/'+$("#name").val())
            },
            error: function(e) {
                console.log(e);
            },
            complete: function(data) {
               console.log(data);
            }
        });
    });
});