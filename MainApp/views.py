from django.shortcuts import render
from django.http import  HttpResponse
from django.views import View
class MainPage(View):
    def get(self, request):

        return render(request=request, template_name="MainApp/index.html")
    
class ServicesPage(View):
    def get(self, request):
        return render(request=request, template_name="MainApp/list_fixers.html")
    
class ServicesDetailPage(View):
    def get(self, request, pk):
        
        return render(request=request, template_name="MainApp/index.html")