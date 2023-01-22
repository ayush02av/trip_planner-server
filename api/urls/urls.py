from django.urls import path
from ..views import views_user

urlpatterns = [
    path("profile/", views_user.profile.as_view(), name="profile"),
]