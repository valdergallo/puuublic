$(function() {
  $('.redirect').click(function() {
    window.location = $(this).attr('rel');
  });
  //dropdown
  resizeBG();
  $(".dropdown-toggle").dropdown() ;
  $(window).resize(function(){
    resizeBG();
  });

  function resizeBG(){
    if ($(window).width() <= 1024 ){
      $(".dropdown").css('left',920);
    }else{
      $(".dropdown").css('left',1100);
    }
  }

  //login
  $('form#loginUser').submit(function(e){
    e.preventDefault();
    $("ul.errors").empty();
    posts = $(this).serialize();
    send_url = $(this).attr('action');
    $.post(send_url, posts, function(data){
      if (!data.status){
        $('ul.errors').empty();
        $('#signin-modal').modal();
        $('ul.errors').html('<li>' + data.msg + '</li>');
      }else{
        window.location='/dashboard/';
      }

    }, 'json');
  });

  //registro
  $('form#id_signup_form').submit(function(e){
    e.preventDefault();
    $('.green-button').attr('disabled', 'disabled');
    $('.green-button').html('Criando conta, aguarde..');
    //limpa errors
    posts = $(this).serializeArray();
    send_url = $(this).attr('action');
    $.ajax({
      url: send_url, 
      data: posts,
      dataType: 'JSON',
      type: 'POST',
      success: function(data){
        if (!data.status){
          updateCaptcha();
          $('.green-button').html('Criar conta');
          $('.green-button').removeAttr('disabled');
          $("#error-modal").modal();
          html = '';
          $("ul.errors").empty();
          $.each(data.errors,function(key,val){
            html += '<li>' + val + '</li>';
          });
          $("ul.errors").append(html);
        }else{
          //redirect
          window.location = '/dashboard/';
        }
      }
    });
  });
  
  function updateCaptcha(){
     $.getJSON('/captcha/refresh/', {}, function(json) {
      $('img.captcha').attr('src', json.image_url);
      $('#id_captcha_0').val(json.key);
      // This your should update captcha image src and captcha hidden input
    });
  }

  $('.js-captcha-refresh').click(updateCaptcha);

  //Recuperacao senha
  $("form#recover-form").submit(function(e){
    e.preventDefault();
    $("#loading").show();
    $("ul.recover-errors").empty();
    var data = $(this).serializeArray();
    var url = $(this).attr('action');
    $.post(url,data,
      function(result){
        $("#loading").hide();
        $("ul.recover-errors").empty();
        $("ul.recover-errors").append('<li>' + result.msg + '</li>');
      },'json')
  });

  //Adicionar Puuublic
  $("#themeForm").submit(function(e){
    e.preventDefault();
    $("#loading").show();
    var data = $(this).serializeArray();
    var url = $(this).attr('action');
    $.post(url,data,
      function(data){
        if (!data.status){
          $("#loading").hide();
          $("#error-modal").modal();
          $("#errorModalLabel > h3").html('Erro no cadastro');
          $("ul.errors").empty();
          html = '';
          $.each(data.errors,function(key,val){
            html += '<li>' + val + '</li>';
          });
          $("ul.errors").append(html);
        }else{
          window.location = data.url;
        }
      },'json')
  });

  //CONTATO
  $("#formContact").submit(function(e){
    e.preventDefault();
    action = $(this).attr('action');
    data = $(this).serializeArray();
    $.post(
      action,
      data,
      function(data){
        if (!data.status){
          $("#error-modal").modal();
          $("#errorModalLabel > span").html('Preenchimento Incorreto');
          html = '';
          $("ul.errors").empty();
          $.each(data.errors,function(key,val){
            html += '<li>' + val + '</li>';
          });
          $("ul.errors").append(html);
        }else{
          $("#successLabel > span").empty();
          $("#success-modal > .modal-body > p").empty()
      $("#successLabel > span").html('Mensagem enviada');
    $("#success-modal > .modal-body > p").html(data.msg);
    $('#success-modal').modal();
        }
      }
    ,'json');
  });

  //THEME
  $("input#id_title").keypress(function(e){
    setTimeout(function(){
      var totalChars = 50;
      var val = $("input#id_title").val();
      if (val != $(this).attr('placeholder')){
        val = slugify(val);
        $("input#id_url").val(val);
        $("div.auto_url a").html("http://puuublic.com/" + val + '/');
        $(".remaining").html(( totalChars - val.length ).toString() );
      }
    },1000);
  });

  //acc_config
  $("#id_profile-nickname").focusout(function(e){
    var val = $("#id_profile-nickname").val();
    if (val.length > 3){
      val = slugify(val);
    }else{
      val = '';
    }
    $("span.nickname-preview").html("http://puuublic.com/perfil/" + val + '/');
  });


  //autocomplete
  $("#id_theme_name").typeahead({
    source: function( request, response ) {
              $.ajax({
                url: "/publicacao/puuublic/buscar/json/",
                dataType: "json",
                data: { term: request },
                success: function(data) {
                  response(data);
                }
              });
            },
    minLength: 2,
  });

  //favorites
  $('#favorite').click(function(e){
    e.preventDefault();
    data = { 'key': $(this).attr('key') };
    $.ajax({
      dataType: "JSON",
      type: "POST",
      data: data,
      url: '/ajax_add_favorite/',
      success: function(response){
        if (response.status){
          switch(response.action){
            case "add":
              $('#favorite').removeClass('green-button').addClass('btn btn-primary btn-large').html('Favoritado');
              break;          
            case "remove":
              $('#favorite').removeClass('btn btn-primary btn-large').addClass('green-button').html('Favoritar');
              break;       
          }
        }
      }
    });
  });

});

function slugify(str){
  str = str.replace(/^\s+|\s+$/g, ''); // trim
  str = str.toLowerCase();
  var from = "ãàáäâẽèéëêìíïîõòóöôùúüûñç·/_,:;";
  var to   = "aaaaaeeeeeiiiiooooouuuunc------";
  for (var i=0, l=from.length ; i<l ; i++) {
    str = str.replace(new RegExp(from.charAt(i), 'g'), to.charAt(i));
  }

  str = str.replace(/[^a-z0-9 -]/g, '') // remove invalid chars
    .replace(/\s+/g, '-') // collapse whitespace and replace by -
    .replace(/-+/g, '-'); // collapse dashes

  return str;
};

