$(function () {
    $("#process-type-btn").click(function () {

        var JSONObj = { "taille":$("#select").val(), "bord":$("#select2").val() };

        $.ajax({
            type: 'POST',
            url: '/median',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify(JSONObj, null, '\t'),
            cache: true,
            processData: false,
            async: true,
            success: function (data) {
                console.log("success!");
            },
            error: function(e) {
                console.log(e);
            },
            complete: function (data) {
                console.log('complete!');
                $("#filtrer").attr('src', 'static/uploads/ImageFilter.png')
                $("#bruit").attr('src', 'static/uploads/Noise.png')
                $("#histogram").attr('src', 'static/uploads/Histogram.png')
            }
        });
    });
});