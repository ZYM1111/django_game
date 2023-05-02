from django.urls import path
import sys
sys.path.append(r"/home/acs/acapp/game/views")
from views import index

urlpatterns = [
    path('', index, name="index")
]
