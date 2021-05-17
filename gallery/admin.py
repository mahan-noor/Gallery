from django.contrib import admin
from .models import Editor,Location,Image,Category
# Register your models here.

admin.site.register(Editor)
admin.site.register(Location)
admin.site.register(Image)
admin.site.register(Category)