from django.urls import path
from Rezome.views import *

app_name = "Rezome"

urlpatterns = [
    path('', index_view , name='index')
]
