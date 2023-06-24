from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Plant(models.Model):

    plant_name =  models.CharField(max_length=200)

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

    def __str__(self):
        return self.plant_name


class Comment(models.Model):
    post = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

# TODO: have comments for reservoir + general
# TODO: create array of soil moisture
# TODO: Add details e.g. where it came from
# TODO: multiple reservoirs
# TODO: Include users