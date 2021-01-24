from django import forms
""" Models """
from .models import Subscribers

class SubscriptorForm(forms.ModelForm):
    
    class Meta:
        model = Subscribers
        fields = ("email",)

        widgets = {
            'email': forms.EmailInput(
                 attrs = {
                    'placeholder': 'Type your email here..'
                }
            )
        }

