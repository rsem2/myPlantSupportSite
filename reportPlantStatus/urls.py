from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:plant_id>/", views.detail, name="detail"),
    path("<int:plant_id>/comment", views.comment, name="comment"),
]