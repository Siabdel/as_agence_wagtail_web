# pages/context_processors.py
from wagtail.models import Page
from .models import SiteSettings

def global_context(request):
    root_page = Page.objects.filter(depth=2).first()
    menu_items = root_page.get_children().live().in_menu() if root_page else []
    site_settings = SiteSettings.objects.first() or None

    return {
        'menu_items': menu_items,
        'site_settings': site_settings,
    }
