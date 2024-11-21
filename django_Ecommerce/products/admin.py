from django.contrib import admin
from .models import Category,Product

# Register your models here.

@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ["name" , "slug"]
    prepopulated_fields = {'slug' : ('name' , )}
