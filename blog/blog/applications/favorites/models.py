from django.db import models
from django.conf import settings
""" Third party app """
from model_utils.models import TimeStampedModel
""" Models """
from applications.entry.models import Entry
""" Managers """
from .managers import FavoritesManager
# Create your models here.

class Favorites(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_favorites',
        on_delete=models.CASCADE
    )

    entry = models.ForeignKey(
        Entry,
        related_name='entry_favorites',
        on_delete=models.CASCADE
    )

    """ Managers connection """
    objects = FavoritesManager()

    """ For avoiduing register twice on BDD """

    class Meta:
        unique_together = ('user','entry')
        verbose_name = 'Favorites entry'
        verbose_name_plural = 'Favorites entries'

    def __str__(self):
        return self.entry.title