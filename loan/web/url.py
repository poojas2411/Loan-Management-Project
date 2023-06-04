from django.urls import path
from .import views
urlpatterns=[
    path('',views.home,name="home"),
    path('about',views.about,name="about"),
    path('how',views.how,name="how"),
    path('loan',views.loan_status,name="loan_status"),
    path('out',views.out,name='out'),
    path('contact',views.contact,name="contact")
]