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
                var url_name=$("#name").val();
                console.log('url_name: '+url_name)
                $("#myImg").attr('src', 'static/uploads/'+url_name)
            }
        });
    });
});

$(function () {
    $("#process-type-btn").click(function () {
        $.ajax({
            type: 'POST',
            url: '/median',
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
                $("#filtrer").attr('src', 'static/uploads/ImageFilter.png')
                $("#bruit").attr('src', 'static/uploads/Noise.png')
                $("#histogram").attr('src', 'static/uploads/Histogram.png')
            }
        });
    });
});

$(function () {
    $("#process-type-btn2").click(function () {
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