
from django.urls import path
from .import views

urlpatterns = [
    path('',views.Prakash.as_view(),name='info'),
path('tests/',views.Ajay.as_view(),name='prakash'),
path('create/',views.Create.as_view(),name='create'),
path('mpc/',views.Maths.as_view(),name='maths'),
path('prakash/',views.Image.as_view(),name='image'),
path('teju/',views.Gaanesh.as_view(),name='teju'),
path('engineering/',views.Engineering.as_view(),name='engg'),
path('bsc/',views.Bsc.as_view(),name='bsc'),
path('navy/',views.Navy.as_view(),name='navy'),
path('arch/',views.Architecture.as_view(),name='arch'),
path('law/',views.Law.as_view(),name='law'),
path('data/',views.Data.as_view(),name='data'),
path('create/',views.Create.as_view(),name='create'),

path('detail/<int:pk>',views.Detail.as_view(),name='details'),
path('updated/<int:pk>',views.Updateview.as_view(),name='edit_post'),


]
