""" STANDARD LIBRARIES """
from datetime import  timedelta,datetime
from django.db import models
from django.conf import settings
""" django """
from django.template.defaultfilters import slugify
""" third party app """
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField
# Managers
from .managers import EntryManager

class Category(TimeStampedModel):
    short_name = models.CharField(
        'Short Name', 
        max_length=15,
        unique=True
    )

    name = models.CharField(
        'Name',
        max_length=80
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
    """ Manager connection """
    objects = EntryManager()
    class Meta:
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'
    
    def __str__(self):
        return self.title

    def save(self,*args, **kwargs):
        now = datetime.now()
        total_time = timedelta(
            hours = now.hour,
            minutes = now.minute,
            seconds = now.second
        )

        seconds = int(total_time.total_seconds())
        """ Genereater a slug based on titile """
        slug_unique = '%s %s' % (self.title,str(seconds))
        self.slug = slugify(slug_unique)

        """ For overriding save method """
        super(Entry,self).save(*args, **kwargs)