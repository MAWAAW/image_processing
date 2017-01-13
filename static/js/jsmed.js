$(function() {
    $("#process-type-btn").click(function() {
        console.log('NAME::: '+$("input[name=bnoise]:checked").val());
        $.ajax({
            type: 'POST',
            url: '/median',
            contentType: 'application/json',
            data: JSON.stringify({ "size":$("#select").val(), "style":$("#select2").val(),
                                   "mode":$("#select3").val(), "bnoise":$("input[name=bnoise]:checked").val() }),
            dataType: 'json',
            cache: false,
            processData: false,
            async: true,
            success: function(resp) {
                console.log("Success !");

                $("#filtrer").attr('src', 'static/uploads/'+resp.image_name+'_medianFilter.'+resp.image_extension);
                $("#bruit").attr('src', 'static/uploads/'+resp.image_name+'_medianNoisy.'+resp.image_extension);
                $("#histogram").attr('src', 'static/uploads/'+resp.image_name+'_histogram.png');
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
