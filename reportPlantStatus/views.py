from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Plant
from django.template import loader

def index(request):
    template_name = "reportPlantStatus/index.html"
    latest_plant_list = Plant.objects.order_by("-pub_date")[:5]
    context = {"latest_plant_list": latest_plant_list}
    return render(request, template_name,context)
    # latest_plant_list = Plant.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("reportPlantStatus/index.html")
    # context = {
    #     "latest_plant_list": latest_plant_list
    # }
    # return render(request, "reportPlantStatus/index.html", context)

def detail(request, plant_id):
    template_name = "reportPlantStatus/detail.html"
    print("Template")
    print(plant_id)
    plant = get_object_or_404(Plant,pk=plant_id)
    print(plant)
    context = {"plant":plant}
    return render(request, template_name, context)

def comment(request, plant_id):
    return HttpResponse("You're commenting about plant %s." % plant_id)