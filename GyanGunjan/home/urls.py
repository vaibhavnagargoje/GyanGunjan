from django.urls import path,include
from . import views

urlpatterns = [
  path("",views.home,name='home'),
  path('filter/',views.filter_flipbooks,name='filter_flipbooks'),
  path('about-project/',views.about_project, name="about_project"),

]