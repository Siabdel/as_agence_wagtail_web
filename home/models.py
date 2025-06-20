from django.db import models

# pages/models.py
from wagtail.models import Page
from wagtail.fields import StreamField, RichTextField
# import MultiFieldPanel:
from wagtail.admin.panels import FieldPanel, MultiFieldPanel


from wagtail.blocks import (
    CharBlock, TextBlock, URLBlock, EmailBlock,
    StructBlock, ListBlock, IntegerBlock
)
from wagtail.images.blocks import ImageChooserBlock
# Create your models here.
from wagtail.snippets.models import register_snippet



class Accueil(Page):
    body = StreamField([
        ('hero', StructBlock([
            ('title', CharBlock(required=True)),
            ('subtitle', CharBlock()),
            ('background_image', ImageChooserBlock()),
            ('button_text', CharBlock()),
            ('button_url', URLBlock(required=False)),
        ])),
        ('services', StructBlock([
            ('title', CharBlock()),
            ('service_items', ListBlock(StructBlock([
                ('icon', CharBlock()),
                ('title', CharBlock()),
                ('description', TextBlock()),
            ]))),
        ])),
        ('projects', StructBlock([
            ('title', CharBlock()),
            ('project_items', ListBlock(StructBlock([
                ('image', ImageChooserBlock()),
                ('title', CharBlock()),
                ('category', CharBlock()),
            ]))),
        ])),
        ('expertise', StructBlock([
            ('title', CharBlock()),
            ('expertise_items', ListBlock(StructBlock([
                ('number', IntegerBlock()),
                ('title', CharBlock()),
                ('description', TextBlock()),
            ]))),
        ])),
        ('testimonials', StructBlock([
            ('title', CharBlock()),
            ('testimonials', ListBlock(StructBlock([
                ('quote', TextBlock()),
                ('author', CharBlock()),
                ('company', CharBlock()),
            ]))),
        ])),
        ('contact', StructBlock([
            ('title', CharBlock()),
            ('address', CharBlock()),
            ('phone', CharBlock()),
            ('email', EmailBlock()),
        ])),
    ], use_json_field=True, blank=True)

     # modify your content_panels:
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            heading="Hero section",
        ),
        FieldPanel('body'),
    ]





class HomePage(Page):
    # add the Hero section of HomePage:
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Homepage image",
    )
    hero_text = models.CharField(
        blank=True,
        max_length=255, help_text="Write an introduction for the site"
    )
    hero_cta = models.CharField(
        blank=True,
        verbose_name="Hero CTA",
        max_length=255,
        help_text="Text to display on Call to Action",
    )
    hero_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Hero CTA link",
        help_text="Choose a page to link to for the Call to Action",
    )

    body = RichTextField(blank=True)

    # modify your content_panels:
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("image"),
                FieldPanel("hero_text"),
                FieldPanel("hero_cta"),
                FieldPanel("hero_cta_link"),
            ],
            heading="Hero section",
        ),
        FieldPanel('body'),
    ]
    
    
    # pages/models.py
@register_snippet
class SiteSettings(models.Model):
    site_name = models.CharField(max_length=255, default="Agence Web")
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('site_name'),
        FieldPanel('logo'),
    ]

    def __str__(self):
        return self.site_name