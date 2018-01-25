from django.contrib import admin

# Register the Category and Page class to the admin interface

from rango.models import Category, Page
admin.site.register(Category)
admin.site.register(Page)
