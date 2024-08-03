from django.contrib import admin
from django.urls import path, include

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', include('djangoProject.common.urls')),
    path('accounts/', include('djangoProject.accounts.urls')),
    path('pets/', include('djangoProject.pets.urls')),
    path('photos/', include('djangoProject.photos.urls')),
)
