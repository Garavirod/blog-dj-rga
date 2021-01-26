from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.urls import reverse_lazy
""" Models """
from .models import Favorites
# Create your views here.


class UserPageListView(LoginRequiredMixin,ListView):
    template_name = "favorites/profile.html"
    context_object_name = "entries_user"
    """ In case user isn't loggedin, redirect to """
    login_url = reverse_lazy('users_app:user-login')

    def get_queryset(self):
        return Favorites.objects.entries_user_man(self.request.user) 
    
