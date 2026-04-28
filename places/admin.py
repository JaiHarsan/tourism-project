from django.contrib import admin

# MongoEngine models don't work with Django admin
# To manage MongoDB documents, use MongoDB Compass or pymongo scripts

# Uncomment below if using Django ORM instead of MongoEngine:
# from .models import Place
# 
# @admin.register(Place)
# class PlaceAdmin(admin.ModelAdmin):
#     list_display = ('name', 'category', 'city', 'location')
#     list_filter = ('category', 'city')
