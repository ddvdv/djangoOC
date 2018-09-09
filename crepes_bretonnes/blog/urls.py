from django.urls import path
from . import views

urlpatterns = [
        path('date', views.date_actuelle),
        path('addition/<int:nombre1>/<int:nombre2>/', views.addition),
        path('base', views.base),
        path('contact/', views.contact, name='contact'),
]
