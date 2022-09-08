from django.shortcuts import render
from django.http import HttpResponse

def welcome_request(request):
	print('this line added by view function')
	return HttpResponse('<h1>Custom middleware Demo</h1>')