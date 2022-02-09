from django.contrib import admin

#from dashboard.views import books
from .models import *

# Register your models here.
admin.site.register(Notes)   #Admin panelinde Notları göstermek için kaydediyoruz
admin.site.register(Homework)
admin.site.register(Todo)
admin.site.register(Pdf)
