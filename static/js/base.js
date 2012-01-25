$(function() {
    $('.redirect').click(function() {
        window.location = $(this).attr('rel');
    });                                       

	$('#id_signin_form').submit(function(e){
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
			
			$("input").labelify({
                   text : "label"
               });
               
		}, 'json');
	});
});
