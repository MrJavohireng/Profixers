from django.contrib import admin
from .models import Offer, Profile, Order
@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    model=Offer
    fields=["user", "name", "description", "price", "rating"]
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model=Profile
    fields=["user", "full_name", "phone_number", "balance"]
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model=Order
    fields=["user", "order", "status"]