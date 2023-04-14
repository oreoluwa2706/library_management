from django.urls import path, include
from . import views

urlpatterns = [
    path('email/', views.playground),
    path('mmail/', views.play_ground),
    path('mail/', views.play_ground1)
]
