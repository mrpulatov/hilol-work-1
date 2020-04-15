from django.shortcuts import render


def places(request):
	return render(request, 'fihrist01/places.html')