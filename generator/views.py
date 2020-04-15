from django.shortcuts import render
from django.http import HttpRequest
import random

# Create your views here.

def home(request):
	return render(request, 'home.html')

def check(request):

	characters = list('abcdefghijklmnopqrstuvwxyz')
	length = int(request.GET.get('length'))
	if 4 < length < 16:

		if request.GET.get('uppercase'):
			characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

		if request.GET.get('specialChar'):
			characters.extend(list('!@#$%^&*]}{[()'))

		if request.GET.get('numeric'):
			characters.extend(list('0123456789'))
		genPass = ''
		for x in range(length):
			genPass += random.choice(characters)
	else:
		print('Please enter valid range')

	return render(request, 'check.html', {'password':genPass})

