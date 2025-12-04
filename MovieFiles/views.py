from django.shortcuts import render,get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .models import *
# Create your views here.

def Index(request):

   items = Latest_movie.objects.prefetch_related('mv_genres').all()
   genre = Genre.objects.all()
   category = Category.objects.all()
   # items = Latest_movie.objects.all()
   context = {'item':items,"genre":genre,"category":category}
   return render(request,"mvtemp/index.html",context)


def MovieFile(request,mv_id):
   mv = Latest_movie.objects.get(pk = mv_id)
   act_list = mv.mv_actors.split(",")
   new = [kw.strip() for kw in act_list]
   genre = Genre.objects.all()
   category = Category.objects.all()
   context_moviefile = {"mv":mv,"new":new,"genre":genre,"category":category}

   return render(request,"mvtemp/moviefile.html",context_moviefile)

def Genres(request,mv_genre):

   g_name = get_object_or_404(Genre,genre=mv_genre)
   g_movies = g_name.movies.all()
   genre = Genre.objects.all()
   category = Category.objects.all()
   context = {"g_movies":g_movies,"g_name":g_name,"genre":genre,"category":category}
   return render(request,"mvtemp/genres.html",context)

def Category_View(request,mv_category):
   cat_name = Category.objects.get(category=mv_category)
   mv_name = Latest_movie.objects.filter(mv_category = cat_name)
   category = Category.objects.all()
   genre = Genre.objects.all()
   context = {"category":category,"cat_name":cat_name,"mv_name":mv_name,"genre":genre}

   return render(request,"mvtemp/categories.html",context)

def Search_View(request):

   if request.method == "POST":
      search_txt = request.POST['search']
      search_val = Latest_movie.objects.filter(mv_name__icontains = search_txt)
      if not search_val:
         messages.error(request,"Item Does Not Exist")
         return render(request,"mvtemp/search.html")
      else:
         return render(request,"mvtemp/search.html",{"search_val":search_val})
   else:
      return render(request,"mvtemp/search.html")