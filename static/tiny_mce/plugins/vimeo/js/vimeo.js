tinyMCEPopup.requireLangPack();var VimeoDialog={init:function(){var a=document.forms[0];a.VimeoURL.value=tinyMCEPopup.editor.selection.getContent({format:"text"})},insert:function(){function b(a){if(a.toLowerCase().indexOf("vimeo")>0){var b=new RegExp("/[0-9]+","g");var c=b.exec(a);if(c==null){return false}else{return c[0].substring(1)}}return false}var a=document.forms[0].vimeoURL.value;if(a===null){tinyMCEPopup.close();return}var c=b(a);if(c==false){tinyMCEPopup.close()}else{tinyMCEPopup.editor.execCommand("mceInsertContent",false,'<iframe width="600" height="480" src="http://player.vimeo.com/video/'+c+'" frameborder="0" allowfullscreen="allowfullscreen"></iframe>');tinyMCEPopup.close()}}};tinyMCEPopup.onInit.add(YoutubeDialog.init,YoutubeDialog)