from django.urls import path
from . import views

app_name = "favorites_app"
urlpatterns = [
    path(
        'profile',
        views.UserPageListView.as_view(),
        name='ProfilePage'
    )
]