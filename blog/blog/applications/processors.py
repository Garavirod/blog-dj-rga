""" Models """
from applications.home.models import Home

""" Process for recovering email and phone from HomePage """

def home_contact(request):
    """ Recover firs getsiter home """
    home = Home.objects.latest('created')

    """ Context dictionary """
    return {
        'phone': home.phone,
        'email': home.contact_email,
    }