from django.urls import path
from djangoProject.accounts.views import \
    signin_user, signup_user, \
    details_profile, edit_profile, delete_profile

urlpatterns = (
    path("signup/", signup_user, name="signup user"),
    path("signin/", signin_user, name="signin user"),
    path("profile/<int:pk>", details_profile, name="details profile"),
    path("profile/<int:pk>/edit", edit_profile, name="edit profile"),
    path("profile/<int:pk>/delete", delete_profile, name="delete profile"),
)