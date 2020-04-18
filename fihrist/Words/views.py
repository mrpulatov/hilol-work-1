from django.shortcuts import render
from django.db import connection


def get_word(letter_id):
    with connection.cursor() as cursor:
        cursor.execute('SELECT id, word FROM words_uz WHERE letter_id='+ str(letter_id))
        row = cursor.fetchall()

    return row

def words(request,  letter_id):
	All_words_from_some_letter = []
	get_words_from_letter = get_word(letter_id)
	for word in get_words_from_letter:
		word_info = {
		'word_id': word[0],
		'word_name': word[1]
		}
		All_words_from_some_letter.append(word_info)
	context = {'All_words_info': All_words_from_some_letter}


	return render(request, 'fihrist01/words.html', context)
