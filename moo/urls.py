from django.urls import path
from moo import views

urlpatterns = [path('', views.index, name='home'),
               path('history', views.history, name="history")]
