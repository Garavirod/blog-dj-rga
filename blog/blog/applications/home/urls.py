#
from django.urls import path
from . import views

app_name = "home_app"

urlpatterns = [
    path(
        '', 
        views.HomePageView.as_view(),
        name='index',
    ),  
    path(
        'register-subscriptor', #to access by url
        views.SubscriptorCreateView.as_view(),
        name='add-subscriptor',
    ), 
    path(
        'contact-form', #to access by url
        views.ContactCreateView.as_view(),
        name='ContactForm',
    ), 
]