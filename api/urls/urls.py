from django.urls import path, include
from ..views import views_user, views_place

urlpatterns = [
    path("profile/", views_user.profile.as_view(), name="profile"),
    path("place/", views_place.place.as_view(), name="place"),
]