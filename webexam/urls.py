from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include('webexam.profiles.urls')),
    path('', include('webexam.notes.urls'))
]
