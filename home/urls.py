
from django.urls import path, include
from home import views
from django.views.generic import TemplateView

urlpatterns = [
    path('',views.ListTurni.as_view(),name="home"),

]
