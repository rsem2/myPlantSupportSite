from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import (Plant, Reservoir)
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
    plant = get_object_or_404(Plant,pk=plant_id)
    context = {"plant":plant}
    return render(request, template_name, context)

def comment(request, plant_id):
    return HttpResponse("You're commenting about plant %s." % plant_id)

def reservoir_list(request):
    template_name = "reportPlantStatus/reservoir_index.html"
    context={}
    return render(request, template_name, context)

def reservoir_detail(request, reservoir_id):
    template_name = "reportPlantStatus/reservoir_detail.html"
    reservoir = get_object_or_404(Reservoir,pk=reservoir_id)
    context={"reservoir": reservoir}
    return render(request, template_name, context)

def add_plant(request):
    template_name = "reportPlantStatus/create_plant.html"
    context={}
    return render(request, template_name, context)

def add_reservoir(request):
    template_name = "reportPlantStatus/create_reservoir.html"
    context={}
    return render(request, template_name, context)

def edit_plant(request,plant_id):
    template_name = "reportPlantStatus/edit_or_delete_plant.html"
    plant = get_object_or_404(Plant,pk=plant_id)
    context={"plant":plant}
    return render(request, template_name, context)

def edit_reservoir(request, reservoir_id):
    template_name = "reportPlantStatus/edit_or_delete_reservoir.html"
    reservoir = get_object_or_404(Reservoir,pk=reservoir_id)
    context={"reservoir":reservoir}
    return render(request, template_name, context)

