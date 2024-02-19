from django import template
from menu.models import MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    menu_items = MenuItem.objects.filter(menu_name=menu_name, parent=None).select_related('children')

    def render_submenu(menu_item):
        submenu_items = menu_item.children.all()
        if not submenu_items:
            return ''

        submenu_html = '<ul>'
        for item in submenu_items:
            active_class = 'active' if request.path == item.url else ''
            submenu_html += f'<li class="{active_class}"><a href="{item.url}">{item.title}</a>'
            submenu_html += render_submenu(item)
            submenu_html += '</li>'
        submenu_html += '</ul>'
        return submenu_html

    menu_html = '<ul>'
    for item in menu_items:
        active_class = 'active' if request.path == item.url else ''
        menu_html += f'<li class="{active_class}"><a href="{item.url}">{item.title}</a>'
        menu_html += render_submenu(item)
        menu_html += '</li>'
    menu_html += '</ul>'
    return menu_html
