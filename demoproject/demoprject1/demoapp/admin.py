from django.contrib import admin

# Register your models here.
from . models import news,work
admin.site.register(news)
admin.site.register(work)