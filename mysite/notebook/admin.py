from django.contrib import admin

from .models import Document, Category, User


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone')

admin.site.register(Document)
admin.site.register(Category)
admin.site.register(User)

