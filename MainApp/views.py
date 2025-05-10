from django.shortcuts import render
from django.http import  HttpResponse
from django.views import View
from .models import Offer
class MainPage(View):
    def get(self, request):
        offer=Offer.objects.order_by("rating").all()[:8]
        context={"data":offer,}
        return render(request=request, template_name="MainApp/index.html", context=context)
    
class ServicesPage(View):
    def get(self, request):
        return render(request=request, template_name="MainApp/list_fixers.html")
    
class ServicesDetailPage(View):
    def get(self, request, pk):
        return render(request=request, template_name="MainApp/index.html")