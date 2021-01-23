from django.db import models
""" third party app """
from model_utils.models import TimeStampedModel #Created and updated atr models


class Home(TimeStampedModel):
    """ Models for Main page """
    title = models.CharField(
        'Name',
        max_length=30,
    )

    ddescription = models.TextField()
    about_title = models.CharField(
        'Title use',
        max_length=50
    )
    about_text = models.TextField()
    contact_email = models.EmailField(
        'email contact',
        blank=True,
        null=True
    )

    phone = models.CharField(
        'Phone conctact',
        max_length=20
    )

    class Meta:
        verbose_name = 'Main page',
        verbose_name_plural = 'Main page'

    def __str__(self):
        return self.title

class Subscribers(TimeStampedModel):
    email = models.EmailField()
    class Meta:
        verbose_name = 'Subscriptor'
        verbose_name_plural = 'Subsciptors'

    def __str__(self):
        return self.email

class Contact(TimeStampedModel):
    full_name = models.CharField(
        'Names',
        max_length=60
    )

    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.full_name