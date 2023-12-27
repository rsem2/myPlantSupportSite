from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required

from .models import (Plant, Reservoir)
from .forms import PlantModelForm

def index(request):
    template_name = "reportPlantStatus/index.html"
    #TODO: only show living plants
    # latest_plant_list = Plant.objects.order_by("-pub_date")[:5]
    latest_plant_list = Plant.objects.order_by("-pub_date")
    context = {"latest_plant_list": latest_plant_list}
    return render(request, template_name,context)

def detail(request, plant_id):
    template_name = "reportPlantStatus/detail.html"
    plant = get_object_or_404(Plant,pk=plant_id)
    reservoir = None
    if plant.reservoir is not None:
        reservoir = Reservoir.objects.get(id = plant.reservoir.pk)
    context = {"plant":plant, "reservoir": reservoir}
    
    print(request)
    if "delete" in request.POST:
        plant.delete()
        return HttpResponseRedirect("/reportPlantStatus/")
    return render(request, template_name, context)

@login_required(login_url='/login')
def comment(request, plant_id):
    return HttpResponse("You're commenting about plant %s." % plant_id)

def reservoir_list(request):
    template_name = "reportPlantStatus/reservoir_index.html"
    context={}
    return render(request, template_name, context)

def reservoir_detail(request, reservoir_id):
    template_name = "reportPlantStatus/reservoir_detail.html"
    reservoir = get_object_or_404(Reservoir,pk=reservoir_id)
    print(reservoir.reservoir_status)
    print(reservoir.get_status())
    # print(reservoir.reservoir_status._name_)
    context={"reservoir": reservoir}
    return render(request, template_name, context)

@login_required(login_url='/login')
def add_plant(request):
    template_name = "reportPlantStatus/create_plant.html"
    form = PlantModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit = False)
        obj.user = request.user
        obj = form.save()
        if "add_more" in request.POST:
            print("or are you here")
            form = PlantModelForm()
        elif "add" in request.POST:
            new_address = "/reportPlantStatus/{}".format(obj.pk)
            return HttpResponseRedirect(new_address)  
    context = {"form":form}
    return render(request, template_name, context)

@login_required(login_url='/login')
def add_reservoir(request):
    template_name = "reportPlantStatus/create_reservoir.html"
    context={}
    return render(request, template_name, context)

@login_required(login_url='/login')
def edit_plant(request,plant_id):
    template_name = "reportPlantStatus/edit_plant.html"
    plant = get_object_or_404(Plant,pk=plant_id)
    form = PlantModelForm(request.POST or None, request.FILES or None, instance = plant)
    return_address = "/reportPlantStatus/{}".format(plant_id)
    if "cancel" in request.POST:
        return HttpResponseRedirect(return_address) 
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(return_address) 
    context={"plant":plant, "form":form}
    return render(request, template_name, context)

@login_required(login_url='/login')
def edit_reservoir(request, reservoir_id):
    template_name = "reportPlantStatus/edit_reservoir.html"
    reservoir = get_object_or_404(Reservoir,pk=reservoir_id)
    context={"reservoir":reservoir}
    return render(request, template_name, context)

