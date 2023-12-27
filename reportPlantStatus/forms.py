from django import forms

from .models import(Plant, Reservoir, Comment)

class PlantModelForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['plant_name', 'details','image', 'plant_status',]

    def clean_title(self, *args, **kwargs):
        instance = self.instance
        plant_name = self.cleaned_data.get('plant_name')
        qs = Plant.objects.filter(title__iexact=plant_name)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("This name has already been used. Please try again.")
        return plant_name
