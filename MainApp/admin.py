from django.contrib import admin
from .models import Offer, Profile, Order
@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    model=Offer
    fields=["user", "name", "description", "price"]
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model=Profile
    fields=["user", "full_name", "phone_number", "balance"]
@admin.register(Order)
class ProfileAdmin(admin.ModelAdmin):
    model=Profile
    fields=["user", "order", "status"]