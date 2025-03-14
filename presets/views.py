from django.shortcuts import render

from .models import Preset

def preset_list(request):
    presets = Preset.objects.all()  # Get all presets from the database
    return render(request, 'presets/preset_list.html', {'presets': presets})

# Create your views here.
