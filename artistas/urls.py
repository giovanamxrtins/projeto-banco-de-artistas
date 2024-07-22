from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info_artistas/', include('info_artistas.urls'))
]
