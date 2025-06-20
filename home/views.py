from django.shortcuts import render
from wagtail.models import Page
from django.conf import settings

# pages/context_processors.py
def global_context(request):
    root_page = Page.objects.filter(depth=2).first()
    menu_items = root_page.get_children().live().in_menu() if root_page else []
    
    return {
        'menu_items': menu_items,
        'site_settings': settings.SITE_SETTINGS,
    }
