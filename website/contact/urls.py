
from django.urls import path
from .import views

urlpatterns = [

path('complain/',views.Contactuss.as_view(),name='complaint'),
]
