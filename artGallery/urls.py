from django.urls import path

from . import views

app_name = "artGallery"

urlpatterns = [
    # Create
    path("add/", views.CreateArt.as_view(), name="add"),
    # Read
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
]
