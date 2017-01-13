$(function() {
    $("#process-type-btn").click(function() {
        $.ajax({
            type: 'POST',
            url: '/median',
            contentType: 'application/json',
            data: JSON.stringify({ "size":$("#select").val(), "style":$("#select2").val(),
                                   "mode":$("#select3").val(), "bnoise":$("#select4").val() }),
            dataType: 'json',
            cache: true,
            processData: false,
            async: true,
            success: function(resp) {
                console.log("Success !");
                console.log(resp.image_name+'ImageFilter.png')
                $("#filtrer").attr('src', 'static/uploads/'+resp.image_name+'ImageFilter.png');
                $("#bruit").attr('src', 'static/uploads/'+resp.image_name+'Noise.png');
                $("#histogram").attr('src', 'static/uploads/'+resp.image_name+'Histogram.png');
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

/*$(function () {
    $("#process-type-btn").click(function() {
        $.post('/median',
        JSON.stringify({ "taille":$("#select").val(), "bord":$("#select2").val() }),
        function(data, status){
            alert("Data: " + data.url_filtrer + "\nStatus: " + status);
        });
    });
});*/
