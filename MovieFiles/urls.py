from django.urls import path
from .views import *

urlpatterns = [
    path("",Index,name="index"),
    path("moviefile/<int:mv_id>",MovieFile,name="moviefile"),
    path("genres/<slug:mv_genre>",Genres,name="genres_url"),
    path("category/<str:mv_category>",Category_View,name="category_view"),
    path("search/",Search_View,name="search_url")
]
