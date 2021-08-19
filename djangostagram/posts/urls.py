from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('', views.index, name = 'index'),
    #This line will transform and send the information into a request object and 
    # to the function passed as a second parameter (e.g. views.main). The information
    # is sent from the html files.
]