from django.contrib.sitemaps import Sitemap
from django.urls import reverse_lazy
from datetime import timedelta, datetime
""" models """
from applications.entry.models import Entry

""" Create s asite map for Entry model """
class EntryStieMap(Sitemap):
    """ Frwuwncy a section is changed """
    changefreq = 'weekly'
    priority = 0.8 # 0 -1 scale
    protocol = 'https'

    """ Which item belog this sitemap """
    def items(self):
        return Entry.objects.filter(public=True)

    def lastmod(self, obj):
        return obj.created

""" Redefining class """
class Sitemap(Sitemap):
    protocol = 'https'
    def __init__(self,names):
        self.names = names
    
    def items(self):
        return self.names

    def changefreq(self, obj):
        return 'weekly'

    def lastmod(self, obj):
        return datetime.now()

    def location(self, obj):
        return reverse_lazy(obj)