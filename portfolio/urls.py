from django.urls import path
from .views import home, ContactView, portfolio_detail, contact


urlpatterns = [
    path('', home, name='home'),
    path('contactme', contact, name='contacturl'),
    path('contact/', ContactView, name='contact'),
    path("portfolio/<int:pk>/", portfolio_detail, name="portfolio_detail"),

]
