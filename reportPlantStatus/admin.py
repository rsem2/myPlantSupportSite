from django.contrib import admin

from .models import(
    Plant,
    Comment,
    Reservoir
)

admin.site.register(Plant)
admin.site.register(Reservoir)
admin.site.register(Comment)