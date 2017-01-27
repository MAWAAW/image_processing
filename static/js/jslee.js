$(function() {
    $("#process-type-btn").click(function() {
        $.ajax({
            type: 'POST',
            url: '/lee',
            contentType: 'application/json',
            data: JSON.stringify({ "size":$("#select").val(), "style":$("#select2").val() }),
            dataType: 'json',
            cache: true,
            processData: false,
            async: true,
            success: function(resp) {
                console.log("Success !");
                console.log(resp.image_name+'ImageFilter.png')
                $("#filtrer").attr('src', 'static/uploads/'+resp.image_name+'_LeeFilter'+resp.image_num+'.'+resp.image_extension);
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