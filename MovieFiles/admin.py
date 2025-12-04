from django.contrib import admin
from .models import *
from django import forms
# Register your models here.

class MovieAdminForm(forms.ModelForm):
    class Meta:
        model = Latest_movie
        fields = '__all__'
        widgets = {
            'mv_genres':forms.CheckboxSelectMultiple,
        }

class MovieAdmin(admin.ModelAdmin):
    form = MovieAdminForm
    
# class MovieAdmin(admin.ModelAdmin):
#     form = MovieAdminForm
#     list_filter = ['m-_genres']

admin.site.register(Genre)
admin.site.register(Latest_movie, MovieAdmin)
admin.site.register(Category)