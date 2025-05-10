
from django.urls import path
from .views import MainPage, ServicesDetailPage, ServicesPage
urlpatterns = [
    path("", MainPage.as_view()),
    path('services/',ServicesPage.as_view(), name='services'),
    path('services/<int:pk>/',ServicesDetailPage.as_view(), name='service_detail'),
    # path('order/', name='order'),
]
