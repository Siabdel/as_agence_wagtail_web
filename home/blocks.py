
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock


class HeroBlock(blocks.StructBlock):
    background_image = ImageChooserBlock(required=True, help_text="Image de fond du header")
    title = blocks.CharBlock(required=True, max_length=255, help_text="Titre principal")
    subtitle = blocks.TextBlock(required=False, help_text="Sous-titre")
    button_text = blocks.CharBlock(required=False, max_length=100, help_text="Texte du bouton principal")
    button_url = blocks.URLBlock(required=False, help_text="URL du bouton principal")

    class Meta:
        template = "home/blocks/hero_block.html"
        icon = "image"
        label = "Hero Header"


class ButtonBlock(blocks.StructBlock):
    text = blocks.CharBlock(required=True, max_length=50)
    url = blocks.URLBlock(required=False)
    style = blocks.ChoiceBlock(choices=[
        ('primary', 'Bouton principal (plein)'),
        ('secondary', 'Bouton secondaire (outline)'),
    ], default='primary')

    class Meta:
        icon = "link"
        label = "Bouton"

class AdvancedHeroBlock(blocks.StructBlock):
    use_video = blocks.BooleanBlock(required=False, default=False, help_text="Utiliser une vidéo comme fond ?")
    background_image = ImageChooserBlock(required=False, help_text="Image de fond")
    background_video = EmbedBlock(required=False, help_text="Lien vidéo (YouTube, Vimeo...)")
    
    title = blocks.CharBlock(required=True, max_length=255)
    subtitle = blocks.TextBlock(required=False)
    
    text_position = blocks.ChoiceBlock(choices=[
        ('start', 'Aligné à gauche'),
        ('center', 'Centré'),
        ('end', 'Aligné à droite'),
    ], default='center')

    buttons = blocks.ListBlock(ButtonBlock(required=False), required=False)

    class Meta:
        template = "home/blocks/advanced_hero_block.html"
        icon = "image"
        label = "Hero avancé"

## Services block
class ServiceItemBlock(blocks.StructBlock):
    icon = blocks.CharBlock(required=True, help_text="Classe CSS de l’icône (ex : 'bi bi-briefcase')")
    title = blocks.CharBlock(required=True, max_length=100)
    description = blocks.TextBlock(required=True)

    class Meta:
        icon = "placeholder"
        label = "Service"
        template = "home/blocks/service_item.html"  # pour un item seul (optionnel)

class ServicesBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, max_length=100, help_text="Titre de la section")
    services = blocks.ListBlock(ServiceItemBlock())

    class Meta:
        icon = "list-ul"
        label = "Section Services"
        template = "home/blocks/services_block.html"


class ClientItemBlock(blocks.StructBlock):
    logo = ImageChooserBlock(required=True, help_text="Logo du client")
    name = blocks.CharBlock(required=False)
    alt_text = blocks.CharBlock(required=False, help_text="Texte alternatif pour l’accessibilité")

    class Meta:
        icon = "image"
        label = "Client"



class ClientLogoBlock(blocks.StructBlock):
    logo = ImageChooserBlock(required=True, help_text="Logo du client")
    alt_text = blocks.CharBlock(required=False, help_text="Texte alternatif")

class TestimonialBlock(blocks.StructBlock):
    quote = blocks.TextBlock(required=True, help_text="Citation ou témoignage")
    author = blocks.CharBlock(required=True, max_length=100, help_text="Nom du client")
    role = blocks.CharBlock(required=False, max_length=100, help_text="Poste ou entreprise")

class ClientsBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, max_length=100)
    clients = blocks.ListBlock(ClientLogoBlock())
    testimonial = TestimonialBlock(required=False)
    enable_carousel = blocks.BooleanBlock(required=False, default=True, help_text="Activer le carousel de logos")

    class Meta:
        template = "home/blocks/clients_block.html"
        icon = "group"
        label = "Clients + Témoignage"
