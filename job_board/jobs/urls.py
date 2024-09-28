from django.urls import path,include
from jobs import views

urlpatterns = [
    path("get_industries/",views.get_industries, name='get-industries')

]