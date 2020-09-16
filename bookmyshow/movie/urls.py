from django.urls import include
from django.urls import path
from .views import MovieView

urlpatterns = [
    path("movies", MovieView.as_view(), name="movies"),
]
