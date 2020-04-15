from django.shortcuts import render


def words(request):
	return render(request, 'fihrist01/words.html')
