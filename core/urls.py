from . import views
from django.urls import path

from django.conf import settings

app_name = 'core'

urlpatterns = [
    path('',views.dashboard, name='dashboard'),


]
