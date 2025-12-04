from django.shortcuts import render,get_object_or_404
from .fav import Fav
from MovieFiles.models import *
from django.http import JsonResponse
# Create your views here.

def Fav_Summary(request):

    fav = Fav(request)

    # getting the movie from the cart class
    fav_movies = fav.get_fav()
    category = Category.objects.all()
    genre = Genre.objects.all()
    context = {"category":category,"genre":genre,"fav_movies":fav_movies}
    return render(request,"Fav_summary.html",context)

def Fav_Add(request):
    fav = Fav(request)

    # test for the post
    if request.POST.get('action') == 'post':
        # Passing the value into a variable
        mv_id = int(request.POST.get("fav_id"))

        # checking if object actually exists
        mv_checker = get_object_or_404(Latest_movie, id=mv_id)
        # saving the value in the sesssions
        fav.add(mv_checker)

        response = JsonResponse({"id":mv_id})

        return response



def Fav_Delete(request):
    fav = Fav(request)

    # test for the post
    if request.POST.get('action') == 'post':
        # Get Id of Movie Chosen
        mv_id = int(request.POST.get("del_id"))
        fav.delete(mv_id)

        response = JsonResponse({'Mv_id':mv_id})
        return response