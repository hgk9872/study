from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('write/', write, name='write'),
    path('list/', list, name='list'),
    path('view/(?P<num>[0-9]+)/$', view),
]