from django.urls import path
from . import views

app_name = "favorites_app"
urlpatterns = [
    path(
        'profile',
        views.UserPageListView.as_view(),
        name='ProfilePage'
    ),
    path(
        'add-entry/<pk>/',
        views.AddFavoritesViews.as_view(),
        name='AddFavorite'
    ),
    path(
        'delete-favorite/<pk>/',
        views.DeleteFavoriteView.as_view(),
        name='DeleteFavorite'
    )
]