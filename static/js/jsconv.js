$(function() {
    $("#process-type-btn").click(function() {
        $.ajax({
            type: 'POST',
            url: '/convolution',
            contentType: 'application/json',
            data: JSON.stringify({ "size":$("#select").val(), "style":$("#select2").val() }),
            dataType: 'json',
            cache: true,
            processData: false,
            async: true,
            success: function(resp) {
                console.log("Success !");
                $("#filtrer").attr('src', 'static/uploads/'+resp.image_name+'_moyenneurFilter'+resp.image_num+'.'+resp.image_extension);
                $("#bruit").attr('src', 'static/uploads/'+resp.image_name+'_moyenneurNoisy'+resp.image_num+'.'+resp.image_extension);
                $("#histogram").attr('src', 'static/uploads/'+resp.image_name+'_histogram'+resp.image_num+'.png');
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
