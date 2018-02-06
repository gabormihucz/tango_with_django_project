from django.contrib import admin

# Register the Category and Page class to the admin interface

from rango.models import Category, Page

from rango.models import UserProfile # user auth - chap9

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}



class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'url']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
