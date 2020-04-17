from django.shortcuts import render
from .models import letters_uz


All_letters = []

Letters =  letters_uz.objects.all()


for letter in Letters:
	 letter_info={
	 'letter_id' : letter.id,
	 'letter' : letter.letter
	 }
	 All_letters.append(letter_info)

context = {"All_letters_info": All_letters}

def index(request):
	return render(request, 'fihrist01/index.html', context)

