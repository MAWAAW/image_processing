$(function() {
    $("#process-type-btn").click(function() {
        $("#filtrer").attr('src','static/ajax-loader.gif');
        $("#bruit").attr('src','static/ajax-loader.gif');
        $("#histogram").attr('src','static/ajax-loader.gif');
        $.ajax({
            type: 'POST',
            url: '/median',
            contentType: 'application/json',
            data: JSON.stringify({ "size":$("#select").val(), "style":$("#select2").val(),
                                   "mode":$("#select3").val(), "noise_dosage":$("input[name=rangeInput]").val() }),
            dataType: 'json',
            cache: true,
            processData: false,
            async: true,
            success: function(resp) {
                console.log("Success !");
                $("#filtrer").attr('src', 'static/uploads/'+resp.image_name+'_medianFilter'+resp.image_num+'.'+resp.image_extension);
                $("#bruit").attr('src', 'static/uploads/'+resp.image_name+'_medianNoisy'+resp.image_num+'.'+resp.image_extension);
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

$(function () {
    $('#rangeInput').on('input change', function () {
        $('#rangeText').text($('#rangeInput').val());
    });
});
