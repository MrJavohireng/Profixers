from django.contrib import admin
from .models import Profile, WorkDays, Services, Basket, Order
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields=["user","full_name","phone_number","email","balance","avatar"]
    list_display=["user", "full_name", "phone_number", "balance"]
    list_display_links=["user", "full_name"]
@admin.register(WorkDays)
class WorkDaysAdmin(admin.ModelAdmin):
    fields=["name"]
    list_display=["name"]
@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    fields=["user","name","description","price","active_days","rating"]
    list_display=["user","name","price","rating"]
    list_display_links=["user", "name"]
    filter_horizontal=["active_days"]
@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    fields=["user", "services"]
    filter_horizontal=["services"]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields=["basket","city","street","house","apartment","comment_house","date","pay_type","comment"]
    list_display=["basket","city","street","house","apartment","comment_house","date","pay_type","comment"]
    
    