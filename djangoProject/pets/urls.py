from django.urls import path, include

from djangoProject.pets.views import create_pet, edit_pet, delete_pet, details_pet

urlpatterns = (
    path("create/", create_pet, name= "create pet"),
    path("<str:username>/pet/<slug:pet_slug>/", include([
        path("", details_pet, name="details pet"),
        path("edit/", edit_pet, name="edit pet"),
        path("delete/", delete_pet, name="delete pet"),
    ]))
)
