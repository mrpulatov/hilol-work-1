from django.urls import path
from . import views 

urlpatterns = [
    path('', views.places_buy_word, name = 'place-ask-buy-word'), #words

]