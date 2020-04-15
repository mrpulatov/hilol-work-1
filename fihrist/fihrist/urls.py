from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(Letters.urls)), #letters
    path('words/', include(Words.urls)), #words
    path('places/', include(Places.urls)), #places
]
