"""
Proyecto Curso Django
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
"""  SEO Sitemap """
from django.contrib.sitemaps.views import sitemap
""" Created SiteMap """
from applications.home.sitemap import (EntryStieMap, Sitemap,)

urlpatterns_main = [
    path('admin/', admin.site.urls),
    re_path('', include('applications.users.urls')),
    re_path('', include('applications.home.urls')),
    re_path('', include('applications.entry.urls')),
    re_path('', include('applications.favorites.urls')),
    # urls for ckeditor beacuse thta is another application with its own views and urls.
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #for serving static files like images adding to array its urls too

""" Object sitemap xml generator """
sitemaps = {
    'site': Sitemap(
        [
            'home_app:index'# can be added more
        ] 
    ),
    'entries': EntryStieMap
}

urlpatterns_sitemap = [
    path(
        'sitemap.xml/', 
        sitemap, 
        {'sitemaps':sitemaps},
        name = 'django.contrib.sitemaps.views.sitemap' #from django doc
    )
]


urlpatterns = urlpatterns_main + urlpatterns_sitemap
