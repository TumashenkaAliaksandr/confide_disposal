from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from webapp.views import *



app_name = 'webapp'

urlpatterns = [
    path('', index, name='home'),
    path('disposal/', Disposal, name='disposal'),
    path('slider/', slider, name='slider'),
    path('contacts/', contacts, name='contacts'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)