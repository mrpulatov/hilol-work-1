from django.urls import path
from . import views 


urlpatterns = [
    path('<int:letter_id>/', views.words, name = 'word-ask'), #words

]