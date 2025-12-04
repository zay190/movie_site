from django.db import models

# Create your models here.
class Genre(models.Model):
    genre = models.CharField(max_length=30)

    def __str__(self):
        return self.genre

class Category(models.Model):
    category = models.CharField(max_length=40)

    def __str__(self):
        return self.category 

class Latest_movie(models.Model):
    mv_name = models.CharField(max_length=50,blank=False)
    mv_desc = models.TextField(blank=True)
    mv_genres = models.ManyToManyField(Genre, related_name='movies')
    mv_image = models.ImageField(upload_to='uploads/image',null=True)
    mv_actors = models.CharField(max_length=500,help_text='Enter words seperated by comma',null=True,blank=True)
    mv_category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.mv_name