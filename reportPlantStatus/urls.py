from django.urls import path
from .views import(
    index,
    detail,
    comment,
    reservoir_list,
    reservoir_detail,
    add_plant,
    add_reservoir,
    edit_plant,
    edit_reservoir,
)

urlpatterns = [
    path("", index, name="index"),
    path("<int:plant_id>/", detail, name="detail"),
    path("<int:plant_id>/comment/", comment, name="comment"),
    path("new/", add_plant),
    path("<int:plant_id>/edit", edit_plant),
    path("reservoir/", reservoir_list),
    path("reservoir/new", add_reservoir),
    path("reservoir/<int:reservoir_id>/",reservoir_detail),
    path("reservoir/<int:reservoir_id>/edit/",edit_reservoir),
]