from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
from django.utils.text import slugify


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(null=True, upload_to="images/", blank=True)
    thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(150, 150)], format="PNG",
                                      options={'quality': 60})


