from django.urls import path
from . import views 

urlpatterns = [
    path('<int:word_id>/', views.places, name = 'place-ask'), #words

]