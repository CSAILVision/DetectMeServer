from django import template
from leaderboards.models import Category

register = template.Library()


@register.inclusion_tag('leaderboards/navmenu.html')
def navmenu(selected_item):
    """ Provides the navigation menu with the selected item highlighted """
    ctx = {'categories': Category.objects.all()}
    if selected_item:
        ctx['selected_item'] = selected_item
    return ctx
