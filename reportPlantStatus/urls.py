from django.urls import path
from .views import(
    index,
    detail,
    comment,
)

urlpatterns = [
    path("", index, name="index"),
    path("<int:plant_id>/", detail, name="detail"),
    path("<int:plant_id>/comment", comment, name="comment"),
]