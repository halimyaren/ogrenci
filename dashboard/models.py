from asyncio.windows_events import NULL
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title    #Notları listelediğimizde başlıklarına göre çıksın

    class Meta:
        verbose_name = "notlar"
        verbose_name_plural = "notlar"    #Görünmesini istediğimiz ifade

class Homework(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length = 50)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due = models.DateTimeField()
    is_finished = models.BooleanField(default = False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Ödevler"
        verbose_name_plural = "Ödevler"    #Görünmesini istediğimiz ifade

class Todo(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     title = models.CharField(max_length=100)
     is_finished = models.BooleanField(default=False)

     def __str__(self):
        return self.title

class Pdf(models.Model):
    ders = models.CharField(max_length=30)
    sinif = models.CharField(max_length=7)
    pdf = models.FileField(upload_to='static/pdfs/')
    kapak = models.ImageField(upload_to = 'static/kapaklar/',default='',blank=True,null=True)

    def __str__(self):
        return self.ders