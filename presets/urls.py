from django.urls import path
from .views import preset_list # ✅ Import the view


urlpatterns = [
    path('',preset_list, name='preset_list'),
]
