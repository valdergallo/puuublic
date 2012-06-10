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
                alert(data.msg)
			    //window.location='/';
			}

		}, 'json');
	});


	$('form#id_signup_form').submit(function(e){
		e.preventDefault();
		posts = $(this).serializeArray();
		send_url = $(this).attr('action');
		$.post(send_url, posts,
            function(data){
			    console.log(data);
                alert(data.msg);
                if (!data.status){
                    html = '';
                    $("ul.signupErrors").empty();
                    $.each(data.errors,function(key,val){
                        html += '<li>' + val + '</li>';
                    });
                    $("ul.signupErrors").append(html);
                }
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
    $("form.form_contact").submit(function(e){
       e.preventDefault();
       action = $(this).attr('action');
       data = $(this).serializeArray();
       $.post(
            action,
            data,
            function(result){
                alert(result.msg);
            }
       ,'json');
    });


});

function alert(msg) {
    $("div#modal p").empty();
    $("div#modal p").append(msg);
    $("div#modal").overlay({
        top: 260,
        mask: {
            color: '#fff',
            loadSpeed: 200,
            opacity: 0.5,
        },
        load: true
    });
}


function confirm(msg,callback) {

}
