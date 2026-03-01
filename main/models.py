from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify


class Service(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)

    icon = models.CharField(
        max_length=50,
        help_text='Font Awesome icon class (e.g., fa-video)'
    )

    description = models.TextField(help_text="Short text for homepage cards")
    content = HTMLField(help_text="Full service page content")

    # SEO
    seo_title = models.CharField(max_length=60, blank=True)
    seo_description = models.CharField(max_length=160, blank=True)
    seo_image = models.ImageField(upload_to='seo/', blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Services'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ServiceImage(models.Model):
    service = models.ForeignKey(
        Service,
        related_name='images',
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='services/')
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.service.name} image"


class Partner(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='partners/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Partners'

    def __str__(self):
        return self.name
    




class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    excerpt = models.TextField(max_length=300)
    content = models.TextField()
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-published_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
