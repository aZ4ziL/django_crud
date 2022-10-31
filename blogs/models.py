from django.db import models
from django.utils.translation import gettext, gettext_lazy as _
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(_("title"), max_length=100, unique=True)
    slug = models.SlugField()
    logo = models.ImageField(_("logo"), upload_to="categories")
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)
