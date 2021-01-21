from django import template
from django.db.models import Avg, OuterRef, Subquery
from menus.models import Menu, MenuItem


register = template.Library()



@register.inclusion_tag('menus/tags/menu.html')
def draw_menu(menu_name):
    items = Menu.objects.get(name=menu_name).children.filter(parent=None)
    return {'items': items}
