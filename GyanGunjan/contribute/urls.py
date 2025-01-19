from django.urls import path,include
from . import views

urlpatterns = [
  path("",views.Contribute_view,name='contribute'),

]