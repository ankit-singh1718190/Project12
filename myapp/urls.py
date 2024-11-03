from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentDets, name='Stud'),  # Root URL, goes to 'home' view
    #path('about/', views.about, name='about'),  # /about/ URL, goes to 'about' view
]
