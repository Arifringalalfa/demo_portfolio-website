
from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='home'),
    path('about/', views.aboutpage, name='about'),
    path('contact/', views.contactpage, name='contact'),
    path('mobile/', views.mobile, name='mobile'),
    path('laptop/', views.laptop, name='laptop'),
    path('computer/', views.computer, name='computer'),
    path('accessories/', views.accessories, name='accessories'),

]
