from django.urls import path
from webapp.views import *



app_name = 'webapp'

urlpatterns = [
    path('', index, name='home'),
    path('disposal/', Disposal, name='disposal'),
    ]