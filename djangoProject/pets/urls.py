from django.urls import path, include

from djangoProject.pets.views import create_pet, edit_pet, delete_pet, details_pet

urlpatterns = (
    path("create/", create_pet, name= "pet_create"),
    path("<str:username>/pet/<slug:pet_slug>/", include([
        path("", details_pet, name="details_pet"),
        path("edit/", edit_pet, name="edit_pet"),
        path("delete/", delete_pet, name="delete_pet"),
    ]))
)