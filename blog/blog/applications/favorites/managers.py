from django.db import models

class FavoritesManager(models.Manager):
    def entries_user_man(self,active_user):
        return self.filter(
            entry__public=True,
            user = active_user
        ).order_by('-created')