from django.shortcuts import render

from .models import words_uz



get_words = words_uz.objects.all()







def words(request,  letter_id):
	All_words_from_some_letter = []
	for word in get_words:
		if word.letter_id == letter_id:
			word_info = {
			'word_id': word.id,
			'word_name': word.word
			}
			All_words_from_some_letter.append(word_info)
	context = {'All_words_info': All_words_from_some_letter}


	return render(request, 'fihrist01/words.html', context)
