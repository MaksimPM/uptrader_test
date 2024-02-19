from django import template
from django.utils.safestring import mark_safe
from menu.models import MenuItem

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(title=menu_name, parent=None)
    result = ''
    for item in menu_items:
        result += f'Меню: <a href="{item.url}">{item.title}</a></br>'
        children = MenuItem.objects.filter(parent=item)
        if children:
            for child in children:
                result += f'&emsp;• <a href="{child.url}">{child.title}</a><br>'
    return mark_safe(result)
