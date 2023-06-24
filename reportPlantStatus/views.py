from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Plant
from django.template import loader

def index(request):
    latest_plant_list = Plant.objects.order_by("-pub_date")[:5]
    template = loader.get_template("reportPlantStatus/index.html")
    context = {
        "latest_plant_list": latest_plant_list
    }
    return render(request, "reportPlantStatus/index.html", context)

def detail(request, plant_id):
    plant = get_object_or_404(Plant,pk=plant_id)
    return render(request, "reportPlantStatus/detail.html", {"plant":plant})

def comment(request, plant_id):
    return HttpResponse("You're commenting about plant %s." % plant_id)