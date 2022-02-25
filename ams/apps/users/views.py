from django.shortcuts import render
from django.views.generic import TemplateView

class UsersView(TemplateView):
    template_name = 'users/users.html'
    extra_context = {}
