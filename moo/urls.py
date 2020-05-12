from django.urls import path
from moo import views

urlpatterns = [path('', views.index, name='home'),
               path('moolist', views.moolist, name="moolist")]
