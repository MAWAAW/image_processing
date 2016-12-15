$(function () {
    $("#process-type-btn").click(function () {
        $.ajax({
            type: 'POST',
            url: '/convolution',
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
                console.log('complete ! ');
            }
        });
    });
});