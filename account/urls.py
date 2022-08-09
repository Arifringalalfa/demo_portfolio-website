from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_log, name='login'),
    path('logout/', views.user_logOut, name='logout'),
]
