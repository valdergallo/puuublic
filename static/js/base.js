$(function() {
    $('.redirect').click(function() {
        window.location = $(this).attr('rel');
    });

	$('form#id_signin_form').submit(function(e){
		e.preventDefault();
		posts = $(this).serialize();
		send_url = $(this).attr('action');
		$.post(send_url, posts, function(data){
			console.log(data);

			if (!data.status){
			    $('#id_signin_form .error').html(data.msg);
			}else{
			    window.location='/';
			}
            /*
			$("input").labelify({
                   text : "label"
               });
            */
		}, 'json');
	});


    //PLACEHOLDERS
    $('[placeholder]').focus(function() {
        var input = $(this);
        if (input.val() == input.attr('placeholder')) {
            input.val('');
            input.removeClass('placeholder');
        }
        }).blur(function() {
            var input = $(this);
            if (input.val() == '' || input.val() == input.attr('placeholder')) {
                input.addClass('placeholder');
                input.val(input.attr('placeholder'));
            }
        }).blur();



    //CONTATO
    $("form#form_contact").submit(function(e){
       e.preventDefault();
       action = $(this).attr('action');
       data = $(this).serializeArray();
       $.post(
            action,
            data,
            function(result){
                console.log(result);
                if (result.status){
                    alert($("#modal-content"),result.msg);
                }else{
                    alert($("#modal-content"),"Erro no envio!");
                }
            }
       );
    });


});

