# -*- encoding: utf-8 -*-
from publication.forms import SearchForm 
from friendship.forms import LoginForm

def global_includes(request):
    """
    Formulário de Pesquisa no Contexto das páginas
    """

    search_form = SearchForm()
    login_form = LoginForm()
    return {
        'search_form':search_form,
        'login_form':login_form,
        }


