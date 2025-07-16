
from django import template

register = template.Library()

@register.filter
def batch(iterable, batch_size):
    try:
        batch_size = int(batch_size)
    except (ValueError, TypeError):
        return [iterable]  # Retourne la liste telle quelle si erreur

    return [iterable[i:i + batch_size] for i in range(0, len(iterable), batch_size)]
