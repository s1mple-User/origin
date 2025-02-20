from django.contrib import admin
from .models import Category,Blog,FooterImages
from parler.admin import TranslatableAdmin


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ('name',)

admin.site.register(Blog)
admin.site.register(FooterImages)

# Register your models here.    
