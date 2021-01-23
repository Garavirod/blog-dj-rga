from django.db import models

class EntryManager(models.Manager):
    def entry_on_coverPage(self):
        return self.filter(
            public=True,
            cover_page=True,
        ).order_by('-created').first() #first element found in query