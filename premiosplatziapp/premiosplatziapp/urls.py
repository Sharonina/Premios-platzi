from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # Significa que en polls va a buscar un archivo urls
    path('polls/', include("polls.urls"))
]
