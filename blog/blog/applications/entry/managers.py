from django.db import models

class EntryManager(models.Manager):

    def entry_on_coverPage(self):
        return self.filter(
            public=True,
            cover_page=True,
        ).order_by('-created').first() #first element found in query

    def entry_articles(self):
        """ REturn last 4 entries """
        return self.filter(
            public=True,
            in_home=True,
        ).order_by('-created')[:4]

    def entry_recent_articles(self):
        """ REturn last 6 entries """
        return self.filter(
            public=True,
        ).order_by('-created')[:6]