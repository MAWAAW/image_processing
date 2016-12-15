$(function () {
    $("#upload-file-btn").click(function () {
        console.log('ajax upload');
        var form_data = new FormData($('#upload-file')[0]);
        console.log(form_data);
        $.ajax({
            type: 'POST',
            url: '/',
            data: form_data,
            contentType: false,
            cache: true,
            processData: false,
            async: true,
            success: function (data) {
                console.log('Success!');
            },
            error: function(e) {
                console.log(e);
            },
            complete: function (data) {
                $("#myImg").attr('src', 'static/uploads/'+$("#name").val())
            }
        });
    });
});