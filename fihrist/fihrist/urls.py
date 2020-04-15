from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(letters.urls)), #letters
    path('words/', include(words.urls)), #words
    path('places/', include(places.urls)), #places
]
