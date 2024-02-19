from django.shortcuts import render
from menu.templatetags.menu_tags import draw_menu


def index(request):
    main_menu = draw_menu('main_menu')
    return render(request, 'index.html', {'main_menu': main_menu})
