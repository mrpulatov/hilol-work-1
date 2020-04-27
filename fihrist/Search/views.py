from django.shortcuts import render

from django.db import connection
# Create your views here.



def get_places(some_word):
    with connection.cursor() as cursor:
        ask = "SELECT suras.sura_name_uz, ayats.ayat_number, ayats.ayat_translation_uz FROM ayats, suras WHERE (ayat_translation_uz ~* ' "
        ask = ask + str(some_word)
        ask = ask + "' ) and (ayats.sura_id=suras.id) ORDER BY suras.id, ayats.ayat_number LIMIT 15 OFFSET 0"
        cursor.execute(ask)
        row = cursor.fetchall()

    return row


def get_count(some_word):
    with connection.cursor() as cursor:
        ask = "SELECT COUNT(1) FROM ayats WHERE (ayat_translation_uz ~* ' "
        ask = ask + str(some_word)
        ask = ask + "')"
        cursor.execute(ask)
        number = cursor.fetchall()
    return number[0]



def places_buy_word(request):
	All_places_contain_word=[]
	some_word = request.GET.get('some_word')
	word_info={
	'word': some_word,
	'count': get_count(some_word)[0]
	}
	get_places_info = get_places(some_word)
	for place in get_places_info:
		place_info={
		'sura_name': place[0],
		'ayat_number': place[1],
		'ayat_translation_uz': place[2],
		}
		All_places_contain_word.append(place_info)
	context = {'All_places_info': All_places_contain_word, 'word':word_info}




	return render(request, 'fihrist01/places.html', context)