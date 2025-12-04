from django.urls import path
from .views import *

urlpatterns = [
    path("summary/",Fav_Summary,name="fav_summary"),
    path("add/",Fav_Add,name="fav_add"),
    path("delete/",Fav_Delete,name="fav_del"),
]