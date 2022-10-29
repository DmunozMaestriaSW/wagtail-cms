from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import RichTextField

from wagtail.models import Page


class NoticiaPage(Page):
    body = RichTextField()
    banner = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
        FieldPanel('banner'),
    ]

    subpage_types = ["Noticia"]


class Noticia(Page):
    date = models.DateField("Fecha publicacin")
    summary = models.CharField(max_length=250)
    body = RichTextField()
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels =  Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("summary"),
        FieldPanel("body"),
        FieldPanel("image"),
    ]

    parent_page_types = ["NoticiaPage"]