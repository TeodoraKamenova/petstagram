from django.urls import path

from djangoProject.common.views import index

urlpatterns = (
    path('', index, name='index'),
)
