from django.shortcuts import render
import random
from django import forms
from django.forms import forms

from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import *


class IndexPage(TemplateView):
    template_name = 'generatorapp/index.html'

    def get(self, request, *args, **kwargs):
        form = IndexForm()

        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = IndexForm(request.POST)
        if form.is_valid():
            password_length = form.cleaned_data['password_length']
            letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            numbers = '1234567890'
            special_numbers = '!@#$%^&*()_+~=-'
            if 'letters' in request.POST:
                password = [random.choice(letters) for i in range(password_length)]
            if 'letters_numbers' in request.POST:
                password = [random.choice(letters+numbers) for i in range(password_length)]
            if 'letters_numbers_special' in request.POST:
                password = [random.choice(letters+numbers+special_numbers) for i in range(password_length)]

            final_password = ''.join(password)
        return render(request, self.template_name, context={'form': form, 'password': final_password})

