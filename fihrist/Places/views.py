from django.shortcuts import render


def places(request, word_id):
	return render(request, 'fihrist01/places.html')