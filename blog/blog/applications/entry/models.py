from django.db import models
from django.conf import settings
""" third party app """
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Category(TimeStampedModel):
    short_name = models.CharField(
        'Short Name', 
        max_length=15,
        unique=True
    )

    name = models.CharField(
        'Name',
        max_length=30
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Tag(TimeStampedModel):
    """ articles' tags """
    name = models.CharField(
        'Name',
        max_length=30
    )

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    
    def __str__(self):
        return self.name


class Entry(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE    
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    tag = models.ManyToManyField(Tag)
    title = models.CharField(
        'Title',
        max_length=200
    )

    brief = models.TextField('Brief')
    content = RichTextUploadingField('content')

    public = models.BooleanField(default=False)
    image = models.ImageField(
        'Image',
         upload_to = 'Entry'
    )
    cover_page = models.BooleanField(default=False)
    in_home = models.BooleanField(default=False)
    slug = models.SlugField(
        editable=False,
        max_length=300
    )

    class Meta:
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'
    
    def __str__(self):
        return self.title