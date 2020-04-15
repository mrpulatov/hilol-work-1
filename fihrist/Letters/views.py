from django.shortcuts import render


def index(request):
	return render(request, 'fihrist01/index.html')
