from django.urls import path, include
from . import views

urlpatterns = [
    path('recpies1/', views.recipe_detail)
]