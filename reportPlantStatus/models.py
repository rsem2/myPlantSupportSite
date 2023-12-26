from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db.models.query import QuerySet
from django.utils import timezone
from django.db.models import Q


User = settings.AUTH_USER_MODEL

class Reservoir(models.Model):
    reservoir_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image/', blank=True,null=True)
    details = models.TextField(null=True, blank=True)
    water_level = models.IntegerField(default=0)
    class ReservoirStatus(models.IntegerChoices):
        BRILLIANT = 1, _("Brilliant")
        GOOD = 2, _("Good")
        OK = 3, _("OK")
        BAD = 4, _("Bad")
        DEAD = 5, _("Dead")
        MISSING = 6, _("Missing")

    pub_date = models.DateTimeField("date published")
    updated  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.reservoir_name


class Plant(models.Model):
    plant_name =  models.CharField(max_length=200,unique=True)
    image = models.ImageField(upload_to='image/', blank=True,null=True)
    details = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User,default = 1, null=True,on_delete=models.SET_NULL)
    reservoir = models.ForeignKey(Reservoir,null=True,on_delete=models.SET_NULL,blank=True)
    class PlantStatus(models.IntegerChoices):
        BRILLIANT = 1, _("Brilliant")
        GOOD = 2, _("Good")
        OK = 3, _("OK")
        BAD = 4, _("Bad")
        DEAD = 5, _("Dead")
        MISSING = 6, _("Missing")

    plant_status = models.IntegerField(
        choices=PlantStatus.choices,
        default=PlantStatus.OK
    )

    soil_moisture = models.IntegerField(default=0)
    pub_date = models.DateTimeField("date published")
    updated  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.plant_name


class Comment(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='comments', blank=True)
    title = models.CharField(max_length=80)
    contents = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    user = models.ForeignKey(User,default = 1, null=True,on_delete=models.SET_NULL)
    
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return '{} by {}'.format(self.title, self.user)

# TODO: have comments for reservoir + general
# TODO: create array of soil moisture
# TODO: Add details e.g. where it came from
# TODO: multiple reservoirs
# TODO: Include users