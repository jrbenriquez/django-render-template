from django.db import models

from wagtail.models import Page
from wagtail import blocks
from wagtail.fields import StreamField
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.admin.panels import MultiFieldPanel
from wagtailcodeblock.blocks import CodeBlock
from wagtail.images.blocks import ImageBlock
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
    PublishingPanel,
)
from wagtail.fields import RichTextField
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting,
)
from wagtail.models import (
    DraftStateMixin,
    PreviewableMixin,
    RevisionMixin,
    TranslatableMixin,
)
from wagtail.snippets.models import register_snippet


class HomePage(Page):
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Homepage image",
    )

    hero_text = models.CharField(
        blank=True, max_length=255, help_text="Write an introduction for the site"
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

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("hero_text"),
                FieldPanel("hero_cta"),
                FieldPanel("hero_cta_link"),
            ],
            heading="Main Section",
        ),
        FieldPanel("body"),
    ]

class HowItWorksPage(Page):

    body = StreamField([
            ('heading', blocks.CharBlock(form_classname="title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageBlock()),
            ('code', CodeBlock(label='Code Block')),
            ("rich_text", blocks.RichTextBlock(features=["bold", "italic", "link", "ul", "ol", "h2", "h3"])),
        ], use_json_field=True, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]


@register_setting
class NavigationSettings(BaseGenericSetting):
    linkedin_url = models.URLField(verbose_name="LinkedIn URL", blank=True)
    github_url = models.URLField(verbose_name="GitHub URL", blank=True)
    x_url = models.URLField(verbose_name="X URL", blank=True)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("linkedin_url"),
                FieldPanel("github_url"),
                FieldPanel("x_url"),
            ],
            "Social settings",
        )
    ]

@register_snippet
class FooterText(
    DraftStateMixin,
    RevisionMixin,
    PreviewableMixin,
    TranslatableMixin,
    models.Model,
):

    body = RichTextField()

    panels = [
        FieldPanel("body"),
        PublishingPanel(),
    ]

    def __str__(self):
        return "Footer text"

    def get_preview_template(self, request, mode_name):
        return "base.html"

    def get_preview_context(self, request, mode_name):
        return {"footer_text": self.body}

    class Meta(TranslatableMixin.Meta):
        verbose_name_plural = "Footer Text"
