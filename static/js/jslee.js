$(function() {
    $("#process-type-btn").click(function() {
        console.log("on rentre dans la fonction")
        $("#filtrer").attr('src','static/ajax-loader.gif');
        $("#bruit").attr('src','static/ajax-loader.gif');
        $("#histogram").attr('src','static/ajax-loader.gif');
        $.ajax({
            type: 'POST',
            url: '/lee',
            contentType: 'application/json',
            data: JSON.stringify({ "size":$("#select").val(), "style":$("#select2").val(),
                                    "mode":$("#select3").val(), "noise_dosage":$("input[name=rangeInput]").val()}),
            dataType: 'json',
            cache: true,
            processData: false,
            async: true,
            success: function(resp) {
                console.log("Success !");
                $("#filtrer").attr('src', 'static/uploads/'+resp.image_name+'_LeeFilter'+resp.image_num+'.'+resp.image_extension);
                $("#bruit").attr('src', 'static/uploads/'+resp.image_name+'_leeNoisy'+resp.image_num+'.'+resp.image_extension);
                $("#histogram").attr('src', 'static/uploads/'+resp.image_name+'histogram'+resp.image_num+'.png');
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
