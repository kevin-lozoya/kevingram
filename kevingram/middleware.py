"""Kevingram middleware catalog."""

from django.shortcuts import redirect
from django.urls import reverse
import re

class ProfileCompletionMiddleware:
    """Profile completion middleware.

    Ensure every user that is interacting with the platform
    have their profile picture and biografy.
    """

    def __init__(self, get_response):
        """Middleware initialization."""

        self.get_response = get_response

    def __call__(self, request):
        """Code to be executed for each request before the view is called."""

        if not request.user.is_anonymous \
            and not request.user.is_staff \
            and not re.match(r'\S+(media)\S*', request.path):
            profile = request.user.profile
            
            if not profile.website or not profile.biografy:
                if request.path not in [reverse('update_profile'), reverse('logout')]:
                    return redirect('update_profile')

        response = self.get_response(request)
        return response