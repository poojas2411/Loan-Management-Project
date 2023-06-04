from django.urls import path
from .import views

urlpatterns=[
      path('',views.acc,name='acc'),
      path('registration',views.regis,name="regis"),
      path('out',views.out,name='out'),
    ]