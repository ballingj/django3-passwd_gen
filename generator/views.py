from django.shortcuts import render
#from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    '''Home Page to display password options'''
    return render(request, 'generator/home.html')

def about(request):
    '''About Page to display app info'''
    return render(request, 'generator/about.html')

def password(request):
    '''Generate a random string for password'''

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length', 12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    print(request)
    return render(request, 'generator/password.html', {'password': thepassword})
