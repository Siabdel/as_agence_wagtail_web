from wagtail.blocks import StructBlock, TextBlock, RichTextBlock, URLBlock, ImageChooserBlock
from wagtail.admin.panels import FieldPanel

class ServiceCardBlock(StructBlock):
    title = CharBlock(required=True, help_text="Titre du service")
    icon = ImageChooserBlock(help_text="Icône associée au service")
    description = TextBlock(help_text="Description initiale du service")
    detailed_description = RichTextBlock(help_text="Description détaillée du service")
    link_url = URLBlock(help_text="URL vers la page dédiée")

    class Meta:
        template = 'blocks/service_card_block.html'
        icon = 'placeholder'
        label = 'Carte de solution'
