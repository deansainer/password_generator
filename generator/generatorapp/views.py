from django.shortcuts import render
import random


def index(request):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '1234567890'
    special_numbers = '!@#$%^&*()_+~=-'

    password = [random.choice(letters + numbers + special_numbers) for i in range(16)]

    password1 = ''.join(password)
    context = {'password': password1}

    return render(request, 'generatorapp/index.html', context)
